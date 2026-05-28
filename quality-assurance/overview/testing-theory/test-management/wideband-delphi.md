# Wideband Delphi

## Summary

Wideband Delphi is a consensus-based estimation technique that uses a group of experts to estimate project effort, time, or cost.

It is based on the Delphi Method, but includes more interaction and discussion between participants.

The main idea:

- experts estimate independently;
- estimates are compared anonymously;
- assumptions are discussed;
- estimates are revised;
- the group moves toward a more reliable estimate.

Wideband Delphi is useful when estimation needs expert judgment and team discussion.

## Delphi Method

The Delphi Method is a structured communication technique originally developed as a systematic forecasting method.

It uses a panel of experts.

The process usually works in rounds:

1. Experts answer questions or provide estimates independently.
2. A facilitator summarizes the answers anonymously.
3. Experts review the summary and reasoning.
4. Experts revise their answers if needed.
5. The process repeats until results stabilize or consensus is reached.

The goal is to reduce the range of answers and move the group toward a more accurate forecast.

The Delphi Method was developed in the 1950s and 1960s at the RAND Corporation.

## What Is Wideband Delphi?

Wideband Delphi is a variant of the Delphi Method.

It was introduced in the 1970s by Barry Boehm and John A. Farquhar.

The word `wideband` means that this version includes more communication and interaction between participants than the original Delphi Method.

In software estimation, Wideband Delphi helps estimate:

- development effort;
- testing effort;
- project duration;
- task size;
- cost;
- uncertainty.

## Estimation Team

A Wideband Delphi estimation team usually includes 3 to 7 people.

Typical participants:

- project manager;
- moderator;
- experienced experts;
- developers;
- QA engineers;
- representatives from the team that will do the work.

The moderator facilitates the process and keeps the discussion structured.

## Meetings

Wideband Delphi usually includes two main meetings:

- Kickoff Meeting;
- Estimation Meeting.

## Kickoff Meeting

The moderator conducts the kickoff meeting.

During this meeting, the team receives:

- problem specification;
- high-level task list;
- assumptions;
- project constraints;
- estimation goals;
- estimation units.

Examples of estimation units:

- hours;
- person-days;
- story points;
- ideal days;
- cost units.

The team discusses:

- scope;
- unclear requirements;
- estimation issues;
- assumptions;
- dependencies;
- risks.

After the kickoff meeting, the moderator prepares a structured document with:

- problem specification;
- high-level task list;
- assumptions;
- constraints;
- agreed estimation units.

This document is shared with the estimation team.

## Individual Preparation

After kickoff, each team member works independently.

Each participant:

- creates a detailed Work Breakdown Structure;
- estimates each task;
- documents assumptions;
- identifies risks and questions;
- prepares an individual total estimate.

Independent preparation is important because it reduces group pressure and anchoring bias.

## Estimation Meeting

The estimation meeting is where estimates are discussed and refined.

If some team members are not ready, the moderator should give more time rather than force weak estimates.

## Step 1: Collect Initial Estimates

At the beginning, the moderator collects initial estimates from each team member.

The estimates are shown anonymously.

Example:

```text
Round 1 estimates:
120h, 160h, 210h, 240h, 300h
```

The team sees the range, but not who gave which estimate.

## Step 2: Show Estimate Range

The moderator plots estimates on a board or shared document.

The goal is to show:

- lowest estimate;
- highest estimate;
- spread between estimates;
- how much disagreement exists.

Names are not shown.

This helps people discuss the estimate without personal pressure.

## Step 3: Discuss Task Lists And Assumptions

Each team member reads their task list and assumptions aloud.

Important rule:

> Detailed tasks and assumptions are discussed, but individual task estimates are not revealed.

This allows the group to discover:

- missed tasks;
- hidden assumptions;
- unclear scope;
- different interpretations;
- dependencies;
- risks.

The combined task lists often create a more complete project view.

