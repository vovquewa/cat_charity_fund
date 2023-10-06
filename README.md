# QRKot
API Приложение для Благотворительного фонда поддержки котиков.

## Описание
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии
    - Python 3.10
    - FastAPI
    - Alembic
    - Uvicorn

## Запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:vovquewa/cat_charity_fund.git
```
```bash
cd cat_charity_fund
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
```
* Если у вас Linux/macOS
```bash
source venv/bin/activate
```
* Если у вас windows
```bash
source venv/scripts/activate
```
3. Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
4. Подготовить базу данных:
```bash
alembic upgrade head
```
5. Запустить проект:
```bash
uvicorn app.main:app --reload
```

## Документация API
[REDOC](http://127.0.0.1:8000/redoc)
[SWAGGER](http://127.0.0.1:8000/docs)

## Справка
```bash
uvicorn app.main:app --help
```

## Автор
[Владимир Козлов](https://github.com/vovquewa/)
