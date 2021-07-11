[![Foodgram workflow](https://github.com/TizJourney/foodgram-project-react/actions/workflows/foodgram_workflow.yaml/badge.svg)](https://github.com/TizJourney/foodgram-project-react/actions/workflows/foodgram_workflow.yaml)

# foodgram проект
* Адрес проекта: http://www.tiz-foodgram.ml/

# Сайт для работы с рецептами
Сайт содержит фукнкциональность для сохранения рецептов. 
Предназначен для работы с множеством пользователей.

## Функциональность
* Веб-интерфейс для работы с рецептами: создание, листинг, детальная информация рецептов
* Работа с большим количеством пользователей. Поддерживается регистрация новых пользователей, смена и сброс пароля, работа за логином
* Есть backend-часть, которая включает в себя базу данных для хрананения информации о пользователях, рецептах и так далее.

### Технологии
* Django: основной python framework, на основе которого сделан api
* Frontend: HTML, JavaScript, CSS

## Локальная версия
### Инструация по запуску локальной версии
* Ставим виртуальное окружение: `python -m venv venv`
* Ставим пакеты `pip install -r requirements_dev.txt`
* Создать базу данных: `python manage.py makemigrations` и `python manage.py migrate`
* Создать супер пользователя: `python manage.py createsuperuser`
* Запустить `fill_ingridients.sh` для загрузки в базу данных начального набора ингридиентов
* Создать наборы фильтров при помощи команды `python manage.py init_tags`
* Использовать скрипт для запуска локальной версии `run_local.sh`

### Локальная версия
* Локальная версия доступа по адресу: http://127.0.0.1:8000/
* Админка приложения: http://127.0.0.1:8000/admin
* Посылка почты происходит в файлы `sent_emails`
* Загруженные изображения складываются в папку: `media`
* База данных находится в файле: `db.sqlite3`

## Облачная версия
### Инструация по запуску облачной версии
* Зайти на продакшен машину 
* Перейти в папку конфигов: `cd ~/foodgram`
* Инициация базы данных: `sudo docker-compose exec web python manage.py migrate --noinput`
* Создать администратора: `sudo docker-compose exec web python manage.py createsuperuser`
* Загрузить ингредиенты в базу: `sudo docker-compose exec web python manage.py fill_ings ingredients.json`
* Создать фильтры: `sudo docker-compose exec web python manage.py init_tags`


### Устройство проекта
Логически проект разбит на 4 приложения: 
* основной: foodgram. здесь находится основной управлящий код для запуска, настройки и так далее
* users: приложения для работы с пользователем, авторизация и т.д.
* web: приложение для отрисовки web-интрфейса сайта
* api: здесь находятся endpoint'ы, на которые ходит сайт через JavaScript для получения информации на лету

### Настройки прокта
Настройки проекта состоят из 3х частей (находятся в приложении `foodgram`):
* `settings_common` - общая часть настроек
* `settings_local` - настройки для локального запуска, здесь включен режим debug'а
* `settings` - настройки для продакшен версии сайта

## License
[MIT](https://github.com/Factotum8/news_nmap/blob/master/LICENSE)

## Автор
Бондарь Константин. e-mail: kostya.bondar@gmail.com
