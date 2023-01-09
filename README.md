# шев
Телеграм-бот, который генерирует безумные рецепты с помощью нейронной сети. Написан на Python с использованием aiogram и RabbitMQ  

### Структура
Нейронная сеть - Предобученная ruGPT3Small, с помощью [датасета](/dataset/recipes.txt). [Парсер](/train/parser2.py). [JupyterNotebook](/train/notebook.ipynb)  
[Скрипт](/model/model.py), генерирующий рецепты  
[Телеграм-бот](/tgbot/bot.py)  

### Архитектура
![alt text](/Diagram.jpg)
