# Kanban

## Summary

Kanban is an Agile framework for managing work by visualizing workflow, limiting work in progress, and continuously improving the process. A team can see all tasks on a Kanban board, understand current capacity, and identify bottlenecks faster.

The main idea of Kanban is to make work transparent and manage the flow of tasks. Unlike Scrum, Kanban does not require fixed-length sprints, roles, or ceremonies. Work moves continuously: a new task is pulled when the team has capacity.

## Key Points

- Kanban visualizes work through boards and cards.
- Work in progress is controlled through WIP limits.
- The team optimizes flow instead of planning work only in sprint blocks.
- Kanban helps identify bottlenecks and reduce cycle time.
- Main metrics include cycle time, lead time, cumulative flow diagram, and control chart.
- Kanban works well for support, operations, maintenance, and teams with a continuous stream of incoming tasks.
- Scrum uses fixed sprints, while Kanban uses continuous flow.

## Notes

### What Is Kanban?

Kanban is a work management method that helps teams see tasks, control workload, and improve delivery.

In software development, Kanban is often used by Agile and DevOps teams. It helps teams synchronize work in real time: everyone can see what is planned, what is in progress, what is blocked, and what is done.

### Kanban Flow

Kanban flow is the movement of tasks through a workflow from start to finish.

A simple flow may look like this:

- **To Do**
- **In Progress**
- **Done**

In a real software team, the workflow may be more detailed:

- Backlog
- Ready
- In Progress
- Code Review
- Testing
- Done

The point is not the number of columns. The board should reflect the team's real process.

### How to Structure Kanban Flow

#### 1. Visualize Workflow

The team starts by visualizing the process on a Kanban board.

Each column represents a stage of work. Each task is represented by a Kanban card. This makes it easy to understand where work is and what is happening right now.

#### 2. Standardize Workflow

The workflow should be clear and agreed upon.

The team defines what each column means, when a task can move forward, and which criteria must be met.

For example, the `Testing` column may mean that a task is already developed, deployed to a test environment, and ready for QA verification.

#### 3. Identify Blockers and Dependencies

The Kanban board should make blockers and dependencies visible.

If a task is stuck in one column, it is a signal: information may be missing, there may be a technical issue, someone may be overloaded, or there may be a dependency on another team.

#### 4. Set WIP Limits

**WIP limit** is a limit on how many tasks can be in a specific column at the same time.

For example, if `Code Review` has a WIP limit of 2, the team should not keep more than two tasks in review at once.

WIP limits help:

- reduce multitasking;
- finish started work faster;
- reveal bottlenecks;
- improve focus;
- stabilize flow.

#### 5. Encourage Collaboration

Kanban works better when the team thinks "our flow" instead of "my task."

If the `Testing` column is overloaded, developers can help QA: clarify acceptance criteria, fix the environment, check simple cases, or react faster to defects.

#### 6. Use Kanban Cards

A Kanban card represents one work item.

A card usually contains:

- title;
- description;
- assignee;
- priority;
- acceptance criteria;
- estimate or size;
- links to requirements, design, tickets, or pull requests;
- status and blockers.

A good card helps people understand the work without unnecessary meetings.

### History of Kanban

Kanban did not originate in software development. Its roots are connected to Toyota and manufacturing in the late 1940s.

Toyota wanted to manage inventory better and produce parts just in time. The idea was similar to a supermarket: keep only the inventory that is needed and replenish it based on actual demand.

The word **kanban** is often translated from Japanese as "signboard" or "card." In manufacturing, a card signaled what materials were needed, in what quantity, and when they should be replenished.

Later, this approach was adapted for software teams: instead of physical materials, the team manages the flow of tasks.

### Kanban for Software Teams

Software teams use Kanban to match work in progress with the team's real capacity.

This provides:

- flexible planning;
- work transparency;
- less overload;
- faster delivery;
- focus on continuous improvement;
- clearer bottlenecks.

Kanban is especially useful when work arrives continuously and is hard to package into a sprint in advance: support issues, production bugs, operations, maintenance, and DevOps tasks.

### Kanban Board

The Kanban board is the team's main tool.

It can be physical or digital. Modern software teams usually use digital boards because they provide traceability, remote access, links, history, and integration with other tools.

The board should be the single source of truth. If work is not visible on the board, the team cannot manage the flow.

### Kanban Cards

Kanban cards represent individual work items.

The main value of cards is visibility. The team can see:

- who is working on a task;
- which stage it is in;
- whether there are blockers;
- how many tasks are in progress;
- where queues are forming.

