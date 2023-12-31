# Scrapy parser PEP Document's

## Цель
Данный проект является учебным и создан в рамках обучения на курсе Python-Backend.
Работа с фреймворком Scrapy.

## Описание
Проект предназначен для сбора информации о документах PEP:
 - Номер
 - Наименование
 - Статус
 - Количество

## Используемые Технологии
- Python
- Scrapy

## Как запустить проект
- Клонировать репозиторий
```
git clone git@github.com:Comsomolec/scrapy_parser_pep.git
```
- Перейти в директорию с проектом
- Установить и активировать виртуальное окружение 

```
python -m venv venv
```

Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

Если у вас windows

    ```
    source venv/scripts/activate
    ```
- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
## Как запустить и работать с парсингом
- Перейти в директорию /pep_parse 
- Запустить парсер
```
scrapy crawl pep
```

## Вывод данных:
С корневой директории перейти в /results
- Файл pep_Дата.csv. Хранит в себе список документов PEP с указанием номера документа и его наименование.
- Файл status_summary_Дата.csv. Хранит в себе список текущих статусов документов PEP и их количество.

## Автор
<a href="https://github.com/Comsomolec" target="_blank">Сабирзянов_Сергей</a>