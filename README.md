# Описание

Форматы и плагины для просмотра файлов игры Приключения Капитана Блада. Описание форматов в шаблонах .bt для программы 010Editor.

**Ссылки**

Исходный код игры Приключения Капитана Блада https://github.com/storm-devs/captain-blood

## Форматы

 № | Формат файла       | Шаблон (010Editor)     |    Описание |
| :--- | :--------- | :----------- | :---------- |
| 1 | .pkx        | [PKX.bt](formats/010editor/PKX.bt)        |   архив игровых ресурсов  |
| 2 | .txx       | [TXX.bt](formats/010editor/TXX.bt)        |  текстуры |

    Как использовать шаблоны  010Editor
    0. Установить 010Editor.
    1. Открыть нужный файл игры.
    2. Применить шаблон через меню Templates-Run template.   
    
##  Инструменты

| № | Плагин       | Программа | Описание |  
| :--- | :--------- | :----------- | :---- | 
| 1 | [fmt_cb_txx.py](https://github.com/AlexKimov/cb-file-formats/tree/master/plugins/noesis/fmt_cb_txx.py) | Noesis  | Просмотр текстур .txx |
| 1 | [unpack_pkx.bms](https://github.com/AlexKimov/cb-file-formats/blob/master/scripts/unpack_pkx.bms) | Quickbms | Распаковка файлов ресурсов .pkx  |
    Как просмотреть текстуры
    1. Скачать Noesis https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91 .
    2. Скопировать скрипт в папку ПапкасNoesis/plugins/python.
    3. Открыть Noesis.
    4. Открыть файл текстур игры. 
    
    Как распаковать файлы игры
    1. Нужен quickbms https://aluigi.altervista.org/quickbms.htm
    2. Для запуска в репозитории лежит bat файл с настройками, нужно открыть его и задать свои пути: до места, где находится quickbms, папки с игрой и места куда нужно сохранить результат.
    3. Запустить процесс через bat файл или вручную (задав свои параметры для запуска quickbms, документация на английском есть здесь https://aluigi.altervista.org/papers/quickbms.txt ). 
    4. В итоге строка в файле будет выглядеть так:
       ПутькQuickbms\quickbms.exe -K -d -e -Y -F "*.pkx" unpack_pkx.bms "F:\git\cb\data" unpacked
       -K -d -e -Y -F - параметры распаковки, есть в документации на quickbms
       "*.pkx" - формат файлов архивов игры, которые нужно распаковать
       ПутькQuickbms\quickbms.exe - место, где находится программа
       unpack_pkx.bms - название файла скрипта распаковки, должен быть
       "F:\git\cb\data" - папка с файлами игры
       unpacked - папка в которую нужно все распаковать
