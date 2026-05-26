# Boundary Value Analysis

## Summary

Boundary Value Analysis, или BVA, - это test design technique, которая фокусируется на testing values at the boundaries between equivalence partitions.

Идея BVA: defects часто появляются на границах диапазонов. Поэтому вместо случайного выбора values внутри диапазона QA проверяет edge values: minimum, maximum, and values just outside the valid range.

Эта техника обычно используется вместе с Equivalence Partitioning.

Проще:

- `Equivalence Partitioning` помогает найти группы values.
- `Boundary Value Analysis` помогает проверить edges between those groups.

## Key Points

- BVA основана на testing boundaries between partitions.
- Проверяются valid boundaries and invalid boundaries.
- Особенно полезна для numeric ranges, string length, dates, quantities and limits.
- Boundary defects часто возникают из-за ошибок типа `<`, `<=`, `>`, `>=`.
- BVA делает testing более effective, потому что targets risky values.
- BVA often complements Equivalence Partitioning.
- Open boundaries нужно уточнять или тестировать experience-based approach.

## Notes

### What Is Boundary Value Analysis?

Boundary Value Analysis проверяет values на краях partitions.

Если system accepts values from `1` to `99`, boundaries are:

- minimum valid value: `1`;
- maximum valid value: `99`;
- invalid value just below minimum: `0`;
- invalid value just above maximum: `100`.

Почему это важно?

Developers часто ошибаются именно на boundaries:

- allowed `0` instead of `1`;
- rejected `99` by mistake;
- accepted `100`;
- confused `<` with `<=`;
- forgot maximum value check.

### BVA and Equivalence Partitioning

BVA usually starts after equivalence partitions are identified.

Example:

For input range `1` to `99`:

Equivalence partitions:

| Partition | Type | Example |
| --- | --- | --- |
| `< 1` | Invalid | `0` |
| `1` to `99` | Valid | `50` |
| `> 99` | Invalid | `100` |

Boundary values:

| Boundary Value | Type |
| --- | --- |
| `0` | Invalid boundary |
| `1` | Valid boundary |
| `99` | Valid boundary |
| `100` | Invalid boundary |

EP gives representative values. BVA gives edge values.

### Example: Printer Copies

Imagine a printer field where user can enter number of copies from `1` to `99`.

Valid partition:

- `1` to `99`

Invalid partitions:

- `< 1`
- `> 99`

Boundary values:

| Value | Meaning | Expected Result |
| --- | --- | --- |
| `0` | just below valid range | Error |
| `1` | minimum valid value | Accepted |
| `99` | maximum valid value | Accepted |
| `100` | just above valid range | Error |

These four values are stronger than randomly testing values such as `25`, `50`, `75`.

### Example: Bank Savings Account

In the Equivalence Partitioning example, interest rate depends on account balance:

- `$0.00` to `$100.00` gets `3%`;
- `$100.01` to `$999.99` gets `5%`;
- `$1000.00+` gets `7%`;
- values below `$0.00` are invalid.

Boundary values:

| Value | Type | Expected Result |
| --- | --- | --- |
| `-$0.01` | Invalid boundary | Error |
| `$0.00` | Valid boundary | 3% |
| `$100.00` | Valid boundary | 3% |
| `$100.01` | Valid boundary | 5% |
| `$999.99` | Valid boundary | 5% |
| `$1000.00` | Valid boundary | 7% |

These values target the exact places where interest rate changes.

### Why Random Testing Is Weaker

Imagine a tester checks:

```text
$50, $100, $150, $200, $250, ... $800
```

This tester accidentally hits `$100`, but misses many important boundaries:

- `-$0.01`;
- `$0.00`;
- `$100.01`;
- `$999.99`;
- `$1000.00`;
- possible maximum balance.

Random or evenly spaced values can create many tests but still miss the riskiest points.

BVA is more intentional.

## Open Boundaries

An open boundary exists when one side of a partition is not defined.

Example:

Specification says:

- `$1000.00 and above` gets `7%`.

But it does not define maximum account balance.

