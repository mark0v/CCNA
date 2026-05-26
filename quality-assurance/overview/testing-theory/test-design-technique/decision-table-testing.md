# Decision Table Testing

## Summary

Decision Table Testing - это specification-based / black-box test design technique, которая помогает тестировать combinations of conditions and actions.

Equivalence Partitioning и Boundary Value Analysis хорошо работают для отдельных inputs and ranges. Но если behavior системы зависит от combinations of inputs, events, states или business rules, удобнее использовать decision table.

Decision table показывает:

- какие conditions существуют;
- какие combinations этих conditions возможны;
- какие actions/outcomes должны произойти для каждой combination.

Эта техника особенно полезна для business logic.

## Key Points

- Decision table помогает тестировать combinations.
- Техника полезна для complex business rules.
- Каждая column обычно представляет отдельное rule/combination.
- Conditions часто имеют values `True/False`, `Yes/No`, `Y/N`.
- Actions показывают expected outcome для каждой rule.
- Decision tables помогают находить gaps, contradictions и ambiguity in specifications.
- Если combinations слишком много, QA выбирает prioritized subset.
- Decision table иногда называют cause-effect table.

## Notes

### What Is a Decision Table?

Decision table - это table, которая связывает conditions with actions.

Она отвечает на вопрос:

> If these conditions are true or false, what should the system do?

Decision tables are useful when:

- multiple inputs affect result;
- business rules have combinations;
- behavior changes depending on conditions;
- specification has many "if/then" rules;
- QA needs to make combinations visible.

### Why EP and BVA Are Not Enough

Equivalence Partitioning helps divide input values into classes.

Boundary Value Analysis helps test edges between classes.

But they are less convenient when behavior depends on combinations.

Example:

Discount depends not only on one input, but on a combination:

- new customer;
- loyalty card;
- coupon.

Testing each input separately may miss important combination defects.

Decision table helps see all possible combinations.

## How To Use Decision Tables

Typical steps:

1. Identify function or subsystem with conditional logic.
2. Identify conditions that affect behavior.
3. Identify possible values for each condition.
4. Create combinations of conditions.
5. Identify expected actions/outcomes for each combination.
6. Review table for missing or impossible combinations.
7. Create test cases for rules.
8. Prioritize rules if there are too many combinations.

### Combination Growth

If conditions are binary, number of combinations is:

```text
2^n
```

Where `n` is the number of conditions.

Examples:

| Number of Conditions | Number of Combinations |
| --- | --- |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

This is why large sets of conditions should be split into smaller groups where possible.

## Example 1: Loan Application

Imagine a loan application where customer can enter:

- repayment amount;
- term of loan.

Business rule version 1:

- if repayment amount is entered, process loan amount;
- if term is entered, process term;
- if both are entered, process both or compromise between them;
- if nothing is entered, show error.

### Empty Decision Table

| Conditions / Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Repayment amount entered? |  |  |  |  |
| Term of loan entered? |  |  |  |  |
| Process loan amount |  |  |  |  |
| Process term |  |  |  |  |
| Error message |  |  |  |  |

### Add Input Combinations

With two boolean conditions we have four combinations.

| Conditions / Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Repayment amount entered? | T | T | F | F |
| Term of loan entered? | T | F | T | F |
| Process loan amount |  |  |  |  |
| Process term |  |  |  |  |
| Error message |  |  |  |  |

### Add Expected Outcomes

| Conditions / Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Repayment amount entered? | T | T | F | F |
| Term of loan entered? | T | F | T | F |
| Process loan amount | Y | Y |  |  |
| Process term | Y |  | Y |  |
| Error message |  |  |  | Y |

The table reveals an important missing scenario:

> What happens if customer enters nothing?

If specification did not mention this, decision table helped expose ambiguity.

### Changed Rule: Customer Cannot Enter Both

Now imagine business changes the rule:

- customer cannot enter both repayment amount and term;
- if both are entered, show error;
- if neither is entered, show error.

Decision table:

| Conditions / Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Repayment amount entered? | T | T | F | F |
| Term of loan entered? | T | F | T | F |
| Process loan amount |  | Y |  |  |
| Process term |  |  | Y |  |
| Error message | Y |  |  | Y |

In this version, actions are mutually exclusive: only one outcome happens for each combination.

Same table can be written with result in one row:

| Conditions / Result | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
| --- | --- | --- | --- | --- |
| Repayment amount entered? | T | T | F | F |
| Term of loan entered? | T | F | T | F |
| Result | Error message | Process loan amount | Process term | Error message |

