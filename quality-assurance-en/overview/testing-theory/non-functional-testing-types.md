# Non-Functional Testing Types

## Summary

Non-Functional Testing verifies not what the system does, but how it does it.

If functional testing answers "does the feature work according to requirements?", non-functional testing answers:

> How well, fast, reliable, secure, usable, and resilient is the system?

Non-functional testing evaluates quality attributes of the product: performance, reliability, usability, security, compatibility, scalability, accessibility, recovery, and other characteristics.

## Key Points

- Non-functional testing evaluates quality characteristics of the system.
- It is important for user experience, stability, security, and production readiness.
- Performance testing includes load, stress, soak, volume, scalability, and spike testing.
- Usability testing checks ease of use.
- Accessibility testing checks whether users with disabilities can use the product.
- Security testing finds vulnerabilities and verifies protection mechanisms.
- Compatibility testing checks behavior in different environments.
- Mobile applications have specific non-functional checks: interruption, network, installation, and memory leak testing.

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

Both are needed. A product can be functionally correct but still fail users because it is slow, insecure, unstable, or hard to use.

## 1. Performance Testing

Performance Testing is a broad category for testing techniques that evaluate responsiveness, stability, speed, and throughput under load.

Performance testing helps understand:

- how fast the system responds;
- how stable it is under load;
- how many users it can handle;
- where bottlenecks are;
- what happens under peak traffic;
- whether performance degrades over time.

### Load Testing

Load Testing checks system behavior under expected user load.

Expected load can include normal load, peak business load, expected number of concurrent users, and expected transaction volume.

### Stress Testing

Stress Testing checks the system beyond expected limits.

The goal is to find the breaking point and understand how the system behaves under extreme load.

Stress testing also checks recovery after failure.

### Soak / Stability / Endurance Testing

Soak Testing, Stability Testing, or Endurance Testing checks the system under normal load for a long time.

The goal is to find issues that do not appear immediately:

- memory leaks;
- performance degradation;
- resource exhaustion;
- slow database growth;
- connection leaks;
- logging/storage problems.

### Volume Testing

Volume Testing evaluates system behavior with large amounts of data.

Focus:

- database size;
- large files;
- many records;
- big reports;
- search performance;
- import/export operations.

### Scalability Testing

Scalability Testing checks whether the system can increase capacity when resources or load grow.

It answers:

> Can the system scale?

### Spike Testing

Spike Testing checks system reaction to sudden traffic spikes.

Example:

Traffic jumps from 500 to 10,000 users in one minute after a marketing campaign.

## 2. Usability Testing

Usability Testing evaluates how easily and comfortably users can use the product.

Focus:

- ease of learning;
- navigation;
- clarity of UI;
- user satisfaction;
- error prevention;
- efficiency of workflows;
- understandability of messages.

### Accessibility Testing

Accessibility Testing checks whether the product can be used by people with disabilities.

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

## 3. Security Testing

Security Testing verifies whether the system is protected from unauthorized access, data leaks, and attacks.

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

## 4. Compatibility Testing

Compatibility Testing checks whether an application works correctly in different environments.

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

## 5. Mobile Non-Functional Testing

Mobile applications have additional non-functional risks.

### Interruption Testing

Interruption Testing checks how a mobile app reacts to interruptions:

- incoming call;
- SMS;
- push notification;
- low battery;
- network loss;
- app goes to background;
- screen lock;
- device rotation.

### Network Testing

Network Testing checks behavior under different network conditions:

- Wi-Fi;
- 5G/4G/3G/2G;
- roaming;
- weak signal;
- offline mode;
- network switching;
- high latency;
- packet loss.

### Installation Testing

Installation Testing checks installation, update, and uninstall flows.

### Memory Leak Testing

Memory Leak Testing checks whether the app releases temporarily allocated memory correctly.

Memory leaks can cause slow performance, crashes, battery drain, or degraded user experience over time.

## 6. Other Non-Functional Types

### Localization Testing

Localization Testing checks whether the product is adapted for a specific region or language.

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

Compliance Testing checks whether the product follows required laws, standards, or regulations.

### Recovery Testing

Recovery Testing checks whether an application can recover after failure.

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
