# totalifetakehome

This is an patient appointment management system.

## To run and build

To run the system you must have Python 3 with pip installed onto your system along with Node JS. After cloning the repository, a virtual environment will be used to manage python dependencies. Check if you have virtualenv using `python3 -m virtualenv --help` and install via `python3 -m pip install --user virtualenv`.

Create the virtual environment via these commands:
```
python3 -m virtualenv venv # creates the virtualenv folder names venv
source venv/bin/activate
```

Run the command `pip install -r requirements.txt` at the top level of the directory to install python dependencies.

Follow these steps to install all Node dependencies and build the frontend static files:

```
cd frontend/
npm install
npm run build
```

Navigate to the backend to set up the database/superuser(check this again pls):

```
cd backend/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # create the admin account with a username/password
```

Then to run the server use `python3 manage.py runserver` and navigate to http://127.0.0.1:8000/ to see the app work!