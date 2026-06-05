# HTML And CSS Fundamentals

Source: pasted article about HTML and CSS fundamentals  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, HTML, CSS, DOM, selectors, box model  
Language: English  
Translation pair: quality-assurance/overview/web-testing/html-css-fundamentals.md

## Summary

HTML and CSS are foundational web page technologies. HTML describes structure and meaning of content, while CSS controls visual presentation: colors, sizes, spacing, layout, and visual states.

For QA, this knowledge is not about building pages from scratch. It is about being able to:

- understand DOM in the `Elements` tab;
- find elements for bug reports and automation;
- distinguish content bugs from CSS/layout bugs;
- test responsive issues;
- explain to developers what exactly is broken in UI.

Main idea:

> QA does not have to be a frontend developer, but should understand HTML/CSS well enough to read a page as structure, not only as a picture.

## Key Points

- HTML consists of elements, tags, attributes, and nested structure.
- Semantic HTML helps accessibility, SEO, and maintainability.
- CSS selects elements with selectors and applies style rules to them.
- `id` should be unique on a page, while `class` can be used on many elements.
- CSS Box Model explains element size through `content`, `padding`, `border`, and `margin`.
- For QA, forms, links, buttons, images, lists, layout, visibility, and states are especially important.

## Notes

## What Is HTML?

HTML means HyperText Markup Language.

HTML tells the browser what structure exists on the page:

- headings;
- paragraphs;
- links;
- images;
- lists;
- forms;
- buttons;
- sections;
- tables.

HTML is not a programming language. It does not execute logic; it describes content and structure.

Example:

```html
<h1>Login</h1>
<p>Please enter your email and password.</p>
<button>Sign in</button>
```

For QA, HTML matters because the browser turns it into DOM, which is visible in Chrome DevTools.

## Elements And Tags

An HTML element usually consists of:

- opening tag;
- content;
- closing tag.

Example:

```html
<p>Hello, world!</p>
```

Here:

- `<p>` is the opening tag;
- `Hello, world!` is the content;
- `</p>` is the closing tag.

Some elements can be self-closing or do not use a separate closing tag in the usual way, for example images:

```html
<img src="logo.png" alt="Company logo">
```

## Common HTML Elements

| Element | Meaning | QA focus |
| --- | --- | --- |
| `<html>` | Root page element. | Usually not tested directly. |
| `<head>` | Metadata, title, links to CSS/JS. | Title, meta, connected resources. |
| `<body>` | Visible part of the page. | Main area for UI checks. |
| `<h1>`-`<h6>` | Headings. | Hierarchy, accessibility, SEO basics. |
| `<p>` | Paragraph. | Text content, wrapping, localization. |
| `<div>` | Generic block container. | Layout, grouping, CSS classes. |
| `<span>` | Generic inline container. | Inline text styling. |
| `<a>` | Link. | `href`, navigation, target, accessible text. |
| `<img>` | Image. | `src`, `alt`, loading, broken images. |
| `<ul>`, `<ol>`, `<li>` | Lists. | Correct order, bullet/number display, nesting. |
| `<input>` | Form input. | Type, validation, placeholder, disabled state. |
| `<button>` | Button. | Click behavior, disabled/loading state. |
| `<form>` | Form container. | Submit behavior, validation, errors. |

## Attributes

Attributes add extra information to HTML elements.

Example:

```html
<a href="/profile" class="nav-link" id="profile-link">Profile</a>
```

Here:

- `href` tells where the link goes;
- `class` helps style or find the element;
- `id` identifies one specific element.

QA often checks attributes in DevTools:

- `href` for links;
- `src` and `alt` for images;
- `type`, `name`, `value`, `placeholder` for inputs;
- `disabled`, `readonly`, `required`;
- `aria-*` attributes for accessibility;
- `data-testid` or similar attributes for automation.

## Nesting And Parent/Child Structure

HTML elements are nested inside other elements.

Example:

```html
<nav>
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/settings">Settings</a></li>
  </ul>
</nav>
```

`nav` is a parent, `ul` is its child, `li` elements are children of `ul`, and links are children of `li`.

For QA this matters because:

- layout depends on nesting;
- CSS selectors often depend on parent/child relationships;
- automation locators may use element hierarchy;
- a bug can happen because an element is placed in the wrong container.

## Semantic HTML

Semantic HTML means using elements according to their meaning, not only for visual result.

Examples:

- use `<button>` for clickable action, not clickable `<div>`;
- use `<a>` for navigation;
- use headings in meaningful order;
- use `<label>` for form fields;
- use `<main>`, `<nav>`, `<header>`, `<footer>` for page structure.

Why QA should care:

- screen readers rely on semantics;
- keyboard navigation works better with native controls;
- forms become easier to test and automate;
- SEO and accessibility improve;
- bugs appear when custom elements imitate native controls poorly.

## What Is CSS?

CSS means Cascading Style Sheets.

CSS controls how HTML looks:

- colors;
- fonts;
- font size;
- spacing;
- borders;
- backgrounds;
- layout;
- responsiveness;
- visibility;
- hover/focus states;
- animations.

Example:

```css
button {
  background-color: #005fcc;
  color: white;
  padding: 8px 12px;
}
```

## How CSS Is Connected To HTML

CSS can be added:

1. Inline, directly on an element.
2. Inside a `<style>` tag.
3. In an external CSS file connected with `<link>`.

External CSS is the normal production approach:

```html
<link rel="stylesheet" href="/styles.css">
```

For QA, missing or broken CSS often appears as:

- unstyled page;
- broken layout;
- wrong fonts/colors;
- missing icons;
- mobile layout not applied;
- old styles loaded from cache.

## CSS Selectors

Selectors define which HTML elements receive a style rule.

