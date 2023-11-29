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
for i in range(10):
    Cell.objects.create(user=User.objects.last(), cell_value=i)
exit
```
