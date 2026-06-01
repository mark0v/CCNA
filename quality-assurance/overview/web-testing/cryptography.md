# Cryptography

## Summary

Cryptography - это набор методов, которые помогают защищать данные с помощью encryption, decryption, keys, hash functions и digital signatures.

В web testing cryptography важна не потому, что QA должен вручную реализовывать AES или RSA. Важно понимать, где cryptography используется в реальных web systems:

- HTTPS защищает traffic между browser и server;
- passwords обычно хранятся как hashes, а не plain text;
- tokens and sessions помогают управлять authentication;
- digital signatures помогают подтвердить integrity и authenticity;
- encryption защищает sensitive data in transit и at rest.

Главная мысль:

> Cryptography помогает сделать данные unreadable для посторонних и detectable при подмене.

## Basic Terms

Перед тем как говорить о cryptography, нужно понимать базовые термины.

| Term | Meaning |
| --- | --- |
| Plain text | Исходные readable data или message. |
| Cipher text | Encrypted data, которые выглядят unreadable без key. |
| Encryption | Процесс превращения plain text в cipher text. |
| Decryption | Процесс превращения cipher text обратно в plain text. |
| Key | Секретное или публичное значение, которое используется algorithm для encryption/decryption. |
| Algorithm | Математический метод, который выполняет cryptographic operation. |
| Hash | Fixed-length fingerprint данных. |
| Digital signature | Cryptographic proof, что message или document пришел от ожидаемого sender и не был изменен. |

## What Is Cryptography?

Cryptography - это practice and science of protecting information.

Она помогает:

- скрывать sensitive data от unauthorized users;
- проверять, что данные не были изменены;
- подтверждать identity участников обмена;
- защищать communication over network;
- снижать риск data breaches.

В web applications cryptography чаще всего встречается в:

- HTTPS;
- password storage;
- API authentication;
- signed tokens;
- cookies and sessions;
- payment processing;
- document signing;
- secure file storage.

## How Cryptography Works

Базовый flow encryption/decryption выглядит так:

```text
Plain Text -> Encryption Algorithm + Key -> Cipher Text
Cipher Text -> Decryption Algorithm + Key -> Plain Text
```

Пример:

1. User отправляет sensitive message.
2. System превращает readable message в cipher text.
3. Cipher text передается через network.
4. Receiver использует correct key.
5. Cipher text превращается обратно в readable message.

Если attacker перехватит cipher text, он не должен понять исходные данные без key.

## Simple Example

Samuel хочет отправить Yary message с trade secrets.

Если message идет через public network без защиты, attacker Evy может:

- прочитать message;
- изменить message;
- подменить content;
- скрыть факт вмешательства.

С cryptography flow становится безопаснее:

1. Samuel encrypts message.
2. Через network идет cipher text.
3. Evy видит unreadable data.
4. Yary decrypts message with correct key.
5. Если cipher text был изменен, integrity check может показать tampering.

Это не делает систему магически неуязвимой, но сильно снижает риск чтения и незаметной подмены данных.

## Main Security Goals

Cryptography поддерживает несколько security goals.

## Confidentiality

Confidentiality означает, что unauthorized users не могут прочитать данные.

Пример:

HTTPS не дает постороннему легко прочитать login/password между browser и server.

## Integrity

Integrity означает, что можно обнаружить изменение данных.

Пример:

Если downloaded file изменился, его hash тоже изменится.

## Authentication

Authentication помогает подтвердить, кто участвует в communication.

Пример:

TLS certificate помогает browser понять, что он подключается к ожидаемому website, а не к поддельному server.

## Non-Repudiation

Non-repudiation помогает доказать, что sender действительно выполнил action или подписал document.

Пример:

Digital signature может подтвердить, что document был подписан конкретным private key.

## Types Of Cryptography

## Symmetric Key Cryptography

Symmetric cryptography использует один и тот же key для encryption и decryption.

Flow:

```text
Same key encrypts data
Same key decrypts data
```

Плюсы:

- fast;
- хорошо подходит для bulk data encryption;
- часто используется для больших объемов данных.

Минусы:

- нужно безопасно передать shared key;
- если key leaked, attacker может decrypt data.

Пример algorithm:

- AES.

QA angle:

QA обычно не проверяет math внутри AES, но может проверять, что sensitive data не передается в plain text и что encryption включен там, где должен быть.

## Asymmetric Key Cryptography

Asymmetric cryptography использует key pair:

- public key;
- private key.

Public key можно распространять. Private key должен оставаться secret.

Один common flow:

```text
Public key encrypts data
Private key decrypts data
```

Пример:

Bob хочет отправить encrypted message Alice.

