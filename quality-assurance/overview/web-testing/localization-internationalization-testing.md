# Localization And Internationalization Testing

## Summary

Localization testing and internationalization testing проверяют, готов ли продукт работать для пользователей из разных languages, regions и cultures.

Коротко:

- internationalization (`i18n`) - продукт технически готов к переводу и разным locales;
- localization (`l10n`) - продукт адаптирован под конкретный language/region;
- globalization - общий процесс подготовки продукта к global markets.

Главная идея:

> Internationalization делает продукт готовым к локализации. Localization проверяет, что конкретная локальная версия выглядит и работает естественно для local users.

## Why This Matters

Для global web products недостаточно просто перевести текст.

Пользователь ожидает, что приложение будет корректно показывать:

- язык;
- date/time format;
- numbers;
- currency;
- address format;
- phone format;
- names;
- sorting rules;
- keyboard input;
- legal and privacy content;
- local payment/shipping options;
- culturally appropriate colors, icons and images.

Если локализация сделана плохо, user может не доверять продукту, неправильно понимать actions или вообще не сможет завершить flow.

## What Is Internationalization

Internationalization (`i18n`) - это design and development approach, при котором application заранее готовят к поддержке разных languages, scripts, formats и locales.

Это не перевод сам по себе. Это техническая готовность к переводу.

Примеры i18n requirements:

- all user-facing text вынесен из source code в resource files;
- application поддерживает Unicode;
- UI может расширяться под длинный текст;
- layout поддерживает right-to-left languages;
- date/time/number/currency formats зависят от locale;
- database хранит Unicode data;
- sorting and search учитывают language rules;
- code не делает assumptions вроде "один символ = один byte";
- automated tests не завязаны на English text.

## What Is Localization

Localization (`l10n`) - это адаптация product, application или content под конкретный locale.

Locale обычно включает:

- language;
- country/region;
- cultural expectations;
- date/time formats;
- number formats;
- currency;
- measurement units;
- legal requirements.

Localization включает:

- translated UI text;
- translated help/documentation;
- localized error messages;
- local currencies and prices;
- local payment methods;
- local address/phone formats;
- region-specific content;
- culturally appropriate images/icons/colors;
- local terms and legal notices.

## I18n Vs L10n

| Area | Internationalization | Localization |
| --- | --- | --- |
| Short name | `i18n` | `l10n` |
| Main focus | Product is ready for multiple locales. | Product is adapted for a specific locale. |
| Stage | Design/development level. | Content/configuration/product release level. |
| Language | Code is language-independent. | Specific language is used. |
| Typical checks | Unicode, resource files, RTL support, locale-aware formats. | Translation, local formats, local content, legal/cultural fit. |
| Example bug | UI breaks when German text is longer. | Russian translation is incorrect or inconsistent. |

## Scope Of Testing

Main areas:

- language and text;
- UI layout;
- date/time;
- numbers and currency;
- names and addresses;
- keyboard and input;
- sorting/search;
- graphics and cultural content;
- legal/regional requirements;
- database and file encoding;
- integrations and payments;
- automation stability.

## Language Testing

Check:

- all visible text is translated;
- translation matches product context;
- no mixed languages in one screen unless required;
- terminology is consistent;
- spelling and grammar are correct;
- placeholders are substituted correctly;
- plural forms are correct;
- gender/case forms are correct where applicable;
- error messages are localized;
- tooltips, labels, modals and notifications are localized.

Common bugs:

- untranslated English text remains;
- variable order breaks sentence meaning;
- placeholder is missing: `Hello, {name}`;
- pluralization is wrong: `1 items`;
- text is translated literally but sounds unnatural.

## UI Layout Testing

Translated text can be longer or shorter than English. Some scripts also require different alignment or rendering.

Check:

- no truncated text;
- no overlapping controls;
- buttons fit translated labels;
- tables and forms remain readable;
- tooltips and modals fit content;
- line breaks are acceptable;
- responsive layout still works;
- font supports required characters;
- icons do not conflict with local meaning.

Example:

German and Finnish text can be much longer than English. Chinese/Japanese text may be more compact. Arabic and Hebrew require right-to-left layout.

## Unicode And Character Rendering

Check:

- application supports Unicode end to end;
- non-Latin characters render correctly;
- emoji/special symbols behave as expected;
- accents and diacritics are not lost;
- text is not replaced by `???` or squares;
- copy/paste preserves characters;
- exported files preserve encoding;
- emails and PDFs show localized text correctly.