Common selectors:

```css
p {
  color: black;
}

.error-message {
  color: red;
}

#submit-button {
  background: green;
}
```

Meaning:

- `p` selects all `<p>` elements;
- `.error-message` selects elements with `class="error-message"`;
- `#submit-button` selects element with `id="submit-button"`.

QA should know selectors because they help:

- inspect styles in DevTools;
- communicate UI bugs;
- understand automation locators;
- verify whether CSS class/state changed after action.

## Id Vs Class

`id` should identify one unique element on the page.

```html
<button id="submit-button">Submit</button>
```

`class` can be shared by many elements.

```html
<p class="error-message">Email is required</p>
<p class="error-message">Password is required</p>
```

Practical QA note:

- duplicated `id` can break labels, scripts, anchors and automation;
- missing expected class can break styling or state;
- class names often show component state, for example `active`, `disabled`, `selected`, `error`.

## CSS Rule Syntax

CSS rule has:

- selector;
- property;
- value.

Example:

```css
.card {
  background-color: white;
  border: 1px solid #ddd;
  padding: 16px;
}
```

Each declaration usually ends with semicolon.

In DevTools, QA can temporarily disable or change a declaration to test whether it causes the visual bug.

## Common CSS Properties

| Property | What it controls | QA example |
| --- | --- | --- |
| `color` | Text color. | Text has too low contrast. |
| `background-color` | Element background. | Error block has wrong color. |
| `font-size` | Text size. | Text too small on mobile. |
| `width`, `height` | Element size. | Button or image wrong size. |
| `margin` | Space outside border. | Elements too close/far apart. |
| `padding` | Space inside border. | Text touches button edge. |
| `border` | Border around element. | Missing input error border. |
| `display` | Element layout/display mode. | Element hidden with `display: none`. |
| `position` | Element positioning. | Sticky header covers content. |
| `z-index` | Layer order. | Dropdown opens behind modal. |

## CSS Box Model

Browser treats many HTML elements as boxes.

The box model has four parts:

- `content` - actual text/image/content area;
- `padding` - space inside the element around content;
- `border` - line around padding/content;
- `margin` - space outside the element.

Example:

```css
.box {
  width: 200px;
  padding: 16px;
  border: 1px solid black;
  margin: 12px;
}
```

For QA, box model helps explain:

- why element is wider than expected;
- why content has too much/too little spacing;
- why two blocks overlap;
- why text touches border;
- why mobile layout breaks.

## QA Checks With HTML/CSS

When testing UI, QA can inspect:

- element exists in DOM;
- text is correct;
- link has correct `href`;
- image has correct `src` and `alt`;
- input has correct type and validation attributes;
- button is not accidentally disabled;
- class changes after state change;
- CSS rule is applied or overridden;
- element is visible and clickable;
- layout works at different widths;
- focus state is visible;
- content is semantic enough for accessibility.

## Common HTML/CSS Bugs

Typical bugs:

- broken or empty link;
- missing `alt` on meaningful image;
- duplicated `id`;
- wrong heading order;
- clickable `<div>` instead of button;
- text overlaps on mobile;
- button text does not fit;
- error message exists in DOM but is hidden;
- CSS class for error state is not applied;
- `z-index` puts dropdown behind another block;
- fixed header covers content;
- form label is not connected to input;
- style works in Chrome but breaks in Safari.

## Bug Report Tips

For HTML/CSS bugs include:

- page URL;
- browser and viewport;
- screenshot/video;
- exact element or area;
- expected and actual result;
- DevTools observation, if useful;
- CSS rule/class/attribute involved, if clear;
- whether bug reproduces in other browsers or screen sizes.

Example:

> On mobile width 390px, the `Submit` button text wraps into two lines and overlaps the icon. Reproduces in Chrome and Safari. In DevTools, `.submit-button` has fixed width `120px`; increasing width or allowing icon/text wrap fixes the issue.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| HTML | Markup language that describes page structure and content. |
| CSS | Stylesheet language that controls visual presentation. |
| Element | HTML unit represented by tag and content. |
| Tag | Markup syntax such as `<p>` or `</p>`. |
| Attribute | Extra element data such as `href`, `src`, `class`, `id`. |
| DOM | Browser's tree representation of HTML. |
| Selector | CSS pattern that selects elements for styling. |
| Class | Reusable attribute for styling/groups of elements. |
| ID | Unique element identifier on a page. |
| Box Model | CSS model of `content`, `padding`, `border`, `margin`. |
| Semantic HTML | HTML written according to meaning and structure. |

## Questions

### 1. Why should QA know HTML and CSS?

Answer: To understand DOM, analyze layout bugs, inspect elements in DevTools, write precise bug reports, and work better with automation locators.

### 2. How is HTML different from CSS?

Answer: HTML describes page structure and content, while CSS controls visual styling and layout.

### 3. What is an attribute?

Answer: Extra information inside an HTML tag, such as `href`, `src`, `class`, `id`, or `disabled`.

### 4. How is `id` different from `class`?

Answer: `id` should be unique on a page, while `class` can be used on many elements.

### 5. What is a CSS selector?

Answer: A pattern that selects HTML elements for applying CSS rules.

### 6. What is included in the CSS Box Model?

Answer: `content`, `padding`, `border`, and `margin`.

### 7. Why is semantic HTML important for QA?

Answer: It affects accessibility, keyboard navigation, forms, automation, and user experience quality.

## What To Review Later

- Main HTML elements: links, images, lists, forms, buttons.
- Attributes: `href`, `src`, `alt`, `class`, `id`, `type`, `disabled`.
- CSS selectors: element, class, id.
- Box Model: content, padding, border, margin.
- How to use DevTools `Elements`, `Styles`, and `Computed` for UI bugs.
