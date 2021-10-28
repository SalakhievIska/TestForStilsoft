<p align="center">
  <img src="https://github.com/SalakhievIska/TestForStilsoft/blob/dev/fronted/src/assets/logo.png" alt="Study" width="100" />
</p>

<h1 align="center">TestForStilsoft</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D" alt="VueJs">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
</p>

## Версия 0.1.1
+ Добавлена валиадция на бекенде
+ Удален bus из фронтед
+ Пагницаия происходит теперь на беке
+ Фильтр по строковым полям теперь по части слова, а не полное совпадение
+ Исправление багов и некоторые улучшения

## Технологии

Проект не подготовлен к production, использовать только локально

В проекте используются различные open-source технологии

- Vue.js
- Vuetify
- Axios
- lodash
- Django
- DRF

## Установка

### Fronted

```sh
cd fronted
npm i
npm run serve:open
```

### Backend

```sh
cd backend
python3 -m venv venv
```

##### Windows
```sh
venv/Scripts/activate.bat
```

##### Linux
```sh
source venv\bin\activate
```

```sh
pip install -U -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Веб-приложение готово и запущено!
