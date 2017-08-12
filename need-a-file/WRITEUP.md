# Need a file: Write-up

На открытом сайте ничего нет. Даже если мы попробуем другие методы, всякие URL,
заголовки и прочее. Что ж, попробуем другой порт. Для поиска портов используем
всем известную утилиту `nmap` ([download](https://nmap.org/download.html)).

Попробуем сначала узнать, вдруг искомый порт очень известен: сделаем быструю
проверку:

```
$ nmap 47.91.94.243
Starting Nmap 7.12 ( https://nmap.org ) at 2017-08-07 22:29 +05
Nmap scan report for 47.91.94.243
Host is up (0.12s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 8.80 seconds
```

Понятно, что порт 22 — SSH-порт для управления сервером, значит, ничего полезного
мы не нашли.

Что ж, осталось лишь запустить полный перебор (`-sS` — пробуем на каждый порт
делать TCP Connect, `-p1-65535` — порты с 1 по 65535):

```
# nmap -sS -p1-65535 47.91.94.243
```

Ждём примерно бесконечность и узнаём наличие сервисов на портах 31338 и 41337.
Снова запустим `nmap`, чтобы узнать тип сервиса на этих портах (`-A` — подробная
информация о порту, `-p31338,41337` — список портов):

```
# nmap -A -p31338,41337 47.91.94.243
Starting Nmap 7.12 ( https://nmap.org ) at 2017-08-07 22:34 +05
Nmap scan report for 47.91.94.243
Host is up (0.071s latency).
PORT      STATE SERVICE VERSION
31338/tcp open  http    Apache httpd 2.4.18
| http-ls: Volume /
| SIZE  TIME              FILENAME
| 572   2017-08-08 13:03  app.py
| 12    2017-08-08 11:57  flag.txt
|_
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Index of /
41337/tcp open  http    Apache httpd 2.4.18
| http-ls: Volume /
| SIZE  TIME              FILENAME
| 572   2017-08-08 13:03  app.py
| 12    2017-08-08 11:57  flag.txt
|_
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Index of /

...
```

На обоих портах обычные HTTP-сервера, на которых, по всей видимости, открыт
листинг одной и той же директории.

По названию `app.py` похоже, что это исходный код скрипта на порту 31337.

Смотрим в исходный код `app.py`. Видим `bcrypt`-хеш. Единственная возможность
получить строку, которая была захеширована — перебрать исходную строку.

Возьмем список из очень популярных паролей и проверим каждый функцией `checkpw`.
Подойдет `qwertyuiop`.

Наконец, получаем файл `flag`. Определяем по первым байтам, что это JPEG-картинка.

Флаг: **uctf_you_hacked_the_world**
