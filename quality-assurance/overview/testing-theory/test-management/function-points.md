# Function Points

## Summary

Function Point, or FP, is a unit of measurement used to express the amount of business functionality that a software system provides to users.

Function Points measure software size from the user and business perspective, not from the technical code perspective.

Function Point Analysis, or FPA, helps teams estimate:

- software size;
- effort;
- cost;
- productivity;
- project duration;
- testing effort.

The core idea is to measure what the system does for the user.

## Why Function Points Matter

Software size can be measured in different ways.

For example:

- lines of code;
- number of modules;
- number of user stories;
- number of screens;
- number of APIs;
- function points.

Function Points are useful because they focus on business functionality instead of implementation details.

This means two applications written in different languages can still be compared by the amount of functionality they provide.

## Function Point Analysis

Function Point Analysis is a technique that quantifies the functions contained in software using terms that are meaningful to users.

It is based on requirements and functional behavior.

FPA looks at:

- data maintained by the application;
- data referenced from outside;
- inputs entering the application;
- outputs leaving the application;
- inquiries that retrieve information.

The result is a functional size expressed in Function Points.

## Standards

Several standards and public specifications exist for functional size measurement.

Examples:

- COSMIC;
- FiSMA;
- IFPUG;
- Mark-II;
- NESMA.

IFPUG Function Point Analysis is one of the most widely known approaches.

Function Point counting is governed by rules, processes, and guidelines, such as those described by the International Function Point Users Group.

## Short History

The concept of Function Points was introduced by Alan Albrecht at IBM in 1979.

The method was refined in the 1980s.

The International Function Point Users Group, or IFPUG, was founded in 1986 and became one of the main organizations supporting Function Point Analysis.

Over time, Function Point counting practices became standardized and used as a recognized approach for functional sizing.

## Elementary Process

An Elementary Process, or EP, is the smallest unit of functional user requirement.

It should be:

- meaningful to the user;
- a complete transaction;
- self-contained;
- able to leave the application in a consistent business state.

Example:

```text
User submits a payment.
```

This is meaningful, complete, and changes the system state.

## Types Of Functions

In Function Point Analysis, functions are usually divided into two major groups:

- Data Functions;
- Transaction Functions.

## Data Functions

Data Functions represent logical data used or maintained by the application.

There are two main types:

- Internal Logical Files;
- External Interface Files.

## Internal Logical File

An Internal Logical File, or ILF, is a user-identifiable group of logically related data maintained inside the application boundary.

The application owns and maintains this data.

Examples:

- customer records;
- orders;
- invoices;
- user profiles;
- product catalog managed by the application.

The main idea:

> ILF is data stored and maintained by the application being measured.

## External Interface File

An External Interface File, or EIF, is a user-identifiable group of logically related data used by the application, but maintained by another application.

The application references this data but does not own or maintain it.

Examples:

- exchange rates from an external finance system;
- customer data maintained by a CRM;
- product data maintained by another service;
- tax rules provided by an external system.

The main idea:

> EIF is external data used for reference.

## Transaction Functions

Transaction Functions represent processes where data moves between the user, external applications, and the application being measured.

There are three main types:

- External Inputs;
- External Outputs;
- External Inquiries.

## External Input

An External Input, or EI, is a transaction where data enters the application from outside its boundary.

Examples:

- user submits a registration form;
- admin creates a product;
- customer places an order;
- another system sends data through API.

The input may:

- update an Internal Logical File;
- change application state;
- submit control information;
- trigger business processing.

The main idea:

> EI brings data into the application.

## External Output

An External Output, or EO, is a transaction where data leaves the application and includes processing or derived information.

Examples:

- generated invoice;
- report with calculated totals;
- exported analytics file;
- email notification with computed data;
- API response with business processing.

An EO may also update an Internal Logical File.

The main idea:

> EO sends processed data out of the application.

## External Inquiry

