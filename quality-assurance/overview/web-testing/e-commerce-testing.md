# E-Commerce Testing

## Summary

E-commerce testing - это проверка online store или retail web application, где пользователь ищет product, добавляет его в cart, проходит checkout, оплачивает order и получает post-order service.

Для e-commerce качество сайта напрямую влияет на revenue:

- user может уйти после одной медленной page;
- неверная price или discount может привести к финансовым потерям;
- broken checkout напрямую блокирует продажи;
- security issue разрушает trust;
- плохая mobile experience снижает conversion.

Главная идея:

> E-commerce testing проверяет не только отдельные страницы, а весь purchase journey: discovery -> product -> cart -> checkout -> payment -> order -> return/support.

## What Makes E-Commerce Testing Special

E-commerce applications обычно более динамичные, чем обычные content sites.

Часто меняются:

- products;
- prices;
- stock status;
- promotions;
- banners;
- recommendations;
- payment rules;
- shipping options;
- tax rules;
- availability by region.

Поэтому QA должен думать не только о static UI, но и о data, business rules, integrations, analytics, performance and security.

## Main Test Areas

E-commerce testing обычно включает:

- functional testing;
- usability testing;
- search and filtering testing;
- cart testing;
- checkout testing;
- payment testing;
- order management testing;
- database testing;
- security testing;
- performance testing;
- mobile/responsive testing;
- compatibility testing;
- accessibility testing;
- localization testing;
- analytics and conversion checks;
- regression automation.

## Homepage And Hero Banners

Homepage часто содержит hero image, carousel, offers, categories, recommendations and campaign banners.

Что проверить:

- hero banner loads correctly;
- carousel auto-scroll работает согласно requirements;
- hover/pause behavior корректный;
- click ведет на правильный category/product/deal page;
- expired promotion не показывается;
- banner корректно выглядит на desktop/mobile;
- image не перекрывает important content;
- page не становится медленной из-за тяжелых images;
- tracking event отправляется при click, если требуется.

Common bug: banner показывает sale, но click ведет на старую или пустую campaign page.

## Search

Search - один из самых важных flows в online store. Если user не может найти product, conversion падает.

Проверить:

- search by product name;
- search by brand;
- search by category;
- search by SKU/model;
- typo tolerance;
- synonyms;
- empty search;
- no results state;
- sorting;
- pagination;
- suggestions/autocomplete;
- search history;
- search on mobile;
- search within category.

Примеры:

- `camera`;
- `Canon EOS 700D`;
- `wireless headphones`;
- `iPhone charger`;
- product SKU.

Ожидаемо:

- results relevant;
- unavailable items handled correctly;
- filters match result set;
- result count is accurate;
- search query remains visible after search;
- no irrelevant sponsored product dominates results unless product rules allow it.

## Categories And Listing Pages

Category/listing pages помогают user browse products.

Проверить:

- category hierarchy;
- breadcrumbs;
- filters;
- sorting;
- pagination/infinite scroll;
- product cards;
- price display;
- discount badges;
- availability;
- ratings;
- quick add to cart;
- compare/wishlist;
- SEO-friendly URLs;
- empty category state.

Important checks:

- filters combine correctly;
- removing filter updates results;
- sorting does not reset selected filters unexpectedly;
- pagination preserves filters;
- product count matches backend;
- mobile filters are usable.

## Product Details Page

Product details page должен дать user enough confidence to buy.

Проверить:

- product title;
- images/gallery/video;
- price;
- discount;
- stock status;
- variants: size/color/storage/etc.;
- quantity selector;
- product specifications;
- reviews and ratings;
- delivery options;
- return policy;
- warranty;
- seller information;
- related products;
- add to cart;
- wishlist/compare;
- breadcrumbs.

Variant scenarios:

- selected size changes stock;
- selected color changes images;
- unavailable variant cannot be purchased;
- price changes for variant are correct;
- selected variant is preserved in cart.

