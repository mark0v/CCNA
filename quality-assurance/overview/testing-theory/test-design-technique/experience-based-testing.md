# Experience Based Testing

## Summary

Experience Based Testing - это подход к проектированию тестов, при котором test cases создаются на основе опыта, интуиции, знания домена и прошлой работы тестировщика с похожими системами.

В отличие от более формальных техник, таких как Equivalence Partitioning или Boundary Value Analysis, здесь нет жесткого алгоритма, который всегда приводит разных QA к одинаковому набору тестов.

Опытный tester использует то, что он уже видел раньше:

- типичные места, где появляются bugs;
- слабые зоны похожих приложений;
- особенности домена;
- поведение пользователей;
- прошлые production issues;
- собственную интуицию.

Такие техники помогают находить проверки, которые не всегда очевидны при использовании только структурированных test design techniques.

## When To Use It

Experience Based Testing особенно полезно, когда:

- requirements отсутствуют;
- requirements неполные или слишком общие;
- документация устарела;
- знания о продукте ограничены;
- времени на формальный подход мало;
- structured testing уже выполнен, но хочется проверить рискованные зоны глубже;
- tester давно работает с этим продуктом или доменом.

Например, после выполнения основных тестов по требованиям QA может дополнительно пройтись по областям, которые исторически часто ломались.

## Why Experience Matters

Опыт помогает tester видеть сценарии, которые обычный пользователь или новый QA может не заметить.

Представим eCommerce application.

Без документации пользователь может понять базовые действия:

- найти товар;
- добавить товар в cart;
- применить discount code;
- оформить заказ;
- вернуть товар.

Но опытный QA будет смотреть глубже.

Например:

- что будет, если ввести отрицательное значение в quantity field;
- как пересчитается refund, если пользователь купил 3 товара, применил discount, а потом вернул 1 товар;
- обновляется ли cart при login в нескольких sessions;
- что будет, если товар добавлен в cart, но затем стал out of stock;
- что будет, если товар стал out of stock прямо перед нажатием `Place order`;
- корректно ли система работает с несколькими вкладками браузера;
- не ломается ли discount logic после частичного возврата.

Такие проверки часто рождаются не из формальной таблицы, а из опыта работы с похожими продуктами.

## Types Of Experience Based Testing

К experience based techniques обычно относят несколько подходов.

### Error Guessing

Error Guessing - это техника, при которой tester предполагает, где приложение может сломаться.

QA использует опыт, чтобы выбрать зоны с высоким риском:

- сложная business logic;
- поля ввода;
- границы значений;
- integrations;
- миграции данных;
- расчеты;
- permissions;
- старые дефекты, которые могут повториться.

### Exploratory Testing

Exploratory Testing - это одновременное изучение продукта, проектирование тестов и выполнение проверок.

Tester не просто идет по заранее написанному сценарию. Он исследует приложение, наблюдает результат, меняет направление проверки и углубляется туда, где видит риск.

Этот подход полезен, когда:

- мало документации;
- продукт быстро меняется;
- нужно быстро понять качество новой функциональности;
- важно найти неожиданные сценарии.

### Checklist Based Testing

Checklist Based Testing использует список проверок, созданный на основе опыта команды.

Checklist может включать:

- common validation checks;
- security basics;
- UI consistency checks;
- browser compatibility checks;
- payment flow checks;
- API response checks;
- typical regression risks.

Checklist не такой детальный, как full test case, но помогает не забыть важные области.

## Limitations

Experience Based Testing сильна, но у нее есть ограничения.

Качество проверки сильно зависит от tester:

- его опыта;
- знания домена;
- знания продукта;
- внимательности;
- способности замечать риски.

Если опыта мало, тестирование может быть поверхностным.

Еще одна проблема - coverage трудно измерить. В формальных техниках проще показать, какие partitions, boundaries или rules покрыты. В experience based testing это сложнее.

Поэтому такой подход не всегда подходит как единственный метод, особенно если проект требует:

- строгую отчетность;
- traceability;
- test coverage matrix;
- контрактные доказательства покрытия;
- compliance documentation.

## When Not To Use It Alone

Experience Based Testing не стоит использовать как единственный подход, если:

- нужно доказать покрытие требований;
- есть regulatory или contractual requirements;
- команда должна предоставить test matrix;
- tester плохо знает домен;
- продукт новый и опыта с ним пока нет;
- функциональность критична и требует формального покрытия.

В таких случаях experience based testing лучше использовать как дополнение к structured techniques.

## Best Practice

Хороший подход - комбинировать structured и experience based techniques.

Например:

1. Сначала покрыть требования через Equivalence Partitioning, Boundary Value Analysis, Decision Tables или State Transition Testing.
2. Затем использовать experience based testing, чтобы пройтись по рискованным зонам.
3. После найденных defects обновить checklists или regression suite.

Так команда получает и измеримое покрытие, и пространство для интуитивного поиска дефектов.

## Key Idea

Experience Based Testing помогает QA думать как человек, который уже видел, где software обычно ломается.

Главная мысль:

> Experience does not replace structure. It strengthens it.

## Questions

1. What is Experience Based Testing?
2. When is Experience Based Testing useful?
3. Why is coverage difficult to measure in this approach?
4. What is the difference between Error Guessing and Exploratory Testing?
5. Why should Experience Based Testing be combined with structured techniques?

## What To Review Later

- Error Guessing
- Exploratory Testing
- Checklist Based Testing
- Risk Based Testing
- Test Coverage
