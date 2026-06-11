# Website Performance Testing For QA

Source: user-provided Plerdy article, corrected with current Web Vitals guidance
Date added: 2026-06-11
Related plan item: Performance Testing
Tags: QA, performance testing, website performance, Core Web Vitals, Lighthouse, WebPageTest
Language: English
Translation pair: quality-assurance/overview/06-performance-testing/website-performance-testing.md

## Summary

Website performance depends on the complete delivery chain:

```text
DNS/TLS -> CDN/server -> HTML -> CSS/JS/fonts/images
-> browser main thread -> rendering -> user interaction
```

QA should combine:

- **lab testing:** controlled synthetic measurements;
- **field/RUM data:** real users, devices, and networks;
- **load testing:** backend behavior under concurrent traffic;
- **functional checks:** correctness under slow and failed conditions.

One Lighthouse score or one page-load value cannot describe the complete user experience.

## Key Points

- Current Core Web Vitals are `LCP`, `INP`, and `CLS`.
- Recommended field thresholds are LCP <= 2.5 s, INP <= 200 ms, and CLS <= 0.1 at the 75th percentile.
- Lighthouse cannot measure real field INP; Total Blocking Time is a lab proxy.
- Field and lab results answer different questions.
- TTFB helps diagnose server and network contribution but is not complete page performance.
- Heavy JavaScript, render-blocking resources, images, fonts, and third parties are common bottlenecks.
- Test cold and warm cache, mobile and desktop, different networks, and geographies.
- Performance budgets should cover user metrics and resource sizes or counts.
- Website speed testing and server load testing complement each other.

## Notes

## Lab Versus Field Data

| Data | Strength | Limitation |
| --- | --- | --- |
| Lab | Repeatable, debuggable, works before release | Simulated device, network, and interaction |
| Field/RUM | Real users, devices, networks, and behavior | Noisier, delayed, requires enough traffic |

Use lab data to diagnose and prevent regressions. Use field data to understand actual user experience.

PageSpeed Insights can contain:

- Chrome User Experience Report field data when available;
- Lighthouse lab audit.

Do not compare them as identical measurements.

## Core Web Vitals

| Metric | Meaning | Good threshold |
| --- | --- | ---: |
| LCP | Loading of the largest visible content element | <= 2.5 s |
| INP | Responsiveness across user interactions | <= 200 ms |
| CLS | Visual stability | <= 0.1 |

Evaluate the 75th percentile separately for mobile and desktop field traffic.

FID was replaced by INP as a Core Web Vital in 2024.

## Supporting Metrics

- **TTFB:** time until the first response byte;
- **FCP:** first rendered text, image, or content;
- **TBT:** lab measure of main-thread blocking;
- **Speed Index:** how quickly visible content appears;
- **DOMContentLoaded/load:** browser lifecycle events;
- **resource size/count:** transfer and request cost.

No supporting metric should become a universal pass/fail rule without product context.

## Common Bottlenecks

### Server And Network

- slow origin;
- distant region;
- missing CDN or cache;
- DNS and TLS delay;
- overloaded backend;
- slow database or API;
- excessive redirects;
- large HTML;
- poor compression.

### CSS And JavaScript

- render-blocking CSS;
- large bundles;
- unused code;
- long tasks;
- expensive hydration;
- synchronous third-party scripts;
- frequent layout or style recalculation.

Moving every script to the footer is not a universal fix. Use `defer`, `async`, code splitting, and loading strategy according to dependencies.

### Images, Fonts, And Media

- oversized dimensions;
- inefficient format;
- missing responsive images;
- eager loading below the fold;
- missing dimensions causing CLS;
- slow font loading;
- autoplay or large media.

### Third Parties

- analytics;
- tag managers;
- advertisements;
- chat widgets;
- social embeds;
- consent platforms.

Measure the transfer, main-thread, and privacy cost of each third party.

### Hosting And Capacity

Shared or noisy hosting, limited CPU, slow disks, or exhausted pools can increase TTFB. Validate under realistic traffic, not only one request.

## Test Matrix

Cover:

- mobile and desktop;
- low-end and high-end device profiles;
- fast and constrained network;
- cold and warm cache;
- first and repeat view;
- anonymous and authenticated users;
- primary pages and templates;
- different locations;
- empty and data-heavy states;
- third-party enabled and disabled comparison.

