# State Transition Testing

## Summary

State Transition Testing is a black-box test design technique used when system behavior depends on the current state and previous events.

If the same input can produce a different output depending on what happened before, the system can be treated as a finite state system.

The technique helps model states, transitions, events, and actions, then design tests that cover important state changes.

## Key Points

- State transition testing is useful for systems with states.
- System behavior depends on current state and event.
- The same event can produce different results in different states.
- The model is usually represented as a state diagram or state transition table.
- Main elements: states, transitions, events, actions.
- The technique is black-box because tests are derived from behavior model/specification.
- Coverage can be measured by states, transitions, transition pairs, and longer transition sequences.

## Notes

### What Is State Transition Testing?

State Transition Testing is used when some aspect of the system can be described as a finite state machine.

Finite state machine means:

- system has limited number of possible states;
- transitions move system from one state to another;
- events trigger transitions;
- actions may happen during transitions;
- not every transition is allowed.

Simple idea:

> System behavior depends not only on current input, but also on current state.

### Example: ATM Withdrawal

Imagine user requests to withdraw `$100` from ATM.

First time, account has sufficient funds:

- input: withdraw `$100`;
- state: sufficient funds;
- result: cash is given;
- new state may become insufficient funds.

Second time, user makes same request:

- input: withdraw `$100`;
- state: insufficient funds;
- result: transaction rejected.

Same input. Different state. Different output.

### Example: Word Processor

Document can have two states:

- open;
- closed.

If document is open:

- event: Close;
- action: document closes;
- new state: closed.

If document is already closed:

- event: Close;
- action: not available / error / disabled command;
- state remains closed.

## Four Parts of State Transition Model

### 1. States

States are possible conditions of the system.

Examples:

- open / closed;
- logged in / logged out;
- sufficient funds / insufficient funds;
- active / inactive;
- draft / submitted / approved / rejected;
- cart empty / cart has items.

### 2. Transitions

Transitions are movements from one state to another.

Not all transitions are allowed.

### 3. Events

Events trigger transitions.

Examples:

- user clicks button;
- card inserted;
- PIN entered;
- payment received;
- timeout occurs;
- file closed;
- balance requested.

### 4. Actions

Actions are results of transitions.

Examples:

- show error message;
- eject card;
- give cash;
- close document;
- update order status;
- send email;
- lock account.

## State Diagram

State transition model is often represented as a state diagram.

Typical notation:

- states are circles/boxes;
- transitions are arrows;
- events are labels on arrows;
- actions may be shown near transitions.

Example:

```text
Closed --Open document--> Open
Open --Close document--> Closed
Closed --Close document--> Closed + Error/Disabled
```

## Example: PIN Entry

Imagine ATM card PIN entry.

Possible states:

- start;
- wait for PIN;
- first incorrect try;
- second incorrect try;
- third incorrect try;
- access account;
- eat card.

Events:

- card inserted;
- enter PIN;
- PIN OK;
- PIN not OK;
- timeout;
- cancel.

Possible scenarios:

### Test 1: Correct PIN First Time

Flow:

1. Start.
2. Card inserted.
3. Wait for PIN.
4. Enter PIN.
5. PIN OK.
6. Access account.

### Test 2: Incorrect PIN Three Times

Flow:

1. Start.
2. Card inserted.
3. Wait for PIN.
4. PIN not OK.
5. First incorrect try.
6. PIN not OK.
7. Second incorrect try.
8. PIN not OK.
9. Third incorrect try.
10. Eat card.

### Test 3: Incorrect First, Correct Second

Flow:

1. Card inserted.
2. PIN not OK.
3. First incorrect try.
4. Enter PIN again.
5. PIN OK.
6. Access account.

### Additional Missing Transitions

A real ATM model should also include:

- timeout from wait for PIN;
- timeout after incorrect attempts;
- cancel from wait for PIN;
- cancel after incorrect attempts;
- transition from eat card back to start;
- card eject behavior.

State transition modeling helps notice these missing paths.

## Transitions That Stay in Same State

Transition does not always change state.

Example:

State: `Access account`.

Event: `Request balance`.

Action:

- show balance.

New state:

- still `Access account`.

This is still a transition, even if start and end state are the same.

## How To Derive Test Cases

Test conditions can be derived from:

- each state;
- each transition;
- each event;
- each action;
- valid transitions;
- invalid transitions;
- transition pairs;
- transition triples;
- important end-to-end state flows.

Typical steps:

1. Identify system states.
2. Identify events.
3. Identify allowed transitions.
4. Identify forbidden transitions.
5. Identify actions.
6. Draw state diagram or create state table.
7. Choose coverage target.
8. Create test cases.

## State Transition Coverage

### State Coverage

Tests visit each state at least once.

### Transition Coverage

Tests execute each transition at least once.

This is also known as `0-switch coverage`.

### Transition Pair Coverage

Tests cover pairs of transitions.

This is also known as `1-switch coverage`.

### Transition Triple Coverage

Tests cover triples of transitions.

This is also known as `2-switch coverage`.

## State Transition Table

State transitions can also be represented as a table.

Example: document state.

| Current State | Event | Action | Next State |
| --- | --- | --- | --- |
| Closed | Open document | Open file | Open |
| Open | Close document | Close file | Closed |
| Closed | Close document | Show error / command disabled | Closed |
| Open | Edit document | Save changes in memory | Open |

## When To Use State Transition Testing

Use this technique when:

- system has clear states;
- behavior depends on previous actions;
- same input can produce different outputs;
- workflows have status changes;
- invalid transitions matter;
- business process moves through stages;
- object lifecycle is important.

Good areas:

- login/logout;
- account lockout;
- ATM flows;
- order status;
- payment status;
- document workflow;
- ticket lifecycle;
- booking systems;
- subscription lifecycle;
- approval process.

## Advantages

- Good for systems with states.
- Helps test valid and invalid transitions.
- Finds missing transitions and undefined behavior.
- Useful for business workflows.
- Helps visualize behavior.
- Can be as detailed or abstract as needed.
- Supports clear coverage criteria.

## Limitations

- Not useful when system has no meaningful states.
- Large state models can become complex.
- Requires good understanding of business process.
- Missing states lead to weak tests.
- Many transition combinations can create too many tests.
- May need prioritization for large workflows.

## Common Mistakes

- Testing only happy path.
- Ignoring invalid transitions.
- Forgetting timeout/cancel/error events.
- Assuming transition always changes state.
- Not modeling recovery paths.
- Not checking same event in different states.
- Creating too detailed model for low-risk area.
- Creating too abstract model for critical area.

## Commands / Terms

- `State Transition Testing` - test design technique based on states and transitions.
- `Finite State Machine` - model with finite number of states and rules for transitions.
- `State` - condition or mode of the system.
- `Transition` - movement from one state to another.
- `Event` - trigger that causes transition.
- `Action` - result of transition.
- `State Diagram` - visual model of states and transitions.
- `State Transition Table` - tabular model of current state, event, action and next state.
- `0-switch coverage` - coverage of individual transitions.
- `1-switch coverage` - coverage of transition pairs.
- `2-switch coverage` - coverage of transition triples.

## Questions

1. What is state transition testing?
2. What is a finite state machine?
3. Why can the same input produce different outputs?
4. What are the four parts of state transition model?
5. What is the difference between state and transition?
6. What is an event?
7. What is an action?
8. What is 0-switch coverage?
9. Why should invalid transitions be tested?
10. When is state transition testing useful?

## What To Review Later

- Decision Table Testing
- Business workflows
- State diagrams
- State transition tables
- Valid transitions
- Invalid transitions
- Test coverage
- Black-box test design
