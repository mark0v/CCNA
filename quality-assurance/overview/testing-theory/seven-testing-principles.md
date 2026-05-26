# Seven Testing Principles

## Summary

Seven Testing Principles - это базовые идеи, которые объясняют, как нужно думать о software testing.

Они помогают не ожидать от тестирования невозможного, правильно расставлять приоритеты, начинать QA activities раньше, обновлять test cases и помнить, что качество зависит не только от отсутствия defects, но и от того, насколько продукт решает реальные needs пользователя.

## Key Points

- Testing показывает наличие defects, но не доказывает их полное отсутствие.
- Exhaustive testing почти всегда невозможно.
- Testing нужно начинать как можно раньше.
- Большая часть defects часто концентрируется в небольшом количестве modules.
- Одни и те же tests со временем перестают находить новые bugs.
- Testing зависит от context продукта.
- Software без найденных errors все равно может быть плохим, если он не решает user needs.

## Notes

### 1. Testing Shows Presence of Defects

Testing can show that defects are present, but it cannot prove that there are no defects.

Даже если application тщательно протестирована и все test cases прошли успешно, нельзя честно сказать, что продукт на 100% defect-free. Testing снижает количество undiscovered defects, но отсутствие найденных defects не является доказательством полной correctness.

Практический смысл:

- QA не гарантирует, что bugs нет вообще.
- QA дает информацию о качестве и рисках.
- Чем лучше testing strategy, тем ниже вероятность критичных пропущенных defects.

Example:

Если команда протестировала checkout flow и не нашла defects, это значит только то, что в проверенных сценариях defects не обнаружены. Но могут остаться edge cases, integration issues, environment-specific bugs или data-related problems.

### 2. Exhaustive Testing Is Impossible

Exhaustive testing означает проверить все возможные inputs, states, combinations и preconditions.

В реальных проектах это почти всегда невозможно из-за количества combinations, времени и ресурсов.

Example:

Если на форме есть 15 input fields, и у каждого поля 5 возможных значений, количество комбинаций будет:

```text
5^15 = 30,517,578,125
```

Проверить более 30 billion combinations вручную или даже автоматизированно в рамках обычного проекта нереалистично.

Поэтому testing должен быть risk-based и priority-based:

- тестируем critical flows;
- покрываем high-risk areas;
- выбираем representative values;
- используем equivalence partitioning;
- используем boundary value analysis;
- комбинируем manual и automation wisely.

Практический смысл:

QA не пытается проверить абсолютно все. QA выбирает самое важное и рискованное.

### 3. Early Testing

Testing activities должны начинаться как можно раньше в SDLC.

Это называется shift-left testing: QA подключается не только после development, а уже на этапах requirements, design, planning и refinement.

Early testing помогает:

- найти ambiguity в requirements;
- предотвратить defects до написания code;
- улучшить acceptance criteria;
- снизить cost of fixing defects;
- сделать продукт более testable.

Example:

Если QA видит в requirement фразу "system should be fast", это не testable requirement. Лучше уточнить заранее: "search results should load within 2 seconds for 95% of requests under normal load".

### 4. Defect Clustering

Defect clustering означает, что defects часто распределены неравномерно.

Небольшое количество modules может содержать большую часть defects или чаще вызывать operational failures.

Причины:

- complex business logic;
- frequent changes;
- poor code quality;
- weak ownership;
- legacy code;
- integrations;
- unclear requirements.

Практический смысл:

Если один module постоянно ломается, QA должен уделить ему больше внимания. Это может быть candidate для deeper regression, code review, refactoring или additional automation.

Example:

В e-commerce application большинство critical defects может находиться не во всех страницах, а в checkout, payment и discount calculation.

### 5. Pesticide Paradox

Pesticide paradox означает: если повторять одни и те же tests снова и снова, со временем они перестают находить новые defects.

Это не значит, что regression tests бесполезны. Они важны для проверки already known risks. Но если test suite никогда не обновляется, он начинает "привыкать" к продукту.

Чтобы избежать pesticide paradox:

- регулярно review test cases;
- добавлять новые scenarios;
- менять test data;
- использовать exploratory testing;
- анализировать production defects;
- обновлять regression suite после новых features;
- удалять устаревшие или duplicate tests.

Практический смысл:

Test suite должен жить вместе с продуктом. Если продукт меняется, tests тоже должны меняться.

### 6. Testing Is Context Dependent

Testing depends on context.

Разные продукты требуют разных testing approaches. Нельзя одинаково тестировать медицинскую систему, banking application, game, landing page, embedded software и e-commerce website.

Context влияет на:

- testing depth;
- documentation level;
- regulatory requirements;
- risk tolerance;
- needed test environments;
- security requirements;
- performance expectations;
- release process.

Examples:

- Safety-critical software требует строгих reviews, documentation, validation и traceability.
- E-commerce site требует сильного фокуса на checkout, payments, usability, performance и compatibility.
- Mobile application требует testing на разных devices, OS versions, network conditions и screen sizes.
- Internal admin tool может иметь меньше compatibility requirements, но высокий фокус на permissions и data accuracy.

Практический смысл:

Good testing is not universal checklist testing. Good testing adapts to product risk and context.

### 7. Absence-of-Errors Fallacy

Absence-of-errors fallacy означает: если defects не найдены или исправлены, это еще не значит, что software полезен и успешен.

Продукт может работать технически корректно, но быть бесполезным, если он:

- не решает user problem;
- не соответствует business needs;
- неудобен;
- построен не по тем requirements;
- слишком сложен для целевой аудитории;
- не дает ожидаемой value.

Example:

Команда может идеально протестировать report generation feature, но если users на самом деле нуждаются не в PDF report, а в real-time dashboard, отсутствие bugs в PDF feature не делает продукт успешным.

Практический смысл:

QA должен думать не только "does it work according to specification?", но и "does it help the user achieve the goal?"

## Commands / Terms

- `Testing shows presence of defects` - testing finds defects, but cannot prove their absence.
- `Exhaustive testing` - attempt to test all possible combinations, usually impossible.
- `Early testing` - starting testing activities as early as possible.
- `Shift-left testing` - moving QA involvement earlier in SDLC.
- `Defect clustering` - most defects are often concentrated in a small number of modules.
- `Pesticide paradox` - repeated unchanged tests stop finding new defects.
- `Context dependent testing` - testing approach depends on product/domain/risk.
- `Absence-of-errors fallacy` - defect-free software can still fail user needs.
- `Risk-based testing` - focusing testing effort on high-risk areas.

## Questions

1. What are the seven testing principles?
2. Why can't testing prove that there are no defects?
3. Why is exhaustive testing impossible?
4. What is early testing?
5. What does defect clustering mean?
6. What is the pesticide paradox?
7. Why is testing context dependent?
8. What is absence-of-errors fallacy?
9. How can QA avoid pesticide paradox?
10. Why should QA use risk-based testing?

## What To Review Later

- STLC phases
- Risk-based testing
- Shift-left testing
- Test case review
- Regression testing
- Exploratory testing
- Requirement testability
