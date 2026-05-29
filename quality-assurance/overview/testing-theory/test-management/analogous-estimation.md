# Analogous Estimation

## Summary

Analogous Estimation is an estimation technique that uses information from similar past projects to estimate the duration, effort, or cost of a current project.

It is called analogous because the estimate is based on analogy:

```text
This new project is similar to that previous project,
so its effort and duration may be similar too.
```

This technique is useful when the team has limited information about the current project but has historical data from similar work.

## What Is Analogous Estimation?

Analogous Estimation uses parameters from historical data as the basis for estimating similar parameters for a future activity or project.

Examples of parameters:

- scope;
- cost;
- duration;
- effort;
- team size;
- complexity.

Examples of scale measures:

- size;
- number of features;
- number of modules;
- number of integrations;
- business complexity;
- technical complexity.

Analogous estimation combines:

- historical project data;
- expert judgment;
- project manager experience;
- team experience.

## When To Use Analogous Estimation

Use Analogous Estimation when:

- the project is in an early stage;
- detailed requirements are not available yet;
- management needs quick cost or duration estimates;
- there is limited information about the current project;
- similar past projects exist;
- the team needs a rough estimate quickly;
- a detailed bottom-up estimate is not possible yet.

It is especially useful during early decision-making, when executives want to understand whether a project is worth starting.

## Why It Is Useful

In real projects, managers are often asked for estimates before all details are known.

At that moment:

- scope may be incomplete;
- requirements may be high-level;
- architecture may not be finalized;
- team composition may be unknown;
- risks may be unclear.

Analogous estimation gives a practical starting point by using past project experience.

It may not be perfect, but it is often better than guessing from nothing.

## Requirements

For Analogous Estimation, useful inputs include:

- data from previous projects;
- data from ongoing similar projects;
- work hours per week for team members;
- previous project cost data;
- previous project duration data;
- current project domain;
- current project technology;
- current project complexity;
- similar modules from past projects;
- similar activities from past projects;
- expert judgment from experienced people.

The stronger and more relevant the historical data, the better the estimate.

## Step 1: Identify Current Project Domain

Start by understanding the domain of the current project.

Examples:

- eCommerce;
- banking;
- healthcare;
- education;
- logistics;
- mobile application;
- internal admin system.

Domain matters because projects in different domains can have very different risks and complexity.

Example:

Testing a banking payment flow is usually riskier than testing a simple marketing page.

## Step 2: Identify Current Technology

Identify the technology stack and technical context.

Examples:

- web application;
- mobile application;
- API backend;
- microservices;
- cloud infrastructure;
- database-heavy system;
- third-party integrations.

Technology affects:

- development effort;
- testing complexity;
- automation effort;
- environment setup;
- required skills.

## Step 3: Find Similar Past Projects

Look for historical data from similar projects.

Useful sources:

- project archives;
- test summary reports;
- estimation sheets;
- sprint reports;
- defect reports;
- time tracking systems;
- release notes;
- project management tools.

If a similar full project exists, it can be used as a baseline.

## Step 4: Compare Projects

Compare the current project with the past project.

Consider:

- scope;
- features;
- complexity;
- integrations;
- team size;
- technology;
- quality requirements;
- timeline;
- risks;
- non-functional requirements.

Example:

| Factor | Past Project | Current Project |
| --- | --- | --- |
| Domain | eCommerce | eCommerce |
| Platforms | Web only | Web + Mobile |
| Payment | One provider | Two providers |
| Team | 4 devs, 2 QA | 5 devs, 2 QA |
| Duration | 3 months | Estimated slightly longer |

If the current project is larger or more complex, adjust the estimate.

## Step 5: Estimate Duration And Cost

Use the past project data and expert judgment to estimate the current project.

Example:

```text
Past similar project: 10 weeks
Current project has about 20% more scope

Estimate = 10 weeks x 1.2 = 12 weeks
```

For testing:

```text
Past project regression: 5 days
Current project has one extra platform

Testing estimate = 7-8 days
```

## Step 6: Use Similar Modules If No Similar Project Exists

Sometimes no complete past project is similar.

In that case, look for similar modules.

Examples:

- login module;
- checkout module;
- reporting module;
- notification module;
- file upload module;
- payment integration;
- user management.

Estimate the current project by combining estimates for similar modules.

## Step 7: Use Similar Activities

If similar modules are not available, look for similar activities.

Examples:

- API testing;
- mobile regression;
- payment gateway testing;
- test automation setup;
- performance testing;
- database migration testing;
- compatibility testing.

This helps estimate specific parts of QA work.

## Step 8: Apply Expert Judgment

Historical data should not be used blindly.

Experienced people should review and adjust the estimate based on:

- current team skill;
- new technology;
- changed process;
- risk level;
- environment stability;
- requirement clarity;
- automation coverage;
- expected defect rate.

Analogous Estimation is strongest when historical data and expert judgment work together.

## QA Example

Suppose a QA team tested a similar eCommerce checkout project last year.

Historical data:

```text
Functional testing: 8 days
Regression testing: 4 days
Bug retesting: 3 days
Total QA effort: 15 days
```

Current project differences:

- same checkout flow;
- one additional payment provider;
- mobile testing is also required;
- automation coverage is better than last year.

Adjusted estimate:

```text
Base effort: 15 days
Extra payment provider: +3 days
Mobile testing: +4 days
Automation benefit: -2 days

Estimated QA effort: 20 days
```

This is not exact, but it is defendable.

## Advantages

Advantages of Analogous Estimation:

- simple;
- fast;
- useful in early project stages;
- requires less detailed information;
- based on real historical data;
- can use expert judgment;
- works for whole projects and individual tasks;
- useful when detailed decomposition is not available yet.

It can also be used inside WBS estimation for tasks that are similar to previous work.

## Limitations

Limitations:

- less accurate than detailed bottom-up estimation;
- depends heavily on quality of historical data;
- can be misleading if the past project is not truly similar;
- expert judgment can be biased;
- may ignore new risks;
- weak if the organization does not collect project data.

Analogous Estimation is usually better for rough early estimates than for final commitments.

## Common Mistakes

Common mistakes:

- choosing a past project that only looks similar;
- ignoring differences in technology or scope;
- using outdated data;
- not adjusting for team skill;
- forgetting environment and integration differences;
- presenting a rough estimate as exact;
- not documenting assumptions.

## Best Practices

Good practices:

- use the most similar past project available;
- compare differences explicitly;
- document assumptions;
- adjust for scope and complexity;
- involve experienced people;
- use ranges instead of single numbers;
- update the estimate when more information appears;
- combine with other estimation techniques when possible.

## Key Idea

Analogous Estimation is a practical early estimation technique based on similar past work.

Главная мысль:

> If you do not know enough about the new project yet, start with what similar past projects can teach you.

## Questions

1. What is Analogous Estimation?
2. When is Analogous Estimation useful?
3. What historical data is needed?
4. Why should expert judgment be used with historical data?
5. What are the limitations of Analogous Estimation?

## What To Review Later

- Historical Data
- Expert Judgment
- Project Estimation
- Work Breakdown Structure
- Bottom-Up Estimation
- Estimation Assumptions
