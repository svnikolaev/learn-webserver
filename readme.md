# how to run the app

powershell run:
($env:FLASK_APP="webapp") -and ($env:FLASK_ENV="development") -and ($env:FLASK_DEBUG=1) -and (flask run)
