# Chrome DevTools For Web Testing

Source: pasted article about Chrome DevTools  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, Chrome DevTools, browser, debugging, network  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/chrome-devtools-for-web-testing.md

## Summary

Chrome DevTools - это встроенный набор инструментов Chrome, который помогает QA видеть web application глубже, чем обычный UI.

Через DevTools можно:

- проверять HTML и CSS на вкладке `Elements`;
- видеть JavaScript errors, logs и выполнять команды в `Console`;
- анализировать HTTP requests, responses, headers, payload и timing во вкладке `Network`;
- отлаживать JavaScript во вкладке `Sources`;
- проверять cookies, localStorage, sessionStorage, cache и service workers во вкладке `Application`;
- смотреть performance, memory, security и accessibility signals;
- эмулировать mobile viewport, slow network и слабый CPU.

Главная мысль:

> Для QA Chrome DevTools - это способ проверить, что реально происходит между browser, frontend code, network и backend.

## Key Points

- DevTools помогает не только developers, но и QA: искать причины UI bugs, network bugs, validation issues, cache problems и performance issues.
- `Elements` нужен для анализа DOM, CSS, layout, hidden elements, responsive issues и accessibility clues.
- `Console` показывает JavaScript errors, warnings, logs и позволяет быстро проверить DOM/JS behavior.
- `Network` - одна из самых важных вкладок для QA: тут видно requests, status codes, headers, payload, response, timing, cache и WebSocket frames.
- `Application` помогает проверять cookies, storage, cache, service workers и logout/session cleanup.
- `Performance`, `Memory`, `Security` и Lighthouse полезны для более глубокого анализа скорости, HTTPS, accessibility и best practices.
- Mobile emulation в DevTools полезна для быстрой проверки responsive layout, но не заменяет реальные устройства.

## Notes

## Why QA Needs Chrome DevTools

Без DevTools QA видит только результат на экране. Это важно, но часто недостаточно.

Например, кнопка может не работать по разным причинам:

- frontend не отправляет request;
- request уходит, но backend возвращает `400`, `401`, `403`, `500`;
- response приходит правильный, но UI неправильно его отображает;
- JavaScript падает с ошибкой;
- данные взяты из cache или старого localStorage;
- CSS скрывает элемент или перекрывает его другим блоком.

DevTools помогает разделить эти причины и быстрее понять, где искать баг: UI, frontend logic, network, backend, data или browser state.

## Opening And Configuring DevTools

Открыть DevTools можно несколькими способами:

- Right click на элементе -> `Inspect`;
- `Ctrl + Shift + C` - открыть режим выбора элемента;
- `Ctrl + Shift + J` - открыть Console;
- `F12` - открыть DevTools;
- на macOS обычно используются сочетания с `Command + Option`.

DevTools можно расположить:

- снизу страницы;
- слева;
- справа;
- в отдельном окне.

Для QA это практично: при проверке responsive layout или узких экранов иногда удобнее вынести DevTools в отдельное окно, чтобы панель не меняла размер viewport.

В настройках полезно знать:

- `Disable cache` во вкладке `Network`;
- `Disable JavaScript` в settings или command menu;
- device toolbar для mobile emulation;
- `More tools` для дополнительных панелей вроде `Rendering`, `Coverage`, `Sensors`, `Performance monitor`.

## Elements: DOM, CSS And Layout

Вкладка `Elements` показывает DOM tree и CSS styles выбранного элемента.

QA использует ее, чтобы проверить:

- есть ли элемент в DOM;
- не скрыт ли он через `display: none`, `visibility: hidden`, `opacity: 0`;
- не перекрыт ли элемент другим block;
- правильные ли text, attributes, classes и states;
- какие CSS rules реально применились;
- почему layout выглядит не так, как ожидается;
- как ведут себя псевдоклассы вроде `:hover`, `:focus`, `:active`.

Полезные действия:

- выбрать элемент через inspect cursor;
- временно изменить text, class, attribute или CSS property;
- отключить отдельное CSS rule checkbox-ом;
- посмотреть `Computed`, чтобы увидеть финальное значение CSS property;
- проверить box model: `margin`, `border`, `padding`, `content`;
- временно скрыть элемент клавишей `H`;
- удалить элемент клавишей `Delete`;
- поставить DOM breakpoint на изменение node, attribute или удаление элемента.

Важно помнить:

> Изменения в `Elements` временные. Они помогают проверить гипотезу, но не меняют реальный source code.

Пример QA-сценария:

Если button визуально есть, но не нажимается, в `Elements` можно проверить, нет ли поверх него invisible overlay, disabled attribute, неправильного `z-index` или CSS, который блокирует interaction.

## Console: Errors, Logs And Quick Checks

Вкладка `Console` показывает:

- JavaScript errors;
- warnings;
- logs из `console.log`;
- failed resource messages;
- security или CORS warnings;
- результат выполненных JavaScript commands.

