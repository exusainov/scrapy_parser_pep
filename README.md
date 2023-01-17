# scrapy_parser_pep
Проект парсинга pep_parse собирает статусы pep выводит в csv Колонку Нормер, Название, Статус, а также делает подсчёт статусов и выводит в отдельный csv Колонку Статус и Количество.

### Как запустить проект:
​
Клонировать репозиторий и перейти в него в командной строке:
​
```
git clone git@github.com:exusainov/scrapy_parser_pep.git
​
cd scrapy_parser_pep
```
​
Cоздать и активировать виртуальное окружение:
​
```
python -m venv venv
​
source venv/Scripts/activate (source venv/bin/activate - для Mac)
```
​
Установить зависимости из файла requirements.txt:
​
```
python -m pip install --upgrade pip
​
pip install -r requirements.txt
```

Как запустить парсинг scrapy пример использования:

```
cd pep_parse

scrapy crawl pep
```
# Технологии
​
Python3, HTTP, Scrapy
​
​
# Автор
​
- Хусаинов Евгений Маратович (Exusainov@yandex.com)
