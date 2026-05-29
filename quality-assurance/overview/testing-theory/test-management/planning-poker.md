# Planning Poker

## Summary

Planning Poker is a consensus-based estimation technique mostly used in Scrum to estimate effort or relative size of user stories.

It helps Agile teams estimate work by combining:

- expert opinion;
- analogy;
- disaggregation;
- group discussion;
- private voting.

Planning Poker is designed to reduce bias and encourage the whole team to participate in estimation.

## What Is Planning Poker?

Planning Poker is an Agile estimation technique where team members use numbered cards to estimate user stories.

The numbers usually follow the Fibonacci sequence:

```text
1, 2, 3, 5, 8, 13, 21, 34...
```

These numbers commonly represent Story Points.

Story Points are relative estimates. They do not directly mean hours or days.

They usually represent a combination of:

- effort;
- complexity;
- uncertainty;
- risk.

## Short History

Planning Poker was first defined and named by James Grenning in 2002.

It was later popularized by Mike Cohn in the book `Agile Estimating and Planning`.

Today, it is widely used by Scrum teams.

## Why Fibonacci Numbers Are Used

Fibonacci-like numbers are useful because uncertainty grows as work gets bigger.

The difference between `1` and `2` is small.

The difference between `13` and `21` is much larger.

This helps the team avoid false precision.

For example, estimating a story as `17` points can create the illusion of accuracy. Choosing between `13` and `21` forces the team to think in broader size ranges.

## Who Participates?

Planning Poker usually involves the whole Scrum team.

Participants can include:

- developers;
- QA engineers;
- automation engineers;
- UX designers;
- product owner;
- Scrum master;
- business analysts.

The people who will do the work should participate in the estimate.

## Moderator Role

One team member acts as the moderator.

The moderator:

- reads the user story;
- keeps the discussion focused;
- makes sure everyone understands the story;
- prevents pressure or personal criticism;
- controls the voting rounds;
- notes important assumptions or questions.

The moderator can be the Scrum Master, but it does not have to be.

## Planning Poker Process

## Step 1: Present The User Story

The moderator reads the user story.

The team should understand:

- what user problem is being solved;
- what acceptance criteria exist;
- what is included;
- what is not included;
- what dependencies exist.

## Step 2: Ask Questions

Team members ask clarifying questions.

The Product Owner usually answers questions about:

- expected behavior;
- business rules;
- priority;
- scope;
- acceptance criteria.

QA may ask about:

- edge cases;
- negative scenarios;
- supported environments;
- test data;
- integration behavior;
- acceptance criteria gaps.

## Step 3: Private Estimation

Each estimator privately selects a card that represents their estimate.

Cards are not shown immediately.

This prevents anchoring, where one person’s estimate influences everyone else too early.

## Step 4: Reveal Cards Together

After everyone selects a card, all estimates are revealed at the same time.

Example:

```text
Developer A: 5
Developer B: 8
QA: 13
Automation QA: 8
```

If estimates are close, the team may quickly agree.

If estimates vary a lot, the team discusses why.

## Step 5: Discuss Differences

The highest and lowest estimators explain their reasoning.

Example:

- low estimate: "The backend already supports this."
- high estimate: "Mobile and edge cases are not covered yet."

The goal is not to win an argument.

The goal is to discover hidden assumptions, risks, and missing work.

## Step 6: Re-Estimate

After discussion, everyone estimates again privately.

Then cards are revealed again.

This repeats until estimates converge enough for the team to agree.

The number of rounds can vary by story.

## Step 7: Record Notes

The moderator can record useful notes:

- assumptions;
- risks;
- open questions;
- dependencies;
- test concerns;
- scope clarifications.

These notes help later when the story is developed and tested.

## Example

User story:

```text
As a customer,
I want to apply a discount code during checkout,
so that I can reduce my order total.
```

First round estimates:

```text
Developer: 5
Backend developer: 8
QA: 13
Product owner: observes
```

QA explains the higher estimate:

- discount can be fixed amount or percentage;
- invalid codes need validation;
- expired codes need validation;
- partial refund behavior is unclear;
- discount should work with shipping rules.

The team discusses and clarifies scope.

Second round:

```text
Developer: 8
Backend developer: 8
QA: 8
```

Final estimate:

```text
8 story points
```

## Techniques Combined In Planning Poker

Planning Poker combines several estimation ideas.

## Expert Opinion

Team members use their experience to estimate the work.

For example:

- developers estimate technical complexity;
- QA estimates testing complexity;
- automation engineers estimate automation effort;
- product owner clarifies business scope.

## Analogous Estimation

The team compares the current user story with similar stories completed earlier.

Example:

```text
This new discount-code story is similar to the previous coupon feature,
but it has more refund scenarios.
```

Past experience helps make the estimate more realistic.

## Disaggregation

If a user story is too large, the team splits it into smaller stories.

Large stories are harder to estimate accurately.

Example:

Instead of one large story:

```text
Implement checkout discounts
```

Split into:

- apply valid discount code;
- handle invalid and expired codes;
- support percentage discounts;
- support fixed amount discounts;
- handle refunds with discounts.

Smaller stories are easier to estimate, develop, and test.

## Benefits

Planning Poker provides several benefits:

- involves the whole team;
- reduces anchoring bias;
- encourages discussion;
- reveals hidden assumptions;
- exposes unclear requirements;
- helps identify risks;
- supports shared ownership;
- produces quick but reliable estimates;
- helps split oversized stories;
- improves team understanding of the work.

For QA, it is a strong opportunity to raise testability, edge cases, and acceptance criteria questions early.

## Limitations

Limitations:

- estimates are still approximate;
- can take too long if stories are unclear;
- dominant personalities can still influence discussion;
- team needs shared understanding of story points;
- not ideal for very large vague epics;
- historical velocity is needed for planning capacity.

Planning Poker works best when stories are reasonably small and acceptance criteria are clear.

## Common Mistakes

Common mistakes:

- revealing estimates before everyone votes;
- letting one person dominate;
- discussing too long without clarifying scope;
- estimating vague stories;
- treating story points as exact hours;
- ignoring QA and testing effort;
- not splitting very large stories;
- forcing consensus too quickly.

## Best Practices

Good practices:

- keep voting private until reveal;
- include QA in estimation;
- discuss high and low estimates;
- capture assumptions;
- split large stories;
- use past stories as references;
- keep story point scale consistent;
- re-estimate when scope changes;
- use estimates for planning, not performance evaluation.

## Key Idea

Planning Poker helps Agile teams estimate through private voting and structured discussion.

Главная мысль:

> The estimate is useful, but the conversation that reveals assumptions and risks is often even more valuable.

## Questions

1. What is Planning Poker?
2. Why are estimates revealed at the same time?
3. Why does Planning Poker use Fibonacci numbers?
4. How does QA contribute during Planning Poker?
5. When should a user story be split?

## What To Review Later

- Scrum
- Story Points
- Analogous Estimation
- Wideband Delphi
- User Stories
- Acceptance Criteria