This means the upper boundary is open.

### How To Handle Open Boundaries

Open boundaries are difficult to test, but QA should not ignore them.

Possible approaches:

1. Check specification again.
2. Ask business analyst, product owner or developer.
3. Check related requirements.
4. Check database field limits.
5. Check UI input restrictions.
6. Check API validation rules.
7. Use experience-based testing with large values.

Example:

If account balance field supports six digits plus two decimals, maximum value may be:

```text
$999,999.99
```

Then QA can use this as maximum boundary candidate.

If no maximum can be found, QA should document the uncertainty and test large values to explore behavior.

## BVA for Strings

BVA is not only for numbers. It can be applied to string length.

Example:

Name field accepts `1` to `30` characters.

Partitions:

- `0` characters: invalid;
- `1` to `30` characters: valid;
- `31+` characters: invalid.

Boundary values:

| Length | Type | Expected Result |
| --- | --- | --- |
| `0` | Invalid boundary | Error |
| `1` | Valid boundary | Accepted |
| `30` | Valid boundary | Accepted |
| `31` | Invalid boundary | Error |

Examples:

- empty string;
- one-character name;
- 30-character name;
- 31-character name.

### BVA for Dates

Example:

Booking date must be from today to 90 days ahead.

Boundary values:

- yesterday;
- today;
- tomorrow;
- today + 89 days;
- today + 90 days;
- today + 91 days.

### BVA for File Upload

Example:

File size must be up to `10 MB`.

Boundary values:

- `0 MB` or empty file if relevant;
- very small valid file;
- exactly `10 MB`;
- `10 MB + 1 byte`;
- unsupported file type if type validation exists.

## Common Boundary Patterns

Common values to check:

- minimum valid value;
- maximum valid value;
- just below minimum;
- just above maximum;
- empty/null value;
- zero;
- one;
- negative one;
- maximum field length;
- one character over maximum;
- first valid date;
- last valid date;
- value at business rule transition.

## Advantages

- Finds defects at high-risk edges.
- Reduces unnecessary test cases.
- Works well with Equivalence Partitioning.
- Easy to apply to ranges and limits.
- Useful for input validation.
- Helps find off-by-one errors.
- Makes test design more intentional.

## Limitations

- Requires clear boundaries.
- Open boundaries can be hard to test.
- Not enough for complex business logic by itself.
- Does not replace decision tables or state transition testing.
- Poorly defined requirements can make BVA uncertain.
- May miss defects inside a partition.

## Common Mistakes

- Testing only middle values and missing boundaries.
- Forgetting invalid boundaries.
- Not checking just outside the valid range.
- Ignoring open boundaries.
- Not stating assumptions about decimals or precision.
- Confusing EP representative values with BVA boundary values.
- Forgetting string length boundaries.
- Missing boundaries in dates, file sizes and counts.

## Commands / Terms

- `Boundary Value Analysis` - test design technique focused on edges between partitions.
- `Boundary Value` - value at or near the edge of a partition.
- `Valid Boundary` - boundary value inside a valid partition.
- `Invalid Boundary` - boundary value inside an invalid partition.
- `Open Boundary` - boundary that is not fully specified.
- `Equivalence Partitioning` - technique for grouping values into equivalent classes.
- `Off-by-One Error` - defect caused by incorrect boundary logic.
- `Minimum Value` - lowest accepted value.
- `Maximum Value` - highest accepted value.

## Questions

1. What is Boundary Value Analysis?
2. Why are boundaries important in testing?
3. How is BVA related to Equivalence Partitioning?
4. What are valid and invalid boundaries?
5. What boundary values would you test for range `1` to `99`?
6. What is an open boundary?
7. How can QA handle open boundaries?
8. How can BVA be applied to string length?
9. What is an off-by-one error?
10. What are common mistakes when using BVA?

## What To Review Later

- Equivalence Partitioning
- Input validation
- Off-by-one errors
- Numeric ranges
- String length testing
- Date boundaries
- Open boundaries
- Decision Table Testing
