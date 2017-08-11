# Deployment

Установите Python 3.4+ и библиотеку `bcrypt` версии 3.1+.

Поднимите Apache с включенным `mod_wsgi` (Python 3). Добавьте сайт с конфигом
`site.conf`, где `#APP_DIR#` — директория, где лежит `app.py` и `flag.txt`.
Скопируйте `tmp-flag` в `/tmp/flag` (для `Windows` — в `C:\flag`, но тогда
в строке 18 замените `/tmp` на `C:/`).