Common bug: user selects black XL, but cart receives default white M.

## Shopping Cart

Cart is the bridge between browsing and checkout.

Проверить:

- add item to cart;
- add same item again;
- update quantity;
- remove item;
- clear cart;
- cart total;
- subtotal;
- tax;
- shipping estimate;
- discount/coupon;
- unavailable item handling;
- stock limit;
- guest cart persistence;
- logged-in cart persistence;
- cart merge after login;
- cart across tabs/devices if supported.

Important edge cases:

- product goes out of stock while it is in cart;
- price changes after item was added;
- coupon expires before checkout;
- user closes browser and returns later;
- user logs in after building guest cart;
- user uses two tabs and changes quantity in both.

## Checkout

Checkout must be short, clear and reliable.

Проверить:

- guest checkout;
- logged-in checkout;
- account creation after purchase;
- shipping address;
- billing address;
- delivery method;
- payment method;
- order summary;
- tax calculation;
- coupon application;
- terms acceptance;
- validation messages;
- edit cart from checkout;
- back/forward browser behavior;
- session timeout;
- abandoned checkout recovery if supported.

Flow checks:

1. Add product to cart.
2. Open checkout.
3. Enter address.
4. Select shipping.
5. Select payment.
6. Review order.
7. Place order.
8. Verify confirmation page and email.

## Payment Testing

Payment is high-risk because it touches money, trust and compliance.

Проверить:

- card payment;
- saved card;
- digital wallet;
- bank transfer;
- cash on delivery;
- gift card/store credit;
- split payment if supported;
- successful payment;
- failed payment;
- declined card;
- timeout;
- duplicate click on Pay;
- redirect to payment provider;
- return from payment provider;
- payment cancellation;
- refund flow.

Security/compliance focus:

- card data is not stored unless allowed and compliant;
- payment page uses HTTPS;
- logs do not contain sensitive payment data;
- failed payment does not create paid order;
- successful payment creates exactly one order;
- repeated refresh does not duplicate charge.

Common bug: payment succeeds, but order remains `pending` because callback/webhook failed.

## Order Confirmation

After successful purchase, user should receive clear confirmation.

Проверить:

- order number generated;
- confirmation page shown;
- confirmation email/SMS sent;
- order details are correct;
- payment status is correct;
- shipping address is correct;
- invoice/receipt is available if required;
- order appears in account history;
- inventory decreased correctly;
- analytics purchase event sent once.

## After-Order Flows

E-commerce does not end at payment.

Проверить:

- order tracking;
- cancel order;
- change order;
- return request;
- exchange request;
- refund;
- reorder;
- review product;
- contact support;
- download invoice;
- warranty/service request.

Important rules:

- cancellation may be allowed only before shipment;
- return window may depend on product category;
- refund status must match payment provider state;
- email notifications must match actual order state.

## User Account

Проверить:

- registration;
- login/logout;
- password reset;
- profile update;
- address book;
- saved payment methods;
- order history;
- wishlist;
- recently viewed products;
- loyalty points;
- subscriptions;
- privacy settings.

Security focus:

- user cannot access another user's orders;
- address/payment data is protected;
- session expires correctly;
- remember me works safely;
- password reset tokens expire.

## Promotions And Coupons

Promotions are frequent sources of bugs.

Проверить:

- fixed discount;
- percentage discount;
- free shipping;
- buy one get one;
- category-specific coupons;
- user-specific coupons;
- first-order coupons;
- coupon expiration;
- minimum order value;
- coupon stacking rules;
- max usage count;
- region restrictions.

Edge cases:

- apply coupon then remove product;
- apply coupon to unavailable product;
- use coupon twice;
- combine coupon with sale item;
- change shipping address after coupon applied;
- coupon expires during checkout.

## Recommendations And Featured Products

Recommended, related and featured products often come from business rules, analytics or recommendation systems.

Проверить:

- block is visible where expected;
- products are relevant enough;
- unavailable products are hidden or marked correctly;
- price and discount are correct;
- click opens correct product;
- recommendation does not show already purchased item when rules prohibit it;
- personalized recommendations do not leak another user's behavior.

QA usually does not test every product manually. Better focus on algorithm/rules, data source and high-risk examples.

## Database And Inventory

Проверить:

- order saved correctly;
- order items saved correctly;
- payment status saved correctly;
- inventory updates after purchase;
- inventory restores after cancellation/refund if required;
- price in order remains historical;
- cart data persists according to requirements;
- user account data is linked correctly;
- audit/history records exist for important changes.

Important: order price should usually not change after purchase even if product price changes later.

## Performance Testing

Performance strongly affects conversion.

Проверить:

- homepage load time;
- search response time;
- category page under load;
- product page under load;
- cart update performance;
- checkout performance;
- payment callback/webhook handling;
- peak traffic during sale;
- database performance;
- cache behavior;
- CDN behavior;
- image optimization.

High-risk events:

- Black Friday;
- New Year sales;
- product launch;
- flash sale;
- email campaign;
- ad campaign.

Metrics:

- response time;
- throughput;
- error rate;
- CPU/memory;
- database query time;
- payment provider latency;
- conversion drop under load.

## Security Testing

Security is critical because e-commerce handles personal data, addresses, payments and order history.

Проверить:

- authentication;
- authorization;
- checkout access control;
- order access control;
- coupon abuse;
- price tampering;
- quantity tampering;
- cart/order ID manipulation;
- payment callback validation;
- CSRF;
- XSS;
- SQL injection;
- sensitive data in logs;
- HTTPS certificate;
- rate limiting;
- bot protection.

Examples:

- change product price in request;
- change order ID in URL;
- reuse expired coupon;
- call payment success callback manually;
- access another user's invoice.

## Mobile And Responsive Testing

Many e-commerce purchases happen on mobile.

Проверить:

- homepage layout;
- mobile navigation;
- search;
- filters drawer;
- product images;
- variant selection;
- add to cart;
- checkout forms;
- address autocomplete;
- payment provider redirect;
- sticky buttons;
- keyboard behavior;
- touch targets;
- page speed on mobile network.

Common bug: payment iframe or provider page does not fit mobile viewport.

## Compatibility Testing

Проверить:

- Chrome;
- Edge;
- Firefox;
- Safari;
- mobile Safari;
- Android Chrome;
- different screen sizes;
- different OS;
- slow network;
- browser back/forward;
- browser autofill;
- printing order/invoice.

Safari and mobile browsers deserve special attention because cookies, payments and tracking can behave differently.

## Accessibility Testing

E-commerce should be usable without a mouse and with assistive technologies.

Проверить:

- keyboard navigation;
- focus order;
- visible focus indicator;
- screen reader labels;
- form error announcements;
- color contrast;
- product images alt text;
- modal/dialog accessibility;
- checkout usable by keyboard;
- no keyboard traps;
- payment flow accessibility.

Accessibility defects can directly block purchase.

## Analytics And Conversion

Analytics does not replace QA, but e-commerce QA should know which events are business-critical.

Проверить:

- product view event;
- add to cart event;
- remove from cart event;
- begin checkout event;
- payment event;
- purchase event;
- order value;
- currency;
- coupon;
- user/session identifiers according to privacy rules;
- event sent once, not duplicated.

Conversion-related checks:

- no unnecessary steps in checkout;
- errors are clear;
- guest checkout available if required;
- trust signals visible;
- payment methods are familiar to region;
- cart totals are transparent.

## Automation Strategy

Do not try to automate every product and every category. Automate stable, high-value flows.

Good automation candidates:

- homepage smoke;
- search product;
- product details;
- add to cart;
- update cart;
- guest checkout with test payment;
- login checkout;
- order confirmation;
- coupon happy/negative cases;
- basic order history;
- critical API checks;
- broken link/status checks.

