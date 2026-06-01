# Cookie Testing

## Summary

Cookie testing - это проверка того, как web application создает, хранит, читает, обновляет и удаляет HTTP cookies.

Cookies часто отвечают за:

- login session;
- remember me;
- shopping cart;
- user preferences;
- tracking;
- personalization;
- A/B testing;
- security behavior.

Главная идея:

> Cookie - маленькая часть client-side state. Если она хранится неправильно, ломаются sessions, privacy, access control и user experience.

## What Is A Cookie?

HTTP cookie - это небольшая порция данных, которую server отправляет browser через HTTP response header `Set-Cookie`.

Browser сохраняет cookie и затем отправляет ее обратно server в следующих requests через header `Cookie`.

Упрощенный flow:

1. User открывает website.
2. Server отвечает page и header `Set-Cookie`.
3. Browser сохраняет cookie.
4. User открывает следующую page.
5. Browser автоматически добавляет cookie в request.
6. Server использует cookie, чтобы понять session, preferences или другой context.

Пример:

```http
Set-Cookie: session_id=abc123; Path=/; HttpOnly; Secure; SameSite=Lax
```

Следующий request:

```http
Cookie: session_id=abc123
```

## Why Cookies Are Needed

HTTP сам по себе stateless: каждый request независим. Server не помнит предыдущий request, если application не использует дополнительный mechanism для state.

Cookies помогают поддерживать context между requests.

Примеры:

- user залогинился, и server связывает `session_id` с его account;
- user добавил product в cart, а cart сохраняется между page refresh;
- user выбрал language/theme, и site применяет preference;
- user согласился с cookie banner, и banner больше не показывается;
- analytics system отличает returning user от new user.

## Session Cookies And Persistent Cookies

Есть два базовых типа cookies.

| Type | Meaning | Example |
| --- | --- | --- |
| Session cookie | Живет до закрытия browser session или до session timeout. | Login session, temporary cart. |
| Persistent cookie | Имеет `Expires` или `Max-Age` и может жить дни, месяцы или годы. | Remember me, preferences, consent. |

Session cookie обычно не имеет explicit expiration date. Persistent cookie имеет срок жизни.

QA должен проверять, что cookie type соответствует requirements. Например, `remember_me` может быть persistent, но `session_id` часто должен истекать раньше и быть защищен.

## Important Cookie Attributes

Cookie behavior задается attributes.

| Attribute | What It Controls | QA Focus |
| --- | --- | --- |
| `Expires` | Absolute expiration date. | Cookie живет ровно столько, сколько нужно. |
| `Max-Age` | Lifetime in seconds. | Session не становится вечной случайно. |
| `Domain` | Для каких domains cookie отправляется. | Cookie не утекает на лишние subdomains. |
| `Path` | Для каких URL paths cookie отправляется. | Cookie доступна только нужной части сайта. |
| `Secure` | Cookie отправляется только по HTTPS. | Sensitive cookies не уходят по HTTP. |
| `HttpOnly` | JavaScript не может читать cookie. | Session cookie защищена от простого XSS theft. |
| `SameSite` | Cross-site sending behavior. | CSRF risk снижен, external login/payment flows не сломаны. |

Для QA особенно важны `Secure`, `HttpOnly`, `SameSite`, `Domain`, `Path` и expiration.

## Where To Inspect Cookies

Обычно cookies удобнее проверять в browser developer tools.

Chrome / Edge:

1. Open DevTools.
2. Go to `Application`.
3. Open `Storage`.
4. Select `Cookies`.
5. Choose the domain.

Firefox:

1. Open DevTools.
2. Go to `Storage`.
3. Select `Cookies`.

Также cookies можно увидеть в network requests:

- response header `Set-Cookie`;
- request header `Cookie`.

Это полезно, когда нужно понять, кто именно создает cookie и в какой момент она отправляется обратно на server.

## What To Test

Cookie testing включает несколько направлений:

- creation;
- storage;
- update;
- deletion;
- expiration;
- browser settings;
- security attributes;
- privacy compliance;
- cross-browser behavior;
- multi-user behavior;
- multi-environment behavior.

## Cookie Creation

Проверить:

- cookie создается после нужного action;
- cookie не создается раньше времени;
- name соответствует expected behavior;
- value не пустой, если должен быть state;
- domain и path корректные;
- expiration корректный;
- security attributes выставлены правильно.