Important areas:

- frontend rendering;
- API payloads;
- database storage;
- logs;
- file import/export;
- email templates;
- PDF/report generation.

## Right-To-Left And Bidirectional Text

For languages like Arabic and Hebrew, check right-to-left (`RTL`) behavior.

Check:

- layout mirrors correctly;
- menus and navigation align correctly;
- input fields support RTL text;
- numbers and Latin fragments remain readable;
- mixed text works: Arabic + English + numbers;
- icons with direction are mirrored only when appropriate;
- cursor movement and selection feel natural.

Bidirectional text bugs are often subtle, so test real content, not only short sample words.

## Date, Time And Calendar

Check:

- date format matches locale;
- time format matches locale: 12-hour vs 24-hour;
- timezone is correct;
- calendar type is correct if product supports non-Gregorian calendars;
- week starts on correct day;
- holidays and business days are region-aware;
- daylight saving time does not break calculations;
- date picker uses localized month/day names.

Examples:

- `06/01/2026` can mean June 1 or January 6 depending on locale.
- Some countries use Monday as first day of week, others use Sunday.

## Numbers, Currency And Units

Check:

- decimal separator is correct;
- thousand separator is correct;
- negative numbers are displayed correctly;
- currency symbol/code is correct;
- currency position is correct;
- rounding rules are correct;
- measurement units match region;
- conversion is accurate where needed.

Examples:

- `1,234.56` in US style;
- `1 234,56` in many European locales;
- `$10.00` vs `10,00 EUR`;
- miles vs kilometers;
- pounds vs kilograms.

## Names, Addresses And Phone Numbers

Check:

- name fields support different lengths and scripts;
- application does not assume first name + last name only;
- address fields match target country;
- postal code validation is region-aware;
- phone number validation supports local formats;
- government IDs are requested only where legally and product-wise needed.

Common bugs:

- mandatory ZIP code for country without ZIP codes;
- name field rejects apostrophes, hyphens or non-Latin letters;
- phone field accepts only US format;
- address form cannot handle long city names.

## Sorting, Search And Collation

Different languages sort text differently.

Check:

- alphabetical sorting follows locale rules;
- search handles accents and case correctly;
- search works with non-Latin input;
- filters do not break localized values;
- database collation matches expected behavior;
- uppercase/lowercase transformations are correct.

Example:

Sorting `ä`, `å`, `ö`, `é` can differ by language and region.

## Keyboard And Input

Check:

- user can type local characters;
- keyboard shortcuts do not conflict with local input;
- IME input works for Chinese/Japanese/Korean;
- copy/paste works;
- validation accepts local punctuation;
- forms handle RTL input where needed;
- password rules are clear and not accidentally language-hostile.

## Graphics, Colors And Cultural Fit

Localization includes cultural context, not only text.

Check:

- images are appropriate for target region;
- icons are not offensive or misleading;
- colors do not carry wrong cultural meaning;
- gestures and symbols are acceptable;
- examples and names are localized;
- legal or medical claims match local rules;
- maps, flags and regional labels are correct.

## Feature Availability By Region

Some features may exist only in specific markets.

Check:

- unavailable features are hidden or disabled correctly;
- user sees region-appropriate payment methods;
- shipping methods match country;
- tax calculation matches locale;
- legal disclaimers appear where needed;
- app store links and support links point to correct region.

Example:

An e-commerce site may support card payments globally, but local bank transfer or cash-on-delivery only in selected countries.

## Database Testing

Database must support localized data.

Check:

- Unicode characters are stored and retrieved correctly;
- no data loss during save/update/migration;
- collation supports expected sorting/search;
- field lengths are enough for localized text;
- import/export preserves encoding;
- logs and reports do not corrupt characters;
- backup/restore preserves localized data.

Risk example:

If database column or migration uses wrong encoding, `Марія`, `José`, `李雷` can become corrupted or unreadable.

## File Transfer And Export

If product imports or exports files, check encoding and formatting.

Check:

- CSV export uses expected delimiter and encoding;
- Excel/PDF reports show localized text;
- downloaded file names support local characters;
- uploaded files with localized names are accepted;
- file content is not corrupted;
- date/number formats in exported reports match locale.

## Automation Considerations

Automation can help, but tests must be written carefully.

Good practices:

- do not locate elements by visible English text if test must run across locales;
- use stable IDs/test attributes;
- keep test data locale-aware;
- compare resource keys where possible;
- separate layout checks from translation quality checks;
- run smoke tests across all supported locales;
- run deeper tests on high-risk locales.

Automation can catch:

- missing translations;
- broken layout screenshots;
- untranslated resource keys;
- login/search/cart flows across locales;
- wrong date/number formatting;
- encoding issues in API/database.

Human review is still important for translation quality and cultural fit.

## Localization Test Cases

| ID | Scenario | Expected Result |
| --- | --- | --- |
| L-01 | Open app in Russian locale. | UI text is translated and no English fallback appears unexpectedly. |
| L-02 | Open long translated page. | Text is not truncated or overlapping. |
| L-03 | Submit form with local characters. | Data is saved and displayed correctly. |
| L-04 | Enter localized phone number. | Validation accepts correct local format. |
| L-05 | Check date picker. | Date format, month names and week start match locale. |
| L-06 | View price. | Currency symbol, position and separators are correct. |
| L-07 | Search with accented/non-Latin text. | Relevant records are found correctly. |
| L-08 | Export report. | File preserves localized text and formats. |
| L-09 | Change language setting. | UI updates and preference persists after reload. |
| L-10 | Check region-specific feature. | Feature is visible only for supported locale/region. |

## Internationalization Test Cases

| ID | Scenario | Expected Result |
| --- | --- | --- |
| I-01 | Switch product language. | UI loads text from resources, not hardcoded strings. |
| I-02 | Use pseudo-localization with expanded text. | Layout handles longer strings. |
| I-03 | Use RTL locale. | Layout mirrors and input works correctly. |
| I-04 | Save Unicode data through UI/API. | Database stores and returns exact value. |
| I-05 | Run main flow in multiple locales. | Core behavior is independent of language. |
| I-06 | Check API date/number handling. | Backend uses stable formats internally and localizes only at boundaries. |
| I-07 | Verify automated selectors. | Tests do not fail only because visible language changed. |

## Common Bugs

Common localization and internationalization defects:

- hardcoded English strings;
- broken layout due to long translation;
- untranslated validation messages;
- wrong date format;
- wrong decimal separator;
- corrupted Unicode in database;
- search fails for accented characters;
- RTL layout partially mirrored;
- currency displayed with wrong symbol;
- region-specific payment method missing;
- automation tests break after language switch;
- CSV export corrupts local characters;
- legal text missing for target region.

## Practical Checklist

Before release, check:

- supported locales are defined;
- translations are complete;
- fallback language behavior is expected;
- pseudo-localization was tested;
- at least one long-text language was tested;
- at least one non-Latin script was tested;
- RTL tested if supported;
- date/time/currency/number formats verified;
- database stores Unicode correctly;
- search and sorting checked;
- file export/import checked;
- local legal/privacy requirements reviewed;
- production monitoring includes locale-specific errors.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Localization | Adapting product to a specific language, culture and region. |
| `l10n` | Short form of localization. |
| Internationalization | Designing product so it can support multiple locales. |
| `i18n` | Short form of internationalization. |
| Globalization | Broader process of making product ready for global markets. |
| Locale | Language + region + formatting/cultural rules. |
| Unicode | Character standard for representing text from many writing systems. |
| RTL | Right-to-left writing direction. |
| Collation | Locale-specific sorting and comparison rules. |
| Pseudo-localization | Testing with artificial translated-looking text to expose i18n issues early. |

## Questions

### 1. What is localization testing?

Localization testing checks whether a product is correctly adapted for a specific language, region and culture.

### 2. What is internationalization testing?

Internationalization testing checks whether product design and code can support localization for multiple languages and regions.

### 3. Is localization only translation?

No. It also includes formats, currency, names, addresses, legal requirements, cultural expectations, images and region-specific features.

### 4. Why is Unicode important?

Unicode allows applications to store and display characters from many writing systems without data corruption.

### 5. Why do translated texts break UI?

Different languages need different text lengths and layout behavior. A button that fits English may not fit German or Russian.

### 6. Why test date and number formats?

Because the same value can be interpreted differently in different locales, which can cause user confusion or business errors.

### 7. Can localization testing be fully automated?

No. Automation helps with coverage and regression, but translation quality and cultural fit still need human review.

## What To Review Later

- Web Application Testing Guide
- Cookie Testing
- HTTP Headers
- Database Testing
- API Testing
- Accessibility Testing
- Security Testing
- Mobile Testing