Be careful with:

- unstable UI elements;
- dynamic recommendations;
- real payment providers;
- changing product catalog;
- parallel tests sharing same user/cart;
- tests depending on exact live prices.

Use test data and environments designed for automation.

## Example E-Commerce Test Cases

| ID | Scenario | Expected Result |
| --- | --- | --- |
| E-01 | Search existing product by name. | Relevant product appears in results. |
| E-02 | Apply price filter and sorting. | Results match filter and order. |
| E-03 | Select product variant and add to cart. | Correct variant appears in cart. |
| E-04 | Update item quantity in cart. | Totals, tax and shipping update correctly. |
| E-05 | Apply valid coupon. | Discount is applied according to rules. |
| E-06 | Apply expired coupon. | Clear error message is shown; total unchanged. |
| E-07 | Checkout as guest. | Order can be placed without account if supported. |
| E-08 | Payment declined. | Order is not marked paid; user can retry. |
| E-09 | Payment succeeds. | One order is created, confirmation page/email shown. |
| E-10 | Product goes out of stock before payment. | User cannot complete purchase or sees clear message. |
| E-11 | Login as user A and open user B order URL. | Access is denied. |
| E-12 | Cancel order before shipment. | Order status and inventory update according to rules. |

## Common Bugs

Common e-commerce defects:

- wrong product variant in cart;
- stale price in checkout;
- coupon applied incorrectly;
- duplicate order after refresh;
- payment success but order pending;
- inventory not updated;
- unavailable product can be purchased;
- cart lost after login;
- another user's order accessible by URL;
- mobile checkout button hidden;
- slow search under load;
- broken product images;
- tax/shipping calculated incorrectly;
- purchase analytics duplicated.

## Practical Checklist

Before release, check:

- critical search and category flows;
- main product details flow;
- cart add/update/remove;
- guest and logged-in checkout;
- all active payment methods;
- coupons and promotions;
- inventory and order persistence;
- order confirmation and email;
- cancellation/return flow;
- mobile checkout;
- browser compatibility;
- security around price/order/payment;
- performance for peak traffic;
- analytics purchase event;
- production smoke checklist.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| PDP | Product Details Page. |
| PLP | Product Listing Page. |
| Cart | Temporary basket of selected products. |
| Checkout | Flow where user confirms address, shipping, payment and order. |
| Payment gateway | External or internal service that processes payment. |
| SKU | Stock Keeping Unit, product inventory identifier. |
| Inventory | Available stock quantity. |
| Conversion rate | Percentage of visitors who become buyers or complete target action. |
| A/B testing | Comparing two variants to see which performs better. |
| Abandoned cart | Cart created but not purchased. |

## Questions

### 1. What is e-commerce testing?

E-commerce testing checks online shopping flows, including search, product pages, cart, checkout, payment, order management, security and performance.

### 2. Do QA engineers need to test every product?

Usually no. QA should test representative products, high-risk categories, data rules and algorithms rather than every catalog item manually.

### 3. Why is payment testing high-risk?

Because failures can cause lost orders, duplicate charges, wrong order statuses or loss of customer trust.

### 4. What is the most critical e-commerce flow?

The purchase journey from product discovery to order confirmation is usually the highest priority.

### 5. Why test inventory?

Because users should not buy unavailable products, and stock must update correctly after purchase, cancellation or return.

### 6. Why is mobile testing important for e-commerce?

Many users browse and buy from phones, so mobile usability and performance directly affect conversion.

### 7. What should be automated first?

Stable critical regression flows: search, product details, add to cart, checkout, test payment and order confirmation.

## What To Review Later

- Web Application Testing Guide
- Cookie Testing
- Localization And Internationalization Testing
- HTTP Status Codes
- HTTP Headers
- Security Testing
- Performance Testing
- Database Testing
- API Testing

