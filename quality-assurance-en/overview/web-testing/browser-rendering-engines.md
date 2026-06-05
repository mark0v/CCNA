# Browser Rendering Engines

Source: pasted article about rendering engines in browsers  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, browsers, rendering engine, compatibility, cross browser testing  
Language: English  
Translation pair: quality-assurance/overview/web-testing/browser-rendering-engines.md

## Summary

A rendering engine is the browser component that turns HTML, CSS, images, and some JavaScript-driven results into the visual page on screen.

For QA, this topic matters because different browsers may use different rendering engines:

- Chrome, Edge, and Opera use `Blink`;
- Safari uses `WebKit`;
- Firefox uses `Gecko`;
- old Internet Explorer used `Trident`.

Because of this, the same web page may look or behave slightly differently across browsers. This is why cross browser testing is not a formality, but a practical protection against browser-specific bugs.

## Key Points

- A browser consists of several components: user interface, browser engine, rendering engine, networking, JavaScript engine, UI backend, and data storage.
- The rendering engine parses HTML/CSS, builds the DOM tree and render tree, calculates layout, and paints the page.
- JavaScript can change DOM/CSSOM, so the page may be re-rendered after user actions or network responses.
- Different rendering engines may handle CSS, HTML, fonts, forms, scrolling, animations, and mobile viewport differently.
- QA should understand rendering basics to investigate layout bugs, responsive issues, and cross browser defects more effectively.

## Notes

## Why Rendering Engines Matter For QA

When a user opens a website, the browser does not simply display an HTML file as text. It:

- receives resources over the network;
- parses HTML;
- loads CSS, images, fonts, and scripts;
- applies styles;
- calculates sizes and positions;
- paints the result on screen;
- reacts to JavaScript, user actions, and data changes.

If everything looks correct in Chrome, that does not guarantee Safari or Firefox will show the page exactly the same way. The difference may be small, such as a different scrollbar, or critical, such as a checkout button moving outside the screen.

## Main Browser Components

## User Interface

User interface means browser controls around the page:

- address bar;
- back/forward buttons;
- reload;
- tabs;
- bookmarks;
- browser menus.

QA usually does not test browser UI directly, but should understand that it is not part of the web application. The web app is inside the viewport.

## Browser Engine

The browser engine connects the user interface and the rendering engine.

It receives actions from browser UI and coordinates how the page loads, updates, and renders.

For example, when the user clicks reload, the browser engine coordinates the process: the networking layer fetches resources, the rendering engine rebuilds the page, and cache may participate in loading.

## Rendering Engine

The rendering engine is responsible for displaying web content.

It works with:

- HTML;
- CSS;
- images;
- fonts;
- XML/SVG in some cases;
- visual results after JavaScript changes.

The rendering engine determines how DOM and CSS become pixels on screen.

## Networking

The networking component sends and receives data through protocols:

- HTTP;
- HTTPS;
- FTP in older scenarios;
- WebSocket;
- other network mechanisms.

For QA, this connects to the `Network` tab in DevTools, where you can see which resources the browser loaded and which requests went to the backend.

## JavaScript Engine

The JavaScript engine parses and executes JavaScript.

Examples:

- Chrome/Edge - V8;
- Firefox - SpiderMonkey;
- Safari - JavaScriptCore.

JavaScript can:

- change DOM;
- change classes/styles;
- send network requests;
- create animations;
- handle user events.

Rendering and JavaScript are closely connected: once a script changes state, the rendering engine may need to update the visual result.

## UI Backend

The UI backend uses operating system capabilities to draw basic widgets, fonts, windows, and controls.

Because of this, native controls may look different on Windows, macOS, iOS, and Android.

## Data Storage / Persistence

The browser stores data locally:

- cookies;
- localStorage;
- sessionStorage;
- IndexedDB;
- Cache Storage;
- service worker data.

For QA, this matters when testing login, logout, sessions, cache, PWA, and stale data issues.

## How Rendering Works

Simplified rendering flow:

1. Browser receives an HTML document.
2. Rendering engine parses HTML and builds the DOM tree.
3. Browser loads and parses CSS.
4. Styles are applied to DOM nodes.
5. Render tree is created: only visual elements that need to be drawn.
6. Layout calculates element sizes and coordinates.
7. Paint draws pixels on screen.
8. Composite combines layers into the final image.

The real process is more complex, but this model is enough for QA to understand many UI bugs.

## DOM Tree

DOM tree is the structural tree of HTML elements.

Example:

```html
<main>
  <h1>Checkout</h1>
  <button>Pay</button>
</main>
```

The browser converts this into nodes that JavaScript can work with and that can be inspected in the `Elements` tab.

## CSSOM And Styles

CSS rules become style information.

The browser needs to understand:

- which selectors match an element;
- which rules conflict;
- which specificity is higher;
- which values are inherited;
- which computed values are produced.

