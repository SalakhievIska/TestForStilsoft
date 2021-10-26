# TestForStilsoft

## Технологии

Проект не подготовлен к production, использовать только локально

В проекте используются различные open-source технологии

- Vue.js
- Vuetify
- Axioes
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
