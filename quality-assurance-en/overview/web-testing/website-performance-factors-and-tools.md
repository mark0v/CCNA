# Website Performance Factors And Tools

Source: pasted article about website speed factors and tools  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, performance, page speed, Core Web Vitals, PageSpeed Insights  
Language: English  
Translation pair: quality-assurance/overview/web-testing/website-performance-factors-and-tools.md

## Summary

Website performance shows how quickly and reliably a site loads for users. For QA, it is not only a technical metric, but also part of user experience: a slow page increases bounce rate, lowers conversion rate, and can affect SEO.

When testing web applications, QA should be able to identify common reasons for slow loading, use performance tools, and report problems clearly.

Main idea:

> A beautiful interface does not help if the user waits too long for the page to load.

## Key Points

- Page speed affects user experience, conversion rate, and search ranking.
- Heavy CSS, JavaScript, weak hosting, inefficient code, too many plugins, and hotlinking can slow down a website.
- Performance should be checked on desktop and mobile because network and device conditions differ.
- Core Web Vitals help evaluate real user experience.
- Google PageSpeed Insights and WebPageTest are useful for diagnosing problems.
- QA should look beyond the overall score and focus on specific metrics, reproducible steps, and user impact.

## Notes

## Why Website Performance Matters

A slow website creates several risks:

- the user leaves before the page loads;
- forms and checkout are used less often;
- mobile users receive a worse experience;
- search engines may rank the page lower;
- the team loses trust in the product;
- support receives more complaints.

For QA, a performance issue is not just "the page is slow." A good bug report should show where the problem appears, under what conditions it appears, and why it matters.

## Common Factors That Slow Down A Website

## Heavy CSS And JavaScript

CSS and JavaScript add layout, styling, and interactivity, but files that are too large or loaded incorrectly slow down rendering.

Typical problems:

- large JavaScript bundles;
- render-blocking scripts;
- unused CSS;
- too many third-party scripts;
- tracking scripts in the critical rendering path;
- animations that block smooth interaction.

QA focus:

- check page load on mobile;
- review Lighthouse warnings;
- check First Contentful Paint and Largest Contentful Paint;
- inspect the Network tab in DevTools;
- compare first load and repeat load.

## Bad Server Or Hosting

Hosting affects Time To First Byte, stability, and the site's ability to handle traffic.

Risks:

- slow server response;
- overloaded shared hosting;
- weak database performance;
- no CDN;
- poor configuration;
- unstable uptime.

QA focus:

- measure TTFB;
- check the site from different locations if needed;
- compare staging and production carefully;
- collect evidence from monitoring;
- record exact time and environment.

## Poor Coding Standards

Inefficient code can create extra work for the browser and server.

Examples:

- unnecessary DOM elements;
- duplicated scripts;
- heavy inline styles;
- unoptimized loops or client-side logic;
- large HTML output;
- no minification;
- unused libraries.

QA does not have to rewrite the code, but should recognize the symptoms:

- the page takes too long to become interactive;
- the browser freezes;
- scrolling is not smooth;
- CPU usage is high;
- the Network tab shows unnecessary resources.

## Too Many Widgets And Plugins

CMS sites, especially WordPress-like projects, often use plugins and widgets. Each plugin may add scripts, styles, database queries, or external requests.

Risks:

- slow page load;
- plugin conflicts;
- broken layout after update;
- security issues;
- excessive third-party requests;
- worse mobile performance.

QA focus:

- check pages after plugin updates;
- compare performance before and after changes;
- check console errors;
- review network requests;
- confirm that unused plugins are disabled or removed.

## Hotlinking

Hotlinking happens when another website uses images hosted on your server. Your server serves those images for someone else's page, which can consume bandwidth and slow down your site.

QA usually does not configure protection directly, but should understand the risk.

Symptoms:

- unexpected bandwidth usage;
- server load without matching real traffic;
- slow image delivery;
- hosting warnings or limits.

Possible prevention:

- server rules;
- CDN configuration;
- referrer checks;
- media protection settings.

## Client-Side Factors

Sometimes the issue is not only the website. User-side conditions also matter:

- slow network;
- old device;
- low memory;
- browser extensions;
- VPN or proxy;
- outdated browser;
- mobile battery-saving mode.

QA should separate product issue from environment issue by reproducing on multiple devices, browsers, networks, or test profiles.

## Important Performance Metrics

| Metric | Meaning |
| --- | --- |
| TTFB | Time To First Byte. How fast the server starts responding. |
| FCP | First Contentful Paint. When first visible content appears. |
| LCP | Largest Contentful Paint. When the main content is likely loaded. |
| CLS | Cumulative Layout Shift. How much layout jumps during loading. |
| INP | Interaction to Next Paint. How responsive the page is to user input. |
| Total Blocking Time | How long JavaScript blocks the main thread. |
| Page weight | Total size of resources loaded by the page. |
| Requests count | Number of network requests needed to load the page. |