Примеры:

- `session_id` создается после successful login;
- `cookie_consent` создается после accept в cookie banner;
- cart cookie создается после adding item to cart;
- tracking cookie не создается до consent, если это требуется законом или policy.

## Cookie Storage

Проверить:

- sensitive data не хранится в plain text;
- cookie value не содержит password, token с лишними permissions, card data, personal data без необходимости;
- encrypted/signed cookie нельзя прочитать или изменить вручную без server-side validation;
- cookie size не превышает practical limits;
- application не создает слишком много cookies.

Плохие признаки:

- email, phone, password или role лежат в cookie как plain text;
- `is_admin=true` можно изменить вручную и получить access;
- cookie живет годами без причины;
- cookie доступна JavaScript, хотя хранит session token.

## Cookie Update

Проверить:

- session expiration обновляется только согласно requirements;
- user preferences меняются после изменения settings;
- cart state обновляется после add/remove quantity;
- cookie не остается stale после logout;
- старое значение не конфликтует с новым.

Пример:

Если user меняет language с `en` на `ru`, cookie должна обновиться, а UI должен показывать новый language после reload и в новой tab.

## Cookie Deletion

Проверить:

- logout удаляет или invalidates session cookie;
- delete account очищает related cookies;
- decline cookies не оставляет non-essential tracking cookies;
- clearing cart удаляет cart-related state;
- expired cookie больше не используется server.

Важно: даже если cookie удалена в browser, server-side session тоже должна быть invalidated, если речь о login session.

## Cookies Disabled In Browser

Проверить поведение, если cookies выключены.

Ожидаемое поведение зависит от product, но application не должна crash.

Что проверить:

- понятное сообщение о необходимости включить cookies;
- public pages продолжают открываться, если это возможно;
- login/cart/checkout корректно блокируются или работают fallback-логикой;
- no infinite redirects;
- no blank pages;
- errors logged correctly.

## Accept And Reject Cookies

Для сайтов с cookie consent нужно проверить:

- user может accept all;
- user может reject non-essential cookies;
- user может настроить cookie categories;
- после reject не создаются analytics/marketing cookies;
- essential cookies создаются только если они действительно нужны;
- preferences сохраняются;
- banner не появляется снова без причины;
- user может изменить consent later.

Категории часто выглядят так:

- strictly necessary;
- preferences;
- analytics;
- marketing.

## Corrupted Cookies

QA может вручную изменить cookie value в DevTools и проверить behavior.

Проверить:

- application не падает;
- user не получает чужие данные;
- invalid cookie rejected;
- server создает новую valid cookie, если это допустимо;
- security event логируется, если cookie выглядит tampered;
- error message не раскрывает internals.

Примеры tampering:

- изменить `user_id`;
- изменить `role`;
- изменить expiration;
- удалить часть encrypted value;
- заменить cookie value random string.

## Cookie Security Test Cases

Проверить:

- session cookie имеет `HttpOnly`;
- sensitive cookie имеет `Secure`;
- cookie не отправляется по HTTP;
- `SameSite` выбран осознанно;
- `Domain` не слишком широкий;
- `Path` не слишком широкий;
- logout invalidates session;
- session fixation невозможна;
- cookie replay risk снижен;
- application не доверяет client-side cookie без server validation.

Особенно опасно, если authorization decision строится только на cookie value, которую user может изменить.

## Multi-Browser Testing

Cookies нужно проверить в основных browsers:

- Chrome;
- Edge;
- Firefox;
- Safari;
- mobile browsers.

Почему это важно:

- browsers по-разному ограничивают third-party cookies;
- Safari может строже относиться к tracking;
- privacy settings могут блокировать часть behavior;
- mobile browser может очищать data иначе;
- embedded browsers внутри apps могут иметь свои ограничения.

## Multi-User Testing

Проверить:

- после logout одного user другой user не видит его данные;
- cookies user A не используются для user B;
- shared computer scenario безопасен;
- remember me не логинит неправильного user;
- switching accounts очищает old state.

Пример:

1. Login as user A.
2. Add item to cart.
3. Logout.
4. Login as user B.
5. Verify cart, profile, orders and preferences belong to user B.

## Multi-Environment Testing

Если есть dev, staging, production, нужно проверить:

- cookies разных environments не конфликтуют;
- domain не слишком широкий;
- staging cookie не ломает production login;
- encryption/signing keys согласованы только там, где это действительно нужно;
- test cookies не отправляются на production domain.

Типичный риск: wildcard domain вроде `.example.com`, из-за которого cookie от staging начинает влиять на production или наоборот.

## E-Commerce Cookie Testing

Для e-commerce особенно важны:

- cart state;
- checkout session;
- payment redirect;
- promo code;
- delivery preferences;
- recently viewed products;
- login/guest checkout;
- consent and tracking.

Test ideas:

- add product to cart, close browser, open site again;
- change quantity and verify cookie/server state;
- login after guest cart and verify merge behavior;
- logout and verify checkout session is cleared;
- payment redirect returns user to correct order;
- coupon is not applied twice because of stale cookie;
- declined marketing cookies do not block purchase.

## Example Cookie Test Cases

| ID | Scenario | Expected Result |
| --- | --- | --- |
| C-01 | Login with valid credentials. | Session cookie is created with correct attributes. |
| C-02 | Logout. | Session cookie is deleted or invalidated; protected pages require login. |
| C-03 | Disable cookies and open login page. | Application shows clear message or graceful fallback. |
| C-04 | Delete cookies manually and refresh protected page. | User is redirected to login or session is recreated safely. |
| C-05 | Modify `user_id` cookie manually. | Access is denied; no other user's data is shown. |
| C-06 | Accept only necessary cookies. | Analytics/marketing cookies are not created. |
| C-07 | Reject cookie banner. | Non-essential cookies are not stored. |
| C-08 | Change language preference. | Preference cookie updates and persists after reload. |
| C-09 | Open site in another browser. | Cookie behavior remains consistent with requirements. |
| C-10 | Use HTTP instead of HTTPS. | Secure cookies are not sent over HTTP. |
| C-11 | Session reaches timeout. | User is logged out or asked to re-authenticate. |
| C-12 | Login as user A, logout, login as user B. | No state from user A leaks to user B. |

## Common Bugs

Common cookie-related defects:

- session cookie missing `HttpOnly`;
- sensitive cookie missing `Secure`;
- wrong expiration;
- logout does not invalidate server-side session;
- stale cart after login;
- consent rejected but tracking cookies still created;
- cookie path/domain too broad;
- cookie works in Chrome but fails in Safari;
- infinite redirect when cookies disabled;
- user sees old preferences after update;
- different environments overwrite each other's cookies.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Cookie | Small piece of data stored by browser for a website. |
| `Set-Cookie` | Response header used by server to create/update cookie. |
| `Cookie` | Request header used by browser to send cookies to server. |
| Session cookie | Cookie that usually expires when browser session ends. |
| Persistent cookie | Cookie with `Expires` or `Max-Age`. |
| `Secure` | Sends cookie only over HTTPS. |
| `HttpOnly` | Prevents JavaScript from reading cookie. |
| `SameSite` | Controls cross-site cookie sending. |
| Cookie consent | User's choice about optional cookies. |
| Session fixation | Attack where attacker forces victim to use known session id. |

## Questions

### 1. What is cookie testing?

Cookie testing checks how a web application creates, stores, updates, sends and deletes cookies.

### 2. Why are cookies important in web testing?

They often support login sessions, cart state, preferences, personalization and tracking.

### 3. Should sensitive data be stored in cookies?

Usually no. If unavoidable, it must be protected, encrypted or signed, and validated server-side.

### 4. What should happen after logout?

Session cookie should be removed or invalidated, and protected pages should no longer be accessible.

### 5. Why test cookies with disabled browser cookies?

Because the application should fail gracefully instead of crashing, looping redirects or showing blank pages.

### 6. Why is `HttpOnly` important?

It helps prevent JavaScript from reading sensitive cookies, reducing risk from some XSS scenarios.

### 7. Why is `Secure` important?

It prevents cookies from being sent over unencrypted HTTP.

### 8. Why check `Domain` and `Path`?

They control where cookies are sent. Too broad settings can create privacy, security and environment conflicts.

## What To Review Later

- Client-Server Architecture
- HTTP Headers
- HTTPS
- Sessions
- Authentication
- Authorization
- CSRF
- XSS
- Web Application Testing Guide

