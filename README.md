# Pizza App Installation
Clone Repo
 - git clone https://github.com/raphaeltorres/pizzaapp.git

 Create virtualenv
 - virtualenv -p python3 pizzaapp

 Activate virtualenv
 - source pizzaapp/bin/activate

 Install django
 - pip install -r requirements.txt
 - python manage.py migrate
 - python manage.py runserver

 Commands

 Create pizza - python manage.py pizza

 Sell pizza - python manage.py pizza_transaction

 Pizza List

 http://localhost:8000/
