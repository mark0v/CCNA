# Cryptography

## Summary

Cryptography is a set of methods that protect data using encryption, decryption, keys, hash functions, and digital signatures.

In web testing, cryptography matters not because QA must manually implement AES or RSA. It matters because cryptography appears in real web systems:

- HTTPS protects traffic between browser and server;
- passwords are usually stored as hashes, not plain text;
- tokens and sessions help manage authentication;
- digital signatures help prove integrity and authenticity;
- encryption protects sensitive data in transit and at rest.

Main idea:

> Cryptography helps make data unreadable to outsiders and detectable when tampered with.

## Basic Terms

Before discussing cryptography, it is important to know the basic terms.

| Term | Meaning |
| --- | --- |
| Plain text | Original readable data or message. |
| Cipher text | Encrypted data that is unreadable without a key. |
| Encryption | The process of converting plain text into cipher text. |
| Decryption | The process of converting cipher text back into plain text. |
| Key | A secret or public value used by an algorithm for encryption/decryption. |
| Algorithm | A mathematical method that performs a cryptographic operation. |
| Hash | A fixed-length fingerprint of data. |
| Digital signature | Cryptographic proof that a message or document came from the expected sender and was not changed. |

## What Is Cryptography?

Cryptography is the practice and science of protecting information.

It helps:

- hide sensitive data from unauthorized users;
- verify that data was not changed;
- confirm the identity of communication participants;
- protect communication over a network;
- reduce the risk of data breaches.

In web applications, cryptography commonly appears in:

- HTTPS;
- password storage;
- API authentication;
- signed tokens;
- cookies and sessions;
- payment processing;
- document signing;
- secure file storage.

## How Cryptography Works

The basic encryption/decryption flow looks like this:

```text
Plain Text -> Encryption Algorithm + Key -> Cipher Text
Cipher Text -> Decryption Algorithm + Key -> Plain Text
```

Example:

1. A user sends a sensitive message.
2. The system converts the readable message into cipher text.
3. Cipher text travels over the network.
4. The receiver uses the correct key.
5. Cipher text becomes a readable message again.

If an attacker intercepts the cipher text, they should not understand the original data without the key.

## Simple Example

Samuel wants to send Yary a message with trade secrets.

If the message travels over a public network without protection, attacker Evy can:

- read the message;
- modify the message;
- replace the content;
- hide the interference.

With cryptography, the flow becomes safer:

1. Samuel encrypts the message.
2. Cipher text travels over the network.
3. Evy sees unreadable data.
4. Yary decrypts the message with the correct key.
5. If cipher text was changed, an integrity check may detect tampering.

This does not make the system magically invulnerable, but it greatly reduces the risk of reading and silent tampering.

## Main Security Goals

Cryptography supports several security goals.

## Confidentiality

Confidentiality means unauthorized users cannot read the data.

Example:

HTTPS prevents an outsider from easily reading login/password data between browser and server.

## Integrity

Integrity means a change in data can be detected.

Example:

If a downloaded file changes, its hash also changes.

## Authentication

Authentication helps confirm who participates in communication.

Example:

A TLS certificate helps the browser know it is connected to the expected website, not a fake server.

## Non-Repudiation

Non-repudiation helps prove that a sender really performed an action or signed a document.

Example:

A digital signature can prove that a document was signed with a specific private key.

## Types Of Cryptography

## Symmetric Key Cryptography

Symmetric cryptography uses the same key for encryption and decryption.

Flow:

```text
Same key encrypts data
Same key decrypts data
```

Pros:

- fast;
- good for bulk data encryption;
- often used for large amounts of data.

Cons:

- the shared key must be transferred safely;
- if the key leaks, an attacker can decrypt data.

Example algorithm:

- AES.

QA angle:

QA usually does not test the math inside AES, but can check that sensitive data is not transmitted in plain text and that encryption is enabled where expected.

## Asymmetric Key Cryptography

Asymmetric cryptography uses a key pair:

- public key;
- private key.

The public key can be shared. The private key must remain secret.

One common flow:

```text
Public key encrypts data
Private key decrypts data
```

Example:

Bob wants to send an encrypted message to Alice.

1. Alice creates a public/private key pair.
2. Bob gets Alice's public key.
3. Bob encrypts the message with Alice's public key.
4. Alice decrypts the message with her private key.

Pros:

- public keys are easier to share;
- private keys do not need to be sent over the network;
- used for TLS, digital signatures, and key exchange.

Cons:

- slower than symmetric encryption;
- not ideal for large amounts of data.

Example algorithms:

- RSA;
- ECC.

## Hash Functions

A hash function converts input of any size into fixed-length output.

Example:

```text
"hello" -> hash value
```

Important properties:

- same input should produce same hash;
- small input change should strongly change the hash;
- original input should not be recoverable from the hash;
- it should be hard to find two different inputs with the same hash.

Hash functions are used for:

- password storage;
- integrity checks;
- digital signatures;
- file verification;
- blockchain;
- detecting data changes.

Important:

Hashing is not encryption. A hash cannot be "decrypted" back. It can only be compared with a new hash.

## Digital Signatures

A digital signature helps confirm:

- who signed the data;
- that the data was not changed after signing.

Usually the sender signs a hash of the data with their private key. The receiver verifies the signature with the sender's public key.

Examples:

- signed documents;
- software updates;
- code signing;
- certificates;
- secure transactions.

QA angle:

If a system uses signatures, QA should check behavior for:

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

For QA, it is more important to understand purpose and risks than to manually calculate formulas.

## Cryptography In Web Applications

## HTTPS And TLS

HTTPS uses TLS to protect communication between browser and server.

TLS helps:

- encrypt traffic;
- authenticate the server through certificate;
- protect data from tampering;
- reduce man-in-the-middle risk.

Check:

- site opens over HTTPS;
- certificate is valid;
- HTTP redirects to HTTPS;
- no mixed content;
- sensitive forms are not submitted over HTTP;
- cookies have `Secure` flag where needed.

## Password Storage

Passwords should not be stored in plain text.

Usually a system stores a password hash, often with salt.

Correct idea:

```text
User password -> hash function -> stored hash
```

During login:

```text
Entered password -> hash function -> compare with stored hash
```

Check:

- password is not returned in API response;
- password is not visible in logs;
- reset flow does not send old password;
- database does not store plain text password;
- error messages do not reveal too much information.

## Tokens And Sessions

Web applications often use tokens or session cookies.

Cryptography may be used for:

- signing tokens;
- protecting session integrity;
- generating secure random values;
- validating expiration;
- preventing tampering.

Check:

- token expires;
- invalid token is rejected;
- modified token is rejected;
- logout invalidates session if expected;
- sensitive cookies use `HttpOnly`, `Secure`, `SameSite`.

## Data At Rest

Data at rest is data stored:

- in database;
- in files;
- in backups;
- in cloud storage;
- on user devices.

Sensitive data may require encryption at rest.

Examples:

- payment data;
- personal data;
- medical data;
- private documents;
- API keys.

QA angle:

QA may not test the encryption algorithm itself, but can test product behavior and exposure:

- sensitive data is not visible to extra users;
- exports do not expose secrets;
- backups are not publicly accessible;
- logs do not contain credentials.

## Cryptographic Attacks

## Brute Force Attack

A brute force attack tries possible passwords or keys.

Defenses:

- strong passwords;
- rate limiting;
- account lockout;
- MFA;
- slow password hashing algorithms.

QA checks:

- many failed logins are blocked or limited;
- system does not allow unlimited password guessing;
- error messages do not help the attacker.

## Dictionary Attack

A dictionary attack uses a list of common passwords or words.

QA checks:

- password policy blocks weak passwords;
- breached/common passwords can be rejected if the product supports it;
- rate limiting works.

## Man-In-The-Middle Risk

An attacker tries to stand between client and server.

TLS reduces this risk if certificate validation works correctly.

QA checks:

- no HTTP for sensitive actions;
- invalid certificate is not accepted silently;
- mobile apps use proper certificate validation.

## Side-Channel Attacks

Side-channel attacks use indirect information:

- timing;
- power usage;
- error differences;
- response patterns.

QA rarely tests this deeply, but can notice dangerous behavior:

- login error reveals whether email exists;
- reset flow leaks user existence;
- response time clearly differs for valid/invalid accounts.

## Advantages

Cryptography helps:

- protect confidentiality;
- preserve integrity;
- verify identity;
- support secure authentication;
- enable digital signatures;
- protect transactions;
- reduce impact of intercepted traffic;
- secure stored sensitive data.

## Limitations

Cryptography does not solve every security problem.

Limitations:

- weak keys break security;
- leaked private key compromises protection;
- wrong implementation can be dangerous;
- old algorithms become unsafe;
- encrypted data can still be deleted or corrupted;
- user devices can be compromised;
- logs and screenshots can leak data outside encryption.

Important:

> Strong encryption does not save a badly designed system.

## What QA Should Test

## Transport Security

Check:

- HTTPS is used on sensitive pages;
- certificate is valid;
- HTTP redirects to HTTPS;
- no mixed content;
- secure cookies are configured correctly.

## Sensitive Data Exposure

Check:

- passwords are not visible in API responses;
- tokens do not appear in URLs;
- secrets are not written to browser console;
- personal data is not visible to unauthorized users;
- logs do not contain credentials.

## Authentication And Session Security

Check:

- invalid credentials rejected;
- brute force protection exists;
- session expires;
- logout behavior correct;
- tampered token rejected;
- reset password flow safe.

## Integrity Checks

Check:

- modified signed payload rejected;
- file checksum mismatch detected if supported;
- webhook signature validation works;
- unsigned request rejected when signature required.

## Error Messages

Check:

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

This bug may look like a UI issue, but often it is session/security behavior.

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

Cryptography is a set of methods for protecting data using encryption, decryption, keys, hashes, and signatures.

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

QA should check expiration, rejection of modified tokens, logout behavior, cookie flags, and unauthorized access.

## What To Review Later

- HTTPS and TLS
- HTTP Cookies
- Authentication
- Authorization
- Session Management
- Password Reset Flow
- API Security Testing
- Webhook Signatures