## Tools

### Chrome DevTools

- Network waterfall;
- Performance trace;
- CPU and network throttling;
- coverage;
- rendering diagnostics;
- local overrides.

### Lighthouse

Useful for repeatable lab audits and diagnostics. The score can change with environment and Lighthouse version, so track underlying metrics and budgets.

### PageSpeed Insights

Combines Lighthouse lab data with CrUX field data where available.

### WebPageTest

Useful for:

- test locations and browsers;
- first and repeat view;
- filmstrip and video;
- request waterfall;
- connection view;
- scripting.

### RUM And APM

Use production telemetry for:

- Web Vitals by page;
- device, network, and region segments;
- release comparison;
- JavaScript errors;
- API timing;
- long tasks.

## Performance Budgets

Example:

```text
LCP p75 mobile <= 2.5 s
INP p75 mobile <= 200 ms
CLS p75 <= 0.1
Lighthouse lab LCP <= 2.5 s
initial JS transfer <= 250 KB compressed
third-party JS <= 100 KB compressed
critical page requests <= 60
```

Budgets should be product-specific and versioned. Resource budgets can detect regressions before field metrics deteriorate.

## Test Process

1. Select critical pages and user journeys.
2. Record the field baseline.
3. Define budgets and pass/fail criteria.
4. Fix lab environment and tool versions.
5. Run several samples rather than one.
6. Analyze the waterfall and main thread.
7. Correlate frontend timing with backend or APM.
8. Repeat with cold and warm cache, mobile and desktop.
9. Compare before and after a change.
10. Monitor field data after release.

## Functional Behavior Under Slow Conditions

Verify:

- a loading indicator appears;
- controls do not accept duplicate submission;
- timeout provides a useful error and retry;
- partial content remains usable;
- images have stable placeholders;
- navigation does not lose state;
- offline or failed-resource behavior is controlled;
- stale content is labelled where required.

Fast metrics do not compensate for broken behavior.

## Relationship To Load Testing

A synthetic page test asks:

```text
How fast does one browser experience the page?
```

A backend load test asks:

```text
How does the service perform under many concurrent requests?
```

Run both. A fast page against an idle backend can slow down under traffic, while a fast API does not guarantee fast rendering.

## Typical Defects

- LCP image is discovered late;
- JavaScript blocks interaction;
- cookie banner causes layout shift;
- a third-party script blocks the main thread;
- repeat view is fast but first view is poor;
- mobile field data fails while desktop lab passes;
- cache hides a slow origin;
- responsive image downloads a desktop asset on mobile;
- API is fast but client rendering is expensive;
- Lighthouse score improves while real-user INP regresses.

## Reporting

Include:

- URL and build;
- device, browser, and location;
- network and CPU profile;
- cache state;
- number of runs;
- median and variation;
- LCP, INP, CLS, or lab proxies;
- TTFB, FCP, TBT, and Speed Index;
- transfer size and request count;
- waterfall or trace evidence;
- field segments;
- backend correlation;
- budget result and recommendation.

## QA Checklist

- [ ] Critical pages and journeys are selected.
- [ ] Lab and field data are distinguished.
- [ ] Current Core Web Vitals are used.
- [ ] Mobile and desktop are measured separately.
- [ ] Cold and warm cache are covered.
- [ ] Multiple runs are compared.
- [ ] Waterfall and main thread are analyzed.
- [ ] Backend or APM data is correlated.
- [ ] Third-party impact is measured.
- [ ] Budgets are versioned.
- [ ] Slow and failure functional behavior is checked.
- [ ] Field metrics are monitored after release.

## Interview Focus

1. How do lab and field performance data differ?
2. What are the current Core Web Vitals?
3. Why is a Lighthouse score insufficient?
4. How do TTFB and LCP differ?
5. What causes high INP?
6. Why test first and repeat view?
7. How does website testing differ from backend load testing?
8. What belongs in a performance budget?

## Sources

- User-provided Plerdy article: "Website Performance"
- [Web Vitals](https://web.dev/articles/vitals)
- [Lighthouse performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [WebPageTest](https://www.webpagetest.org/)