In DevTools, this can be inspected through `Styles` and `Computed`.

## Render Tree

The render tree contains only what needs to be visually drawn.

For example, an element with `display: none` exists in DOM, but does not enter the render tree.

For QA, this matters because:

- an element may exist in DOM but be invisible;
- a hidden element may still affect accessibility or scripts;
- an overlay may be visible and block another element.

## Layout

Layout calculates element sizes and positions.

This is where the browser determines:

- width/height;
- margins;
- padding;
- position;
- flex/grid behavior;
- line wrapping;
- responsive breakpoints.

Many visual bugs are layout bugs:

- text overlaps;
- button goes outside a container;
- content jumps;
- fixed header covers a form;
- mobile layout breaks at a specific width.

## Paint And Composite

Paint draws visual parts:

- text;
- backgrounds;
- borders;
- shadows;
- images.

Composite combines layers, such as fixed headers, modal overlays, transformed elements, and animations.

If a layer or `z-index` is wrong, QA may see:

- modal behind page content;
- dropdown under header;
- tooltip hidden;
- clickable area blocked by an invisible element.

## Popular Rendering Engines

| Rendering engine | Browsers | QA notes |
| --- | --- | --- |
| Blink | Chrome, Edge, Opera | Most common engine for Chromium-based browsers. |
| WebKit | Safari, iOS browsers | Critical for iPhone/iPad testing; iOS browsers use WebKit. |
| Gecko | Firefox | May differ in CSS/layout behavior and standards implementation. |
| Trident | Legacy Internet Explorer | Appears only in legacy/corporate contexts. |

## Why Browsers Render Differently

Even with open web standards, browsers may differ because:

- standards implementation is not always identical;
- new CSS/JS features do not arrive at the same time;
- browser bugs exist;
- mobile browsers have additional limitations;
- fonts and native controls depend on OS;
- default styles may differ;
- security policies may be stricter or softer.

QA should not assume that if a feature works in Chrome, it automatically works in Safari and Firefox.

## QA Examples

## Example 1: CSS Layout Bug In Safari

In Chrome, a card grid looks correct, but in Safari cards overlap.

What to check:

- CSS Grid/Flex support;
- computed styles;
- browser-specific CSS bug;
- viewport width;
- media queries;
- Safari version.

## Example 2: Button Hidden On Mobile

On desktop, a button is visible, but on iPhone it is below the viewport and cannot be reached by scrolling.

What to check:

- mobile viewport height;
- fixed/sticky elements;
- virtual keyboard behavior;
- overflow;
- safe area on iOS;
- responsive breakpoint.

## Example 3: Different Form Control

A date input looks and behaves differently in Chrome and Safari.

What to check:

- native browser control behavior;
- expected product requirements;
- custom fallback;
- validation;
- accessibility.

## How QA Uses This Knowledge

Rendering engine basics help QA:

- understand visual bugs faster;
- distinguish frontend bugs from browser limitations;
- choose the right browser matrix;
- write precise bug reports;
- verify CSS fixes in the affected browser;
- understand why real device testing is more important than a Chrome-only check.

## What To Include In A Rendering Bug Report

For a visual/browser-specific bug, include:

- browser name and version;
- rendering engine, if relevant;
- OS and version;
- device model;
- viewport size;
- zoom level;
- screenshot/video;
- expected and actual result;
- whether the bug reproduces in other browsers;
- relevant CSS/DOM observation from DevTools;
- console errors, if any.

Example:

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

### 1. What does a rendering engine do?

Answer: It parses HTML/CSS, builds visual structures, calculates layout, and paints the page on screen.

### 2. Why are rendering engines important for cross browser testing?

Answer: Different engines may interpret HTML, CSS, JavaScript effects, fonts, forms, and layout behavior differently.

### 3. Which browsers use Blink?

Answer: Chrome, Edge, Opera, and other Chromium-based browsers.

### 4. Why should Safari be tested separately?

Answer: Safari uses WebKit, and iOS browsers are also tied to WebKit, so behavior may differ from Chrome/Firefox.

### 5. What is layout in the rendering flow?

Answer: It is the stage where the browser calculates element sizes and coordinates on the page.

### 6. Why can an element exist in DOM but not be displayed?

Answer: For example, if it has `display: none`, it remains in DOM but does not enter the render tree.

### 7. What should be added to a bug report for a visual browser bug?

Answer: Browser/version, OS, device, viewport, screenshot/video, expected/actual result, and comparison with other browsers.

## What To Review Later

- Difference between browser engine, rendering engine, and JavaScript engine.
- Main rendering flow stages: DOM, CSSOM, render tree, layout, paint, composite.
- Blink, WebKit, Gecko, and where they are used.
- How rendering differences create cross browser bugs.
- Which details are needed in a visual/browser-specific bug report.
