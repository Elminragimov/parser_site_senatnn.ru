# parser_site_senatnn.ru
Parser_senat.py 
* Парсит каталог изделий 'Кольца' с сайта senatnn.ru

Используются  библиотеки requests и BeautifulSoup
____

senat2.ipynb

* Читает получившийся csv файл 
* Выявляет минимальную и максимальную цену для каждой категории товаров. Под категорией понимаем всё, 
что идёт до запятой в названии ("Помолвочное кольцо", "Брошь", и тд)
* Сохраняет получивщиеся в файл csv
* Находит Топ 10 товаров в самым большим процентом скидки
* Сохраняет получивщийся результат в отдельный  файл csv

Используется  библиотека Pyspark