For QA, Kanban cards are especially useful because they show which tasks are ready for testing, which returned to fixing, and which passed verification.

### Benefits of Kanban

#### Planning Flexibility

A Kanban team focuses on current work.

When a task is finished, the team pulls the next task from the backlog. A Product Owner or manager can change backlog priorities without breaking a sprint forecast because Kanban is not tied to fixed sprint commitment.

#### Shorter Cycle Time

**Cycle time** is the time from when work starts on a task until the task is completed.

Kanban helps reduce cycle time because the team can see where tasks get stuck and improve flow.

If only one person has a certain skill, that person becomes a bottleneck. Kanban teams often develop shared skills through code review, mentoring, and cross-training.

#### Fewer Bottlenecks

Multitasking reduces efficiency. When too many tasks are started at the same time, the team switches context more often and finishes work more slowly.

WIP limits make bottlenecks visible. If a column reaches its limit, the team should not start new work. Instead, it should help finish work that is already in progress.

#### Visual Metrics

Kanban uses metrics for continuous improvement.

Useful metrics:

- **Cycle Time** - how long a task stays in active work.
- **Lead Time** - how long it takes from request to delivery.
- **Throughput** - how many tasks the team completes in a period.
- **Cumulative Flow Diagram** - shows how many tasks are in each state.
- **Control Chart** - helps analyze cycle time and process stability.

Metrics are not for punishing the team. They are for finding improvements.

#### Continuous Delivery

Kanban works well with CI/CD.

Both ideas focus on frequent delivery of value and reducing delays. The team does not need to wait until the end of a sprint to release. If work is ready and meets the Definition of Done, it can be delivered to users.

### Scrum vs Kanban

Scrum and Kanban are both Agile approaches, but they work differently.

| Area | Scrum | Kanban |
|---|---|---|
| Delivery | Fixed-length sprints | Continuous flow |
| Roles | Product Owner, Scrum Master, Developers | No special roles required |
| Planning | Sprint Planning | Continuous prioritization |
| Main metric | Velocity | Cycle time / Lead time |
| Change | Avoid changing sprint forecast | Change can happen anytime |
| Best fit | Product/feature development | Support, operations, continuous work |

Some teams combine approaches in **Scrumban**: they keep Scrum's planning and backlog discipline while using WIP limits and flow from Kanban.

### Common Kanban Mistakes

Kanban looks simple, but it is easy to use superficially.

Common mistakes:

- the board does not reflect the real workflow;
- there are no WIP limits;
- the team ignores bottlenecks;
- cards are too vague;
- there is no Definition of Done;
- metrics are not used;
- the board becomes a pretty picture instead of a working tool.

### When to Use Kanban

Kanban is useful when:

- tasks arrive continuously;
- priorities change often;
- the team works on support or maintenance;
- fixed sprint scope is hard to plan;
- fast reaction matters;
- bottlenecks must be visible;
- the team wants to improve flow gradually.

## Commands / Terms

- **Kanban** - an Agile framework for visual management of work flow.
- **Kanban Board** - a board showing workflow and tasks.
- **Kanban Card** - a card for one work item.
- **WIP (Work in Progress)** - work that has started but is not finished.
- **WIP Limit** - a limit on how many tasks can be in a state.
- **Cycle Time** - time from work start to completion.
- **Lead Time** - time from request to delivery.
- **Throughput** - number of completed tasks in a period.
- **Cumulative Flow Diagram** - a chart showing tasks across states.
- **Control Chart** - a chart for analyzing cycle time.
- **Scrumban** - a hybrid of Scrum and Kanban.

## Questions

**1. What is Kanban?**  
Kanban is an Agile framework that visualizes work, limits WIP, and helps improve flow.

**2. Why are WIP limits useful?**  
They reduce multitasking, improve focus, and make bottlenecks visible.

**3. How is Kanban different from Scrum?**  
Scrum uses fixed sprints and defined roles. Kanban uses continuous flow and does not require special roles.

**4. What is cycle time?**  
Cycle time is the time from when the team starts working on a task until the task is completed.

**5. When is Kanban especially useful?**  
When tasks arrive continuously, priorities change often, and the team needs fast reaction and visible bottlenecks.

**6. What is a common Kanban mistake?**  
Using a board without WIP limits or flow analysis. Then Kanban becomes just a task list.

## What To Review Later

- Difference between Scrum and Kanban.
- WIP limits.
- Cycle time vs lead time.
- Cumulative flow diagram.
- Control chart.
- Scrumban.
- How QA work moves through Kanban flow.