QA может использовать Console, чтобы:

- понять, падает ли frontend code;
- скопировать error message в bug report;
- проверить значение local variables или DOM state;
- выполнить короткую команду;
- быстро очистить storage или проверить selected element.

Полезные команды и возможности:

```javascript
console.log("debug value");
console.error("Something failed");
console.warn("Check this state");
console.table([{ id: 1, status: "active" }]);
console.time("flow");
console.timeEnd("flow");
```

Chrome также хранит выбранный в `Elements` элемент в переменной `$0`.

Пример:

```javascript
$0.textContent
$0.classList
```

Для bug report важно приложить:

- точный error text;
- stack trace, если он есть;
- page URL;
- шаги воспроизведения;
- browser version;
- screenshot или video;
- related Network request, если ошибка связана с API.

## Sources: JavaScript Debugging

Вкладка `Sources` нужна для отладки JavaScript.

QA не всегда должен глубоко debug-ить code, но полезно понимать базовые возможности:

- открыть загруженные JS/CSS files;
- искать source file или текст по project;
- ставить breakpoints;
- остановить execution на exception;
- смотреть call stack;
- выполнять код step by step;
- форматировать minified code через pretty print;
- проверять, какая function сработала после user action.

Для QA это полезно, когда:

- баг воспроизводится только после конкретного click/input;
- UI меняется неожиданно;
- нужно понять, какой script меняет DOM;
- frontend validation блокирует submit;
- нужно собрать больше технического контекста для developer.

## Network: Requests, Responses And Timing

`Network` - ключевая вкладка для web и API testing.

Она показывает все requests, которые browser отправляет во время загрузки страницы и user actions:

- HTML, CSS, JS, images, fonts;
- XHR/fetch API requests;
- documents;
- redirects;
- WebSocket connections;
- failed requests;
- cached resources.

Что QA проверяет в `Network`:

