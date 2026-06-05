# Responsive Design Testing

Source: pasted article about responsive design  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, responsive design, mobile, viewport, CSS media queries  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/responsive-design-testing.md

## Summary

Responsive design - это подход, при котором website или web application адаптируется под разные screen sizes, devices, orientations и interaction modes без потери usability.

Для QA responsive design testing означает проверку, что content, layout, images, forms, navigation и interactive elements остаются usable на desktop, tablet и mobile.

Главная мысль:

> Responsive testing проверяет не только "влезает ли страница в экран", а может ли user удобно выполнить key flows на разных viewport sizes и real devices.

## Key Points

- Responsive design позволяет использовать один HTML/CSS/JS codebase для разных devices.
- Основные building blocks: viewport meta tag, flexible layout, relative units, CSS media queries, responsive images and navigation.
- Mobile-first thinking важен, потому что значительная часть users открывает web через mobile devices.
- DevTools помогает быстро проверять viewport sizes, но real devices нужны для проверки browser rendering, touch, keyboard, performance и platform-specific behavior.
- QA должен проверять text readability, no horizontal scroll, tap targets, images, forms, menus, orientation changes и critical flows.

## Notes

## What Is Responsive Design?

Responsive design позволяет странице адаптироваться к разным viewport sizes.

Страница должна:

- resize content;
- keep layout readable;
- avoid broken elements;
- adapt navigation;
- scale images;
- support touch interactions;
- work in portrait and landscape;
- keep important actions visible.

Responsive design отличается от отдельной mobile version тем, что обычно используется один application codebase, который меняет layout through CSS and frontend behavior.

## Why Responsive Design Matters

Пользователи открывают сайт с разных устройств:

- desktop monitors;
- laptops;
- tablets;
- phones;
- foldable devices;
- browsers with different zoom levels;
- landscape and portrait orientation.

Если сайт не responsive, users могут столкнуться с:

- horizontal scroll;
- tiny text;
- buttons too small to tap;
- overlapping content;
- hidden CTA;
- broken forms;
- unusable menu;
- images outside containers.

Для business это может означать lost conversions, checkout failures и poor user experience.

## Scope Before Testing

Перед responsive testing нужно понять:

- какие devices используют реальные users;
- какие browsers дают основную долю traffic;
- какие pages and flows critical;
- какие breakpoints заявлены design team;
- какие devices officially supported;
- какие known limitations есть у продукта.

Источники:

- analytics;
- product requirements;
- design specs;
- user support data;
- market/device usage reports;
- business priorities.

Не нужно одинаково глубоко тестировать все возможные widths. Нужно покрывать важные combinations.

## Viewport Meta Tag

Mobile browser должен понимать, как масштабировать page.

Обычно используют:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Если viewport meta tag отсутствует или настроен неверно, mobile browser может отрисовать страницу как desktop page, уменьшенную до tiny scale.

QA symptoms:

- текст слишком маленький;
- page открывается zoomed out;
- layout не соответствует mobile design;
- user вынужден zoom/scroll horizontally.

## CSS Media Queries

Media queries позволяют применять CSS rules в зависимости от screen width, height, orientation или других conditions.

Пример:

```css
@media (max-width: 640px) {
  .card {
    width: 100%;
  }

  .title {
    font-size: 18px;
  }
}
```

QA проверяет:

- корректность breakpoints;
- нет ли layout jump between breakpoints;
- content order остается логичным;
- styles не конфликтуют;
- desktop styles не ломают mobile и наоборот.

## Flexible Layout

Responsive layout обычно строится через:

- percentages;
- `max-width`;
- `min-width`;
- flexbox;
- CSS grid;
- relative units: `em`, `rem`, `%`, `vw`, `vh`;
- avoiding fixed widths where possible.

Fixed width часто вызывает bugs:

```css
.container {
  width: 1200px;
}
```

На mobile такой container может создать horizontal scroll.

## Responsive Text

Текст должен быть readable на всех supported viewport sizes.

QA проверяет:

- text is not too small;
- line length acceptable;
- headings do not overflow;
- button labels fit;
- translated text fits;
- text does not overlap icons;
- zoom does not break layout.

Особенно важно проверять:

- long words;
- localized strings;
- error messages;
- form labels;
- cards with dynamic content.

## Responsive Images

Images должны адаптироваться к containers.

Типичный CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

QA проверяет:

- image does not overflow container;
- aspect ratio is preserved;
- important part of image is not cropped;
- lazy loading works;
- image quality acceptable on high-density screens;
- page does not load unnecessarily huge images on mobile.

Performance note:

> Images часто составляют большую часть page weight, поэтому responsive images влияют не только на layout, но и на load time.

## Data Tables

Tables сложно адаптировать к small screens.

Подходы:

- horizontal scroll inside table container;
- transform rows into cards;
- hide secondary columns;
- show details after click/tap;
- use responsive table wrapper.

QA проверяет:

- user понимает, что table scrollable;
- important columns visible;
- no page-level horizontal scroll;
- sorting/filtering still works;
- rows remain readable;
- screen reader behavior acceptable.

## Navigation Menus

Navigation часто меняется между desktop and mobile.

Desktop:

- top menu;
- sidebar;
- dropdowns.

Mobile:

- hamburger menu;
- bottom navigation;
- hidden drawer;
- collapsible sections.

