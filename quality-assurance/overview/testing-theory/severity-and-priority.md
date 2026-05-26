# Severity and Priority in Testing

## Summary

Severity и Priority - это два разных параметра defect report.

Severity показывает, насколько серьезно defect влияет на functionality, stability, data, security или user experience продукта. Priority показывает, насколько срочно этот defect нужно исправить с точки зрения business value, release plan и customer needs.

Проще:

- `Severity` = насколько defect серьезный технически.
- `Priority` = насколько быстро defect нужно исправить.

Эти параметры часто связаны, но не всегда совпадают. Defect может быть high severity, но low priority. Или наоборот: low severity, но high priority.

## Key Points

- Severity обычно определяет QA engineer.
- Priority обычно определяется вместе с product manager, project manager, client или triage team.
- Severity больше связана с functionality, standards, data integrity и system behavior.
- Priority больше связана с scheduling, business impact, customer expectations и release risk.
- Severity обычно более объективна и реже меняется.
- Priority более субъективна и может меняться в зависимости от project situation.
- Неправильная severity может запутать команду и замедлить STLC.
- Неправильная priority может привести к тому, что команда будет чинить не то, что важно для release.

## Notes

### What Is Bug Severity?

Bug Severity, или Defect Severity, - это степень влияния defect на software product.

Если defect ломает critical functionality, блокирует business flow, приводит к data loss или делает систему unusable, severity будет высокой.

Если defect не ломает functionality и влияет только на внешний вид, текст или minor usability detail, severity будет низкой.

Severity отвечает на вопрос:

> Насколько серьезно этот defect влияет на продукт?

### What Is Bug Priority?

Bug Priority - это порядок, в котором defect должен быть исправлен.

Priority отвечает на вопрос:

> Насколько срочно нужно исправить этот defect?

Priority зависит не только от технической серьезности. На нее влияют:

- business value;
- release date;
- client expectations;
- visibility of the issue;
- affected users;
- legal или compliance risk;
- marketing campaign;
- cost of delay;
- workaround availability.

Например, typo в названии компании на главной странице может иметь low severity, потому что functionality не сломана. Но priority может быть high, потому что это visible issue перед клиентами.

### Types of Severity

Severity levels могут отличаться между компаниями, но часто используются такие уровни:

| Severity | Meaning |
| --- | --- |
| Critical | Система или critical flow полностью не работает. Нет workaround. |
| Major | Важная functionality сломана, но часть системы продолжает работать. |
| Moderate | Есть нежелательное поведение, но система в целом functional. |
| Minor | Небольшой defect с ограниченным влиянием. |
| Cosmetic | UI/text/visual issue без влияния на business logic. |

### Types of Priority

Priority levels обычно проще:

| Priority | Meaning |
| --- | --- |
| High | Нужно исправить как можно скорее. Defect важен для release, клиента или business flow. |
| Medium | Нужно исправить в нормальном рабочем порядке. Defect важен, но не блокирует прямо сейчас. |
| Low | Можно исправить позже, после более важных defects. |

### Severity vs Priority

| Priority | Severity |
| --- | --- |
| Показывает, как быстро defect нужно исправить. | Показывает, насколько серьезен defect для продукта. |
| Связана с scheduling и business needs. | Связана с functionality, standards и technical impact. |
| Обычно определяется вместе с manager/client/product side. | Обычно определяется QA engineer. |
| Driven by business value. | Driven by functional impact. |
| Может меняться со временем. | Обычно менее изменчива. |
| Более субъективна. | Более объективна. |

### High Priority, Low Severity

Это defect, который технически не ломает систему, но должен быть исправлен быстро.

Examples:

- неправильный logo на production website;
- typo в названии компании на главной странице;
- неверная цена в promotional banner;
- неправильный текст в legal disclaimer;
- broken marketing link перед важной campaign.

Functionality может работать нормально, но business impact высокий.

### High Severity, Low Priority

Это defect, который технически серьезный, но не требует немедленного исправления.

Examples:

- critical bug в rarely used admin feature, которая не входит в текущий release;
- crash в старом browser, который официально не поддерживается;
- серьезный defect в module, который будет released только в следующем cycle;
- broken flow behind disabled feature flag.

Impact на functionality высокий, но urgency ниже из-за context, scope или release plan.

### Low Priority, Low Severity

Это minor issue, который не влияет на key functionality и не требует срочного исправления.

Examples:

- небольшое UI alignment issue;
- typo во второстепенной подсказке;
- minor spacing issue;
- cosmetic inconsistency на rarely used page.

### High Priority, High Severity

Это defect, который серьезно ломает продукт и должен быть исправлен немедленно.

Examples:

- user cannot log in;
- payment flow is broken;
- application crashes on launch;
- data is lost or corrupted;
- security vulnerability exposes sensitive information;
- checkout cannot be completed in production.

Такие defects обычно блокируют release или требуют hotfix.

### Tips for Determining Severity

Когда назначаешь severity, смотри на technical и user impact:

- ломается ли critical functionality;
- есть ли workaround;
- сколько пользователей затронуто;
- повторяется ли defect часто;
- влияет ли defect на data integrity;
- есть ли security или compliance risk;
- блокирует ли defect testing или release;
- можно ли изолировать проблему.

Minor defect, который встречается очень часто, может иметь больший реальный impact, чем кажется сначала.

### Defect Triage

Defect triage - это процесс review и prioritization defects, особенно когда defects много, а team capacity ограничена.

Цель triage - решить:

- какие defects исправлять первыми;
- какие defects относятся к текущему release;
- какие можно перенести;
- какие нужно отклонить или уточнить;
- кому назначить defect;
- нужен ли workaround.

Typical triage steps:

1. Review all open defects.
2. Check severity and priority.
3. Clarify unclear reports.
4. Decide release impact.
5. Assign owner/team.
6. Update status and target version.

Хороший triage учитывает и severity, и priority. Только priority без severity может скрыть technical risk. Только severity без priority может игнорировать business context.

### Guidelines for QA

QA должен особенно внимательно выбирать severity, потому что она влияет на defect perception.

Practical guidelines:

- не путать severity и priority;
- назначать severity по actual impact, а не по эмоциям;
- описывать business flow, который affected;
- добавлять evidence: screenshots, logs, video, request/response, environment;
- указывать workaround, если он есть;
- объяснять frequency и reproducibility;
- не завышать severity без причины;
- не занижать severity, если defect влияет на data, security или critical flow.

## Commands / Terms

- `Severity` - seriousness of defect impact on product functionality or quality.
- `Priority` - urgency/order of fixing a defect.
- `Critical` - defect blocks critical flow or system usage.
- `Major` - important functionality is broken, but system is partly usable.
- `Moderate` - noticeable issue, system still works.
- `Minor` - small issue with limited impact.
- `Cosmetic` - visual/text issue without functional impact.
- `Defect Triage` - process of reviewing, prioritizing, assigning, and planning defects.
- `Workaround` - alternative way to continue using the system despite the defect.
- `Business Impact` - effect on users, client, revenue, release, or operations.

## Questions

1. What is severity?
2. What is priority?
3. What is the main difference between severity and priority?
4. Who usually defines severity?
5. Who usually defines priority?
6. Can a defect have high priority and low severity?
7. Can a defect have high severity and low priority?
8. What is defect triage?
9. Why is it dangerous to assign wrong severity?
10. What information should QA include to justify severity?

## What To Review Later

- Severity levels
- Priority levels
- High priority vs high severity examples
- Defect triage
- Defect lifecycle
- Bug report structure
- Business impact vs technical impact
