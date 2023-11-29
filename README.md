### Create .env file and fill it with data further:
```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

### Run docker compose:
```shell
docker compose up
```

### Go into container:
```shell
docker exec -it pseudo-roulette sh
```

### Create superuser and execute the further steps:
```shell
python manage.py createsuperuser
```

### Fill the database with ten cell values in order:
```shell
python manage.py shell
from pseudo_roulette.models import Cell
Cell.objects.create(cell_value=1, weight=20)
Cell.objects.create(cell_value=2, weight=100)
Cell.objects.create(cell_value=3, weight=45)
Cell.objects.create(cell_value=4, weight=70)
Cell.objects.create(cell_value=5, weight=15)
Cell.objects.create(cell_value=6, weight=140)
Cell.objects.create(cell_value=7, weight=20)
Cell.objects.create(cell_value=8, weight=20)
Cell.objects.create(cell_value=9, weight=140)
Cell.objects.create(cell_value=10, weight=45)
exit()
exit
```
