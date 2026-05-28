# Non-Functional Testing Types

## Summary

Non-Functional Testing проверяет не то, что система делает, а как она это делает.

Если functional testing отвечает на вопрос "работает ли feature according to requirements?", то non-functional testing отвечает:

> Насколько хорошо, быстро, надежно, безопасно, удобно и устойчиво работает система?

Нефункциональное тестирование оценивает quality attributes продукта: performance, reliability, usability, security, compatibility, scalability, accessibility, recovery и другие характеристики.

## Key Points

- Non-functional testing оценивает quality characteristics of the system.
- Оно важно для user experience, stability, security и production readiness.
- Performance testing включает load, stress, soak, volume, scalability и spike testing.
- Usability testing проверяет удобство использования.
- Accessibility testing проверяет доступность продукта для людей с ограниченными возможностями.
- Security testing ищет vulnerabilities и проверяет protection mechanisms.
- Compatibility testing проверяет работу в разных environments.
- Для mobile applications есть отдельные важные non-functional checks: interruption, network, installation, memory leak testing.

## Notes

### Functional vs Non-Functional Testing

Functional testing checks what the system does.

Examples:

- user can log in;
- payment is processed;
- report is generated;
- item is added to cart.

Non-functional testing checks how the system behaves.

Examples:

- login completes within 2 seconds;
- payment service handles peak load;
- report generation does not crash under large data volume;
- application remains secure and accessible.

Both are needed. A product can be functionally correct but still fail users because it is slow, insecure, unstable or hard to use.

## 1. Performance Testing

Performance Testing - это общий category для testing techniques, которые оценивают responsiveness, stability, speed и throughput системы under load.

Performance testing помогает понять:

- how fast the system responds;
- how stable it is under load;
- how many users it can handle;
- where bottlenecks are;
- what happens under peak traffic;
- whether performance degrades over time.

### Load Testing

Load Testing проверяет behavior системы under expected user load.

Expected load может включать:

- normal load;
- peak business load;
- expected number of concurrent users;
- expected transaction volume.

Example:

E-commerce site должен выдерживать 5,000 concurrent users during sale without critical slowdown.

### Stress Testing

Stress Testing проверяет system beyond expected limits.

Цель - найти breaking point и понять, как система ведет себя under extreme load.

Stress testing also checks recovery after failure.

Example:

Система рассчитана на 5,000 users, но test gradually increases load to 15,000 users to see where it fails and how it recovers.

### Soak / Stability / Endurance Testing

Soak Testing, Stability Testing или Endurance Testing проверяет system under normal load for a long time.

Цель - найти issues, которые появляются не сразу:

- memory leaks;
- performance degradation;
- resource exhaustion;
- slow database growth;
- connection leaks;
- logging/storage problems.

Example:

Application работает 24-72 hours under normal load, чтобы проверить стабильность.

### Volume Testing

Volume Testing оценивает system behavior with large amounts of data.

Focus:

- database size;
- large files;
- many records;
- big reports;
- search performance;
- import/export operations.

Example:

Проверить, как система работает, когда database содержит 50 million records.

### Scalability Testing

Scalability Testing проверяет, может ли system increase capacity when resources or load grow.

It answers:

> Can the system scale?

Examples:

- add more users;
- add more servers;
- increase database size;
- increase transactions per second;
- compare vertical and horizontal scaling.

### Spike Testing

Spike Testing проверяет reaction системы на sudden traffic spikes.

Example:

После marketing campaign traffic jumps from 500 to 10,000 users in one minute.

QA checks whether system:

- handles spike;
- slows down gracefully;
- rejects requests correctly;
- recovers after spike.

## 2. Usability Testing

Usability Testing оценивает, насколько удобно и понятно users can use the product.

Focus:

- ease of learning;
- navigation;
- clarity of UI;
- user satisfaction;
- error prevention;
- efficiency of workflows;
- understandability of messages.

Example:

New user should be able to complete registration without help and without confusion.

### Accessibility Testing

Accessibility Testing проверяет, может ли product be used by people with disabilities.

It often checks compliance with standards such as WCAG.

Focus:

- keyboard navigation;
- screen reader support;
- color contrast;
- alternative text for images;
- focus order;
- captions;
- readable labels;
- accessible forms.

Accessibility is not "extra polish". For many users it determines whether they can use the product at all.

## 3. Security Testing

Security Testing проверяет, защищена ли system от unauthorized access, data leaks и attacks.

