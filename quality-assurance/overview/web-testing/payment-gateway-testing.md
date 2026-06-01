# Payment Gateway Testing

## Summary

Payment gateway testing - это проверка интеграции между e-commerce application и payment provider, через которую user оплачивает order.

Для QA это high-risk area, потому что ошибки могут привести к:

- failed purchases;
- duplicate charges;
- wrong order status;
- lost revenue;
- incorrect refunds;
- security incidents;
- плохому user trust.

Главная идея:

> Payment testing должен проверять не только кнопку `Pay`, а весь transaction lifecycle: authorization -> capture -> confirmation -> settlement -> void/refund -> reconciliation.

## What Is A Payment Gateway

Payment gateway - это service, который помогает merchant принять payment от customer.

Обычно он:

- получает payment details;
- передает данные в payment processor/acquiring bank;
- получает approve/decline response;
- возвращает результат merchant application;
- поддерживает refunds, voids, webhooks, fraud checks and reporting.

В реальных проектах термины `payment gateway` и `payment processor` иногда используют взаимозаменяемо. Для QA важнее понимать integration flow, callbacks/webhooks, statuses и business rules.

## Key Terms

| Term | Meaning |
| --- | --- |
| Merchant | Company/person selling goods or services. |
| Customer | Buyer who pays for order. |
| Acquiring bank | Bank that supports merchant account and receives funds. |
| Issuing bank | Bank that issued customer card. |
| Authorization | Bank approves payment and reserves funds. |
| Capture | Merchant collects authorized funds. |
| Settlement | Funds are moved to merchant account. |
| Void | Canceling authorized but not yet captured transaction. |
| Refund | Returning captured/settled funds to customer. |
| Chargeback | Customer disputes payment through bank/card network. |
| Webhook | Provider-to-merchant server notification about payment event. |

## Basic Transaction Flow

Typical successful card payment flow:

1. User adds product to cart.
2. User opens checkout.
3. User selects payment method.
4. User submits payment.
5. Application sends payment request to gateway.
6. Gateway/processor asks issuing bank for authorization.
7. Bank approves or declines.
8. Gateway returns response.
9. Application updates order status.
10. User sees success/failed message.
11. Confirmation email/SMS is sent if required.

Depending on product, capture can happen:

- immediately after authorization;
- manually by merchant;
- after shipment;
- in a background job.

## Authorization, Capture, Void And Refund

Payment lifecycle terms matter for test cases.

### Authorization

Authorization reserves money but may not transfer it to merchant yet.

Check:

- authorized amount is correct;
- order status reflects authorization;
- payment can be captured later;
- expired authorization is handled.

### Capture

Capture collects money from authorized transaction.

Check:

- capture amount is correct;
- partial capture works if supported;
- duplicate capture is impossible;
- order moves to correct status.

### Void

Void cancels transaction before capture/settlement.

Check:

- only eligible transactions can be voided;
- held funds are released;
- order status updates;
- customer notification is correct.

### Refund

Refund returns captured/settled money.

Check:

- full refund;
- partial refund;
- refund cannot exceed paid amount;
- refund status syncs with provider;
- inventory/order state updates according to business rules.

## Why Payment Gateway Testing Is Needed

From customer perspective, payment must feel simple:

1. Click `Pay`.
2. Wait a few seconds.
3. See clear success or failure result.

From merchant perspective, system must correctly handle:

- order creation;
- payment authorization;
- capture;
- settlement;
- refund/void;
- fraud checks;
- provider errors;
- webhook events;
- database records;
- reporting and reconciliation.

Any mismatch between payment provider and merchant system can create painful incidents.

Example: gateway captured payment, but merchant app failed to create order.

## Types Of Testing

Payment gateway integration usually needs:

- functional testing;
- integration testing;
- security testing;
- performance testing;
- negative testing;
- database testing;
- webhook testing;
- post-release smoke testing;
- reconciliation checks.

## Test Environment And Sandbox

Most providers offer sandbox/test mode.

QA should prepare:

- sandbox merchant account;
- API keys/test credentials;
- test card numbers;
- test currencies;
- expected response codes;
- webhook endpoint;
- test user accounts;
- test products/orders;
- admin access to provider dashboard;
- application logs access.

Sandbox limitations should be documented. Some sandboxes do not fully simulate:

- real fraud rules;
- bank latency;
- multi-currency behavior;
- 3-D Secure behavior;
- settlement timing;
- chargebacks;
- provider outages.

## Functional Test Cases

Core cases:

- successful payment;
- declined payment;
- insufficient funds;
- invalid card number;
- expired card;
- wrong CVV;
- wrong billing address;
- payment timeout;
- user cancels payment;
- duplicate click on `Pay`;
- browser refresh after payment;
- back button during payment;
- session timeout during checkout;
- payment provider returns user to merchant site;
- confirmation page shows correct information;
- confirmation email is sent.

Expected behavior:

- user sees clear message;
- order status is correct;
- payment status is correct;
- no duplicate order;
- no duplicate charge;
- logs contain useful non-sensitive details.

## Integration Test Cases

Integration checks:

- request sent to payment provider contains correct amount;
- currency is correct;
- order ID/reference is unique;
- customer/billing data is mapped correctly;
- provider response is parsed correctly;
- order status changes according to response;
- failed payment does not mark order as paid;
- successful payment creates exactly one paid order;
- provider dashboard shows transaction;
- merchant database shows matching transaction;
- webhooks update status correctly.

Common mapping bugs:

- first name/last name reversed;
- expiration date formatted incorrectly;
- currency code missing;
- amount sent in wrong unit: dollars instead of cents;
- duplicate transaction ID;
- provider success response treated as failure.

## Payment Methods

If product supports multiple methods, test each independently.

Examples:

- credit/debit card;
- saved card;
- PayPal or wallet;
- bank transfer;
- cash on delivery;
- gift card;
- store credit;
- buy now pay later;
- Apple Pay / Google Pay;
- local payment methods.

For each method, verify:

- success;
- failure;
- cancellation;
- timeout;
- order status;
- user message;
- notification;
- database record.

## Currency And Amount Testing

Check:

- currency configured correctly;
- amount sent to gateway matches order total;
- tax included correctly;
- shipping included correctly;
- discount included correctly;
- rounding is correct;
- decimal separator does not break request;
- multi-currency rules are correct;
- refund amount cannot exceed paid amount.

High-risk cases:

- zero-value order after coupon;
- partial payment;
- gift card + card combination;
- currency conversion;
- tax recalculation after address change.

## Security Testing

Payment security is critical.

Check:

- checkout uses HTTPS;
- sensitive card data is not stored in application DB unless explicitly compliant;
- CVV is never stored;
- logs do not contain full card numbers, CVV or secrets;
- API keys are not exposed in frontend;
- webhook signature is validated;
- callback cannot be forged;
- amount cannot be changed client-side;
- order ID cannot be manipulated;
- user cannot access another user's payment/order;
- tokenized payment methods are protected;
- session timeout works.

Never use real card data in test environments unless explicitly authorized by policy and provider rules.

## Webhook And Callback Testing

Modern providers often notify merchant system through webhooks.

Check:

- webhook endpoint receives events;
- signature is validated;
- unknown event types are handled safely;
- duplicate webhook does not duplicate order/payment state;
- out-of-order events are handled;
- failed webhook retries work;
- provider timeout does not break transaction;
- manual replay is safe;
- logs include event ID/reference.

Important cases:

- payment authorized;
- payment captured;
- payment failed;
- payment canceled;
- refund created;
- refund failed;
- dispute/chargeback created.

## Error Handling

Payment errors should be clear for user and useful for support.

Check:

- provider unavailable;
- network timeout;
- malformed provider response;
- invalid API key;
- fraud check declined;
- 3-D Secure failed;
- webhook delay;
- database unavailable after provider success;
- payment success but confirmation email fails.

User-facing message should be understandable and not too technical.

Bad message:

```text
Object reference not set to an instance of an object.
```

Better message:

```text
We could not process your payment. Please try again or use another payment method.
```

## Duplicate Payment Prevention

Check:

- double click on Pay button;
- page refresh after payment submit;
- browser back and resubmit;
- slow network repeated request;
- webhook delivered twice;
- retry after timeout;
- same order paid from two tabs.

Expected:

- idempotency key or equivalent protection is used;
- one order gets one successful payment;
- duplicate requests are ignored or rejected safely.

## Refund And Void Test Cases

Check:

- void authorized transaction;
- full refund captured transaction;
- partial refund;
- multiple partial refunds;
- refund more than paid amount;
- refund already refunded transaction;
- refund failed at provider;
- refund status updated by webhook;
- inventory restored if business rules require it;
- customer notification sent.

Important distinction:

- void is for not-yet-captured transaction;
- refund is for captured/settled transaction.

## Database Testing

Verify application database state:

- order record;
- payment transaction record;
- payment status;
- provider transaction ID;
- authorization ID;
- capture ID;
- refund ID;
- amount;
- currency;
- user ID;
- timestamps;
- audit trail;
- retry attempts;
- webhook events.

