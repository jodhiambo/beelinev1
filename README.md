# challengegov
### Create a virtual environment in a terminal
  $> virtualenv venv

### Activate the virtual environment
  $> source venv/bin/activate

### Install the dependencies
  $> pip install -r requirements.txt

### Make the migrations
  $> python manage.py makemigrations

### Migrate them to the database
  $> python manage.py migrate

### Run Collectstatic
  $> python manage.py collectstatic

### Create superuser
  $> python manage.py createsuperuser

### Run the server and open it at http://localhost:8000 or http://127.0.0.1:8000
  $> python manage.py runserver