Focus:

- authentication;
- authorization;
- session management;
- password rules;
- access control;
- data encryption;
- input validation;
- SQL injection;
- XSS;
- CSRF;
- sensitive data exposure;
- security headers;
- vulnerability scanning.

Example:

User with regular role should not access admin endpoints, even by changing URL manually.

## 4. Compatibility Testing

Compatibility Testing проверяет, работает ли application correctly in different environments.

### Cross-Browser Testing

Checks application in different browsers:

- Chrome;
- Firefox;
- Safari;
- Edge;
- mobile browsers.

### Cross-Platform Testing

Checks application on different operating systems:

- Windows;
- macOS;
- Linux;
- iOS;
- Android.

### Configuration Testing

Configuration Testing checks how hardware/software configuration changes affect system behavior.

Examples:

- different screen resolutions;
- different memory/CPU conditions;
- different browser settings;
- different OS versions;
- different database configurations.

## 5. Mobile Non-Functional Testing

Mobile applications have additional non-functional risks.

### Interruption Testing

Interruption Testing checks how mobile app reacts to interruptions.

Examples:

- incoming call;
- SMS;
- push notification;
- low battery;
- network loss;
- app goes to background;
- screen lock;
- device rotation.

### Network Testing

Network Testing checks behavior under different network conditions.

Examples:

- Wi-Fi;
- 5G/4G/3G/2G;
- roaming;
- weak signal;
- offline mode;
- network switching;
- high latency;
- packet loss.

### Installation Testing

Installation Testing checks installation, update and uninstall flows.

Examples:

- fresh install;
- update from previous version;
- uninstall;
- reinstall;
- installation with low storage;
- permissions during installation.

### Memory Leak Testing

Memory Leak Testing checks whether app releases temporarily allocated memory correctly.

Memory leaks can cause:

- slow performance;
- crashes;
- battery drain;
- OS killing the app;
- degraded user experience over time.

## 6. Other Non-Functional Types

### Localization Testing

Localization Testing checks whether product is adapted for specific region or language.

Focus:

- translation quality;
- text length;
- date/time formats;
- currency formats;
- number formats;
- address formats;
- right-to-left languages;
- regional legal text.

### Compliance / Regulation Testing

Compliance Testing checks whether product follows required laws, standards or regulations.

Examples:

- financial regulations;
- healthcare privacy requirements;
- governmental standards;
- safety standards;
- industry rules;
- internal company policies.

### Recovery Testing

Recovery Testing checks whether application can recover after failure.

Examples:

- server restart;
- database disconnect;
- network failure;
- power outage;
- service crash;
- restore from backup;
- transaction recovery.

## Functional vs Non-Functional Examples

| Functional Requirement | Non-Functional Requirement |
| --- | --- |
| User can log in. | Login response time must be under 2 seconds. |
| User can upload a file. | Upload must support files up to 100 MB without timeout. |
| User can search products. | Search must return results within 1 second for 95% of requests. |
| Admin can generate report. | Report generation must handle 1 million records. |
| User can pay for order. | Payment flow must be secure and PCI-compliant. |

## Commands / Terms

- `Non-Functional Testing` - testing how the system behaves.
- `Performance Testing` - testing speed, stability and responsiveness.
- `Load Testing` - testing expected load.
- `Stress Testing` - testing beyond expected limits.
- `Soak Testing` - long-duration stability testing.
- `Volume Testing` - testing with large data volumes.
- `Scalability Testing` - testing ability to grow capacity.
- `Spike Testing` - testing sudden load increases.
- `Usability Testing` - testing ease of use.
- `Accessibility Testing` - testing accessibility for users with disabilities.
- `Security Testing` - testing protection against security risks.
- `Compatibility Testing` - testing across environments.
- `Recovery Testing` - testing recovery after failure.

## Questions

1. What is non-functional testing?
2. How is non-functional testing different from functional testing?
3. What is performance testing?
4. What is the difference between load and stress testing?
5. What is soak testing used for?
6. What does accessibility testing check?
7. Why is security testing non-functional?
8. What is compatibility testing?
9. What mobile-specific non-functional tests are important?
10. Why can a functionally correct product still fail users?

## What To Review Later

- Functional vs non-functional testing
- Performance testing types
- Load testing
- Stress testing
- Security testing basics
- Accessibility and WCAG
- Compatibility testing
- Mobile testing
- Recovery testing