1. Alice создает public/private key pair.
2. Bob получает Alice public key.
3. Bob encrypts message with Alice public key.
4. Alice decrypts message with her private key.

Плюсы:

- проще обмениваться public keys;
- private key не нужно отправлять по network;
- используется для TLS, digital signatures и key exchange.

Минусы:

- slower than symmetric encryption;
- не очень удобно для больших объемов данных.

Пример algorithm:

- RSA;
- ECC.

## Hash Functions

Hash function превращает input любого размера в fixed-length output.

Пример:

```text
"hello" -> hash value
```

Важные свойства:

- same input должен давать same hash;
- small input change должен сильно менять hash;
- по hash нельзя нормально восстановить original input;
- сложно найти два разных input с одинаковым hash.

Hash functions используются для:

- password storage;
- integrity checks;
- digital signatures;
- file verification;
- blockchain;
- detecting data changes.

Важно:

Hashing - это не encryption. Hash нельзя "decrypt" обратно. Его можно только сравнить с новым hash.

## Digital Signatures

Digital signature помогает подтвердить:

- кто подписал data;
- что data не изменились после подписи.

Обычно sender подписывает hash данных своим private key. Receiver проверяет signature с помощью sender public key.

Примеры использования:

- signed documents;
- software updates;
- code signing;
- certificates;
- secure transactions.

QA angle:

Если system использует signatures, QA должен проверять поведение при:

- invalid signature;
- expired certificate;
- modified payload;
- wrong public key;
- missing signature.

## Common Cryptographic Algorithms

| Algorithm | Type | Common Use |
| --- | --- | --- |
| AES | Symmetric encryption | Fast encryption of data. |
| RSA | Asymmetric encryption/signing | Key exchange, signatures, certificates. |
| SHA-2 / SHA-3 | Hash functions | Integrity checks, fingerprints. |
| ECC | Asymmetric cryptography | Smaller keys, mobile/IoT/blockchain usage. |
| DES | Old symmetric encryption | Historical algorithm, not recommended for modern security. |

Для QA важнее понимать purpose и risks, чем вручную считать formulas.

## Cryptography In Web Applications

## HTTPS And TLS

HTTPS использует TLS для защиты communication между browser и server.

TLS помогает:

- encrypt traffic;
- authenticate server through certificate;
- protect data from tampering;
- reduce man-in-the-middle risk.

Что проверять:

- site opens over HTTPS;
- certificate is valid;
- HTTP redirects to HTTPS;
- no mixed content;
- sensitive forms are not submitted over HTTP;
- cookies have `Secure` flag where needed.

## Password Storage

Passwords не должны храниться в plain text.

Обычно system хранит password hash, часто вместе с salt.

Правильный idea:

```text
User password -> hash function -> stored hash
```

При login:

```text
Entered password -> hash function -> compare with stored hash
```

Что проверять:

- password не возвращается в API response;
- password не виден в logs;
- reset flow не отправляет old password;
- database не хранит plain text password;
- error messages не раскрывают лишнюю информацию.

## Tokens And Sessions

Web applications часто используют tokens или session cookies.

Cryptography может использоваться для:

- signing tokens;
- protecting session integrity;
- generating secure random values;
- validating expiration;
- preventing tampering.

Что проверять:

- token expires;
- invalid token is rejected;
- modified token is rejected;
- logout invalidates session if expected;
- sensitive cookies use `HttpOnly`, `Secure`, `SameSite`.

## Data At Rest

Data at rest - это данные, которые хранятся:

- in database;
- in files;
- in backups;
- in cloud storage;
- on user devices.

Sensitive data может требовать encryption at rest.

Примеры:

- payment data;
- personal data;
- medical data;
- private documents;
- API keys.

QA angle:

QA может проверять не сам encryption algorithm, а product behavior and exposure:

- sensitive data не отображается лишним users;
- exports не раскрывают secrets;
- backups не доступны publicly;
- logs не содержат credentials.

## Cryptographic Attacks

## Brute Force Attack

Brute force attack перебирает возможные passwords или keys.

Защита:

- strong passwords;
- rate limiting;
- account lockout;
- MFA;
- slow password hashing algorithms.

QA checks:

- много failed logins блокируются или ограничиваются;
- system не позволяет unlimited password guessing;
- error messages не помогают attacker.

## Dictionary Attack

Dictionary attack использует список common passwords или words.

QA checks:

- password policy blocks weak passwords;
- breached/common passwords can be rejected if product supports it;
- rate limiting работает.

## Man-In-The-Middle Risk

Attacker пытается стоять между client and server.

TLS снижает риск, если certificate validation работает правильно.

QA checks:

- no HTTP for sensitive actions;
- invalid certificate не принимается silently;
- mobile apps use proper certificate validation.

## Side-Channel Attacks

