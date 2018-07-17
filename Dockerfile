FROM python:3.7.0-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /code/
WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000"]


