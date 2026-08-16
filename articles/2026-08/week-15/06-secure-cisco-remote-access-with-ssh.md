# Secure Cisco Remote Access With SSH

Source: закрытая страница курса  
Date added: 2026-08-16  
Related plan item: Week 15 / Secure Cisco remote access with SSH  
Tags: SSH, Telnet, remote access, VTY, RSA keys, login local, transport input ssh, Cisco IOS, management security
Language: Russian
Translation pair: articles-en/2026-08/week-15/06-secure-cisco-remote-access-with-ssh.md

## Кратко

- `Telnet` опасен, потому что передает login, password и commands открытым текстом.
- Риск особенно серьезен, если атакующий может перехватить traffic или выполнить man-in-the-middle.
- `SSH` шифрует management session и должен быть стандартом для Cisco devices.
- Для `SSH` нужны hostname, domain name, local user и RSA keys.
- `login local` заставляет VTY lines использовать local user database.
- `transport input ssh` закрывает Telnet и оставляет только SSH.
- Настройку нужно проверять: Telnet должен fail, SSH должен work.

## Главное

- "Telnet insecure" - правильная фраза, но важно понимать почему.
- Telnet не становится безопасным только потому, что его трудно перехватить в конкретной сети.
- Security audit почти всегда ожидает SSH-only management access.
- SSH требует cryptographic identity, поэтому настройка состоит из нескольких шагов.
- RSA keys завязаны на hostname и domain name.
- Если изменить hostname после генерации ключей, может понадобиться пересоздать keys.
- Shared line password хуже, чем username/password в local database.

## Заметки

`Telnet` часто описывают одной фразой: "он небезопасен". Это правда, но половина объяснения.

Опасность не в том, что весь internet автоматически видит твой password. Опасность в том, что Telnet отправляет данные в clear text. Если кто-то может захватить traffic между admin workstation и Cisco device, он может увидеть login information и commands.

Главная мысль:

```text
Telnet опасен не магически. Он опасен потому, что не шифрует management traffic.
```

В современной сети это неприемлемо как постоянная практика.

## Почему Telnet плох

Telnet передает открытым текстом:

- username;
- password;
- commands;
- command output;
- device prompts.

Атакующему нужен способ увидеть traffic:

- packet capture на твоем device;
- доступ к тому же сегменту;
- compromised switch или SPAN;
- man-in-the-middle;
- контроль части network path.

Если такой доступ есть, Telnet session становится читаемой.

Даже если в сети есть `DHCP Snooping`, `Dynamic ARP Inspection` и другие Layer 2 protections, это не делает Telnet acceptable. Эти защиты уменьшают риск отдельных атак, но не меняют факт: Telnet сам по себе не шифрует session.

## Почему SSH лучше

`SSH`, или `Secure Shell`, шифрует remote management session.

Когда admin вводит password или command, traffic не идет через сеть как readable text. Для packet sniffer это encrypted data.

Но SSH - это не одна команда "make secure".

Ему нужны:

- device identity;
- hostname;
- domain name;
- cryptographic keys;
- user credentials;
- VTY line configuration;
- allowed transport protocol.

Именно поэтому настройка SSH длиннее, чем включение Telnet.

## Общий порядок настройки

Типовой порядок:

1. Создать local username и secret.
2. Убедиться, что hostname настроен.
3. Настроить IP domain name.
4. Сгенерировать RSA keys.
5. Включить SSH version 2.
6. На VTY lines включить `login local`.
7. Ограничить remote access командой `transport input ssh`.
8. Проверить, что Telnet закрыт, а SSH работает.

Этот порядок важен. RSA keys строятся на identity устройства. Если hostname и domain name настроены неправильно, keys может понадобиться пересоздать.

## Базовая конфигурация

Пример:

```text
configure terminal

hostname R1
ip domain-name cafe.local

username admin secret StrongPasswordHere

crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4
 login local
 transport input ssh
end
```

Разбор:

| Команда | Что делает |
| --- | --- |
| `hostname R1` | Задает имя устройства. |
| `ip domain-name cafe.local` | Задает domain name для key generation. |
| `username admin secret ...` | Создает local user с защищенным secret. |
| `crypto key generate rsa modulus 2048` | Создает RSA keys для SSH. |
| `ip ssh version 2` | Включает SSHv2. |
| `login local` | Использует local user database на VTY lines. |
| `transport input ssh` | Разрешает только SSH для inbound VTY access. |

## Ключи RSA и идентичность устройства

SSH использует public/private key pair.

На Cisco device RSA keys создаются командой:

```text
crypto key generate rsa modulus 2048
```

Эти keys связаны с device identity, где важны hostname и domain name.

Поэтому плохой порядок выглядит так:

```text
crypto key generate rsa
hostname RealName
ip domain-name cafe.local
```

