# 🤖 07 — Автоматизация тестирования & CI/CD

Language: Russian
Translation pair: quality-assurance-en/overview/07-automation/index.md

> **Твой уровень:** 🔴 ПРОБЕЛ (Git — Not Started; CI — Familiar with; Automation — не в матрице)  
> **Приоритет:** ⭐ НАЧАЛЬНЫЙ (для Junior достаточно понимания основ)

---

## 7.1 Git / Version Control
**Твой уровень:** 🔴 ПРОБЕЛ (из матрицы)

### Зачем QA нужен Git
- Хранение тест-скриптов и автотестов
- Работа с ветками для разных версий тестов
- Code review тестов
- Интеграция с CI/CD pipeline

### Основные команды
```bash
# Клонировать репозиторий
git clone https://github.com/user/repo.git

# Посмотреть статус
git status

# Добавить файлы в индекс
git add .
git add filename.js

# Сделать коммит
git commit -m "Add login test case"

# Отправить на сервер
git push origin main

# Получить изменения
git pull

# Создать ветку
git checkout -b feature/login-tests

# Переключиться на ветку
git checkout main

# Посмотреть историю
git log --oneline
```

### Gitflow — рабочий процесс
- **main** — стабильная продакшн ветка
- **develop** — ветка разработки
- **feature/xxx** — ветки для конкретных фич
- **hotfix/xxx** — срочные фиксы на prod

