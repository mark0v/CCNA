# Cross Browser Testing

Source: pasted article about cross browser testing  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, cross browser testing, compatibility, browsers, devices  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/cross-browser-testing.md

## Summary

Cross browser testing - это проверка, что website или web application корректно работает и выглядит достаточно одинаково в разных browsers, operating systems и devices.

Проверяются не только Chrome, Firefox, Safari и Edge, но и разные версии browsers, desktop/mobile platforms, screen sizes и device capabilities.

Главная мысль:

> Cross browser testing помогает поймать browser-specific bugs до того, как их увидят реальные пользователи.

## Key Points

- Разные browsers используют разные rendering engines и могут по-разному интерпретировать HTML, CSS и JavaScript.
- Невозможно проверить все browser/OS/device combinations, поэтому QA выбирает приоритеты по analytics, market share, target audience и product risks.
- Cross browser testing покрывает functionality, layout, responsiveness, accessibility, performance и иногда browser-specific security behavior.
- Chrome DevTools emulation, simulators и VMs полезны, но real devices и cloud device farms дают более надежную картину.
- Manual testing лучше подходит для exploratory UX checks, а automated tests - для повторяемых regression scenarios в разных browsers.

## Notes

## What Is Cross Browser Testing?

Cross browser testing проверяет, что web product:

- открывается в поддерживаемых browsers;
- сохраняет основную functionality;
- корректно отображает layout;
- не ломает JavaScript behavior;
- остается usable на разных screen sizes;
- работает с browser-specific limitations.

Пример:

Checkout page работает в Chrome, но в Firefox payment gateway не загружается из-за browser-specific JavaScript/API issue. Для бизнеса это критичный bug: часть пользователей не сможет оплатить заказ.

## Why It Is Important

Пользователи не используют один и тот же browser. У кого-то Chrome на Windows, у кого-то Safari на iPhone, у кого-то Firefox на Linux, у кого-то Edge в corporate environment.

Cross browser testing важен, потому что:

- browsers имеют разные rendering engines;
- support новых JavaScript APIs может отличаться;
- CSS properties могут работать по-разному;
- mobile browsers имеют ограничения, которых нет на desktop;
- accessibility behavior может отличаться между browser/screen reader combinations;
- browser updates могут неожиданно изменить behavior.

Для QA цель не в том, чтобы pixel-perfect совпадение было везде. Цель - убедиться, что user может выполнить key flows без критичных проблем.

## What To Test

Обычно cross browser testing делят на несколько зон.

## Base Functionality

Проверить, что основные сценарии работают:

- login/logout;
- registration;
- search;
- forms and validation;
- checkout/payment;
- navigation;
- filters and sorting;
- file upload/download;
- modals, dropdowns, menus;
- cookies and sessions;
- touch input на mobile/tablet.

Если core flow ломается только в одном browser, это всё равно production bug для пользователей этого browser.

## Design And Visual Consistency

Проверить:

- fonts;
- images;
- spacing;
- colors;
- alignment;
- icons;
- forms;
- buttons;
- responsive layout;
- hover/focus/active states.

Допустимы небольшие visual differences между platforms, например native select или scrollbar. Но не допустимы broken layout, overlapping text, missing buttons или unreadable content.

## Accessibility

Проверить:

- keyboard navigation;
- visible focus;
- labels for inputs;
- semantic headings;
- contrast;
- screen reader basics;
- ARIA behavior, если используется;
- browser zoom.

Accessibility может отличаться по browser and assistive technology combination, поэтому для важных продуктов стоит явно определить supported combinations.

## Responsiveness

Проверить:

- desktop, tablet, mobile widths;
- portrait и landscape orientation;
- breakpoints;
- hamburger menu;
- touch targets;
- forms and virtual keyboard;
- отсутствие horizontal scroll;
- корректное поведение sticky/fixed elements.