После такой перестановки можно оказаться в ситуации, где keys нужно regenerate.

Практичнее сначала настроить identity:

```text
hostname R1
ip domain-name cafe.local
```

И только потом генерировать keys.

## Линии VTY и login local

`VTY lines` - это virtual terminal lines для remote access.

С Telnet в старых или простых lab-настройках часто встречается line password:

```text
line vty 0 4
 password cisco
 login
```

Это shared password на line. Все используют один password, username не нужен.

Для SSH лучше:

```text
username admin secret StrongPasswordHere

line vty 0 4
 login local
```

`login local` означает, что device проверяет local user database. Поэтому при подключении появляется prompt для username и password.

Это лучше, чем общий line password, потому что появляется хотя бы базовая user identity.

Для больших сетей local users тоже не идеал. Там обычно приходят к `AAA`, centralized authentication и accounting. Но для CCNA и небольших lab локальная база - правильный старт.

## Команда, которая закрывает Telnet

Ключевая команда:

```text
transport input ssh
```

Она настраивается под VTY lines:

```text
line vty 0 4
 transport input ssh
```

Если просто настроить SSH, но оставить Telnet разрешенным, работа не закончена. Ты добавил secure option, но не убрал insecure option.

`transport input ssh` означает:

```text
Для remote access принимать только SSH.
```

После этого Telnet connection должна закрываться или отклоняться, а SSH connection должна проходить.

## Проверка

Полезные команды:

```text
show ip ssh
show running-config | section line vty
show running-config | include username|ip domain-name|hostname
show crypto key mypubkey rsa
```

Проверка с client side:

```text
telnet 192.168.10.1
ssh -l admin 192.168.10.1
```

Что подтвердить:

- SSH version 2 включен;
- RSA keys существуют;
- local username создан;
- VTY lines используют `login local`;
- VTY lines разрешают только `transport input ssh`;
- Telnet больше не работает;
- SSH принимает username/password.

## Сценарий NetworkChuck Coffee

В NetworkChuck Coffee router и switches держат сеть кафе.

Admin traffic не должен идти открытым текстом. Если кто-то сможет перехватить management session, он не должен получить password и commands в readable form.

Минимальная политика:

- Telnet disabled;
- SSH version 2 enabled;
- local admin user with secret;
- RSA keys generated with adequate modulus;
- VTY restricted to SSH;
- management access documented;
- позже - centralized AAA.

Так remote management становится не просто удобным, а защищенным на базовом уровне.

## Практические замечания

SSH - это стандарт, но не единственная мера.

Дополнительно стоит думать о:

- management VLAN;
- access-class на VTY;
- strong secrets;
- AAA;
- logging;
- role-based access;
- disabling unused services;
- secure out-of-band access;
- documentation.

Но первый шаг простой: не оставлять Telnet открытым.

## Главный вывод

Telnet дает remote management, но делает это открытым текстом. Это неприемлемо для современной сети.

SSH шифрует management session, но требует правильной основы: hostname, domain name, RSA keys, local user, `login local` и `transport input ssh`.

Главное не просто "включить SSH", а закрыть Telnet и проверить результат. Только тогда remote management переходит из "доступ есть" в "доступ защищен".

## Команды и термины

| Термин | Значение |
| --- | --- |
| `Telnet` | Старый протокол remote access без шифрования. |
| `SSH` | Secure Shell, зашифрованный remote access. |
| clear text | Данные, читаемые без расшифровки. |
| `VTY lines` | Virtual terminal lines для удаленных подключений. |
| `username ... secret` | Создает local user с защищенным secret. |
| `ip domain-name` | Domain name, нужный для SSH key generation. |
| `crypto key generate rsa` | Создает RSA keys. |
| `ip ssh version 2` | Включает SSH version 2. |
| `login local` | Использует local user database для login. |
| `transport input ssh` | Разрешает только SSH на VTY lines. |
| `AAA` | Authentication, Authorization, Accounting. |

## Вопросы

### 1. Почему Telnet небезопасен?

Ответ: Он передает login information и commands открытым текстом.

### 2. Что делает SSH лучше Telnet?

Ответ: SSH шифрует remote management session.

### 3. Зачем нужны hostname и domain name перед RSA keys?

Ответ: Они участвуют в identity устройства, на основе которой создаются SSH keys.

### 4. Что делает `login local`?

Ответ: Заставляет VTY lines проверять username/password в local user database.

### 5. Какая команда закрывает Telnet на VTY lines?

Ответ: `transport input ssh`.

## Что повторить позже

- Полный порядок настройки SSH.
- Разницу между line password и `login local`.
- `crypto key generate rsa modulus 2048`.
- `ip ssh version 2`.
- `transport input ssh`.
- Проверку Telnet fail и SSH success.