- правильный endpoint;
- HTTP method: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`;
- status code;
- request headers;
- response headers;
- query params;
- path params;
- payload/body;
- response body;
- timing;
- cache behavior;
- cookies;
- CORS errors;
- WebSocket frames.

### Practical Network Checks

При проверке формы:

1. Открыть `Network`.
2. Очистить список requests.
3. Выполнить действие в UI.
4. Найти нужный request.
5. Проверить method, URL, payload, headers, status code и response.
6. Сравнить response с тем, что показал UI.

Пример:

Если UI показывает "Saved", но `Network` показывает `500`, это bug в frontend error handling. Пользователь не должен видеть success, если backend operation failed.

Если request вообще не ушел, проблема может быть в frontend validation, disabled button, JS error или broken event handler.

### Filtering And HAR

В `Network` можно:

- фильтровать requests по type: `Fetch/XHR`, `JS`, `CSS`, `Img`, `Doc`, `WS`;
- искать по URL или response content;
- включить `Preserve log`, чтобы requests не исчезали после navigation;
- включить `Disable cache`;
- симулировать slow network;
- экспортировать requests в HAR file.

HAR полезен для bug report, если нужно показать полный network flow. Но перед передачей HAR нужно помнить о sensitive data: tokens, cookies, emails, user ids, payment data.

## Application: Cookies, Storage And Cache

Вкладка `Application` помогает проверять browser-side state.

Здесь QA смотрит:

- cookies;
- localStorage;
- sessionStorage;
- IndexedDB;
- Cache Storage;
- service workers;
- manifest;
- clear storage.

Типовые проверки:

- cookie создается после login;
- session очищается после logout;
- sensitive data не лежит в localStorage без необходимости;
- expired token не продолжает работать;
- cache не показывает старую версию UI;
- service worker не держит старые assets после release;
- app корректно работает после `Clear storage`.

Пример:

Если после logout и login другим user браузер показывает данные предыдущего user, нужно проверить cookies, storage, cache и API responses.

## Performance And Memory

Вкладка `Performance` помогает понять, почему страница медленная.

QA может использовать ее для:

- записи page load или user flow;
- анализа long tasks;
- поиска heavy JavaScript;
- просмотра rendering и layout work;
- проверки реакции страницы на slow CPU или slow network;
- сбора evidence для performance bug.

Вкладка `Memory` помогает исследовать memory usage:

- heap snapshot;
- allocation timeline;
- allocation sampling.

QA редко делает глубокий memory profiling, но может заметить симптомы:

- page становится медленнее после долгого использования;
- browser tab потребляет слишком много memory;
- repeated action постепенно ухудшает responsiveness;
- single-page app не очищает старые objects после navigation.

## Security And Lighthouse

Вкладка `Security` показывает:

- использует ли страница HTTPS;
- есть ли mixed content;
- валиден ли certificate;
- какие origins считаются insecure.

Для QA это полезно при проверке:

- HTTPS setup;
- staging/prod certificates;
- mixed HTTP resources на HTTPS page;
- warnings в browser.

Lighthouse помогает быстро получить automated audit по:

- performance;
- accessibility;
- best practices;
- SEO;
- PWA behavior.

Lighthouse не заменяет ручное тестирование, но помогает найти очевидные проблемы и дать команде стартовые recommendations.

## More Tools

В `More tools` есть дополнительные панели, полезные для QA:

| Tool | QA use |
| --- | --- |
| `Rendering` | Проверить paint flashing, FPS, print media, prefers-color-scheme. |
| `Coverage` | Посмотреть, сколько JS/CSS реально используется на странице. |
| `Performance monitor` | Следить за CPU, JS heap, DOM nodes, event listeners. |
| `Sensors` | Эмулировать location, orientation и device conditions. |
| `Request blocking` | Заблокировать URL и проверить fallback/error handling. |
| `Animations` | Анализировать UI animations. |
| `Changes` | Посмотреть временные изменения CSS/HTML, сделанные в DevTools. |

## Mobile View

Device toolbar позволяет быстро проверить responsive behavior:

- выбрать preset device;
- задать width и height вручную;
- менять orientation;
- эмулировать touch input;
- менять user agent;
- комбинировать mobile viewport с slow network.

QA проверяет:

- помещается ли текст;
- не перекрываются ли элементы;
- работает ли menu;
- удобно ли нажимать buttons и links;
- нет ли horizontal scroll;
- корректно ли ведут себя forms;
- не ломается ли layout на разных breakpoints.

Ограничение:

> Mobile emulation в DevTools полезна для быстрой проверки, но реальные iOS/Android devices всё равно нужны для финальной проверки.

## What To Include In Bug Reports

Когда баг найден через DevTools, bug report становится сильнее, если добавить:

- screenshot или video;
- Console error;
- Network request URL, method, status code;
- request payload и response body, если их можно безопасно приложить;
- headers, если проблема в auth, cache, CORS, content type или cookies;
- browser and OS;
- device/viewport;
- HAR file, если нужен полный network flow;
- clear expected result and actual result.

Не прикладывать без очистки:

- auth tokens;
- session cookies;
- passwords;
- payment data;
- private user data.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| DevTools | Встроенные browser tools для анализа страницы, DOM, CSS, JS, network и storage. |
| DOM | Document Object Model; дерево HTML-элементов страницы. |
| CSS Box Model | Модель `content`, `padding`, `border`, `margin`. |
| Console | DevTools tab для JavaScript commands, errors, warnings и logs. |
| Network | DevTools tab для анализа HTTP requests/responses, timing, cache и WebSocket frames. |
| HAR | Формат экспорта network activity из browser/proxy tools. |
| Breakpoint | Точка остановки выполнения script или изменения DOM. |
| WebSocket frames | Messages, которые идут через WebSocket connection. |
| localStorage | Browser storage, который сохраняется после закрытия browser. |
| sessionStorage | Browser storage, который живет в рамках tab/session. |
| Service Worker | Script между page и network/cache, часто используется в PWA. |
| Lighthouse | Automated audit tool для performance, accessibility, best practices, SEO и PWA. |

## Questions

### 1. Зачем QA использовать Chrome DevTools?

Answer: Чтобы видеть не только UI, но и DOM, CSS, JavaScript errors, network requests, storage, cache, performance и security signals.

### 2. Какая вкладка DevTools самая важная для анализа API request из браузера?

Answer: `Network`, потому что там видны method, URL, headers, payload, status code, response и timing.

### 3. Что проверить, если кнопка видна, но не нажимается?

Answer: DOM state, disabled attribute, overlay, z-index, CSS pointer behavior, Console errors и ушел ли request после click.

### 4. Чем `Elements` отличается от `Sources`?

Answer: `Elements` показывает DOM/CSS текущей страницы, а `Sources` используется для просмотра и отладки загруженного JavaScript/CSS source code.

### 5. Почему `Disable cache` полезен при тестировании?

Answer: Он помогает проверить поведение для пользователя без старых cached resources и поймать проблемы с обновлением assets после release.

### 6. Что можно проверить во вкладке `Application`?

Answer: Cookies, localStorage, sessionStorage, IndexedDB, Cache Storage, service workers, manifest и очистку browser-side state.

### 7. Когда стоит экспортировать HAR?

Answer: Когда нужно приложить к bug report полный network flow, особенно если проблема связана с redirects, headers, API calls, timing или failed requests.

### 8. Почему mobile emulation не заменяет реальные устройства?

Answer: DevTools хорошо эмулирует viewport и часть условий, но не полностью повторяет реальные browser engines, OS behavior, performance, touch, keyboard и device-specific issues.

## What To Review Later

- Как быстро открыть `Elements`, `Console` и device toolbar.
- Какие данные смотреть в `Network` для API bug.
- Как проверять cookies, localStorage, sessionStorage и cache.
- Как собрать хороший bug report с Console/Network evidence.
- Ограничения DevTools mobile emulation.