DevTools device toolbar полезен для быстрой проверки, но финальные mobile risks лучше подтверждать на реальных devices или cloud devices.

## Performance

Иногда cross browser testing включает performance checks:

- page load time;
- animation smoothness;
- scrolling;
- memory usage;
- CPU load;
- behavior на older browsers/devices.

Один и тот же frontend может быть приемлемым на desktop Chrome и медленным на mobile Safari или older Android browser.

## Security-Related Browser Behavior

В некоторых проектах проверяют:

- HTTPS enforcement;
- mixed content warnings;
- secure cookie behavior;
- `SameSite`, `Secure`, `HttpOnly`;
- Content Security Policy;
- CORS behavior;
- download warnings;
- browser permission prompts.

Security behavior особенно важно для auth, payments, personal data и admin panels.

## How To Select Browsers

Проверить все невозможно. Нужно выбрать browser matrix.

Основные подходы:

- analytics: Google Analytics, product telemetry, server logs;
- market share: самые популярные browsers/devices в целевом регионе;
- business priority: где находятся paying users;
- risk-based approach: где больше критичных flows;
- client requirements: явно поддерживаемые browsers and OS versions;
- accessibility requirements: нужные browser/screen reader combinations.

Практическое правило:

> Если browser/OS combination дает заметную долю traffic или закрывает важный user segment, его нужно включить в тестирование.

Часто команды начинают с:

- Chrome latest на Windows/macOS;
- Safari latest на macOS/iOS;
- Firefox latest;
- Edge latest;
- Android Chrome;
- iOS Safari.

Для legacy products могут понадобиться older browser versions, но их стоит поддерживать только если это бизнес-необходимость.

## Test Planning

Перед тестированием полезно подготовить test specification:

- features in scope;
- browsers and versions;
- operating systems;
- devices;
- screen sizes;
- test scenarios;
- priorities;
- timelines;
- automation/manual split;
- acceptance criteria;
- known limitations.

Так QA не тестирует хаотично, а покрывает именно то, что важно продукту.

## How Cross Browser Testing Is Done

Типичный flow:

1. Сначала проверить baseline в primary browser, чаще всего Chrome.
2. Подготовить browser/device matrix.
3. Выбрать critical flows.
4. Выполнить manual или automated checks.
5. Сравнить result с expected behavior.
6. Завести browser-specific bugs.
7. Retest fixes в affected browser и сделать короткую regression проверку в остальных.

## Manual Vs Automated Testing

Manual testing полезен для:

- exploratory testing;
- visual checks;
- UX pain points;
- new features;
- flows, которые часто меняются;
- one-time compatibility checks.

Automation полезна для:

- smoke checks;
- regression;
- repeatable user flows;
- CI/CD feedback;
- running the same scenario in multiple browsers.

Примеры tools:

- Selenium;
- Playwright;
- Cypress;
- WebdriverIO;
- BrowserStack, Sauce Labs, LambdaTest для cloud browsers/devices.

Хорошая стратегия обычно сочетает оба подхода: automation покрывает повторяемые сценарии, а manual QA ищет UX и edge cases.

## Infrastructure Options

Для cross browser testing можно использовать:

| Option | Pros | Cons |
| --- | --- | --- |
| Local browsers | Быстро и дешево для базовых проверок. | Ограниченный набор OS/devices. |
| DevTools emulation | Удобно для responsive smoke. | Не заменяет реальные mobile browsers. |
| Virtual machines | Можно поднять разные OS/browser versions. | Поддержка и масштабирование сложнее. |
| Real device lab | Самые реалистичные результаты. | Дорого покупать и поддерживать. |
| Cloud testing platform | Много browser/device combinations без своего lab. | Зависимость от provider и subscription. |

## When To Run Cross Browser Tests

Cross browser checks стоит запускать:

- during development для risky UI/frontend changes;
- в CI для automated smoke/regression;
- на staging/pre-release перед production;
- после browser-specific fix;
- после больших CSS/layout changes;
- после обновления frontend framework или build pipeline;
- перед marketing campaign, checkout release или важным launch.

Минимум перед release нужно пройти critical flows в supported browsers.

## Who Does Cross Browser Testing?

Обычно участвуют:

- QA team - test scenarios, compatibility matrix, bug reports, regression;
- developers - локальные проверки, fixes, automated tests;
- UI/UX designers - visual consistency and layout review;
- product/business stakeholders - supported browsers and priorities;
- marketing team - landing pages, campaigns, analytics-driven browser selection.

QA помогает связать business priorities с practical test coverage.

## Common Cross Browser Bugs

Частые проблемы:

- layout differs in Safari;
- button text overflows on mobile;
- dropdown opens behind another element;
- CSS `position: sticky` behaves differently;
- date input has different native UI;
- unsupported JavaScript API breaks feature;
- file upload works in Chrome but fails in Safari;
- cookies behave differently because of `SameSite`;
- payment iframe blocked in one browser;
- font rendering changes layout;
- focus state invisible in keyboard navigation;
- WebSocket or fetch behavior differs in older browsers.

## Bug Report Tips

Для browser-specific bug report обязательно указать:

- browser name and version;
- OS and version;
- device model, если mobile;
- viewport size/orientation;
- steps to reproduce;
- actual result;
- expected result;
- screenshot/video;
- Console errors;
- Network request details, если relevant;
- whether bug reproduces in other browsers.

Пример хорошей формулировки:

> Reproduces in Firefox 124 on Windows 11, does not reproduce in Chrome 124. Checkout payment iframe stays blank after clicking Pay. Console shows CSP error. Network request to payment provider returns 200.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Cross browser testing | Проверка работы web product в разных browsers, OS и devices. |
| Browser matrix | Список browser/OS/device combinations, которые нужно поддерживать и тестировать. |
| Rendering engine | Компонент browser, который отображает HTML/CSS, например Blink, WebKit, Gecko. |
| Responsive design | Подход, при котором layout адаптируется под разные screen sizes. |
| Compatibility testing | Проверка совместимости продукта с разными platforms, browsers, devices и environments. |
| Baseline browser | Основной browser, в котором сначала проверяют expected behavior. |
| Device lab | Набор реальных устройств для тестирования. |
| Cloud testing platform | Сервис с удаленными browsers/devices для manual или automated checks. |
| HAR | Файл с network activity, полезный для анализа browser-specific request issues. |

## Questions

### 1. Что такое cross browser testing?

Answer: Это проверка, что website или web application корректно работает и выглядит приемлемо в разных browsers, OS и devices.

### 2. Почему нельзя тестировать только в Chrome?

Answer: Пользователи используют разные browsers, а rendering engines, JavaScript support, CSS behavior и browser security rules могут отличаться.

### 3. Как выбрать browsers для тестирования?

Answer: По analytics, market share, target audience, business priorities, risks и explicit client requirements.

### 4. Что такое browser matrix?

Answer: Это список browser/OS/device combinations, которые команда обязуется поддерживать и проверять.

### 5. Какие проверки лучше автоматизировать?

Answer: Повторяемые smoke и regression flows, которые нужно запускать в нескольких browsers.

### 6. Почему mobile emulation не заменяет real devices?

Answer: Emulation не полностью повторяет real browser engine, OS behavior, performance, touch, keyboard и device-specific issues.

### 7. Что обязательно указать в browser-specific bug report?

Answer: Browser/version, OS, device, viewport, steps, expected/actual result, evidence и сравнение с другими browsers.

## What To Review Later

- Как составить browser matrix.
- Чем Blink, WebKit и Gecko могут отличаться для QA.
- Какие flows должны входить в cross browser smoke.
- Как использовать analytics для выбора browsers.
- Как отличать acceptable visual difference от real bug.
