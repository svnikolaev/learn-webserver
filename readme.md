# how to run the app

## powershell run

`$env:FLASK_APP="webapp"; $env:FLASK_ENV="development"; $env:FLASK_DEBUG=1; flask run`

## make migrations

### create migrations folder

`$env:FLASK_APP="webapp"; flask db init`

### make migration

`$env:FLASK_APP="webapp"; flask db migrate -m "users and news tables"`

if FLASK_APP enviromental variable already exists, then just

`flask db migrate -m "comment"`

### make upgrade

`flask db upgrade`

### usefull commands

```sh
alembic stamp head
flask db stamp head
flask db current
flask db migrate
flask db upgrade
```