An External Inquiry, or EQ, is a transaction with both input and output, used to retrieve data without significant processing or updates.

Examples:

- search customer by ID;
- view order details;
- check account balance;
- filter product list.

The main idea:

> EQ retrieves information without changing the system significantly.

## Application Boundary

The application boundary defines what is inside and outside the application being measured.

This is important because the same data can be classified differently depending on the boundary.

Example:

If the application owns customer records, they may be ILF.

If the application only reads customer records from another system, they may be EIF.

Correct boundary definition is critical for accurate Function Point counting.

## RET, DET, And FTR

Function Point counting uses several important terms.

## Record Element Type

A Record Element Type, or RET, is a user-identifiable subgroup of data within an ILF or EIF.

Example:

In a customer file, possible RETs could be:

- personal information;
- billing information;
- shipping information.

## Data Element Type

A Data Element Type, or DET, is a unique user-identifiable data field.

Examples:

- customer name;
- email;
- phone number;
- order date;
- payment amount.

DETs help measure the complexity of data and transaction functions.

## File Type Referenced

A File Type Referenced, or FTR, is an ILF or EIF referenced by a transaction function.

Examples:

- login process references user profile data;
- checkout references order and payment data;
- report generation references invoices and customers.

FTRs help determine complexity for EI, EO, and EQ.

## How Function Points Are Counted

Function Point counting usually follows this logic:

1. Define the application boundary.
2. Identify Data Functions: ILF and EIF.
3. Identify Transaction Functions: EI, EO, and EQ.
4. Count RETs and DETs for data functions.
5. Count FTRs and DETs for transaction functions.
6. Determine complexity.
7. Assign function point values.
8. Sum values to calculate functional size.

The detailed counting rules depend on the selected standard or method.

## Function Points And Estimation

Function Points are often used as input for effort and cost estimation.

Example:

```text
Functional size = 300 FP
Team productivity = 10 FP per person-month

Estimated effort = 300 / 10 = 30 person-months
```

For QA, Function Points can help estimate:

- test design effort;
- test execution effort;
- regression scope;
- required resources;
- project duration.

## Function Points Vs Lines Of Code

| Aspect | Function Points | Lines Of Code |
| --- | --- | --- |
| Measures | Business functionality | Implementation size |
| Depends on language | Less dependent | Highly dependent |
| Useful early from requirements | Yes | Usually no |
| User perspective | Strong | Weak |
| Technical detail | Lower | Higher |

Function Points are often useful earlier in the project because they can be estimated from requirements before code exists.

## Benefits

Benefits of Function Point Analysis:

- measures functionality from user perspective;
- supports early estimation;
- works across technologies;
- helps compare projects;
- supports productivity analysis;
- can improve effort and cost estimation;
- gives a structured sizing method.

## Limitations

Limitations:

- requires training and counting discipline;
- can be time-consuming;
- depends on clear requirements;
- can produce inconsistent results if rules are misunderstood;
- may not capture technical complexity fully;
- needs historical productivity data to be useful for estimation.

Function Points are helpful, but they are not a complete estimation solution by themselves.

## Common Mistakes

Common mistakes:

- counting without defining application boundary;
- confusing ILF and EIF;
- confusing EO and EQ;
- counting technical files instead of user-identifiable data;
- ignoring requirements ambiguity;
- using FP without productivity baseline;
- treating FP estimate as exact.

## Key Idea

Function Points help estimate software size based on business functionality delivered to users.

Главная мысль:

> Function Points measure what the system does for the user, not how many lines of code developers write.

## Questions

1. What is a Function Point?
2. What is Function Point Analysis?
3. What is the difference between ILF and EIF?
4. What is the difference between EI, EO, and EQ?
5. How can Function Points support project estimation?

## What To Review Later

- Function Point Analysis
- Internal Logical File
- External Interface File
- External Input
- External Output
- External Inquiry
- DET
- RET
- FTR
