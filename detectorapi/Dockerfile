FROM python:3.7
WORKDIR /code

EXPOSE 8000

COPY . /code

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

