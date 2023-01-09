FROM python:3.10

RUN mkdir -p /home/user/oop_docker/tgbot/
WORKDIR /home/user/oop_docker/tgbot/

COPY . /home/user/oop_docker/tgbot/
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]