Side-channel attacks используют indirect information:

- timing;
- power usage;
- error differences;
- response patterns.

QA редко тестирует это глубоко, но может замечать dangerous behavior:

- login error reveals whether email exists;
- reset flow leaks user existence;
- response time clearly differs for valid/invalid accounts.

## Advantages

Cryptography помогает:

- protect confidentiality;
- preserve integrity;
- verify identity;
- support secure authentication;
- enable digital signatures;
- protect transactions;
- reduce impact of intercepted traffic;
- secure stored sensitive data.

## Limitations

Cryptography не решает все security problems.

Ограничения:

- weak keys break security;
- leaked private key compromises protection;
- wrong implementation can be dangerous;
- old algorithms become unsafe;
- encrypted data can still be deleted or corrupted;
- user devices can be compromised;
- logs and screenshots can leak data outside encryption.

Важно:

> Strong encryption does not save a badly designed system.

## What QA Should Test

## Transport Security

Проверить:

- HTTPS используется на sensitive pages;
- certificate valid;
- HTTP redirects to HTTPS;
- no mixed content;
- secure cookies configured correctly.

## Sensitive Data Exposure

Проверить:

- passwords не видны в API responses;
- tokens не попадают в URL;
- secrets не пишутся в browser console;
- personal data не видна unauthorized users;
- logs не содержат credentials.

## Authentication And Session Security

Проверить:

- invalid credentials rejected;
- brute force protection exists;
- session expires;
- logout behavior correct;
- tampered token rejected;
- reset password flow safe.

## Integrity Checks

Проверить:

- modified signed payload rejected;
- file checksum mismatch detected if supported;
- webhook signature validation works;
- unsigned request rejected when signature required.

## Error Messages

Проверить:

- errors do not expose keys;
- stack traces not shown to user;
- invalid token error is safe;
- login errors do not leak too much account information.

## Example Bug Investigation

Bug:

```text
After logout, user can still open account page using Back button.
```

QA investigation:

1. Is the page loaded from browser cache?
2. Is session cookie still valid?
3. Does backend reject request without active session?
4. Are protected API calls returning `401` or still `200`?
5. Are cache headers correct for sensitive pages?

This bug may look like UI issue, but often it is session/security behavior.

## Common Mistakes

Common mistakes:

- sending sensitive data over HTTP;
- storing passwords in plain text;
- putting tokens in URL query parameters;
- exposing secrets in logs;
- accepting expired or modified tokens;
- showing stack traces to users;
- using weak password reset flows;
- assuming HTTPS alone fixes all security problems;
- using old or broken algorithms;
- not testing negative security scenarios.

## Commands / Terms

| Term | Meaning |
| --- | --- |
| Plain text | Readable original data. |
| Cipher text | Encrypted unreadable data. |
| Encryption | Converting plain text into cipher text. |
| Decryption | Converting cipher text back into plain text. |
| Key | Value used by cryptographic algorithm. |
| Symmetric encryption | Same key encrypts and decrypts data. |
| Asymmetric encryption | Public/private key pair is used. |
| Hash function | One-way function that creates fixed-length fingerprint. |
| Digital signature | Proof of authenticity and integrity. |
| AES | Common symmetric encryption algorithm. |
| RSA | Common asymmetric algorithm. |
| SHA | Family of secure hash algorithms. |
| TLS | Protocol used to secure HTTPS. |
| Certificate | Digital document used to verify server identity. |
| Salt | Random value added before hashing passwords. |
| MFA | Multi-factor authentication. |

## Questions

### 1. What is cryptography?

Cryptography is a set of methods for protecting data using encryption, decryption, keys, hashes and signatures.

### 2. What is the difference between plain text and cipher text?

Plain text is readable original data. Cipher text is encrypted data that should be unreadable without the correct key.

### 3. How is hashing different from encryption?

Encryption can be decrypted with the correct key. Hashing is one-way and is used for comparison or integrity checks.

### 4. What is symmetric encryption?

It is encryption where the same key is used for encryption and decryption.

### 5. What is asymmetric encryption?

It uses a public/private key pair. Public key can be shared, private key must stay secret.

### 6. Why is HTTPS important?

HTTPS protects traffic between browser and server using TLS, reducing the risk of interception and tampering.

### 7. Why should passwords not be stored in plain text?

If database leaks, plain text passwords are immediately exposed. Hashing reduces the damage.

### 8. What should QA check around tokens?

QA should check expiration, rejection of modified tokens, logout behavior, cookie flags and unauthorized access.

## What To Review Later

- HTTPS and TLS
- HTTP Cookies
- Authentication
- Authorization
- Session Management
- Password Reset Flow
- API Security Testing
- Webhook Signatures
