# Browser Rendering Engines

Source: pasted article about rendering engines in browsers  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, browsers, rendering engine, compatibility, cross browser testing  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/browser-rendering-engines.md

## Summary

Rendering engine - это часть browser, которая превращает HTML, CSS, images и часть результатов JavaScript в визуальную страницу на экране.

Для QA эта тема важна, потому что разные browsers могут использовать разные rendering engines:

- Chrome, Edge и Opera используют `Blink`;
- Safari использует `WebKit`;
- Firefox использует `Gecko`;
- старый Internet Explorer использовал `Trident`.

Из-за этого один и тот же web page может выглядеть или работать немного по-разному в разных browsers. Именно поэтому cross browser testing нужен не как формальность, а как практическая защита от browser-specific bugs.

## Key Points

- Browser состоит из нескольких компонентов: user interface, browser engine, rendering engine, networking, JavaScript engine, UI backend и data storage.
- Rendering engine парсит HTML/CSS, строит DOM tree и render tree, рассчитывает layout и рисует страницу.
- JavaScript может менять DOM/CSSOM, поэтому страница может перерисовываться после user actions или network responses.
- Разные rendering engines могут по-разному обрабатывать CSS, HTML, fonts, forms, scrolling, animations и mobile viewport.
- QA должен понимать rendering basics, чтобы лучше расследовать layout bugs, responsive issues и cross browser defects.

## Notes

## Why Rendering Engines Matter For QA

Когда пользователь открывает сайт, browser не просто показывает HTML-файл как текст. Он:

- получает ресурсы по network;
- парсит HTML;
- загружает CSS, images, fonts и scripts;
- применяет styles;
- рассчитывает размеры и позиции элементов;
- рисует result на screen;
- реагирует на JavaScript, user actions и data changes.

Если в Chrome всё выглядит правильно, это не гарантирует, что Safari или Firefox покажут страницу точно так же. Разница может быть маленькой, например другой scrollbar, или критичной, например checkout button уехал за пределы экрана.

## Main Browser Components

## User Interface

User interface - это browser controls вокруг страницы:

- address bar;
- back/forward buttons;
- reload;
- tabs;
- bookmarks;
- browser menus.

QA обычно не тестирует browser UI напрямую, но должен понимать, что это не часть web application. Web app находится внутри viewport.

## Browser Engine

Browser engine - это слой, который связывает user interface и rendering engine.

Он получает actions от browser UI и управляет тем, как page загружается, обновляется и отображается.

Например, когда user нажимает reload, browser engine координирует процесс: networking layer получает ресурсы, rendering engine строит страницу заново, cache может участвовать в загрузке.

## Rendering Engine

Rendering engine отвечает за отображение web content.

Он работает с:

- HTML;
- CSS;
- images;
- fonts;
- XML/SVG в некоторых случаях;
- visual result after JavaScript changes.

Именно rendering engine определяет, как DOM and CSS станут pixels on screen.

## Networking

Networking component отправляет и получает данные через protocols:

- HTTP;
- HTTPS;
- FTP в старых сценариях;
- WebSocket;
- другие network mechanisms.

Для QA это связано с `Network` tab в DevTools: там видно, какие resources browser загрузил и какие requests ушли на backend.

## JavaScript Engine

JavaScript engine парсит и выполняет JavaScript.

Примеры:

- Chrome/Edge - V8;
- Firefox - SpiderMonkey;
- Safari - JavaScriptCore.

JavaScript может:

- менять DOM;
- менять classes/styles;
- отправлять network requests;
- создавать animations;
- обрабатывать user events.

Поэтому rendering и JavaScript тесно связаны: script изменил состояние, rendering engine должен обновить visual result.

## UI Backend

UI backend использует возможности operating system для отрисовки базовых widgets, fonts, windows и controls.

Из-за этого native controls могут выглядеть по-разному на Windows, macOS, iOS и Android.

## Data Storage / Persistence

Browser хранит данные локально:

- cookies;
- localStorage;
- sessionStorage;
- IndexedDB;
- Cache Storage;
- service worker data.

Для QA это важно при проверке login, logout, sessions, cache, PWA и stale data issues.

## How Rendering Works

Упрощенный rendering flow:

1. Browser получает HTML document.
2. Rendering engine парсит HTML и строит DOM tree.
3. Browser загружает и парсит CSS.
4. Styles применяются к DOM nodes.
5. Создается render tree: только visual elements, которые нужно отрисовать.
6. Layout рассчитывает размеры и координаты элементов.
7. Paint рисует pixels на screen.
8. Composite собирает layers в финальное изображение.

В реальности процесс сложнее, но для QA этой модели достаточно, чтобы понимать многие UI bugs.

## DOM Tree

DOM tree - это структурное дерево HTML elements.

Пример:

```html
<main>
  <h1>Checkout</h1>
  <button>Pay</button>
</main>
```

Browser превращает это в nodes, с которыми может работать JavaScript и которые можно видеть во вкладке `Elements`.

## CSSOM And Styles

CSS rules превращаются в style information.

Browser должен понять:

- какие selectors подходят к element;
- какие rules конфликтуют;
- какой specificity выше;
- какие values inherited;
- какие computed values получились.

В DevTools это видно через `Styles` и `Computed`.

## Render Tree

Render tree содержит только то, что нужно визуально отрисовать.

Например, element с `display: none` есть в DOM, но не попадает в render tree.

Для QA это важно:

- element может существовать в DOM, но быть невидимым;
- hidden element может всё ещё влиять на accessibility или scripts;
- overlay может быть visible и перекрывать другой element.

## Layout

