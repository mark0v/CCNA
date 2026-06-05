# OWASP Top 10 2025 For QA

Source: pasted article about OWASP Top 10:2025 and official OWASP Top 10:2025 pages  
Date added: 2026-06-05  
Related plan item: Web Testing  
Tags: QA, web testing, security testing, OWASP, vulnerabilities, application security  
Language: English  
Translation pair: quality-assurance/overview/web-testing/owasp-top-10-2025-for-qa.md

## Summary

OWASP Top 10 is an awareness document about the most important risks for web applications. The 2025 version shows which classes of problems remain critical for modern applications: access control, misconfiguration, supply chain, cryptography, injection, design, authentication, integrity, logging, and exceptional conditions.

For QA, this is not a checklist to "test everything in one day." It is a risk map. It helps understand where a web application most often breaks from a security point of view, what questions to ask the team, and what checks to consider during testing planning.

Main idea:

> OWASP Top 10 helps QA think not only about functional bugs, but also about how an application can be misused or used unsafely.

## Key Points

- OWASP Top 10:2025 keeps Broken Access Control as the A01 risk.
- Security Misconfiguration moved higher because more application behavior depends on configuration.
- Software Supply Chain Failures became a broad standalone category instead of focusing only on outdated components.
- Injection and Cryptographic Failures remain important, but in 2025 they are lower than in 2021.
- A new category appears in 2025: A10 - Mishandling of Exceptional Conditions.
- QA should use OWASP as a guide for risk-based testing, security questions, bug reports, and collaboration with developers/security engineers.

## Notes

## OWASP Top 10:2025 Categories

| ID | Category | QA meaning |
| --- | --- | --- |
| A01:2025 | Broken Access Control | Users can access data or actions they should not access. |
| A02:2025 | Security Misconfiguration | Application, server, cloud or framework settings are unsafe. |
| A03:2025 | Software Supply Chain Failures | Dependencies, build pipeline or distribution process introduce risk. |
| A04:2025 | Cryptographic Failures | Sensitive data is not protected correctly. |
| A05:2025 | Injection | Untrusted input changes commands, queries or scripts. |
| A06:2025 | Insecure Design | The system is designed without enough security controls. |
| A07:2025 | Authentication Failures | Login, session or identity checks can be bypassed or abused. |
| A08:2025 | Software or Data Integrity Failures | Code, updates, data or trust boundaries are not verified correctly. |
| A09:2025 | Security Logging & Alerting Failures | Important security events are not logged or do not trigger action. |
| A10:2025 | Mishandling of Exceptional Conditions | Errors, abnormal states or edge cases are handled insecurely. |

## How QA Should Use OWASP Top 10

QA usually does not replace a security engineer or penetration tester. But QA can help prevent many issues earlier by asking good questions and testing risky flows.

Use OWASP Top 10 to:

- identify security-sensitive areas;
- add negative scenarios to test cases;
- improve acceptance criteria;
- review API behavior;
- check permissions and roles;
- report security issues clearly;
- communicate risk to developers and product owners;
- decide what should be escalated to AppSec.

## A01: Broken Access Control

Broken Access Control means a user can do something they should not be allowed to do.

Examples:

- regular user opens admin page;
- user changes another user's data;
- API returns data from another account;
- hidden button is removed from UI, but API still allows the action;
- direct URL access bypasses permissions;
- ID in URL can be changed to access another object.

QA checks:

- test different roles;
- test direct URLs;
- modify IDs in requests;
- check API authorization, not only UI visibility;
- verify object-level permissions;
- test disabled, blocked or deleted accounts.

## A02: Security Misconfiguration

Security Misconfiguration happens when settings are unsafe or inconsistent.

Examples:

- debug mode enabled in production;
- default credentials are still active;
- directory listing is enabled;
- unnecessary services are exposed;
- security headers are missing;
- CORS is too permissive;
- error pages expose stack traces.

QA checks:

- inspect response headers;
- check error pages;
- verify environment banners and debug information;
- test CORS behavior if APIs are exposed;
- confirm production does not expose staging tools;
- review deployment-specific behavior.

## A03: Software Supply Chain Failures

Software Supply Chain Failures cover risks in dependencies, build systems, packages, containers, and delivery pipelines.

Examples:

- vulnerable dependency;
- untrusted package;
- compromised build script;
- outdated container image;
- missing dependency scanning;
- unsigned or unverified artifact.

QA checks:

- ask whether dependency scanning exists;
- verify version information is tracked;
- check release notes for dependency updates;
- report visible outdated libraries if found;
- make sure test environments use approved builds;
- avoid installing random test tools into product environments.

## A04: Cryptographic Failures

Cryptographic Failures happen when sensitive data is not protected correctly.

Examples:

- HTTP instead of HTTPS;
- weak TLS configuration;
- passwords stored or logged in plain text;
- tokens exposed in URLs;
- sensitive data cached in browser;
- personal data visible in logs.

QA checks:

- verify HTTPS usage;
- check password reset links and tokens;
- inspect browser storage for sensitive data;
- check logs if accessible in test environment;
- avoid screenshots that expose secrets;
- test that sensitive data is masked where needed.

## A05: Injection

Injection happens when user input is interpreted as a command, query, or script.

Examples:

- SQL Injection;
- command injection;
- Cross-Site Scripting;
- LDAP injection;
- template injection.

QA checks:

- test input validation;
- use simple negative payloads carefully in safe environments;
- verify output encoding;
- check search, filters, comments, forms and URL parameters;
- inspect whether unexpected scripts execute;
- escalate suspicious behavior to security specialists.

