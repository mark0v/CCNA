# HTML And CSS Fundamentals

Source: pasted article about HTML and CSS fundamentals  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, HTML, CSS, DOM, selectors, box model  
Language: Russian  
Translation pair: quality-assurance-en/overview/web-testing/html-css-fundamentals.md

## Summary

HTML и CSS - базовые технологии web page. HTML описывает структуру и смысл content, а CSS отвечает за внешний вид: цвета, размеры, отступы, layout и visual states.

Для QA эти знания нужны не для того, чтобы верстать страницы с нуля, а чтобы уверенно:

- понимать DOM во вкладке `Elements`;
- находить элементы для bug reports и automation;
- отличать content bug от CSS/layout bug;
- проверять responsive issues;
- объяснять developers, что именно сломалось в UI.

Главная мысль:

> QA не обязан быть frontend developer, но должен понимать HTML/CSS достаточно, чтобы читать страницу как структуру, а не только как картинку.

## Key Points

- HTML состоит из elements, tags, attributes и nested structure.
- Semantic HTML помогает accessibility, SEO и maintainability.
- CSS выбирает элементы через selectors и применяет к ним style rules.
- `id` должен быть уникальным на странице, а `class` можно использовать на многих элементах.
- CSS Box Model объясняет размеры элемента через `content`, `padding`, `border` и `margin`.
- Для QA особенно важны forms, links, buttons, images, lists, layout, visibility и states.

## Notes

## What Is HTML?

HTML расшифровывается как HyperText Markup Language.

HTML говорит browser, какая структура есть у страницы:

- headings;
- paragraphs;
- links;
- images;
- lists;
- forms;
- buttons;
- sections;
- tables.

HTML не является programming language. Он не выполняет logic, а описывает content and structure.

Пример:

```html
<h1>Login</h1>
<p>Please enter your email and password.</p>
<button>Sign in</button>
```

Для QA HTML важен, потому что именно его browser превращает в DOM, который виден в Chrome DevTools.

## Elements And Tags

HTML element обычно состоит из:

- opening tag;
- content;
- closing tag.

Пример:

```html
<p>Hello, world!</p>
```

Здесь:

- `<p>` - opening tag;
- `Hello, world!` - content;
- `</p>` - closing tag.

Некоторые элементы могут быть self-closing или не иметь отдельного closing tag в привычном виде, например images:

```html
<img src="logo.png" alt="Company logo">
```

## Common HTML Elements

| Element | Meaning | QA focus |
| --- | --- | --- |
| `<html>` | Root element страницы. | Обычно не тестируется напрямую. |
| `<head>` | Metadata, title, links to CSS/JS. | Проверка title, meta, connected resources. |
| `<body>` | Видимая часть страницы. | Основная область UI checks. |
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

### 1. Зачем QA знать HTML и CSS?

Answer: Чтобы понимать DOM, анализировать layout bugs, проверять элементы в DevTools, писать точные bug reports и лучше работать с automation locators.

### 2. Чем HTML отличается от CSS?

Answer: HTML описывает структуру и content страницы, а CSS управляет visual styling and layout.

### 3. Что такое attribute?

Answer: Это дополнительная информация внутри HTML tag, например `href`, `src`, `class`, `id`, `disabled`.

### 4. Чем `id` отличается от `class`?

Answer: `id` должен быть уникальным на странице, а `class` может использоваться на многих элементах.

### 5. Что такое CSS selector?

Answer: Это pattern, который выбирает HTML elements для применения CSS rules.

### 6. Что входит в CSS Box Model?

Answer: `content`, `padding`, `border` и `margin`.

### 7. Почему semantic HTML важен для QA?

Answer: Он влияет на accessibility, keyboard navigation, forms, automation и качество user experience.

## What To Review Later

- Основные HTML elements: links, images, lists, forms, buttons.
- Attributes: `href`, `src`, `alt`, `class`, `id`, `type`, `disabled`.
- CSS selectors: element, class, id.
- Box Model: content, padding, border, margin.
- Как использовать DevTools `Elements`, `Styles` и `Computed` для UI bugs.
