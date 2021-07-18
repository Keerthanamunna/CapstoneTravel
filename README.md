# Capstone project for Full Stack Nanodegree

# Travel Diaries API
# Introduction
The Travel Diaries is an idea where the travellers can upload their trip details or memories in the tables. One is Venue details and the other is the travellers details.
There are three differents users roles (and related permissions), Which are:

- Viewer
    - Can view venues and travellers details
- Co Admin
    - All permissions a Viewer has and...
    - Add or delete an Traveller from the database
    - Modify travellers or venues
- Admin
    - All permissions a Co Admin has and
    - Add or delete a venue from the database

# Motivation
- I got this idea so that the knowledge gained from all the projects can be applied here and I tried to build it using all the skills I learned from this course. 


While running locally: http://localhost:5000
## Getting Started

### Installing Dependencies

#### Python 3.8.5

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Create and activate the virtual environment
```
python3 -m venv env
source env/bin/activate
```
#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```
pip install -r requirements.txt
```

## Running the server
First always create a virtual env and activate it
'''
python -m virtualenv env
source env/bin/activate
'''
Install the dependencies:
```
pip install -r requirements.txt
```
We need to cretae the database in postgres
```
DROP DATABASE capstone;
CREATE DATABASE capstone;
```
Each time you open a new terminal session, run setup.sh or below
```
source setup.sh
```
Or else run the below 
```
export DATABASE_URL=postgres://lefhzcctthxtje:1ea8a85ae1e29e19f67f3aab242aa47607888834d86dfbd8e47736049f453960@ec2-3-231-69-204.compute-1.amazonaws.com:5432/das47c7c1fgqn8
export DATABASE_URL=postgresql://postgres:root@localhost:5432/capstone
```
```
export FLASK_APP=app.py
export AUTH0_DOMAIN='kittu-fsnd.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='travel'
export CLIENT_ID='VdqHlVe9I4vPlLZijNZP6uNVwBJpZGe5'

pip install -r requirements.txt

```

To run the server, execute:

```
export FLASK_APP=app
export FLASK_ENV=development # enables debug mode
python3 app.py
or 
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

This will install all of the required packages we selected within the `requirements.txt` file.
# Error Handling
Errors due to RBAC are returned.
Errors are returned in the following format:

```
{
    "error": 404,
    "message": "resource not found",
    "success": false
}

{
  "success": "False",
  "error": 422,
  "message": "Unprocessable entity"
}
```
The API will return the following errors based on how the request fails:
    - 400: Bad Request
    - 422: Unprocessable Entity
    - 500: Internal Server Error
    - 401: Unauthorized
    - 403: Forbidden
    - 404: Not Found
    - 405: Method Not Allowed

# Endpoints

#### GET /

- General
    - root endpoint
    - requires no authentication
- Sample Request
    - `http://127.0.0.1:5000/`

- Sample Response

```
{
  "message": "done the FSND!!", 
  "success": true
}
```


#### GET /venues

- General
    - Get all the venues
    - requires `get:venues` permission

- Sample Request
    - `http://127.0.0.1:5000/venues`

- Sample Response

```
{
  "success": true, 
  "venues": [
    {
      "duration": 4, 
      "id": 1, 
      "visit_year": 2005, 
      "vname": "Boston 3"
    }, 
    {
      "duration": 2, 
      "id": 2, 
      "visit_year": 1998, 
      "vname": "Connecticut"
    }, 
    {
      "duration": 3, 
      "id": 3, 
      "visit_year": 2012, 
      "vname": "Newyork 1"
    }, 
    {
      "duration": 2, 
      "id": 4, 
      "visit_year": 2015, 
      "vname": "Newjersey 2"
    }, 
    {
      "duration": 2, 
      "id": 5, 
      "visit_year": 1976, 
      "vname": "Island I"
    }, 
    {
      "duration": 2, 
      "id": 6, 
      "visit_year": 2018, 
      "vname": "Paris"
    }, 
    {
      "duration": 2, 
      "id": 7, 
      "visit_year": 1976, 
      "vname": "Honkong"
    }
  ]
}
```

#### GET /venue/{venue_id}

- General
    - Gets an specific actor
    - requires `get:venues-info` permission

- Sample Request
    - `http://127.0.0.1:5000/venues/1`

- Sample Response


```
{
  "success": true, 
  "venue": {
    "duration": 4, 
    "id": 1, 
    "visit_year": 2005, 
    "vname": "Boston 3"
  }
}

```

#### POST /venues
- General
    - Creates a new Venue
    - Requires `post:venue` permission
- Sample Request
    - `http://127.0.0.1:5000/venues`
    - Request Body
    ```
    {
      "duration": 3, 
      "id": 6, 
      "visit_year": 2010, 
      "vname": "japan"
    },
    ```
- Sample Response

```json
{
    "created_venue": "japan",
    "success": true,
    "total_venues": 12
}  
```

#### PATCH /venues/{venue_id}

