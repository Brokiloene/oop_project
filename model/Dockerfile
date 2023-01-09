FROM python:3.10

RUN mkdir -p /home/user/oop_docker/model/
WORKDIR /home/user/oop_docker/model/

COPY . /home/user/oop_docker/model/
RUN pip3 --default-timeout=1000 install -r requirements.txt

CMD ["python3", "model.py"]