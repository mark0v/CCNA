# Extreme Programming

## Summary

Extreme Programming, or XP, is an Agile software development framework that strongly emphasizes engineering practices, code quality, fast feedback, and a sustainable pace for the team.

XP helps teams handle changing requirements, reduce technical risk, and deliver high-quality software through short cycles, automated tests, continuous integration, pair programming, and simple design.

## Key Points

- XP is one of the most engineering-specific Agile frameworks.
- Its main goal is higher quality software and better quality of life for the development team.
- XP is especially useful with changing requirements and technical uncertainty.
- Core values are communication, simplicity, feedback, courage, and respect.
- XP emphasizes practices such as pair programming, test-first programming, continuous integration, small releases, and refactoring.
- XP works best in small, closely collaborating, cross-functional teams.
- Many teams do not use XP fully, but adopt selected engineering practices from it.

## Notes

### What Is Extreme Programming?

Extreme Programming is an Agile framework focused not only on process management but also on software engineering practices.

Scrum mostly describes roles, events, and artifacts. XP more directly answers the question: "How should a team write quality code when requirements change?"

The word "Extreme" does not mean chaos. It means useful practices are taken seriously and applied with discipline. If code review is useful, XP uses pair programming as continuous review. If testing is useful, XP writes tests before production code.

### When XP Is Applicable

XP is especially appropriate when:

- software requirements change dynamically;
- the project has fixed time and uses new technology;
- the team is small and collaborates closely;
- team members can communicate frequently;
- the technology stack supports automated unit and functional tests;
- fast feedback and high code quality are important.

XP cannot always be implemented fully. Distributed teams, rigid organizations, or projects without test automation can struggle. Still, individual XP practices can often be adopted.

### Values of XP

#### Communication

Software development is a team sport. The team constantly shares knowledge about requirements, code, architecture, risks, and defects.

XP emphasizes direct communication, preferably face-to-face, with whiteboards, diagrams, or other visual tools.

#### Simplicity

Simplicity asks: "What is the simplest thing that will work?"

The team should not build complex future-oriented design unless current requirements require it. Simple design is easier to maintain, test, and change.

#### Feedback

XP is built around short feedback loops.

Feedback comes from tests, customer conversations, pair programming, continuous integration, and working software. The team quickly sees what works and what must change.

#### Courage

Courage is the willingness to act even when uncertainty or fear exists.

The team needs courage to discuss problems, change practices that do not work, accept difficult feedback, refactor code, and make blockers visible.

#### Respect

XP cannot work without respect.

Team members must respect each other to communicate honestly, give feedback, accept criticism, and find simple solutions together.

### Core XP Practices

XP practices are interconnected. They can be applied separately, but the strongest effect appears when they support each other.

Classic XP practices include:

- Planning Game;
- Small Releases;
- Metaphor;
- Simple Design;
- Testing;
- Refactoring;
- Pair Programming;
- Collective Ownership;
- Continuous Integration;
- Sustainable pace;
- On-site Customer;
- Coding Standard.

Later descriptions refined those practices into a more practical set.

### Sit Together

Because communication is one of XP's main values, the team should be able to communicate quickly and easily.

The ideal is a shared workspace without barriers. Distributed teams can partially replace this with high-quality calls, shared boards, chat, and documentation.

### Whole Team

XP assumes a cross-functional team where everyone needed for delivery works together.

This may include developers, QA, a customer representative, analyst, UX, DevOps, and other roles. The key idea is that the team works toward a shared goal instead of passing tasks between silos.

### Informative Workspace

The workspace should make work transparent.

The team uses information radiators: boards, charts, test status, build status, blockers, and progress indicators. The current project state should be visible without long reports.

### Energized Work

XP supports sustainable pace.

Knowledge work requires focus and mental energy. Constant overtime lowers quality, increases defects, and damages the team.

Energized work means the team works intensely but avoids chronic overwork.

### Pair Programming

Pair Programming means two people write production code together at one workstation or in one remote session.

One person may be the driver and write code, while the other is the navigator and thinks about design, edge cases, readability, and risks. The roles change regularly.

Benefits:

- continuous code review;
- fewer defects;
- faster knowledge sharing;
- fewer bottlenecks;
- better focus.

### Stories

XP uses stories to describe what users want to do with the product.

A story is a short description of a user need that helps planning and acts as a reminder for a future conversation.

A story should not replace communication. It should start a conversation between the customer and the team.

### Weekly Cycle

The Weekly Cycle is similar to a short iteration.

At the start of the week, the team and customer choose stories to implement. The team breaks them into tasks and works toward tested features.

At the end of the cycle, the team demonstrates the result and gets feedback.

### Quarterly Cycle

