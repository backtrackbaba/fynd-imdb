# Fynd IMDB
### A simple Django based RESTful API application similar to IMDB


## Tech Stack

<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>PostgreSQL</td>
    <td>Django Rest Framework</td>
    <td>Gunicorn</td>
    <td>Nginx</td>
    <td>DigitalOcean</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://cdn.svgporn.com/logos/python.svg" width="100" height="100"/></td>
    <td valign="top"><img src="https://cdn.svgporn.com/logos/django.svg" width="100" height="100"/></td>
    <td valign="top"><img src="https://cdn.svgporn.com/logos/postgresql.svg" width="100" height="100"/></td>
    <td valign="top"><img src="https://www.django-rest-framework.org/img/logo.png" width="200" height="100"/></td>
    <td valign="top"><img src="https://cdn.svgporn.com/logos/gunicorn.svg" width="100" height="100"/></td>
    <td valign="top"><img src="https://cdn.svgporn.com/logos/nginx.svg" width="100" height="100"/></td>
    <td valign="top"><img src="https://cdn.svgporn.com/logos/digital-ocean.svg" width="100" height="100"/></td>
  </tr>
 </table>


## Local Installation

1) Clone the application by running `git clone https://github.com/backtrackbaba/fynd-imdb.git`

2) Go to the clone repository and create a `.env` file to house all the environment variables. Refer to 
[this](https://github.com/backtrackbaba/fynd-imdb-devops/blob/master/environments/.env) file in the `fynd-imdb-devops`
repo to get the required variables.

3) Install all the Python dependencies by running `pip install -r requirements.txt` from the root of the repo. Please 
use an appropriate virtual env to keep the dependencies isolated across projects.

4) `cd` into the `src` folder and type in `python manage.py migrate` to create the required the database tables.

5) Once the tables are created type in `python manage.py seed_db` to seed the database with the initial data.

6) Now that the data is loaded, you can simply run the application by typing in `python manage.py runserver` and then 
navigate to [`http://localhost:8000`](http://localhost:8000) to check out the application.

7) If you wish to edit any data, you'll need to have an admin access. To do that, you could create a superuser by 
typing is `python manage.py createsuperuser` and typing in the asked data. Once it's created you can access the admin 
dashboard [here](http://localhost:8000/admin)

---  