### Ресурсы
- 🔗 [Top 20 Git Commands](https://dzone.com/articles/top-20-git-commands-with-examples)
- 🔗 [Git Book (RU)](https://git-scm.com/book/ru)
- 🔗 [Git Cheat Sheet](https://www.cloudways.com/blog/git-cheat-sheet/)

---

## 7.2 CI/CD — основы
**Твой уровень:** 🟡 Familiar with

### Что такое CI/CD
- **CI (Continuous Integration)** — автоматическая сборка и тестирование при каждом коммите
- **CD (Continuous Delivery)** — автоматическая доставка на staging
- **CD (Continuous Deployment)** — автоматический деплой на продакшн

### Роль QA в CI/CD
- Автотесты запускаются в pipeline при каждом PR
- Smoke тесты запускаются при деплое
- QA gate — тесты должны пройти для merge в main

### Популярные CI/CD инструменты
| Инструмент | Хостинг | Особенности |
|-----------|---------|-------------|
| **GitLab CI/CD** | Self-hosted / Cloud | .gitlab-ci.yml |
| **GitHub Actions** | Cloud | .github/workflows/ |
| **Jenkins** | Self-hosted | Многолетний стандарт |
| **CircleCI** | Cloud | Быстрая конфигурация |
| **TeamCity** | JetBrains | Популярен в .NET |

### Пример .gitlab-ci.yml (базовый)
```yaml
stages:
  - test

run-tests:
  stage: test
  image: node:18
  script:
    - npm install
    - npm test
  only:
    - merge_requests
    - main
```

### Ресурсы
- 🔗 [What is CI/CD? (RedHat)](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
- 🔗 [GitLab CI/CD Guide](https://about.gitlab.com/topics/ci-cd/)
- 🔗 [CI/CD Explained (Synopsys)](https://www.synopsys.com/glossary/what-is-cicd.html)

---

## 7.3 Docker для тестировщика
**Твой уровень:** 🔴 ПРОБЕЛ

### Основные концепции
- **Image** — шаблон для создания контейнера (как класс)
- **Container** — запущенный экземпляр image (как объект)
- **Dockerfile** — инструкции для создания image
- **docker-compose** — запуск нескольких контейнеров вместе

### Основные команды для QA
```bash
# Посмотреть запущенные контейнеры
docker ps

# Посмотреть логи контейнера
docker logs container_name
docker logs -f container_name  # в режиме реального времени

# Запустить контейнер
docker run -d -p 8080:80 nginx

# Остановить контейнер
docker stop container_name

# Запустить compose (несколько сервисов)
docker-compose up -d

# Войти в контейнер
docker exec -it container_name bash
```

### docker-compose пример (test environment)
```yaml
version: '3'
services:
  app:
    image: myapp:latest
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=postgres
  postgres:
    image: postgres:14
    environment:
      POSTGRES_DB: testdb
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test
```

### Ресурсы
- 🔗 [Docker: Get Started](https://docs.docker.com/get-started/overview/)
- 🔗 [Docker для QA (qagroup.com.ua)](https://qagroup.com.ua/publications/shcho-take-docker-i-navishcho-vin/)

---

## 7.4 Основы автоматизации тестирования
**Твой уровень:** 🔴 ПРОБЕЛ (необязательно для Junior, но важно понимать)

### Когда автоматизировать
✅ **Автоматизировать:**
- Smoke / Regression тесты (часто запускаются)
- Тесты, которые нужно запускать на разных браузерах/устройствах
- API тесты (стабильны, быстро выполняются)
- Load тесты

❌ **НЕ автоматизировать:**
- Exploratory тестирование
- Тесты, которые часто меняются
- One-time тесты
- Usability тестирование

### Пирамида тестирования
```
        /\
       /E2E\          ← мало, дорого, медленно
      /------\
     /  API   \       ← золотая середина
    /----------\
   /  Unit Tests \    ← много, дёшево, быстро
  /--------------\
```

### Основные фреймворки

#### Selenium (Web — Java/Python/JS/.NET/Ruby)
- Самый популярный для UI автоматизации
- WebDriver API — управление браузером
- Поддержка всех браузеров
- 🔗 [Selenium Documentation](https://www.selenium.dev/documentation/)

#### Playwright (Web — JS/Python/Java/.NET)
- Современная альтернатива Selenium
- Auto-wait, трейсинг, снапшоты
- Поддержка Chromium, Firefox, WebKit
- 🔗 [Playwright Docs](https://playwright.dev/docs/intro)

#### Cypress (Web — JavaScript)
- Только для Chromium-based браузеров
- Отличный Developer Experience
- Real-time execution в браузере
- 🔗 [Cypress Docs](https://docs.cypress.io/guides/overview/why-cypress)

#### Appium (Mobile — любой язык)
- Автоматизация iOS и Android приложений
- Использует WebDriver протокол
- Поддержка Native, Hybrid, Mobile Web

#### RestAssured / Postman Newman (API)
- RestAssured — Java библиотека для API тестов
- Newman — командная строка для Postman Collections

### Ресурсы
- 🔗 [Test Automation University](https://testautomationu.applitools.com/) — БЕСПЛАТНЫЕ курсы!
- 🔗 [Best Automation Frameworks 2025](https://www.browserstack.com/guide/best-test-automation-frameworks)

---

## 7.5 Основы программирования для QA
**Твой уровень:** 🔴 ПРОБЕЛ (необходимо для автоматизации)

### Что нужно знать (JavaScript / Python)
```javascript
// Базовые типы данных
let name = "Oleksandr";    // string
let age = 30;               // number
let isActive = true;        // boolean
let data = null;            // null

// Массивы
let items = [1, 2, 3];
items.push(4);              // добавить
items[0];                   // обратиться по индексу

// Объекты
let user = {
  name: "Alex",
  email: "alex@test.com"
};
user.name;                  // обратиться к полю

// Условия
if (status === "active") {
  console.log("User is active");
} else {
  console.log("User is inactive");
}

// Циклы
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// Функции
function checkStatus(user) {
  return user.status === "active";
}
```

### Ресурсы для изучения
- [JavaScript для начинающих (MDN)](https://developer.mozilla.org/ru/docs/Learn/JavaScript)
- [Python для QA (Test Automation University)](https://testautomationu.applitools.com/)

---

## ✅ Чеклист по разделу

- [ ] Умею клонировать репозиторий, создавать ветки, делать коммиты и пуши
- [ ] Понимаю Gitflow (main/develop/feature/hotfix)
- [ ] Знаю что такое CI/CD и роль QA в нём
- [ ] Умею читать простой .gitlab-ci.yml / GitHub Actions файл
- [ ] Умею запустить `docker ps`, `docker logs`, `docker-compose up`
- [ ] Понимаю пирамиду тестирования
- [ ] Знаю разницу Selenium / Playwright / Cypress / Appium
- [ ] Написал хотя бы один простой автотест (API или UI)
- [ ] Прошёл хотя бы 1 курс на Test Automation University

---

## 📚 Рекомендуемый путь для начала автоматизации

1. **Месяц 1:** Git + базовый JavaScript/Python
2. **Месяц 2:** Postman Newman — запуск API тестов из командной строки
3. **Месяц 3:** Playwright или Cypress — простые UI тесты
4. **Месяц 4:** Интеграция тестов в GitLab CI pipeline