Each rule can become one test case.

## Example 2: Credit Card Discounts

Imagine credit card application with discounts.

Conditions:

- new customer gets `15%` discount today;
- existing customer with loyalty card gets `10%`;
- customer with coupon gets `20%`;
- coupon cannot be used with new customer discount;
- discounts can be added where applicable;
- customer cannot be both new customer and loyalty card holder.

Conditions:

- New customer?
- Loyalty card?
- Coupon?

There are three boolean conditions, so:

```text
2^3 = 8 combinations
```

Decision table:

| Conditions / Actions | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 | Rule 6 | Rule 7 | Rule 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| New customer? | T | T | T | T | F | F | F | F |
| Loyalty card? | T | T | F | F | T | T | F | F |
| Coupon? | T | F | T | F | T | F | T | F |
| Error message | Y | Y |  |  |  |  |  |  |
| 15% discount |  |  |  | Y |  |  |  |  |
| 10% discount |  |  |  |  | Y | Y |  |  |
| 20% discount |  |  | Y |  | Y |  | Y |  |
| Total discount | N/A | N/A | 20% | 15% | 30% | 10% | 20% | 0% |

### Important Observations

Rules 1 and 2 are impossible/invalid because customer cannot be both:

- new customer;
- loyalty card holder.

Expected result: error message.

Rule 3 requires assumption:

- new customer has coupon;
- coupon cannot be combined with new customer discount;
- coupon gives bigger discount (`20%`) than new customer discount (`15%`);
- we assume system applies `20%`.

This assumption should be checked with business/product owner.

Rule 5:

- loyalty card + coupon;
- discounts can be added;
- total discount is `30%`.

Rule 8:

- no discount conditions;
- total discount is `0%`.

## When To Use Decision Tables

Use decision tables when:

- multiple conditions affect outcome;
- business rules are complex;
- combinations matter;
- specification contains many if/then rules;
- QA wants to find missing combinations;
- system has eligibility rules;
- discounts, permissions, validations or workflows depend on several factors.

Good areas:

- pricing;
- discounts;
- loan approvals;
- insurance rules;
- user permissions;
- form validation;
- shipping rules;
- tax calculation;
- access control;
- business workflows.

## Prioritizing Rules

If decision table is small, test every rule.

If decision table is large, testing all combinations may be impractical.

Prioritize:

- high-risk combinations;
- business-critical rules;
- invalid/impossible combinations;
- combinations with history of defects;
- combinations around legal/compliance rules;
- combinations used by many users;
- combinations involving money/security/data.

Do not choose arbitrary subset. Use risk and business value.

## Advantages

- Makes complex business rules visible.
- Helps find missing requirements.
- Helps find contradictory rules.
- Good for combinations of inputs/events/states.
- Useful for communication with developers and business analysts.
- Each rule can become a test case.
- Supports systematic test design.

## Limitations

- Number of combinations grows quickly.
- Large tables can become hard to maintain.
- Binary conditions are simpler than multi-value conditions.
- May require splitting logic into smaller tables.
- Does not replace EP, BVA or state transition testing.
- Requires clear understanding of business rules.

## Common Mistakes

- Trying to put too many conditions in one table.
- Testing arbitrary combinations instead of using full table.
- Forgetting invalid/impossible combinations.
- Not checking assumptions with business.
- Treating blank cells ambiguously.
- Not updating decision table when rules change.
- Confusing actions that can happen together with mutually exclusive outcomes.

## Commands / Terms

- `Decision Table` - table showing conditions, combinations and actions.
- `Rule` - one combination of conditions in a decision table.
- `Condition` - input, event or state that affects outcome.
- `Action` - expected result for a rule.
- `Cause-Effect Table` - another name sometimes used for decision table.
- `T/F` - True/False.
- `Y/N` - Yes/No.
- `Mutually Exclusive` - only one action can happen for a combination.
- `Combination` - set of condition values.

## Questions

1. What is decision table testing?
2. When should QA use decision tables?
3. Why are decision tables useful for business rules?
4. What is a rule in a decision table?
5. How many combinations exist for three boolean conditions?
6. Why can large decision tables become difficult?
7. How can decision tables reveal missing requirements?
8. What should QA do with assumptions found during table design?
9. When can one rule become one test case?
10. How should QA prioritize decision table rules?

## What To Review Later

- Equivalence Partitioning
- Boundary Value Analysis
- State Transition Testing
- Business rules
- Cause-effect logic
- Test case prioritization
- Risk-based testing
