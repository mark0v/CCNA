# Equivalence Partitioning

## Summary

Equivalence Partitioning, or EP, is a black-box test design technique where input or output values are divided into groups called equivalence partitions or equivalence classes.

The idea is simple: if the system should handle several values in the same way, there is no need to test every value. One representative value from each partition may be enough.

This technique helps make testing more efficient and effective: fewer test cases, but better coverage of important groups.

## Key Points

- Equivalence Partitioning is a specification-based / black-box technique.
- It can be applied at any level of testing.
- It is often one of the first test design techniques to use.
- Test conditions are divided into groups that should be treated equivalently.
- One representative test value is usually selected from each partition.
- Valid and invalid partitions should both be considered.
- Tester should think not only about what is written in the specification, but also about missing or undefined cases.
- EP can be applied to inputs and outputs.

## Notes

### What Is Equivalence Partitioning?

Equivalence Partitioning divides a set of test conditions into groups that should be processed in the same way by the software.

These groups are called:

- equivalence partitions;
- equivalence classes.

Both terms mean the same thing.

Example idea:

If all values from `1` to `100` should be handled the same way, QA does not need to test every value. One representative value from that class may be enough.

### Why One Value Can Be Enough

In EP we assume:

- if one value from a partition works, other values in the same partition likely work too;
- if one value from a partition fails, other values in the same partition likely fail too.

This is an assumption, so partitions must be defined carefully.

EP does not mean "test less without thinking". It means "test less, but intentionally".

### Valid and Invalid Partitions

Valid partitions are groups of values expected and accepted by the system.

Invalid partitions are groups of values the system should reject or handle with an error.

Important:

`Invalid` does not always mean impossible to enter. It means the value is not expected or not valid for this field/condition.

## Example: Bank Savings Account

Imagine a savings account where interest rate depends on account balance.

Specification:

- balance from `$0` to `$100` gets `3%`;
- balance from `$100` to `$1000` gets `5%`;
- balance `$1000` and above gets `7%`.

At first glance, the specification describes three valid ranges.

But tester should also ask:

- What about balance below `$0`?
- What is the maximum allowed balance?
- Are decimal values allowed?
- How many decimal places are supported?
- What about non-numeric input?

### Initial Partitions

| Partition | Type | Expected Result |
| --- | --- | --- |
| Balance `< 0` | Invalid | Error / reject value |
| Balance `0` to `100` | Valid | 3% interest |
| Balance `100` to `1000` | Valid | 5% interest |
| Balance `1000+` | Valid | 7% interest |

This gives at least four partitions, even though the specification explicitly mentioned only three interest rates.

### Example Test Values

| Test Value | Partition | Expected Result |
| --- | --- | --- |
| `-10.00` | Balance `< 0` | Error / invalid balance |
| `50.00` | `0` to `100` | 3% interest |
| `260.00` | `100` to `1000` | 5% interest |
| `1348.00` | `1000+` | 7% interest |

With four test values, QA covers all identified partitions.

### Assumptions Matter

In this example we assume two decimal places, such as `$100.00`.

But another system may support zero, two, or more decimal places.

QA should state assumptions clearly because unclear assumptions often become defects or missed cases.

## EP for Outputs

Equivalence Partitioning can also be applied to outputs.

In the bank example, output partitions are:

- `3% interest`;
- `5% interest`;
- `7% interest`;
- error message for invalid balance.

Sometimes input partitions and output partitions line up clearly. Sometimes they do not, especially when business rules are more complex.

## Naive Testing vs Equivalence Partitioning

Imagine an inexperienced tester decides to test every `$50`:

```text
$50, $100, $150, $200, $250, ... $800
```

This creates many tests, but may miss important partitions:

- negative balance;
- balance `$1000+`;
- non-numeric value;
- maximum boundary.

So the naive approach can be less effective and less efficient.

EP helps select fewer but more meaningful tests.

## How To Use Equivalence Partitioning

Typical steps:

1. Identify input or output condition.
2. Understand expected behavior from requirements.
3. Split values into valid and invalid partitions.
4. Choose representative value from each partition.
5. State assumptions.
6. Create test cases.
7. Review whether any partition is missing.

### Example: Age Field

Requirement:

User age must be from `18` to `65`.

Partitions:

| Partition | Type | Example |
| --- | --- | --- |
| Age `< 18` | Invalid | `15` |
| Age `18` to `65` | Valid | `30` |
| Age `> 65` | Invalid | `70` |
| Non-numeric input | Invalid | `abc` |
| Empty value | Invalid if required | empty |

For exact edges, use Boundary Value Analysis together with EP.

## Equivalence Partitioning and Boundary Value Analysis

Equivalence Partitioning and Boundary Value Analysis are often used together.

EP helps identify classes.

BVA helps test edges between classes.

Example:

For valid age `18` to `65`:

- EP representative: `30`;
- BVA values: `17`, `18`, `19`, `64`, `65`, `66`.

Together they provide stronger coverage.

## Advantages

- Reduces number of test cases.
- Improves test coverage by groups.
- Helps avoid duplicate similar tests.
- Works well for input validation.
- Useful early in test design.
- Easy to explain and apply.
- Helps find missing invalid cases.

## Limitations

- Depends on correct partition identification.
- May miss defects inside a partition if values are not truly equivalent.
- Needs clear requirements or good assumptions.
- Works best with BVA for numeric ranges.
- Complex business rules may need decision tables or state transition testing.

## Common Mistakes

- Testing only valid partitions.
- Forgetting invalid inputs.
- Choosing too many values from one partition and missing another.
- Not stating assumptions.
- Ignoring output partitions.
- Treating EP as replacement for all other techniques.
- Missing boundaries between partitions.

## Commands / Terms

- `Equivalence Partitioning` - test design technique that divides values into equivalent groups.
- `Equivalence Class` - same as equivalence partition.
- `Valid Partition` - group of accepted values.
- `Invalid Partition` - group of rejected or unexpected values.
- `Representative Value` - one selected value from a partition.
- `Specification-Based Technique` - technique based on requirements/specification.
- `Black-Box Technique` - technique based on external behavior, not code internals.
- `Boundary Value Analysis` - technique focused on edges between partitions.

## Questions

1. What is equivalence partitioning?
2. What is an equivalence class?
3. Why can one value from a partition be enough?
4. What is the difference between valid and invalid partitions?
5. Why should QA think about values not mentioned in specification?
6. Can EP be applied to outputs?
7. What is a representative value?
8. How does EP improve testing efficiency?
9. What is the relationship between EP and BVA?
10. What common mistakes happen when using EP?

## What To Review Later

- Boundary Value Analysis
- Valid and invalid classes
- Input validation
- Output partitions
- Test data design
- Black-box testing
- Specification-based testing