## Core Web Vitals

Core Web Vitals are Google metrics focused on user experience.

Current key metrics:

- LCP: loading performance;
- INP: interaction responsiveness;
- CLS: visual stability.

QA should use them as signals, not as the only truth. A high score is useful, but real user flows still need testing: login, search, product page, checkout, dashboard, forms, and other important pages.

## Tools To Check Website Speed

## Google PageSpeed Insights

Google PageSpeed Insights analyzes a page and provides:

- mobile and desktop performance scores;
- Core Web Vitals;
- opportunities for improvement;
- diagnostics;
- passed audits;
- Lighthouse-based recommendations.

QA focus:

- run tests for key pages;
- compare mobile and desktop results;
- save reports or screenshots;
- note exact URL and test date;
- avoid reporting only the score without context.

## WebPageTest

WebPageTest is a detailed performance testing tool that can run tests from different locations and browsers.

Useful features:

- first view and repeat view;
- location selection;
- browser selection;
- waterfall chart;
- filmstrip/video view;
- multiple test runs;
- advanced settings.

QA focus:

- use repeatable settings;
- compare first load and cached load;
- inspect waterfall for blocking resources;
- check if CDN/cache works;
- use screenshots or filmstrip for evidence.

## Chrome DevTools

Chrome DevTools helps investigate performance locally.

Useful tabs:

- Network;
- Performance;
- Lighthouse;
- Coverage;
- Console.

QA can use DevTools to:

- see slow resources;
- throttle network;
- test mobile viewport;
- identify large JavaScript files;
- check cache behavior;
- capture screenshots and HAR files.

## Practical QA Checklist

Before reporting a website speed issue, check:

- exact URL;
- environment: production, staging, or local;
- browser and version;
- device and OS;
- network condition;
- first load or repeat load;
- logged-in or guest state;
- cache enabled or disabled;
- ad blockers or extensions;
- test tool and settings;
- whether issue reproduces consistently.

## Common Bugs

Typical website performance bugs:

- homepage takes too long to show main content;
- mobile page is much slower than desktop;
- layout jumps while images load;
- page becomes visible but button is not clickable;
- checkout is slow under normal usage;
- large image is loaded instead of optimized version;
- unused JavaScript delays rendering;
- third-party script blocks page load;
- server response time is too high;
- cache is not working after repeat visit.

## Bug Report Tips

For performance bugs include:

- page URL;
- scenario;
- browser/device/network;
- tool used;
- test settings;
- expected threshold;
- actual result;
- screenshot or report link;
- waterfall/HAR if useful;
- business impact if known.

Example:

> Mobile performance issue on `/pricing`: LCP is 6.4s in PageSpeed Insights and main hero image is loaded as a 3.8 MB desktop asset. Expected: LCP under 2.5s and optimized mobile image. Reproduces on Chrome mobile emulation and Android device on 4G profile.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Page speed | How quickly a web page loads and becomes usable. |
| Core Web Vitals | Google metrics for loading, interactivity and visual stability. |
| Lighthouse | Audit engine used by Chrome DevTools and PageSpeed Insights. |
| TTFB | Time needed for the server to start responding. |
| FCP | First visible content on the page. |
| LCP | Time when the largest important content element is rendered. |
| CLS | Metric for unexpected layout shifts. |
| INP | Metric for responsiveness to user input. |
| CDN | Content Delivery Network used to serve assets closer to users. |
| Hotlinking | Using another site's hosted media directly by URL. |
| Waterfall chart | Network timeline showing when resources load. |
| HAR | HTTP Archive file with network request details. |

## Questions

### 1. Why does website performance matter for QA?

Answer: Because speed affects user experience, conversion, SEO, and the ability to complete key user flows.

### 2. What can make a website slow?

Answer: Heavy CSS/JavaScript, weak hosting, poor code, too many plugins, large assets, hotlinking, and third-party scripts.

### 3. Why should QA check mobile performance separately?

Answer: Mobile devices often have slower networks, weaker hardware, and different rendering constraints.

### 4. What is the difference between PageSpeed Insights and WebPageTest?

Answer: PageSpeed Insights gives Lighthouse-based recommendations and Core Web Vitals signals, while WebPageTest provides deeper test configuration, waterfall analysis, and first/repeat view comparison.

### 5. Why is a performance score alone not enough in a bug report?

Answer: The score does not explain the exact user impact, environment, reproducibility, or root symptom.

### 6. What evidence is useful for website speed bugs?

Answer: Tool report, screenshot, exact URL, device/browser/network, metrics, waterfall or HAR file, and clear expected vs actual result.

## What To Review Later

- Core Web Vitals: LCP, INP, CLS.
- Chrome DevTools Network and Performance tabs.
- PageSpeed Insights reports.
- WebPageTest waterfall and filmstrip.
- How to write performance bug reports.