- General
    - Updates the information for a venue
    - requires `patch:venues` permission

- Sample Request
    - `http://127.0.0.1:5000/venues/2`
    
    ```
        {
  "success": true, 
  "venue": {
    "duration": 2, 
    "id": 2, 
    "visit_year": 1998, 
    "vname": "Connecticut"
  }
}
    ```

- Sample Response

```
{
    "patched_venue": 2,
    "success": true,
    "total_venues": 7
}
```

#### DELETE /venues/{venue_id}

 - General
   - deletes the venue
   - requires `delete:venues` permission
 
 - Sample Request
   - `http://127.0.0.1:5000/venues/6`

 - Sample Response

```
{    
    "deleted": 6,
    "success": true,
    "total_venues": 6
}
```


#### GET /travellers

- General
    - Gets the list of all travellers
    - Requires `get:travellers` permission

- Sample Request
    - `http://127.0.0.1:5000/travellers`

- Sample Response

```json
{
  "success": true, 
  "travellers": [
    {
      "gender": "male", 
      "id": 1, 
      "name": "Tommy", 
      "start": "Tue, 11 Feb 2020 18:49:18 GMT"
    }, 
    {
      "gender": "male", 
      "id": 2, 
      "name": "Rani", 
      "start": "Wed, 07 Apr 2021 19:26:34 GMT"
    }, 
    {
      "gender": "female", 
      "id": 3, 
      "name": "Rachel", 
      "start": "Mon, 31 May 2021 18:50:05 GMT"
    }, 
    {
      "gender": "male", 
      "id": 4, 
      "name": "Willi", 
      "start": "Sun, 04 Mar 2001 18:50:22 GMT"
    }, 
    {
      "gender": "female", 
      "id": 5, 
      "name": "Megana", 
      "start": "Mon, 18 Jan 2010 18:49:54 GMT"
    }, 
    {
      "gender": "male", 
      "id": 6, 
      "name": "Evans", 
      "start": "Tue, 18 Mar 2014 19:34:32 GMT"
    }, 
    {
      "gender": "male", 
      "id": 7, 
      "name": "Dolly", 
      "start": "Thu, 18 Mar 2021 19:34:49 GMT"
    }, 
    {
      "gender": "female", 
      "id": 8, 
      "name": "Jenni ", 
      "start": "Thu, 12 Jun 2014 19:35:08 GMT"
    }, 
    {
      "gender": "female", 
      "id": 9, 
      "name": "Rohini", 
      "start": "Tue, 10 Feb 2015 19:35:20 GMT"
    }, 
    {
      "gender": "male", 
      "id": 11, 
      "name": "Chris", 
      "start": "Sun, 23 Feb 2003 19:39:27 GMT"
    }
  ]
}
```
#### GET /travellers/{traveller_id}

- General
   - gets the information for a traveller
   - requires `get:travellers-info` permission
 
- Sample Request
   - `http://127.0.0.1:5000/travellers/2`

- Sample Response
```json
{
  "success": true, 
  "traveller": {
    "gender": "male", 
    "id": 2, 
    "name": "Rani", 
    "start": "Wed, 07 Apr 2021 19:26:34 GMT"
  }
}
```


#### POST /travellers
- General
    - creates a new traveller
    - requires `post:travellers` permission
 
- Sample Request
    - `http://127.0.0.1:5000/travellers`
     ```
        {
  "success": true, 
  "traveller": {
    "gender": "female", 
    "id": 10, 
    "name": "Subhash", 
    "start": "Sat, 09 Mar 2002 19:35:49 GMT"
  }
}
     ```

- Sample Response

```json
{
    "created_traveller": 11,
    "success": true,
    "total_travellers": 12
}
```


#### PATCH /traveller/{traveller_id}
 - General
   - updates the information for a traveller
   - requires `patch:travellers` permission
 
 - Sample Request
   - `http://127.0.0.1:5000/travellers/9`
   - Request Body
     ```
       {
  "success": true, 
  "traveller": {
    "gender": "female", 
    "id": 9, 
    "name": "Rohini", 
    "start": "Tue, 10 Feb 2015 19:35:20 GMT"
  }
}
     ```


```json
{
    "success": true,
    "total_travellers": 12,
    "updated_traveller": 9
}
```
  

#### DELETE /travellers/{traveller_id}
 - General
   - deletes the traveller with a given id
   - requires `delete:travellers` permission
 
 - Sample Request
   - `http://127.0.0.1:5000/travellers/9`


```json
{
    "deleted": 9,
    "success": true,
    "total_travellers": 11
}
```

# Deploy to heroku
-- heroku create name_of_your_app
-- git remote add heroku heroku_git_url
-- heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
-- heroku config --app name_of_your_application
-- Added all the required environment variables for the project
-- git push heroku master
Heroku Link for this is : https://traveldiarie.herokuapp.com/

## Testing
For testing the backend, run the following commands (in the exact order):
```
dropdb capstone
createdb capstone
psql capstone < capstone.sql
python test_app.py
```