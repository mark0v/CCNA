# Cookie Testing

## Summary

Cookie testing checks how a web application creates, stores, reads, updates, and deletes HTTP cookies.

Cookies often support:

- login sessions;
- remember me;
- shopping cart;
- user preferences;
- tracking;
- personalization;
- A/B testing;
- security behavior.

Main idea:

> A cookie is a small piece of client-side state. If it is handled incorrectly, sessions, privacy, access control, and user experience can break.

## What Is A Cookie?

An HTTP cookie is a small piece of data that a server sends to a browser through the HTTP response header `Set-Cookie`.

The browser stores the cookie and sends it back to the server in later requests through the `Cookie` request header.

Simplified flow:

1. User opens a website.
2. Server returns a page and a `Set-Cookie` header.
3. Browser stores the cookie.
4. User opens the next page.
5. Browser automatically adds the cookie to the request.
6. Server uses the cookie to understand the session, preferences, or another context.

Example:

```http
Set-Cookie: session_id=abc123; Path=/; HttpOnly; Secure; SameSite=Lax
```

Next request:

```http
Cookie: session_id=abc123
```

## Why Cookies Are Needed

HTTP is stateless by itself: every request is independent. The server does not remember the previous request unless the application uses an additional state mechanism.

Cookies help maintain context between requests.

Examples:

- a user logs in, and the server connects `session_id` with that account;
- a user adds a product to a cart, and the cart persists across page refreshes;
- a user selects language/theme, and the site applies the preference;
- a user accepts a cookie banner, and the banner stops appearing;
- an analytics system distinguishes a returning user from a new user.

## Session Cookies And Persistent Cookies

There are two basic cookie types.

| Type | Meaning | Example |
| --- | --- | --- |
| Session cookie | Lives until the browser session closes or until session timeout. | Login session, temporary cart. |
| Persistent cookie | Has `Expires` or `Max-Age` and can live for days, months, or years. | Remember me, preferences, consent. |

A session cookie usually has no explicit expiration date. A persistent cookie has a defined lifetime.

QA should verify that the cookie type matches the requirements. For example, `remember_me` may be persistent, but `session_id` usually needs stronger expiration and protection.

## Important Cookie Attributes

Cookie behavior is controlled by attributes.

| Attribute | What It Controls | QA Focus |
| --- | --- | --- |
| `Expires` | Absolute expiration date. | Cookie lives exactly as long as required. |
| `Max-Age` | Lifetime in seconds. | Session does not become permanent by mistake. |
| `Domain` | Domains where the cookie is sent. | Cookie does not leak to unnecessary subdomains. |
| `Path` | URL paths where the cookie is sent. | Cookie is available only to the required part of the site. |
| `Secure` | Cookie is sent only through HTTPS. | Sensitive cookies do not travel over HTTP. |
| `HttpOnly` | JavaScript cannot read the cookie. | Session cookie is safer from simple XSS theft. |
| `SameSite` | Cross-site sending behavior. | CSRF risk is reduced, while external login/payment flows still work. |

For QA, `Secure`, `HttpOnly`, `SameSite`, `Domain`, `Path`, and expiration are especially important.

## Where To Inspect Cookies

Cookies are usually easiest to inspect in browser developer tools.

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

Cookies can also be checked in network requests:

- response header `Set-Cookie`;
- request header `Cookie`.

This helps identify which response creates a cookie and when the browser sends it back to the server.

## What To Test

Cookie testing includes several areas:

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

Check:

- cookie is created after the expected action;
- cookie is not created too early;
- name matches the expected behavior;
- value is not empty when state is required;
- domain and path are correct;
- expiration is correct;
- security attributes are set correctly.

Examples:

- `session_id` is created after successful login;
- `cookie_consent` is created after accepting the cookie banner;
- cart cookie is created after adding an item to cart;
- tracking cookie is not created before consent if required by law or policy.

## Cookie Storage

Check:

- sensitive data is not stored as plain text;
- cookie value does not contain password, overpowered token, card data, or personal data without a valid reason;
- encrypted/signed cookie cannot be manually read or changed without server-side validation;
- cookie size does not exceed practical limits;
- application does not create too many cookies.

Bad signs:

- email, phone, password, or role is stored in a cookie as plain text;
- `is_admin=true` can be changed manually to gain access;
- cookie lives for years without a reason;
- cookie is available to JavaScript even though it stores a session token.

## Cookie Update

Check:

