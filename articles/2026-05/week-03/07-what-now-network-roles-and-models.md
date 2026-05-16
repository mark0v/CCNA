# What Now? Network Roles and Models

Source: закрытая страница курса  
Date added: 2026-05-16  
Related plan item: Week 3 / Network roles and model review  
Tags: network architect, network engineer, network administrator, osi, tcp/ip, three-tier architecture, career, design
Language: Russian
Translation pair: articles-en/2026-05/week-03/07-what-now-network-roles-and-models.md

## Summary

После изучения communication models и design models важно понимать, как эти знания проявляются в реальных ролях. Network Architect обычно отвечает за vision и blueprint сети. Network Engineer реализует этот design и превращает его в работающую infrastructure. Network Administrator поддерживает сеть каждый день: monitoring, maintenance и troubleshooting.

В больших организациях эти роли могут быть разделены. В маленьких компаниях один человек часто носит все три "шляпы". Поэтому важно смотреть не только на job title, но и на реальные responsibilities.

## Key Points

- Network Architect, Network Engineer and Network Administrator are related but distinct roles.
- Network Architect focuses on design, strategy and blueprint.
- Network Engineer implements the design and makes the network work.
- Network Administrator keeps the network running day to day.
- In smaller organizations, one person may perform all three roles.
- Job titles are often used loosely in postings.
- Responsibilities matter more than the title.
- OSI and TCP/IP are core communication models.
- OSI is the daily troubleshooting and communication language for engineers.
- TCP/IP describes the real protocol stack used by modern networks.
- Three-tier architecture is a practical design model for real networks.
- Models create the foundation for routing, switching, protocols and security.

## Notes

### Почему роли важно различать

В networking часто встречаются похожие titles:

- Network Architect;
- Network Engineer;
- Network Administrator.

Снаружи они звучат почти одинаково. В реальной организации это могут быть разные responsibilities.

Понимание разницы помогает:

- читать job postings точнее;
- понимать, кто за что отвечает на проекте;
- не путаться на IT meetings;
- видеть карьерный путь вперед.

### Network Architect

Network Architect отвечает за vision and blueprint.

Он думает о вопросах:

- как сеть должна быть построена;
- какие protocols и standards использовать;
- как соединить buildings, branches or data centers;
- где будет redundancy;
- как design будет scale;
- какие physical and logical connections нужны.

Architect не всегда настраивает каждый switch вручную. Его основная задача - design.

Аналогия:

```text
Building architect designs the building.
Construction team builds it.
```

### Network Engineer

Network Engineer берет design и делает его реальным.

Он занимается:

- configuration;
- implementation;
- testing;
- routing and switching setup;
- firewall or edge configuration;
- wireless deployment;
- validation;
- troubleshooting during rollout.

Если architect creates the blueprint, engineer builds the working network.

Это роль, где design встречается с real configs.

### Network Administrator

Network Administrator keeps the lights on.

Его фокус:

- day-to-day maintenance;
- monitoring;
- user/network support;
- routine changes;
- troubleshooting incidents;
- checking alerts;
- keeping existing infrastructure stable.

Administrator может делать small changes, но обычно big design и major rollout уже сделаны.

Главная задача:

```text
Keep the network running.
```

### Overlap in Small Companies

В large organization роли могут быть разделены:

```text
Architect designs.
Engineer implements.
Administrator operates.
```

В small shop один человек может делать все:

```text
Design the network.
Configure the devices.
Monitor and fix it later.
```

Это нормально для IT. Поэтому title не всегда рассказывает всю историю.

### Job Titles Can Be Loose

В job postings titles часто используются неточно.

Например:

```text
Network Administrator
```

может означать:

- basic monitoring role;
- engineer-level implementation;
- firewall management;
- routing and switching;
- wireless support;
- on-call troubleshooting;
- documentation and design work.

Правильный подход:

```text
Do not read only the title.
Read the responsibilities.
```

Responsibilities show the real job.

### What You Have Learned So Far

К этому моменту уже пройдено несколько важных foundations.

Communication models:

- OSI model;
- TCP/IP model.

Design models:

- SOHO;
- two-tier / collapsed core;
- three-tier architecture;
- MDF/IDF planning;
- spine-leaf as a data center preview.

Это не отдельные disconnected topics. Они связываются в одну картину.

### OSI and TCP/IP Review

OSI and TCP/IP describe network communication.

TCP/IP - это то, что реально работает в modern networks and the internet.

OSI - это language, который engineers используют каждый день:

```text
Layer 1 issue
Layer 2 problem
Check Layer 3
Transport behavior
```

Для troubleshooting OSI особенно важен, потому что помогает быстро сузить область проблемы.

### Three-Tier Architecture Review

Three-tier architecture показывает, как physical/logical network design должен быть structured.

Layers:

- Access;
- Distribution;
- Core.

Access layer connects end devices.

Distribution layer aggregates access and provides policy/redundancy boundaries.

Core layer moves traffic between major network blocks or buildings.

Это помогает избежать random switch sprawl and fragile daisy chains.

### Why This Foundation Matters

Дальше идут более глубокие темы:

- switching;
- routing;
- protocols;
- IP addressing;
- security;
- wireless;
- troubleshooting.

Все они строятся на foundation:

```text
Models -> Communication -> Design -> Configuration -> Troubleshooting
```

Если ты понимаешь models, новые topics легче поставить на место.

### Main Takeaway

Network models and network roles connect theory to real work.

Ты учишь не просто layers and diagrams.

Ты учишься:

- говорить как network professional;
- понимать responsibilities;
- проектировать before plugging things in;
- видеть how communication moves;
- понимать, где твоя роль в проекте.

Это фундамент для всего, что идет дальше.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Network Architect | Role focused on network vision, strategy, standards and design blueprint. |
| Network Engineer | Role focused on implementing, configuring, testing and troubleshooting network infrastructure. |
| Network Administrator | Role focused on daily operation, monitoring, maintenance and support of the network. |
| Responsibility | Actual work expected in a role; often more important than the job title. |
| Blueprint | Planned network design created before implementation. |
| Implementation | Turning a design into a working network through configuration and deployment. |
| Operations | Daily work of keeping systems running and responding to issues. |
| OSI model | Seven-layer communication model used heavily for troubleshooting language. |
| TCP/IP model | Practical communication model used by modern networks and the internet. |
| Three-tier architecture | Design model with access, distribution and core layers. |
| Collapsed core | Two-tier model where core functions are combined with distribution. |
| MDF | Main Distribution Facility; main network distribution room or central point. |
| IDF | Intermediate Distribution Facility; local network distribution point for an area or floor. |

## Questions

### 1. What does a Network Architect usually focus on?

Design, strategy, standards, physical/logical connections and the overall network blueprint.

### 2. What does a Network Engineer usually do?

Implements the design, configures devices, tests the network and troubleshoots during deployment.

### 3. What does a Network Administrator usually do?

Keeps the network running day to day through monitoring, maintenance and troubleshooting.

### 4. Can one person perform all three roles?

Yes. In smaller organizations, one person may act as architect, engineer and administrator.

### 5. Why should you read job responsibilities instead of only job titles?

Because companies use titles loosely, and the responsibilities show the real expected work.

### 6. Which communication model becomes daily troubleshooting language?

The OSI model.

### 7. What is TCP/IP's role?

It is the practical protocol model used by modern networks and the internet.

### 8. Why is three-tier architecture important?

It gives a structured way to design real networks with access, distribution and core layers.

### 9. What does the access layer connect?

End devices such as computers, printers, phones, APs and POS terminals.

### 10. What comes next after this foundation?

Deeper work with routing, switching, protocols, security and troubleshooting.

## What To Review Later

- Network Architect vs Network Engineer vs Network Administrator.
- Reading job responsibilities.
- OSI as troubleshooting language.
- TCP/IP as practical protocol model.
- Three-tier architecture.
- Access, distribution and core layers.
- MDF and IDF basics.
- How models support routing, switching and security.