Database and provider dashboard should reconcile.

## Performance Testing

Payment provider should not become bottleneck in checkout.

Check:

- multiple users paying simultaneously;
- payment request latency;
- webhook processing throughput;
- checkout page response time;
- database locking around order/payment;
- retry behavior under provider latency;
- peak sale traffic.

Do not load test external provider without permission. Use mocks, sandbox limits or agreed test windows.

## Post-Release Smoke Checks

Before go-live:

- live merchant account is configured;
- production API keys are set securely;
- production webhook URL is configured;
- SSL certificate is valid;
- test transaction in live mode is approved by business process;
- refund/void process is known;
- monitoring and alerts are ready;
- support team knows where to find transaction IDs.

After release:

- make a small live transaction if approved;
- verify order status;
- verify provider dashboard;
- verify confirmation email;
- verify refund/void if process allows;
- verify logs and monitoring.

## Example Payment Gateway Test Cases

| ID | Scenario | Expected Result |
| --- | --- | --- |
| PG-01 | Pay with valid test card. | Payment succeeds; one paid order is created. |
| PG-02 | Pay with declined test card. | User sees clear decline message; order is not paid. |
| PG-03 | Enter expired card. | Validation/decline is handled correctly. |
| PG-04 | Click Pay twice. | Only one transaction/order is created. |
| PG-05 | Refresh after payment submit. | No duplicate charge occurs. |
| PG-06 | Provider timeout. | User sees safe message; order/payment status remains consistent. |
| PG-07 | Successful payment webhook delivered twice. | Payment state is not duplicated. |
| PG-08 | Refund full amount. | Provider and app show refunded status. |
| PG-09 | Refund more than paid amount. | Refund is rejected. |
| PG-10 | Void uncaptured authorization. | Authorization is voided and order status updates. |
| PG-11 | Change amount in browser request. | Server rejects tampered amount. |
| PG-12 | Open another user's order/payment URL. | Access is denied. |

## Common Bugs

Common payment defects:

- duplicate charge after double click;
- payment success but order not created;
- order paid but email not sent;
- declined payment shown as success;
- wrong currency;
- amount sent without tax/shipping;
- refund exceeds original payment;
- webhook signature not validated;
- provider dashboard and database mismatch;
- sensitive data in logs;
- timeout leaves order in unclear status;
- sandbox works but production keys/config fail.

## Practical Checklist

Before considering payment integration ready, check:

- sandbox configured;
- test card numbers collected;
- all payment methods tested;
- success/decline/timeout/cancel tested;
- amount/currency/tax/shipping verified;
- order status mapping verified;
- database records verified;
- webhook/callback tested;
- refund and void tested;
- duplicate payment prevention tested;
- sensitive data not logged/stored;
- production configuration plan ready;
- post-release smoke checklist prepared.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Payment gateway | Service that helps merchant accept online payments. |
| Payment processor | Service/company that processes card/payment transactions. |
| Authorization | Approval and funds hold from issuing bank. |
| Capture | Collecting authorized funds. |
| Void | Canceling authorization before capture/settlement. |
| Refund | Returning captured funds to customer. |
| Settlement | Transfer of funds to merchant account. |
| Webhook | Server-to-server event notification from provider. |
| Idempotency | Ensuring repeated request produces one logical result. |
| 3-D Secure | Additional card authentication flow. |
| PCI DSS | Security standard for handling cardholder data. |

## Questions

### 1. What is payment gateway testing?

Payment gateway testing checks whether an application correctly integrates with a payment provider for successful, failed, canceled, refunded and voided transactions.

### 2. Why is sandbox important?

Sandbox allows QA to test payment flows with test cards and fake money before production.

### 3. What is the difference between void and refund?

Void cancels an authorized but not captured transaction. Refund returns money after capture/settlement.

### 4. What is the highest-risk payment bug?

Duplicate charge or payment success without order creation are among the highest-risk bugs.

### 5. Why test webhooks?

Because provider webhooks often update final payment status, refunds, disputes and asynchronous events.

### 6. Should QA use real cards?

Usually no. QA should use sandbox/test cards unless business policy explicitly allows a controlled live transaction.

### 7. What should happen when payment fails?

User should see a clear message, order should not be marked as paid, and logs should allow support/debugging without exposing sensitive data.

## What To Review Later

- E-Commerce Testing
- Web Application Testing Guide
- HTTP Status Codes
- HTTP Headers
- Security Testing
- API Testing
- Database Testing
- Performance Testing
- Cookie Testing