Layout рассчитывает размеры и позиции элементов.

Здесь появляются:

- width/height;
- margins;
- padding;
- position;
- flex/grid behavior;
- line wrapping;
- responsive breakpoints.

Большая часть visual bugs связана именно с layout:

- text overlaps;
- button goes outside container;
- content jumps;
- fixed header covers form;
- mobile layout breaks at specific width.

## Paint And Composite

Paint рисует visual parts:

- text;
- backgrounds;
- borders;
- shadows;
- images.

Composite собирает layers, например fixed header, modal overlay, transformed elements и animations.

Если layer или `z-index` настроены неправильно, QA может увидеть:

- modal behind page content;
- dropdown under header;
- tooltip hidden;
- clickable area blocked by invisible element.

## Popular Rendering Engines

| Rendering engine | Browsers | QA notes |
| --- | --- | --- |
| Blink | Chrome, Edge, Opera | Самый распространенный engine для Chromium-based browsers. |
| WebKit | Safari, iOS browsers | Critical для iPhone/iPad testing; iOS browsers используют WebKit. |
| Gecko | Firefox | Может отличаться в CSS/layout behavior и standards implementation. |
| Trident | Legacy Internet Explorer | Встречается только в legacy/corporate contexts. |

## Why Browsers Render Differently

Даже при open web standards browsers могут отличаться:

- standards implementation не всегда одинаковая;
- новые CSS/JS features появляются не одновременно;
- browser bugs существуют;
- mobile browsers имеют дополнительные ограничения;
- fonts and native controls зависят от OS;
- default styles могут отличаться;
- security policies могут работать строже или мягче.

Поэтому QA не должен считать, что если feature работает в Chrome, она автоматически работает в Safari and Firefox.

## QA Examples

## Example 1: CSS Layout Bug In Safari

В Chrome card grid выглядит правильно, а в Safari карточки наезжают друг на друга.

Что проверить:

- CSS Grid/Flex support;
- computed styles;
- browser-specific CSS bug;
- viewport width;
- media queries;
- Safari version.

## Example 2: Button Hidden On Mobile

На desktop button виден, а на iPhone он ниже viewport и до него нельзя доскроллить.

Что проверить:

- mobile viewport height;
- fixed/sticky elements;
- virtual keyboard behavior;
- overflow;
- safe area on iOS;
- responsive breakpoint.

## Example 3: Different Form Control

Date input выглядит и работает по-разному в Chrome and Safari.

Что проверить:

- native browser control behavior;
- expected product requirements;
- custom fallback;
- validation;
- accessibility.

## How QA Uses This Knowledge

Rendering engine basics помогают QA:

- быстрее понимать visual bugs;
- отличать frontend bug от browser limitation;
- выбирать правильный browser matrix;
- писать точные bug reports;
- проверять CSS fixes в affected browser;
- понимать, почему real device testing важнее одной Chrome-проверки.

## What To Include In A Rendering Bug Report

Для visual/browser-specific bug указать:

- browser name and version;
- rendering engine, если relevant;
- OS and version;
- device model;
- viewport size;
- zoom level;
- screenshot/video;
- expected and actual result;
- whether bug reproduces in other browsers;
- relevant CSS/DOM observation from DevTools;
- console errors, если есть.

Пример:

> Safari 17 on iPhone 14: checkout footer overlaps the Pay button at 390x844 viewport. Chrome mobile emulation does not reproduce. In DevTools, footer has `position: fixed` and button container has no bottom padding.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Rendering engine | Browser component that converts HTML/CSS into pixels on screen. |
| Browser engine | Layer that coordinates browser UI and rendering engine. |
| DOM | Tree representation of HTML document. |
| CSSOM | Parsed CSS information used to apply styles. |
| Render tree | Visual tree used to draw visible elements. |
| Layout | Process of calculating element sizes and positions. |
| Paint | Process of drawing visual parts of elements. |
| Composite | Process of combining layers into the final screen image. |
| Blink | Rendering engine used by Chromium-based browsers. |
| WebKit | Rendering engine used by Safari and iOS browsers. |
| Gecko | Rendering engine used by Firefox. |
| Trident | Legacy rendering engine used by Internet Explorer. |

## Questions

### 1. Что делает rendering engine?

Answer: Он парсит HTML/CSS, строит visual structures, рассчитывает layout и рисует страницу на экране.

### 2. Почему rendering engines важны для cross browser testing?

Answer: Разные engines могут по-разному интерпретировать HTML, CSS, JavaScript effects, fonts, forms и layout behavior.

### 3. Какие browsers используют Blink?

Answer: Chrome, Edge, Opera и другие Chromium-based browsers.

### 4. Почему Safari нужно проверять отдельно?

Answer: Safari использует WebKit, а на iOS browsers также завязаны на WebKit, поэтому поведение может отличаться от Chrome/Firefox.

### 5. Что такое layout в rendering flow?

Answer: Это этап, где browser рассчитывает размеры и координаты элементов на странице.

### 6. Почему элемент может быть в DOM, но не отображаться?

Answer: Например, если у него `display: none`, он остается в DOM, но не попадает в render tree.

### 7. Какие данные добавить в bug report для visual browser bug?

Answer: Browser/version, OS, device, viewport, screenshot/video, expected/actual result и сравнение с другими browsers.

## What To Review Later

- Разницу между browser engine, rendering engine и JavaScript engine.
- Основные этапы rendering flow: DOM, CSSOM, render tree, layout, paint, composite.
- Blink, WebKit, Gecko и где они используются.
- Как rendering differences создают cross browser bugs.
- Какие детали нужны в visual/browser-specific bug report.