The Quarterly Cycle connects short weekly cycles with a broader release plan.

The customer defines high-level features for a quarter or release. The plan can change every week as new information appears.

### Slack

Slack is reserve capacity in the plan.

The team can include low-priority tasks that may be dropped if more important work takes longer. This helps account for uncertainty without breaking the whole forecast.

### Ten-Minute Build

Ten-Minute Build means the whole system should build and run tests in about 10 minutes.

If the build is too slow, the team runs it less often. The less often build and tests run, the later errors are found.

This practice supports Continuous Integration and Test-First Programming.

### Continuous Integration

Continuous Integration means code changes are frequently integrated into the main codebase and checked automatically.

XP follows the idea: if integration hurts, do it more often.

Frequent integration reduces change size, shows conflicts earlier, and lowers the risk of a big integration disaster at the end.

### Test-First Programming

Test-First Programming changes the usual order:

```text
write failing automated test -> run failing test -> write code -> run test -> refactor -> repeat
```

This is close to TDD.

Benefits:

- short feedback cycle;
- fewer bugs;
- clearer design;
- more confidence during refactoring;
- executable specification through tests.

### Incremental Design

Incremental Design means the team does enough upfront thinking to understand the general direction, but detailed design evolves while delivering features.

This reduces the cost of change because design decisions are made with current information.

Refactoring supports incremental design: the team continuously improves code structure, removes duplication, and keeps design simple.

### Roles in XP

XP does not strongly emphasize formal roles, but several roles are common.

#### Customer

The Customer makes business decisions:

- which features are needed;
- how to know the system is done;
- which acceptance criteria to use;
- what budget and business case exist;
- what to do next.

The XP Customer should be actively involved and provide clear direction.

#### Developer

Developers implement stories selected by the Customer.

In XP, "developer" can include everyone involved in product creation because the team is cross-functional.

#### Tracker

The Tracker follows metrics if the team finds that useful.

Examples:

- velocity;
- reasons for velocity changes;
- overtime;
- passing and failing tests;
- build health.

This role is optional.

#### Coach

The Coach helps the team apply XP practices.

This is usually someone with XP experience who helps avoid common mistakes and supports discipline.

### XP Lifecycle

XP lifecycle can be described through stories, release planning, quarterly cycles, and weekly cycles.

1. The Customer describes desired results through stories.
2. The team estimates stories.
3. The Customer prioritizes stories by value.
4. If there is technical uncertainty, the team performs a spike.
5. The team and Customer create a release plan.
6. The team works through weekly cycles.
7. At the end of each cycle, customer review determines whether to continue, change priority, or finish work.

**Spike** is a short time-boxed research activity used to investigate technical unknowns.

### Origins of XP

XP became known through the Chrysler Comprehensive Compensation (C3) project in the 1990s.

Kent Beck was brought in to improve the project and applied the approach that later became Extreme Programming. Ron Jeffries and other participants helped develop and spread these ideas.

### Primary Contribution

XP's main contribution is a set of interconnected engineering practices.

Many Agile teams start with Scrum or Kanban and later add XP practices when they realize they need more technical discipline.

XP reminds us of something important: Agile without engineering excellence can become a nice process on top of weak code.

## Commands / Terms

- **Extreme Programming (XP)** - an Agile framework focused on engineering practices.
- **Pair Programming** - two people developing production code together.
- **Test-First Programming** - tests before code.
- **TDD** - test-driven development.
- **Continuous Integration** - frequent integration with automated checks.
- **Ten-Minute Build** - build and tests are fast enough to run often.
- **Incremental Design** - design evolves gradually with the product.
- **Refactoring** - improving code structure without changing behavior.
- **Story** - a short description of a user need.
- **Spike** - short research into technical uncertainty.
- **Sustainable Pace** - steady work without chronic overwork.

## Questions

**1. What is Extreme Programming?**  
XP is an Agile framework focused on software quality and engineering practices.

**2. What are the five XP values?**  
Communication, simplicity, feedback, courage, and respect.

**3. Why does XP emphasize automated tests?**  
Tests provide fast feedback, reduce defect risk, and make code changes safer.

**4. What is pair programming?**  
It is a practice where two people write production code together while continuously reviewing design, logic, and implementation.

**5. When is XP especially useful?**  
When requirements change, technical uncertainty exists, quality matters, and the team can communicate often.

**6. Why do XP practices work better together?**  
Because they reinforce each other: test-first supports CI, CI supports refactoring, and pair programming improves design and knowledge sharing.

## What To Review Later

- XP values.
- Pair programming.
- Test-first programming and TDD.
- Continuous integration.
- Refactoring.
- Incremental design.
- Difference between Scrum and XP.
- How QA participates in XP.
