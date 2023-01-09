# шев
Телеграм-бот, который генерирует безумные рецепты с помощью нейронной сети. Написан на Python с использованием aiogram и RabbitMQ  

### Пример работы
![alt text](/example.png)

### Структура
Нейронная сеть -- finetune ruGPT3Small. [Датасет](/dataset/recipes.txt). [Парсер](/train/parser2.py). [JupyterNotebook](/train/notebook.ipynb)  
[Скрипт](/model/model.py), генерирующий рецепты  
[Телеграм-бот](/tgbot/bot.py)  

### Архитектура
![alt text](/Diagram.jpg)