## A06: Insecure Design

Insecure Design means the system lacks proper security thinking at the design level.

Examples:

- no rate limit for password reset;
- business rules can be bypassed;
- checkout flow trusts client-side price;
- approval process has no second check;
- account recovery is too easy to abuse.

QA checks:

- test business rules, not only fields;
- think about misuse cases;
- verify limits and validations on server side;
- check workflows with different roles;
- ask what should happen in abnormal scenarios.

## A07: Authentication Failures

Authentication Failures affect login, sessions, and identity verification.

Examples:

- weak password rules;
- no brute-force protection;
- session does not expire;
- logout does not invalidate token;
- password reset token can be reused;
- MFA can be bypassed.

QA checks:

- test login and logout;
- check session expiration;
- verify password reset flow;
- test locked, disabled and deleted users;
- check remember-me behavior;
- verify MFA flows if present.

## A08: Software Or Data Integrity Failures

Integrity failures happen when the system does not verify that code, data, or updates are trustworthy.

Examples:

- unsigned updates;
- unverified webhooks;
- unsafe deserialization;
- data import without validation;
- CI/CD artifacts are not protected;
- critical data can be changed without audit trail.

QA checks:

- test webhook signatures if visible in requirements;
- verify import validation;
- check audit trail for critical changes;
- ask how updates and artifacts are verified;
- test rollback or failed update behavior.

## A09: Security Logging & Alerting Failures

Logging without alerting is often not enough. The system should capture important security events and make them actionable.

Examples:

- failed login attempts are not logged;
- admin actions have no audit trail;
- suspicious activity creates no alert;
- logs expose secrets;
- logs cannot be correlated with user/session.

QA checks:

- verify audit logs for important actions;
- check failed login and access denied events;
- confirm sensitive data is not logged;
- verify timestamps and user identifiers;
- ask who receives alerts for critical events.

## A10: Mishandling Of Exceptional Conditions

This category focuses on abnormal conditions and insecure error handling.

Examples:

- system fails open instead of failing closed;
- missing parameter grants access;
- error reveals internal details;
- timeout creates duplicate transaction;
- exception skips authorization check;
- partial failure leaves inconsistent state.

QA checks:

- test missing and invalid parameters;
- test timeouts and interrupted flows;
- refresh pages during critical actions;
- retry requests;
- check error messages;
- verify system state after failed operations.

## Practical QA Checklist

When testing a web application, ask:

- Which roles exist and what can each role access?
- Are permissions enforced on the server side?
- Are production settings safe?
- Are secrets, tokens and personal data protected?
- Are dependencies scanned and tracked?
- Are user inputs validated and encoded?
- Are business rules protected from client-side manipulation?
- Do sessions expire correctly?
- Are critical actions logged?
- What happens when a request fails halfway?

## Common Security Bug Examples

Typical findings connected to OWASP:

- user can open another user's order by changing ID in URL;
- admin endpoint is hidden from UI but accessible directly;
- API allows action after logout;
- error page exposes stack trace;
- password reset token works more than once;
- comment field executes JavaScript;
- checkout accepts modified price from browser request;
- failed login attempts are not rate limited;
- audit log misses role changes;
- retry after timeout creates duplicate payment.

## Bug Report Tips

For security-related bugs include:

- affected URL or endpoint;
- user role/account;
- exact steps;
- request/response evidence if safe to share;
- expected access or behavior;
- actual unsafe behavior;
- impact;
- environment;
- screenshots or sanitized logs;
- whether the issue is reproducible with another account.

Do not include real passwords, tokens, personal data, or production secrets in bug reports.

Example:

> User with `customer` role can access `/admin/users/42` by direct URL. UI does not show admin navigation, but server returns user details with HTTP 200. Expected: access denied with 403. Impact: unauthorized access to user management data.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| OWASP | Open Worldwide Application Security Project. |
| CWE | Common Weakness Enumeration, a catalog of software weakness types. |
| CVE | Common Vulnerabilities and Exposures, a catalog of known vulnerabilities. |
| Access control | Rules that define who can access data or actions. |
| Authentication | Verifying who the user is. |
| Authorization | Verifying what the user is allowed to do. |
| Misconfiguration | Unsafe or incorrect application/system settings. |
| Injection | Untrusted input changes command, query or script behavior. |
| Integrity | Confidence that code, data or artifacts were not modified incorrectly. |
| Fail closed | Deny access or stop safely when an error happens. |
| Fail open | Allow access or continue unsafely when an error happens. |

## Questions

### 1. What is OWASP Top 10 used for?

Answer: It is used as an awareness and risk guide for common critical web application security risks.

### 2. What is the difference between authentication and authorization?

Answer: Authentication checks who the user is. Authorization checks what that user is allowed to do.

### 3. Why is hiding a button in UI not enough for access control?

Answer: Because attackers or testers can call the API or direct URL without using the visible UI.

### 4. Why is Security Misconfiguration important?

Answer: Unsafe settings can expose data, debug details, admin tools, APIs, or dangerous default behavior.

### 5. What should QA avoid putting into security bug reports?

Answer: Real passwords, tokens, personal data, production secrets, and unsanitized sensitive logs.

### 6. Why should QA test exceptional conditions?

Answer: Errors, missing parameters, timeouts, and partial failures can bypass checks or leave unsafe system states.

## What To Review Later

- OWASP Top 10 official documentation.
- Difference between authentication and authorization.
- IDOR and object-level access control.
- Security headers and CORS basics.
- XSS and SQL Injection basics.
- Secure error handling and fail-closed behavior.
