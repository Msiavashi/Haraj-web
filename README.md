# Haraj-web

### How to contribute:

1. git clone <project-url>

2. git branch branch_name

3. // do your stuff

4. git add

5. git commit -m 'provide an expressive message'

6. git push

7. // send a new PR from branch_name to master

8. // don't merge your own PR!

### How to Setup Database

1. go to haraj directory
2. pip install mysqlclient

run the commands in order:

3. python manage.py makemigrations
4. python manage.py sqlmigrate blogsite 0001_initial
5. python manage.py migrate

## NOTE: change your database username and password if yours in differenct, in settings.py
