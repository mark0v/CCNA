# Responsive Design Testing

Source: pasted article about responsive design  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, responsive design, mobile, viewport, CSS media queries  
Language: English  
Translation pair: quality-assurance/overview/web-testing/responsive-design-testing.md

## Summary

Responsive design is an approach where a website or web application adapts to different screen sizes, devices, orientations, and interaction modes without losing usability.

For QA, responsive design testing means verifying that content, layout, images, forms, navigation, and interactive elements remain usable on desktop, tablet, and mobile.

Main idea:

> Responsive testing checks not only whether a page fits the screen, but whether the user can comfortably complete key flows across viewport sizes and real devices.

## Key Points

- Responsive design allows one HTML/CSS/JS codebase to support different devices.
- Main building blocks: viewport meta tag, flexible layout, relative units, CSS media queries, responsive images and navigation.
- Mobile-first thinking matters because many users access web products from mobile devices.
- DevTools helps quickly test viewport sizes, but real devices are needed for browser rendering, touch, keyboard, performance, and platform-specific behavior.
- QA should verify text readability, no horizontal scroll, tap targets, images, forms, menus, orientation changes, and critical flows.

## Notes

## What Is Responsive Design?

Responsive design lets a page adapt to different viewport sizes.

The page should:

- resize content;
- keep layout readable;
- avoid broken elements;
- adapt navigation;
- scale images;
- support touch interactions;
- work in portrait and landscape;
- keep important actions visible.

Responsive design differs from a separate mobile version because it usually uses one application codebase that changes layout through CSS and frontend behavior.

## Why Responsive Design Matters

Users open websites from many devices:

- desktop monitors;
- laptops;
- tablets;
- phones;
- foldable devices;
- browsers with different zoom levels;
- landscape and portrait orientation.

If the site is not responsive, users may face:

- horizontal scroll;
- tiny text;
- buttons too small to tap;
- overlapping content;
- hidden CTA;
- broken forms;
- unusable menu;
- images outside containers.

For business, this may mean lost conversions, checkout failures, and poor user experience.

## Scope Before Testing

Before responsive testing, understand:

- which devices real users use;
- which browsers have the main traffic share;
- which pages and flows are critical;
- which breakpoints are defined by design team;
- which devices are officially supported;
- which known limitations exist.

Sources:

- analytics;
- product requirements;
- design specs;
- user support data;
- market/device usage reports;
- business priorities.

You do not need to test all possible widths equally deeply. Cover important combinations.

## Viewport Meta Tag

Mobile browser needs to know how to scale the page.

Usually:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

If the viewport meta tag is missing or incorrect, a mobile browser may render the page as a desktop page scaled down to a tiny size.

QA symptoms:

- text is too small;
- page opens zoomed out;
- layout does not match mobile design;
- user has to zoom or scroll horizontally.

## CSS Media Queries

Media queries apply CSS rules depending on screen width, height, orientation, or other conditions.

Example:

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

QA checks:

- breakpoints are correct;
- no layout jump appears between breakpoints;
- content order remains logical;
- styles do not conflict;
- desktop styles do not break mobile and vice versa.

## Flexible Layout

Responsive layout is usually built with:

- percentages;
- `max-width`;
- `min-width`;
- flexbox;
- CSS grid;
- relative units: `em`, `rem`, `%`, `vw`, `vh`;
- avoiding fixed widths where possible.

Fixed width often causes bugs:

```css
.container {
  width: 1200px;
}
```

On mobile, this container may create horizontal scroll.

## Responsive Text

Text should be readable on all supported viewport sizes.

QA checks:

- text is not too small;
- line length acceptable;
- headings do not overflow;
- button labels fit;
- translated text fits;
- text does not overlap icons;
- zoom does not break layout.

Especially important:

- long words;
- localized strings;
- error messages;
- form labels;
- cards with dynamic content.

## Responsive Images

Images should adapt to containers.

Typical CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

QA checks:

- image does not overflow container;
- aspect ratio is preserved;
- important part of image is not cropped;
- lazy loading works;
- image quality acceptable on high-density screens;
- page does not load unnecessarily huge images on mobile.

Performance note:

> Images often make up a large part of page weight, so responsive images affect not only layout, but also load time.

## Data Tables

Tables are hard to adapt to small screens.

Approaches:

- horizontal scroll inside table container;
- transform rows into cards;
- hide secondary columns;
- show details after click/tap;
- use responsive table wrapper.

QA checks:

- user understands that table is scrollable;
- important columns are visible;
- no page-level horizontal scroll;
- sorting/filtering still works;
- rows remain readable;
- screen reader behavior acceptable.

## Navigation Menus

Navigation often changes between desktop and mobile.

Desktop:

- top menu;
- sidebar;
- dropdowns.

Mobile:

- hamburger menu;
- bottom navigation;
- hidden drawer;
- collapsible sections.

QA checks:

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

Mobile/tablet users can rotate the device.

QA checks:

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

### 1. What is responsive design?

Answer: An approach where page layout adapts to different screen sizes, devices, and orientations.

### 2. Why is the viewport meta tag important?

Answer: It tells the mobile browser how to scale and fit the page to the device width.

### 3. What is a breakpoint?

Answer: A screen width or condition where layout changes.

### 4. Why can fixed width be a problem?

Answer: Fixed width may not fit a small viewport and can cause horizontal scroll or overlapping.

### 5. Why does DevTools emulation not replace real devices?

Answer: DevTools does not fully reproduce touch, virtual keyboard, real browser rendering, performance, and device-specific behavior.

### 6. What must be checked in mobile forms?

Answer: Labels, input sizes, validation messages, correct keyboard type, visibility of active field and submit button.

### 7. What should be included in a bug report for a responsive issue?

Answer: URL, viewport, device, browser/OS, orientation, screenshot/video, expected/actual result, and steps.

## What To Review Later

- Viewport meta tag.
- CSS media queries and breakpoints.
- Responsive text, images, tables and navigation.
- Real device vs DevTools emulation.
- Responsive testing checklist and bug report details.
