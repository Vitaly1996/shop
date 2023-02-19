### Shop
### Описание
Данный сервис позволяет создавать платежные формы для товаров с помощью библиотеки Stripe. 


### Технологии
- Python 3.10
- Django 3.0
- Stripe 5.1.1
- Docker 23.0.1
- Postgres
- Timeweb Cloud



### Особенности
- использована технология webhook для подтверждения выполнения успешной оплаты;
- реализована Django Admin панель для просмотре моделей;
- для загрузки проекта применен Docker и docker-compose, подготовлены файлы для развертывания инфраструктуры;

### Установка
- склонировать репозиторий
```sh
git clone github.com/Vitaly1996/shop.git
```
- в директории shop/infra/ создаем файл .env и записываем в него следующие переменные окружения:     
  DB_ENGINE=django.db.backends.postgresql     
  DB_NAME=<имя базы данных>     
  POSTGRES_USER=<ваш_логин для подключения к базе данных>     
  POSTGRES_PASSWORD=<ваш_пароль для подключения к базе данных>     
  DB_HOST=<название сервиса(контейнера)>    
  DB_PORT=<порт для подключения к базе данных>    
  ALLOWED_HOSTS=<список хостов, доступных сайту>
  STRIPE_PUBLIC_KEY= <ваш PUBLIC_KEY от аккаунта STRIPE>
  STRIPE_SECRET_KEY= <ваш SECRET_KEY от аккаунта STRIPE>
  STRIPE_WEBHOOK_SECRET= <ваш WEBHOOK_SECRET>
  SECRET_KEY= <ваш секретный ключ Django>
- в директории shop/infra/.env_exmp можно посмотреть пример заполнения переменных окружения  

- в директории shop/infra/ выполняем команду для сбори контейнеров
```sh
docker-compose up --build
```

- внутри собранных котейнеров создаем и выполняем миграции, создаем суперпользователя и собираем статику
```sh
docker-compose exec web python manage.py makemigrations 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

- проект будет доступен по адресу http://<IP вашей машины>/

### Доступные эндпоинты
- POST /buy/{id} - c помощью которого можно получить Stripe Session Id для оплаты выбранного Item;
- GET /item/{id} - c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy:
- GET /succes - с помощью которого переходим на страничку подтверждения в случае успешной оплаты;
- GET /cancel - с помошью которого переходим на страничку отмены в случае омены платежа;

Развурнутый проект можно посмотреть по адресу: http://90.156.229.65/item/1    
Номер карты для тестирования успешной оплаты: 4242 4242 4242 4242
