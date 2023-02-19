FROM python:3.8.3-slim
WORKDIR /app
COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2==2.8.6

COPY ./ /app
CMD ["gunicorn", "shop.wsgi:application", "--bind", "0:8000" ]

