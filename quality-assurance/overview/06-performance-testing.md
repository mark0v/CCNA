# ⚡ 06 — Performance тестирование

> **Твой уровень:** 🔴 КРИТИЧЕСКИЙ ПРОБЕЛ (все подтемы Not Started в матрице и IDP)  
> **Приоритет:** ⭐⭐ СРЕДНИЙ

---

## 6.1 Виды Performance тестирования
**Твой уровень:** 🔴 ПРОБЕЛ (из IDP)

### Load Testing (Нагрузочное)
- **Цель:** проверить поведение системы при **ожидаемой** нагрузке
- Проверяем: время ответа при N одновременных пользователях
- Пример: 1000 пользователей одновременно делают покупку
- Ключевые метрики: **Response Time, Throughput (RPS), Error Rate**
- 🔗 [Load Testing (Guru99)](https://www.guru99.com/load-testing-tutorial.html)

### Stress Testing (Стрессовое)
- **Цель:** найти предел системы — сколько выдержит до поломки
- Нагрузка **выше ожидаемой** (150%, 200%, ...)
- Проверяем: как система восстанавливается после перегрузки (Graceful Degradation)
- Пример: что будет, если одновременно зайдёт 10.000 вместо ожидаемых 1.000
- 🔗 [Stress Testing (Guru99)](https://www.guru99.com/stress-testing-tutorial.html)

### Stability / Soak Testing (Стабильность)
- **Цель:** поведение системы при **длительной** работе под нагрузкой
- Запускаем нормальную нагрузку на 8-24 часа
- Ищем: **Memory Leaks** (утечки памяти), деградацию производительности со временем
- Пример: система работает нормально 1 час, но через 8 часов начинает тормозить
- 🔗 [Stability Testing (Guru99)](https://www.guru99.com/stability-testing.html)

### Spike Testing (Пиковое)
- **Цель:** резкое увеличение нагрузки за короткий промежуток
- Пример: Black Friday — за 1 минуту нагрузка возрастает в 10 раз
- Проверяем: Auto-Scaling, CDN, Load Balancer

### Configuration Testing
- **Цель:** как производительность меняется при изменении конфигурации
- Пример: больше RAM → быстрее? Другая СУБД → медленнее?
- 🔗 [Configuration Testing](https://www.guru99.com/configuration-testing.html)

---

## 6.2 Ключевые метрики производительности
**Твой уровень:** 🔴 ПРОБЕЛ

### Основные метрики
| Метрика | Описание | Хороший показатель |
|---------|----------|-------------------|
| **Response Time** | Время от запроса до полного ответа | < 2 сек для веб |
| **Latency** | Задержка до первого байта | < 200ms |
| **Throughput (RPS)** | Запросов в секунду, которые может обработать | Зависит от системы |
| **Error Rate** | % ошибочных ответов | < 1% |
| **Concurrent Users** | Количество одновременных пользователей | Зависит от бизнеса |
| **CPU Usage** | Потребление процессора | < 80% под нагрузкой |
| **Memory Usage** | Потребление RAM | Нет роста со временем |
| **TPS** | Транзакций в секунду (для DB) | Зависит от системы |

### Web Vitals (для веб)
- **LCP** (Largest Contentful Paint) — время загрузки главного контента < 2.5s
- **FID** (First Input Delay) — задержка первого взаимодействия < 100ms
- **CLS** (Cumulative Layout Shift) — стабильность layout < 0.1

---

## 6.3 Инструменты Performance тестирования
**Твой уровень:** 🔴 ПРОБЕЛ (из IDP)

### JMeter (Apache) — Open Source
- Самый популярный инструмент нагрузочного тестирования
- GUI и headless режимы
- Поддержка HTTP, HTTPS, FTP, JDBC, WebSocket
- Репорты: Summary Report, Aggregate Report, Graphs

### k6 — Modern Load Testing
- Написан на Go, скрипты на JavaScript
- Хорошая интеграция с CI/CD
- Пример скрипта:
```javascript
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 100,        // 100 virtual users
  duration: '30s', // 30 seconds
};

export default function () {
  http.get('https://api.example.com/users');
  sleep(1);
}
```

### Gatling — Scala-based
- Высокая производительность
- HTML отчёты
- Хорош для CI/CD pipeline

### Locust — Python-based
- Скрипты на Python
- Удобный веб-интерфейс
- Простое масштабирование

### Другие инструменты
- **Artillery** — Node.js, cloud-native
- **BlazeMeter** — облачная платформа на базе JMeter
- **k6 Cloud** — облачное выполнение k6

### Ресурсы
- 🔗 [Performance Testing Tools (SoftwareTestingHelp)](https://www.softwaretestinghelp.com/performance-testing-tools-load-testing-tools/)
- 🔗 [Performance Testing Tools (Edureka)](https://www.edureka.co/blog/performance-testing-tools/)

---

## 6.4 Процесс проведения Performance тестирования
**Твой уровень:** 🔴 ПРОБЕЛ (из IDP)

### 9 этапов
1. **Requirements Analysis** — какие SLA нужно достичь? (Response time < 2s при 500 users)
2. **Test Planning** — выбор инструментов, окружение, сценарии
3. **Test Environment Setup** — изолированная среда = prod-like
4. **Test Scenario Design** — реальные пользовательские сценарии
5. **Script Development** — написание тест-скриптов
6. **Baseline Testing** — тест при минимальной нагрузке (1 user)
7. **Test Execution** — запуск с постепенным ростом нагрузки
8. **Results Analysis** — анализ метрик, поиск bottlenecks
9. **Reporting** — отчёт с выводами и рекомендациями

### Ресурсы
- 🔗 [9 Stages of Performance Testing (a1qa)](https://www.a1qa.com/blog/9-stages-of-effective-performance-testing-process/)

---

## 6.5 Модели нагрузки
**Твой уровень:** 🔴 ПРОБЕЛ (из IDP)

### Типы нагрузочных моделей
- **Closed Workload Model** — фиксированное количество пользователей (Virtual Users)
- **Open Workload Model** — фиксированный поток запросов в секунду (RPS/TPS)
- **Ramp-up** — постепенное увеличение нагрузки
- **Steady State** — постоянная нагрузка
- **Peak Testing** — максимальная нагрузка

### Пример плана нагрузки
```
0-5 мин:    Ramp up от 0 до 100 пользователей
5-25 мин:   Steady state — 100 пользователей
25-30 мин:  Ramp down до 0
```

### Ресурсы
- 🔗 [Load Models (tmap.net)](https://www.tmap.net/wiki/load-model-performance-testing)

---

## 6.6 Типичные проблемы производительности
**Твой уровень:** 🔴 ПРОБЕЛ (из IDP)

### Проблемы и их признаки
| Проблема | Признак | Возможная причина |
|---------|---------|------------------|
| **Memory Leak** | Память растёт со временем | Объекты не освобождаются |
| **CPU Bottleneck** | CPU 100% под нагрузкой | Неэффективный алгоритм |
| **DB Bottleneck** | Медленные запросы | Нет индексов, N+1 запросы |
| **Network Latency** | Большой Round Trip Time | Далёкий сервер, большой payload |
| **Connection Pool** | Connection refused | Пул соединений исчерпан |
| **Thread Deadlock** | Зависание приложения | Конкуренция за ресурс |

### Ресурсы
- 🔗 [Website Speed Factors](https://www.plerdy.com/blog/website-speed-factors-and-tools/)

---

## ✅ Чеклист по разделу

- [ ] Знаю разницу Load / Stress / Stability / Spike тестирования
- [ ] Понимаю ключевые метрики: Response Time, Throughput, Error Rate
- [ ] Умею установить и запустить JMeter
- [ ] Создал базовый тест-план в JMeter (HTTP запросы)
- [ ] Знаю 9 этапов процесса performance тестирования
- [ ] Понимаю что такое Memory Leak и как его обнаружить
- [ ] Знаю как анализировать результаты нагрузочного теста
- [ ] Понимаю разницу открытой и закрытой модели нагрузки
