# Severity and Priority in Testing

## Summary

Severity and Priority are two different parameters in a defect report.

Severity shows how seriously a defect affects product functionality, stability, data, security, or user experience. Priority shows how urgently the defect should be fixed from the perspective of business value, release planning, and customer needs.

In short:

- `Severity` = how serious the defect is technically.
- `Priority` = how soon the defect should be fixed.

These parameters are often related, but they do not always match. A defect can be high severity and low priority, or low severity and high priority.

## Key Points

- Severity is usually defined by a QA engineer.
- Priority is usually defined together with a product manager, project manager, client, or triage team.
- Severity is connected to functionality, standards, data integrity, and system behavior.
- Priority is connected to scheduling, business impact, customer expectations, and release risk.
- Severity is usually more objective and changes less often.
- Priority is more subjective and can change depending on project context.
- Wrong severity can confuse the team and slow down the STLC process.
- Wrong priority can make the team fix the wrong things first.

## Notes

### What Is Bug Severity?

Bug Severity, or Defect Severity, is the degree of impact a defect has on the software product.

If a defect breaks critical functionality, blocks a business flow, causes data loss, or makes the system unusable, severity is high.

If a defect does not break functionality and affects only appearance, text, or a minor usability detail, severity is low.

Severity answers the question:

> How serious is this defect for the product?

### What Is Bug Priority?

Bug Priority is the order in which a defect should be fixed.

Priority answers the question:

> How urgently should this defect be fixed?

Priority depends on more than technical seriousness. It can be affected by:

- business value;
- release date;
- client expectations;
- issue visibility;
- affected users;
- legal or compliance risk;
- marketing campaign;
- cost of delay;
- workaround availability.

For example, a typo in the company name on the homepage may have low severity because functionality is not broken. But it can have high priority because it is visible to customers.

### Types of Severity

Severity levels may differ between companies, but common levels include:

| Severity | Meaning |
| --- | --- |
| Critical | The system or a critical flow is completely blocked. No workaround exists. |
| Major | Important functionality is broken, but part of the system still works. |
| Moderate | Unwanted behavior exists, but the system is still functional. |
| Minor | Small defect with limited impact. |
| Cosmetic | UI/text/visual issue without business logic impact. |

### Types of Priority

Priority levels are usually simpler:

| Priority | Meaning |
| --- | --- |
| High | Must be fixed as soon as possible. Important for release, client, or business flow. |
| Medium | Should be fixed in the normal development flow. Important but not immediately blocking. |
| Low | Can be fixed later after more important defects. |

### Severity vs Priority

| Priority | Severity |
| --- | --- |
| Shows how soon a defect should be fixed. | Shows how serious a defect is for the product. |
| Connected to scheduling and business needs. | Connected to functionality, standards, and technical impact. |
| Usually decided with manager/client/product side. | Usually decided by QA engineer. |
| Driven by business value. | Driven by functional impact. |
| Can change over time. | Usually changes less often. |
| More subjective. | More objective. |

### High Priority, Low Severity

This is a defect that does not technically break the system, but must be fixed quickly.

Examples:

- wrong logo on a production website;
- typo in the company name on the homepage;
- wrong price in a promotional banner;
- incorrect text in a legal disclaimer;
- broken marketing link before an important campaign.

Functionality may work correctly, but the business impact is high.

### High Severity, Low Priority

This is a defect that is technically serious but does not need an immediate fix.

Examples:

- critical bug in a rarely used admin feature outside the current release;
- crash in an old browser that is not officially supported;
- serious defect in a module planned for the next release cycle;
- broken flow behind a disabled feature flag.

Functional impact is high, but urgency is lower because of context, scope, or release plan.

### Low Priority, Low Severity

This is a minor issue that does not affect key functionality and does not require an urgent fix.

Examples:

- small UI alignment issue;
- typo in secondary helper text;
- minor spacing issue;
- cosmetic inconsistency on a rarely used page.

### High Priority, High Severity

This is a defect that seriously breaks the product and must be fixed immediately.

Examples:

- user cannot log in;
- payment flow is broken;
- application crashes on launch;
- data is lost or corrupted;
- security vulnerability exposes sensitive information;
- checkout cannot be completed in production.

These defects usually block release or require a hotfix.

### Tips for Determining Severity

When assigning severity, evaluate technical and user impact:

- whether critical functionality is broken;
- whether a workaround exists;
- how many users are affected;
- how often the defect occurs;
- whether data integrity is affected;
- whether security or compliance risk exists;
- whether the defect blocks testing or release;
- whether the problem can be isolated.

A minor defect that occurs very frequently may have a larger real impact than it first appears.

### Defect Triage

Defect triage is the process of reviewing and prioritizing defects, especially when there are many defects and limited team capacity.

The goal of triage is to decide:

- which defects should be fixed first;
- which defects belong to the current release;
- which defects can be moved later;
- which defects should be rejected or clarified;
- who should own the defect;
- whether a workaround is needed.

Typical triage steps:

1. Review all open defects.
2. Check severity and priority.
3. Clarify unclear reports.
4. Decide release impact.
5. Assign owner/team.
6. Update status and target version.

A good triage process considers both severity and priority.

### Guidelines for QA

QA should be careful when assigning severity because it affects how the defect is perceived.

Practical guidelines:

- do not confuse severity and priority;
- assign severity based on actual impact, not emotion;
- describe the affected business flow;
- add evidence: screenshots, logs, video, request/response, environment;
- mention workaround if it exists;
- explain frequency and reproducibility;
- do not inflate severity without reason;
- do not lower severity when the defect affects data, security, or a critical flow.

## Commands / Terms

- `Severity` - seriousness of defect impact on product functionality or quality.
- `Priority` - urgency/order of fixing a defect.
- `Critical` - defect blocks critical flow or system usage.
- `Major` - important functionality is broken, but system is partly usable.
- `Moderate` - noticeable issue, system still works.
- `Minor` - small issue with limited impact.
- `Cosmetic` - visual/text issue without functional impact.
- `Defect Triage` - process of reviewing, prioritizing, assigning, and planning defects.
- `Workaround` - alternative way to continue using the system despite the defect.
- `Business Impact` - effect on users, client, revenue, release, or operations.

## Questions

1. What is severity?
2. What is priority?
3. What is the main difference between severity and priority?
4. Who usually defines severity?
5. Who usually defines priority?
6. Can a defect have high priority and low severity?
7. Can a defect have high severity and low priority?
8. What is defect triage?
9. Why is it dangerous to assign wrong severity?
10. What information should QA include to justify severity?

## What To Review Later

- Severity levels
- Priority levels
- High priority vs high severity examples
- Defect triage
- Defect lifecycle
- Bug report structure
- Business impact vs technical impact