- session expiration updates only according to requirements;
- user preferences change after settings update;
- cart state updates after add/remove quantity;
- cookie does not stay stale after logout;
- old value does not conflict with the new value.

Example:

If a user changes language from `en` to `ru`, the cookie should update, and the UI should show the new language after reload and in a new tab.

## Cookie Deletion

Check:

- logout deletes or invalidates the session cookie;
- delete account clears related cookies;
- decline cookies does not leave non-essential tracking cookies;
- clearing cart removes cart-related state;
- expired cookie is no longer used by the server.

Important: even if a cookie is deleted in the browser, the server-side session must also be invalidated when it is a login session.

## Cookies Disabled In Browser

Check behavior when cookies are disabled.

Expected behavior depends on the product, but the application should not crash.

Check:

- clear message about enabling cookies;
- public pages still open if possible;
- login/cart/checkout are blocked correctly or use fallback behavior;
- no infinite redirects;
- no blank pages;
- errors are logged correctly.

## Accept And Reject Cookies

For sites with cookie consent, check:

- user can accept all;
- user can reject non-essential cookies;
- user can configure cookie categories;
- analytics/marketing cookies are not created after reject;
- essential cookies are created only when truly necessary;
- preferences are saved;
- banner does not appear again without a reason;
- user can change consent later.

Common categories:

- strictly necessary;
- preferences;
- analytics;
- marketing.

## Corrupted Cookies

QA can manually change a cookie value in DevTools and observe behavior.

Check:

- application does not crash;
- user does not get another user's data;
- invalid cookie is rejected;
- server creates a new valid cookie if allowed;
- security event is logged if the cookie looks tampered;
- error message does not expose internals.

Tampering examples:

- change `user_id`;
- change `role`;
- change expiration;
- remove part of encrypted value;
- replace cookie value with a random string.

## Cookie Security Test Cases

Check:

- session cookie has `HttpOnly`;
- sensitive cookie has `Secure`;
- cookie is not sent over HTTP;
- `SameSite` is chosen intentionally;
- `Domain` is not too broad;
- `Path` is not too broad;
- logout invalidates session;
- session fixation is not possible;
- cookie replay risk is reduced;
- application does not trust client-side cookie without server validation.

It is especially dangerous when authorization decisions are based only on a cookie value that the user can modify.

## Multi-Browser Testing

Check cookies in major browsers:

- Chrome;
- Edge;
- Firefox;
- Safari;
- mobile browsers.

Why it matters:

- browsers restrict third-party cookies differently;
- Safari may be stricter with tracking;
- privacy settings can block part of the behavior;
- mobile browser may clear data differently;
- embedded browsers inside apps can have their own limitations.

## Multi-User Testing

Check:

- after logout of one user, another user does not see their data;
- cookies of user A are not reused for user B;
- shared computer scenario is safe;
- remember me does not log in the wrong user;
- account switching clears old state.

Example:

1. Login as user A.
2. Add item to cart.
3. Logout.
4. Login as user B.
5. Verify cart, profile, orders, and preferences belong to user B.

## Multi-Environment Testing

If there are dev, staging, and production environments, check:

- cookies from different environments do not conflict;
- domain is not too broad;
- staging cookie does not break production login;
- encryption/signing keys are shared only where really needed;
- test cookies are not sent to the production domain.

A typical risk is a wildcard domain like `.example.com`, where a staging cookie starts affecting production or the other way around.

## E-Commerce Cookie Testing

For e-commerce, key areas are:

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
- payment redirect returns user to the correct order;
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

Cookie testing checks how a web application creates, stores, updates, sends, and deletes cookies.

### 2. Why are cookies important in web testing?

They often support login sessions, cart state, preferences, personalization, and tracking.

### 3. Should sensitive data be stored in cookies?

Usually no. If unavoidable, it must be protected, encrypted or signed, and validated server-side.

### 4. What should happen after logout?

Session cookie should be removed or invalidated, and protected pages should no longer be accessible.

### 5. Why test cookies with disabled browser cookies?

Because the application should fail gracefully instead of crashing, looping redirects, or showing blank pages.

### 6. Why is `HttpOnly` important?

It helps prevent JavaScript from reading sensitive cookies, reducing risk from some XSS scenarios.

### 7. Why is `Secure` important?

It prevents cookies from being sent over unencrypted HTTP.

### 8. Why check `Domain` and `Path`?

They control where cookies are sent. Too broad settings can create privacy, security, and environment conflicts.

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