QA проверяет:

- menu opens/closes;
- all links available;
- focus and keyboard behavior;
- tap outside closes menu if expected;
- active state correct;
- menu does not cover important content incorrectly;
- scrolling inside menu works;
- orientation change does not break state.

## Forms On Mobile

Forms are high-risk responsive areas.

QA checks:

- labels visible;
- inputs not too small;
- validation messages fit;
- virtual keyboard does not hide active field or submit button;
- correct input types: email, tel, number, password;
- autocomplete behavior;
- date/time controls;
- error summary and focus behavior;
- submit action visible after keyboard opens.

## Orientation

Mobile/tablet users can rotate device.

QA проверяет:

- portrait and landscape;
- layout recalculates correctly;
- modal/dialog still fits;
- video/image orientation;
- forms keep entered data;
- no duplicated/stuck menu state;
- no horizontal scroll unless intentionally designed.

## Tools For Responsive Testing

Useful tools:

- Chrome DevTools device toolbar;
- Firefox Responsive Design Mode;
- Safari Web Inspector;
- BrowserStack/Sauce Labs/LambdaTest;
- real iOS/Android devices;
- responsive checker tools;
- Playwright/Selenium/WebDriverIO for automated checks.

DevTools is good for quick checks:

- viewport width/height;
- device presets;
- orientation;
- throttling;
- quick CSS debugging.

But real devices are still needed for:

- touch behavior;
- virtual keyboard;
- OS/browser rendering;
- performance;
- font rendering;
- device pixel ratio;
- Safari/iOS quirks.

## Manual Vs Automated Responsive Testing

Manual testing is useful for:

- visual review;
- exploratory checks;
- gestures;
- real device checks;
- UX and readability;
- comparing design with implementation.

Automation is useful for:

- checking critical pages at fixed viewport sizes;
- screenshot comparison;
- smoke flows on mobile/desktop widths;
- detecting horizontal overflow;
- checking visible elements and navigation;
- regression in CI.

Good approach:

> Automate repeatable viewport checks, but keep manual testing for visual quality and real-device behavior.

## Responsive Testing Checklist

Check:

- no horizontal scroll on main pages;
- text readable;
- buttons and links tappable;
- content remains inside containers;
- images resize correctly;
- navigation works;
- forms usable with virtual keyboard;
- modals fit screen;
- tables readable;
- orientation works;
- critical flows completed on mobile and desktop;
- layout matches design breakpoints;
- browser zoom does not break important content;
- performance acceptable on mobile.

## Common Responsive Bugs

Typical issues:

- text overlaps;
- CTA button hidden below sticky footer;
- menu cannot be closed;
- modal larger than viewport;
- image stretched or cropped badly;
- input hidden by keyboard;
- table causes page-level horizontal scroll;
- card grid breaks at one specific width;
- icon overlaps label;
- footer covers content;
- desktop hover-only behavior has no mobile alternative;
- responsive styles missing after CSS cache issue.

## Bug Report Tips

For responsive bugs include:

- URL/page;
- viewport width and height;
- device model;
- browser and OS;
- orientation;
- zoom level if relevant;
- screenshot/video;
- expected and actual result;
- whether bug reproduces in DevTools and real device;
- affected breakpoint;
- steps to reproduce.

Example:

> On iPhone 13 Safari, 390x844 portrait, checkout submit button is hidden behind sticky footer after keyboard opens. Reproduces only on real device, not in Chrome DevTools emulation. Expected: submit button remains visible or page scrolls to it.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Responsive design | Design approach where layout adapts to different screen sizes and devices. |
| Viewport | Visible browser area where page is rendered. |
| Breakpoint | Width/condition where layout changes. |
| Media query | CSS rule that applies styles based on screen/device conditions. |
| Mobile-first | Approach where mobile layout is designed first, then enhanced for larger screens. |
| Fluid layout | Layout using flexible sizes instead of fixed pixel widths. |
| Tap target | Interactive element area that should be large enough for touch. |
| Device pixel ratio | Ratio between physical pixels and CSS pixels. |
| Horizontal scroll | Sideways scrolling, often a responsive bug on mobile pages. |

## Questions

### 1. Что такое responsive design?

Answer: Это подход, при котором page layout адаптируется под разные screen sizes, devices and orientations.

### 2. Почему viewport meta tag важен?

Answer: Он говорит mobile browser, как масштабировать и подгонять страницу под device width.

### 3. Что такое breakpoint?

Answer: Это screen width или condition, при котором layout меняется.

### 4. Почему fixed width может быть проблемой?

Answer: Fixed width может не помещаться на small viewport и вызвать horizontal scroll или overlapping.

### 5. Почему DevTools emulation не заменяет real devices?

Answer: DevTools не полностью повторяет touch, virtual keyboard, real browser rendering, performance and device-specific behavior.

### 6. Что обязательно проверить в mobile forms?

Answer: Labels, input sizes, validation messages, correct keyboard type, visibility of active field and submit button.

### 7. Что указать в bug report для responsive issue?

Answer: URL, viewport, device, browser/OS, orientation, screenshot/video, expected/actual result and steps.

## What To Review Later

- Viewport meta tag.
- CSS media queries and breakpoints.
- Responsive text, images, tables and navigation.
- Real device vs DevTools emulation.
- Responsive testing checklist and bug report details.
