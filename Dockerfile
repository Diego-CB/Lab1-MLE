FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./input ./input
COPY ./main.py ./main.py

CMD [ "python", "./main.py" ]
