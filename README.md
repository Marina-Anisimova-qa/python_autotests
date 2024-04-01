# python_autotests
Пример автотестов на pytest + requests

Автотесты для сайта https://pokemonbattle.me на Python версии не ниже 3.7. Используемые библиотеки Requests и Pytest.
Для запуска установить Visual Studio Code, Python, далее установить расширение Python в VC Сode.
Для установки библиотек нужно открыть терминал VS Code и выполнить команду pip install название_библиотеки
В папке test_pokemons сожержатся:
- файл main.py  - содержит проверки  на создание покемона, смену имени покемона, поймать покемона в покебол
- папка test_pokemons с файлом test_pokemon_MA - содержит проверки 1) что ответ запрос GET /trainers приходит с кодом 200, 2) что в ответе приходит строчка с именем тренера