## Step 4: Revise Estimates

After discussion, each participant revisits their estimate.

They may adjust based on:

- newly discovered tasks;
- corrected assumptions;
- clarified scope;
- risks raised by others;
- dependencies they missed.

The participant then produces a new total estimate.

## Step 5: Collect Round 2 Estimates

The moderator collects revised estimates and plots them again.

Example:

```text
Round 1:
120h, 160h, 210h, 240h, 300h

Round 2:
180h, 200h, 220h, 230h, 250h
```

The range usually becomes narrower because the team has more shared understanding.

## Step 6: Repeat Until Stop Criteria

Discussion and revision continue until one of the stop criteria is met.

Common stop criteria:

- estimates converge to an acceptable range;
- team members are no longer changing estimates;
- time allocated for estimation is over;
- consensus is reached;
- uncertainty is understood and documented.

The goal is not always to get one exact number. Often, the goal is a defensible range.

## Final Output

After the estimation meeting, the project manager or moderator compiles results.

Final output can include:

- master task list;
- final estimate or estimate range;
- assumptions;
- risks;
- dependencies;
- unresolved questions;
- confidence level.

The master task list is created by combining individual task lists.

This final output can then be used for planning, scheduling, and negotiation.

## Example

Suppose a QA team estimates regression testing for a new release.

Round 1:

| Estimator | Estimate |
| --- | --- |
| Anonymous A | 24h |
| Anonymous B | 40h |
| Anonymous C | 60h |
| Anonymous D | 72h |

The range is wide: 24h to 72h.

During discussion, the team discovers:

- one person forgot mobile regression;
- another assumed automation is stable;
- one person included defect retesting;
- another did not include environment setup.

Round 2:

| Estimator | Estimate |
| --- | --- |
| Anonymous A | 48h |
| Anonymous B | 52h |
| Anonymous C | 56h |
| Anonymous D | 60h |

The range is now much narrower: 48h to 60h.

The team may agree on:

```text
Regression testing estimate: 50-60 hours
```

with assumptions documented.

## Advantages

Wideband Delphi has several advantages:

- consensus-based;
- uses expert knowledge;
- includes people who understand the work;
- reduces individual bias through anonymity;
- encourages discussion of assumptions;
- creates a more complete task list;
- simple to understand;
- useful when historical data is limited;
- produces estimates that are easier to defend.

It is especially useful when the people doing the work participate in estimation.

## Disadvantages

Limitations:

- requires management support;
- requires time from experienced people;
- depends on moderator quality;
- may be uncomfortable if management expects a lower number;
- can still be biased if participants lack experience;
- may not work well if assumptions are not documented;
- can be slow for very small tasks.

The final estimate may not be what management wants to hear, but that does not mean it is wrong.

## Best Practices

Good practices:

- choose experienced participants;
- keep estimates anonymous during rounds;
- document assumptions clearly;
- discuss differences, not personalities;
- use a neutral moderator;
- define stop criteria before starting;
- capture risks and dependencies;
- present final estimate as a range when uncertainty is high.

## Common Mistakes

Common mistakes:

- revealing names with estimates too early;
- letting one senior person dominate discussion;
- skipping individual preparation;
- not documenting assumptions;
- forcing consensus too quickly;
- treating the final number as exact;
- ignoring risks discovered during discussion.

## Key Idea

Wideband Delphi helps teams estimate by combining independent expert judgment with structured group discussion.

Главная мысль:

> The value is not only in the final estimate, but in the assumptions and risks discovered along the way.

## Questions

1. What is Wideband Delphi?
2. How is it different from the original Delphi Method?
3. Why are estimates shown anonymously?
4. What happens during the kickoff meeting?
5. What are common stop criteria for Wideband Delphi?

## What To Review Later

- Delphi Method
- Work Breakdown Structure
- Bottom-Up Estimation
- Estimation Assumptions
- Estimation Range
- Project Risk
