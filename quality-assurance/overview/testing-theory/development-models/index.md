# Development Models

## Summary

Development Models - это способы организовать работу над software product: как команда собирает требования, проектирует решение, пишет код, тестирует, выпускает и поддерживает систему.

В этом разделе собраны модели и frameworks, которые часто встречаются в QA и software engineering: Waterfall, V-Model, Scrum, Kanban и Extreme Programming. Они отвечают на разные вопросы. Одни описывают строгую последовательность этапов, другие помогают управлять изменениями, потоком задач и инженерными практиками.

## Key Points

- Development model показывает, как устроен процесс создания software.
- QA важно понимать модель, потому что от нее зависит момент начала тестирования, формат документации, роли и ожидания от команды.
- Waterfall и V-Model больше подходят для стабильных требований и строгой документации.
- Scrum, Kanban и XP ближе к Agile-подходам, где важны feedback, adaptability и continuous improvement.
- Нет одной универсальной модели для всех проектов. Выбор зависит от рисков, требований, команды, домена и скорости изменений.

## Notes

Development model влияет на то, как QA работает каждый день:

- когда тестировщик подключается к проекту;
- как формируются test cases и acceptance criteria;
- насколько подробно ведется документация;
- как команда обрабатывает changes;
- когда и как выполняются reviews, testing, regression и release checks;
- какие artifacts нужны для контроля качества.

Для QA собеседований важно не просто перечислить модели, а объяснить, чем они отличаются на практике.

Например, в Waterfall тестирование часто начинается после завершения разработки, поэтому поздние defects стоят дороже. В V-Model testing activities планируются параллельно development phases, что улучшает traceability. В Scrum команда работает sprint-by-sprint. В Kanban основной фокус - continuous flow и WIP limits. В XP сильный акцент делается на engineering practices: TDD, pair programming, continuous integration и refactoring.

## Questions

- Чем development model отличается от testing life cycle?
- Почему QA должен понимать модель разработки проекта?
- В каких случаях Waterfall или V-Model могут быть лучше Agile-подхода?
- Чем Scrum отличается от Kanban?
- Почему XP считается более engineering-focused framework?

## What To Review Later

- Waterfall vs V-Model
- Scrum roles, events и artifacts
- Kanban board, WIP limits и cycle time
- XP values и engineering practices
- Как выбранная модель влияет на STLC
