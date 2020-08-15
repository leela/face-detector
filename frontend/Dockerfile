FROM python:3.7
WORKDIR /code

ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

COPY . /code

RUN pip install -r requirements.txt

CMD ["flask", "run"]
