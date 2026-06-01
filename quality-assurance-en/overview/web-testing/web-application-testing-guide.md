# Web Application Testing Guide

## Summary

Web application testing is the process of checking a website or web application before release to find defects and verify user experience, security, performance, and integrations.

A web application is usually a client-server system:

- browser acts as the client;
- web server/backend processes requests;
- database stores data;
- network, protocols, browsers, and devices affect user experience.

Main idea:

> Good web testing checks not only "the button was clicked", but the whole path: UI -> request -> server -> database -> response -> UI.

## What Is Web Testing?

Web testing is a software testing practice for websites and web applications.

Goals:

- find bugs before production;
- make sure the system works end to end;
- check compatibility with browsers/devices;
- make sure the website is usable and accessible;
- check performance under load;
- find security vulnerabilities;
- verify data consistency.

For a public website, it is especially important that users can quickly understand the page, complete actions, and avoid broken flows.

## Main Web Testing Areas

Main areas:

- functionality testing;
- usability testing;
- interface testing;
- compatibility testing;
- performance testing;
- security testing;
- database testing;
- production monitoring checks.

These testing types often overlap. For example, a login bug may involve functionality, security, cookies, UI messages, and database.

## Functionality Testing

Functionality testing checks that features work according to requirements.

Check:

- links;
- forms;
- buttons;
- navigation;
- search;
- filters;
- sorting;
- login/signup;
- upload/download;
- shopping cart;
- checkout;
- email notifications;
- cookies and sessions;
- database updates.

## Links

Check:

- internal links;
- external links;
- same-page anchor links;
- email links;
- broken links;
- orphan pages;
- links from sitemap;
- links in menus and footer.

A broken link may be a small UI issue, but to a user it reduces trust in the product.

## Forms

Forms are often a major source of defects.

Check:

- required fields;
- optional fields;
- default values;
- field validation;
- wrong input;
- boundary values;
- error messages;
- success messages;
- data saving;
- duplicate submit;
- file upload if present.

Example:

A signup flow may have several dependent steps. QA should check not only individual fields, but also the complete flow.

## Cookies And Sessions

Cookies are often used for sessions, login state, preferences, and tracking.

Check:

- login session persists correctly;
- session expires as expected;
- logout clears or invalidates session;
- app behavior when cookies disabled;
- cookie encryption/security if required;
- session behavior after deleting cookies;
- `HttpOnly`, `Secure`, `SameSite` flags for sensitive cookies.

## HTML/CSS Validation

HTML/CSS correctness affects rendering, accessibility, SEO, and cross-browser behavior.

Check:

- HTML syntax errors;
- broken layout;
- invalid nesting;
- missing alt text where relevant;
- crawlability if SEO matters;
- responsive CSS behavior;
- visual consistency.

## Database Functionality

Check that UI actions correctly affect data:

- insert;
- update;
- delete;
- search;
- filters;
- sorting;
- data retrieval;
- data consistency across pages.

If a user clicked Save and saw a success message, it still does not prove database state is correct.

## Usability Testing

Usability testing checks how comfortable the website is for real users.

Check:

- website easy to use;
- navigation clear;
- instructions understandable;
- main menu available;
- content logical;
- spelling and grammar;
- colors readable;
- fonts consistent;
- images placed correctly;
- help/search/sitemap available if expected.

## Navigation

Navigation should help the user understand:

- where they are;
- where they can go;
- how to go back;
- how to complete the flow.

Check:

- menu consistency;
- breadcrumbs if present;
- tab order;
- keyboard navigation;
- no dead-end pages;
- back/forward browser behavior;
- important pages reachable from main navigation.

## Content

Content should be:

- meaningful;
- structured;
- easy to read;
- free from spelling mistakes;
- visually consistent;
- not hidden by layout issues;
- relevant to user task.

For e-commerce, content is especially important: wrong price, wrong image, unclear delivery info, or missing description directly affects conversion.

## Interface Testing

Interface testing checks interactions between parts of the system.

Typical web interfaces:

- browser/frontend -> web server;
- web server -> application server;
- application server -> database;
- backend -> external services;
- backend -> email/payment/shipping systems.

Check:

- requests are sent correctly;
- server responses handled correctly;
- database errors handled safely;
- interrupted transactions handled correctly;
- connection reset does not corrupt data;
- user sees understandable error messages.

Example:

If database returns an error, application server should not show raw SQL error or stack trace to the user.

## Compatibility Testing

Compatibility testing checks that website works across user environments.

Main areas:

- browser compatibility;
- operating system compatibility;
- device compatibility;
- mobile browsing;
- printing options.

## Browser Compatibility

Check website in:

- Chrome;
- Firefox;
- Safari;
- Edge;
- mobile browsers.

Focus:

- layout;
- JavaScript behavior;
- AJAX/fetch requests;
- form controls;
- media playback;
- file upload;
- browser-specific settings.

## Operating System Compatibility

Check behavior on:

- Windows;
- macOS;
- Linux;
- Android;
- iOS.

Some UI, fonts, file handling, keyboard shortcuts, or browser features may behave differently.

## Mobile And Responsive Testing

Check:

- responsive layout;
- touch targets;
- screen rotation;
- text truncation;
- horizontal scrolling;
- mobile navigation;
- slow network behavior;
- real devices, not only emulators;
- different screen sizes.

Real devices are important because emulators do not always reproduce device-specific rendering, keyboard, browser, and performance issues.

## Printing

If website supports printing:

- page fits paper;
- fonts readable;
- graphics aligned;
- unnecessary UI hidden;
- important data included;
- print layout matches requirements.

## Performance Testing

Performance testing checks how website behaves under load and different network conditions.

Types:

- load testing;
- stress testing;
- connection speed testing;
- scalability testing;
- resource usage checks.

## Load Testing

Load testing checks expected traffic.

Questions:

- how many users per time unit;
- what is peak load;
- which pages are busiest;
- database response time;
- server response time;
- behavior when many users perform same action.

Example:

For e-commerce, peak load during sale season may be much higher than normal daily traffic.

## Stress Testing

Stress testing pushes system beyond expected limits.

Goal:

- find breaking point;
- see how system fails;
- check recovery;
- check logs and alerts;
- verify data not corrupted.

Common stress targets:

- login;
- signup;
- search;
- checkout;
- payment;
- file upload;
- database-heavy pages.

## Connection Speed

Check website under:

- fast connection;
- slow 3G/4G;
- unstable network;
- offline/online transitions;
- high latency.

User should see loading states, timeouts, and retry options instead of silent failure.

## Security Testing

Security testing helps find vulnerabilities and unsafe behavior.

Basic checks:

- internal pages not accessible without login;
- user cannot access another user's data by changing URL;
- invalid inputs handled safely;
- direct access to restricted files blocked;
- CAPTCHA works if required;
- HTTPS used for sensitive pages;
- error messages do not expose internals;
- security events logged.

## Access Control

Check:

- unauthenticated user blocked;
- authenticated user sees only allowed data;
- role-based permissions work;
- direct API calls do not bypass UI restrictions;
- IDOR issues prevented.

Example:

Changing `userId=123` to `userId=124` in URL or request must not expose another user's data.

## Input Security

Check:

- SQL injection attempts;
- XSS input;
- script tags;
- invalid file upload;
- overly long input;
- special characters;
- malformed JSON;
- path traversal attempts.

QA does not have to be a full security pentester for every project, but basic negative checks are essential.

## Types Of Websites And Testing Focus

## Static Website

Static website shows mostly the same content to visitors.

Focus:

- GUI;
- content;
- images;
- links;
- spelling;
- layout;
- loading speed;
- contact forms if present;
- SEO basics.

Static websites usually have fewer complex functions, but visual and content quality matter a lot.

## Dynamic Web Application

Dynamic web application has frontend and backend logic.

Focus:

- forms;
- login/signup;
- data updates;
- backend changes reflected on frontend;
- validation;
- upload;
- sorting/filtering;
- database consistency;
- role-based behavior.

## E-Commerce Website

E-commerce testing requires extra caution because defects can affect money, orders, and customer trust.

Focus:

- product listing;
- product details;
- search;
- filters;
- cart;
- coupons;
- shipping;
- taxes;
- payment gateway;
- order review;
- order confirmation;
- cancellation/return/exchange;
- inventory updates;
- email/SMS notifications.

Important checks:

- cart updates correctly;
- discounts apply only when expected;
- price remains correct across flow;
- payment failure handled safely;
- no duplicate orders after refresh or retry.

## Mobile Website

Mobile website is viewed in mobile browser.

Focus:

- real device testing;
- responsive layout;
- touch interactions;
- page scrolling;
- navigation;
- text truncation;
- image scaling;
- network speed;
- mobile-specific links;
- performance.

Mobile website is not the same as mobile app. Mobile website runs in browser and usually needs internet connection.

## Database Testing

Database testing verifies that website data is stored, changed, and retrieved correctly.

Check:

- UI and DB consistency;
- insert/update/delete actions;
- transaction behavior;
- DB connectivity;
- permissions;
- query performance;
- data integrity.

E-commerce examples:

- placing order creates correct records;
- canceling order updates status;
- return/exchange updates inventory and order history;
- payment status matches order status.

## Production Checks

After release, quality still needs monitoring.

Production checks can include:

- periodic smoke tests;
- SLA evidence and logs;
- response time monitoring;
- error rate monitoring;
- autoscaling checks;
- load balancer checks;
- real user experience monitoring;
- security event review;
- edge-case checks in real environment.

Production testing must be careful and controlled. Do not run destructive tests against real users or real payments unless process explicitly allows it.

## Questions To Ask Before Testing

Useful planning questions:

- What is expected server load?
- What response time is acceptable?
- Which browsers/devices are supported?
- Who is the target audience?
- What connection speeds are expected?
- Is downtime allowed for maintenance?
- What security requirements exist?
- How reliable must internet connection be?
- How are content updates managed?
- Are there standards for page layout?
- How are internal and external links maintained?
- Is separate test environment available?
- How should browser caching be handled?
- What logging and reporting are required?
- Which integrations must be tested?

## Example Web Testing Checklist

Use this as a compact starting checklist:

- links work;
- forms validate input;
- required fields enforced;
- errors are clear;
- cookies and sessions work;
- UI is readable and consistent;
- navigation is clear;
- website works in supported browsers;
- website works on supported devices;
- API requests and responses are correct;
- database state matches UI actions;
- performance acceptable under expected load;
- sensitive pages require authentication;
- authorization cannot be bypassed;
- HTTPS is used for sensitive actions;
- logs capture important failures;
- production smoke checks are defined.

## Common Mistakes

Common mistakes:

- testing only happy paths;
- ignoring cookies and session behavior;
- not checking database after UI action;
- testing only one browser;
- relying only on emulator for mobile;
- ignoring slow network;
- not testing unauthorized access;
- not checking broken links;
- skipping performance until production;
- not checking error handling between server and database;
- treating UI success message as proof of real success.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Web testing | Testing websites or web applications before or after release. |
| Functionality testing | Checking that features work as required. |
| Usability testing | Checking how easy and pleasant the website is to use. |
| Interface testing | Checking communication between system components. |
| Compatibility testing | Checking browsers, OS, devices and environments. |
| Performance testing | Checking speed, scalability and behavior under load. |
| Security testing | Checking vulnerabilities and access control. |
| Load testing | Testing expected or peak user load. |
| Stress testing | Testing beyond normal limits to see failure/recovery. |
| Static website | Website with mostly fixed content. |
| Dynamic web application | Web app with backend logic and changing data. |
| E-commerce testing | Testing purchase, cart, payment and order flows. |
| Production smoke test | Small safe check after deployment. |

## Questions

### 1. What is web testing?

Web testing is checking a website or web application for functionality, usability, compatibility, performance, security and data correctness.

### 2. Why is web testing more than UI testing?

Because web apps include browser, server, database, network, protocols, integrations and security behavior.

### 3. What should QA check in forms?

Required fields, validation, defaults, invalid input, error messages, submission behavior and data saving.

### 4. Why are cookies important in web testing?

They often control sessions, login state, preferences and security behavior.

### 5. Why is compatibility testing important?

Users open websites from different browsers, devices, operating systems and network conditions.

### 6. What is the difference between load and stress testing?

Load testing checks expected/peak load. Stress testing pushes the system beyond limits to observe failure and recovery.

### 7. Why should QA check database state?

UI success message does not guarantee data was saved, updated or deleted correctly.

### 8. Why are production checks needed?

Real environments can reveal issues with traffic, configuration, integrations, monitoring and infrastructure that were not visible in test environment.

## What To Review Later

- Client-Server Architecture
- Web Server
- HTTP Status Codes
- HTTP Headers
- Cookies
- CORS
- API Testing
- Performance Testing
- Security Testing
- Database Testing
