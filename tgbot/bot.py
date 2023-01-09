import random, pika, uuid

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

b1 = KeyboardButton('/Рецепт')
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(b1)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    # user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    # logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!", reply_markup=kb)

answer = ''
@dp.message_handler(commands=['Рецепт'])
async def start_handler(message: types.Message):
    letters = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    prompt = '<s>' + ''.join(random.choice(letters) for i in range(random.randint(2, 6))) + 'Название: '

    connection_parameters = pika.ConnectionParameters('rabbit')
    connection = pika.BlockingConnection(connection_parameters)

    def on_reply_message_received(ch, method, properties, body):
        ch.stop_consuming()
        body_str = body.decode("utf-8")
        print(f"Received: {body_str}")
        global answer
        answer = body_str
        print(f"Answer: {answer}")

    channel = connection.channel()
    reply_queue = channel.queue_declare(queue='', exclusive=True)
    channel.basic_consume(queue=reply_queue.method.queue,
                          on_message_callback=on_reply_message_received)
    channel.queue_declare(queue='request-queue')

    cor_id = str(uuid.uuid4())
    print(f"Sending Request: {prompt}")

    channel.basic_publish('', routing_key='request-queue', properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ), body=prompt)

    print("Starting Client")

    channel.start_consuming()
    global answer
    await message.answer(answer)

if __name__ == '__main__':
    executor.start_polling(dp)
