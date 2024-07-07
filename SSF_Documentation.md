# SSF_app Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)

    - [Details](#project-structure-details)
3. [Installation](#installation)
4. [Troubleshooting](#troubleshooting)
5. [API Documentation](#api-documentation)
    - [Community API](#community-api)
    - [Competition API](#competition-api)
    - [Scoring API](#scoring-api)
    - [Serie API](#serie-api)
6. [Views and Viewsets](#views-and-viewsets)
   - [Home Views](#home-views)
     - [community_home_view](#community_home_view)
     - [competition_home_view](#competition_home_view)
     - [scoring_home_view](#scoring_home_view)
     - [serie_home_view](#serie_home_view)
   - [API Viewsets](#api-viewsets)
     - [Community Viewsets](#community-api-viewsets)
     - [Competition Viewsets](#competition-api-viewsets)
     - [Scoring Viewsets](#scoring-api-viewsets)
     - [Serie Viewsets](#serie-api-viewsets)
    - [Miscellaneous Viewsets](#miscellaneous-viewsets)
7. [Business Logic](#business-logic)
    - [utils.py](#utilities)
    - [prel_results.py](#prel_results.py)
    - [insert_competitors.py](#insert_competitors)
8. [Models](#models)
    - [Community Models](#community-models-documentation)
        - [Model: Person](#model-person)
        - [Model: Club](#model-club)
        - [Model: LifterLicense](#model-lifterlicense)
        - [Model: RefereeLicense](#model-refereelicense)
        - [Model: District](#model-district)
        - [Model: Violation](#model-violation)
    - [Competition Models](#competition-models-documentation)
        - [Model: Discipline](#model-discipline)
        - [Model: AgeCategory](#model-agecategory)
        - [Model: WeightClass](#model-weightclass)
        - [Model: CompetitionType](#model-competitiontype)
        - [Model: Competition](#model-competition)
        - [Model: QualifyingWeight](#model-qualifyingweight)
        - [Model: Group](#model-group)
        - [Model: RefereeAssignment](#model-refereeassignment)
    - [Scoring Models](#scoring-models-documentation)
        - [Model: Result](#model-result)
        - [Model: Lift](#model-lift)
    - [Serie Models](#serie-models)
        - [Model: Series](#model-series)
        - [Model: Division](#model-division)
        - [Model: Team](#model-team)
        - [Model: Round](#model-round)
        - [Model: RoundResult](#model-roundresult)
  



9. [Migrations](#migrations)
10. [Roles](#Roles)
11. [Tests](#tests)
12. [URLs, views & routing](#urls,_views_&_routing)
13. [Media](#media)
14. [Contributing](#contributing)
15. [License](#license)



## Introduction
The SSF_app is a software solution designed to assist the management of powerlifting competitions for Styrkelyftsförbundet in Sweden. It offers a comprehensive set of features and an intuitive interface, simplifying the entire competition process, from registration to scoring and results management. Organizers can easily create and manage competitions, while participants can register, track their progress, and view competition details. The SSF_app streamlines administrative tasks associated with powerlifting events, allowing organizers to focus on delivering a seamless experience for athletes and spectators. With its functionality and user-friendly design, the SSF_app is a valuable tool for Styrkelyftsförbundet in Sweden to enhance the powerlifting competition experience.

## Project Structure

The directory structure of the SSF_app project is as follows:

```
SSF
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
├── wsgi.py

SSF_app/
│
├── __pycache__/
│   └── [pycache files]
├── api/
│   ├── __pycache__/
│   │   └── [pycache files]
│   ├── __init__.py
│   ├── community_serializers.py
│   ├── competition_serializers.py
│   ├── scoring_serializers.py
│   └── Serie_serializers.py
├── business_logic/
│   ├── insert_competitors.py
│   ├── prel_results.py
│   └── utils.py
├── media/
│   └── [media files]
├── migrations/
│   └── [model migration files]
├── models/
│   ├── __init__.py
│   ├── Community.py
│   ├── Competition.py
│   ├── score_math.py
│   ├── Scoring.py
│   └── Serie.py
├── routers/
│   ├── __pycache__/
│   │   └── [pycache files]
│   ├── __init__.py
│   ├── community_router.py
│   ├── competition_router.py
│   ├── scoring_router.py
│   └── series_router.py
├── templates/
│   └── [template files]
├── tests/
│   └── [test files]
├── urls/
│   ├── __pycache__/
│   │   └── [pycache files]
│   ├── __init__.py
│   ├── community.py
│   ├── competition.py
│   ├── landing_urls.py
│   ├── login_urls.py
│   ├── scoring.py
│   └── serie.py
├── views/
│   ├── __pycache__/
│   │   └── [pycache files]
│   ├── __init__.py
│   ├── community_home_view.py
│   ├── community_view.py
│   ├── competition_home_view.py
│   ├── competition_view.py
│   ├── landing_views.py
│   ├── login_view.py
│   ├── scoring_home_view.py
│   ├── scoring_view.py
│   ├── serie_home_view.py
│   └── serie_view.py
├── __init__.py
├── admin.py
├── apps.py
├── filters.py
├── models.py
├── views.py
├── staticfiles/
│   └── [static files]
├── venv/
│   └── [virtual environment files]
├── .env
├── .gitignore
├── debug.log
├── manage.py
├── Notes.txt
├── Procfile
├── requirements.txt
├── runtime.txt
└── SSF_Documentation.md

```


## Project Structure Details

[Back to Table of Contents](#table-of-contents)

The project directory is `SSF_app`, which contains several subdirectories and files. Here's a breakdown of each directory:

- `__pycache__/`: This directory is used by Python to cache compiled bytecode files.

- `api/`: This directory contains files related to the API functionality of the SSF_app. It includes serializers for the community, competition, scoring, and Serie models.

- `business_logic/`: This directory contains Python scripts that handle the business logic of the SSF_app. It includes scripts for inserting competitors, preliminary results, and utility functions.

- `media/`: This directory is used to store media files, such as placeholder PDF files.

- `migrations/`: This directory contains migration files generated by Django for managing database schema changes.

- `models/`: This directory contains the Django models that represent the data structure of the SSF_app. It includes the following files:
  - `Community.py`: Represents the community model.
  - `Competition.py`: Represents the competition model.
  - `score_math.py`: Contains functions for calculating scores.
  - `Scoring.py`: Represents the scoring model.
  - `Serie.py`: Represents the Serie model.

- `routers/`: This directory contains files related to configuring API routers. It includes the following files:
  - `__init__.py`: Initializes the routers module.
  - `community_router.py`: Configures the router for the community API.
  - `competition_router.py`: Configures the router for the competition API.
  - `scoring_router.py`: Configures the router for the scoring API.
  - `series_router.py`: Configures the router for the series API.

- `templates/`: This directory is used for storing HTML templates used by the SSF_app.

- `tests/`: This directory contains test files for testing the functionality of the SSF_app.

- `urls/`: This directory is used for configuring URL routing within the SSF_app. It includes the following files:
  - `__init__.py`: Initializes the URLs module.
  - `community.py`: URL configurations for the community module.
  - `competition.py`: URL configurations for the competition module.
  - `landing_urls.py`: URL configurations for the landing pages.
  - `login_urls.py`: URL configurations for the login module.
  - `scoring.py`: URL configurations for the scoring module.
  - `serie.py`: URL configurations for the series module.

- `views/`: This directory contains Python files that define the views of the SSF_app. It includes the following files:
  - `__init__.py`: Initializes the views module.
  - `community_home_view.py`: View for the community home page.
  - `community_view.py`: View for community-related actions.
  - `competition_home_view.py`: View for the competition home page.
  - `competition_view.py`: View for competition-related actions.
  - `landing_views.py`: View for landing pages.
  - `login_view.py`: View for login actions.
  - `scoring_home_view.py`: View for the scoring home page.
  - `scoring_view.py`: View for scoring-related actions.
  - `serie_home_view.py`: View for the series home page.
  - `serie_view.py`: View for series-related actions.

- `admin.py`: This file contains the Django admin site configuration for the SSF_app.

- `apps.py`: This file contains the application configuration for the SSF_app.

- `filters.py`: This file contains the implementation of filters for the SSF_app. Filters are used to manipulate and transform data in Django templates.

- `models.py`: This file defines the Django models used in the SSF_app.

- `views.py`: This file defines additional views not covered in the `views/` directory.

- `staticfiles/`: This directory is used for storing static files, such as CSS, JavaScript, and images.

- `venv/`: This directory contains the virtual environment for the SSF_app project.

- `.env`: This file contains environment variables for the SSF_app project.

- `.gitignore`: This file specifies files and directories to be ignored by Git.

- `debug.log`: This file contains debug logs for troubleshooting.

- `manage.py`: This file is the command-line utility for managing the Django project.

- `Procfile`: This file is used by Heroku to run the SSF_app project.

- `requirements.txt`: This file lists the Python dependencies for the SSF_app project.

- `runtime.txt`: This file specifies the Python runtime to be used by the SSF_app project.

- `SSF_Documentation.md`: This file contains the documentation for the SSF_app project.

## Installation


Follow the steps below to install and set up the SSF_app project.

[Back to Table of Contents](#table-of-contents)

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.12.1
- Git

### Setup

1. **Clone the Repository**  

   First, clone the SSF_app repository from GitHub to your local machine. (note: repository prone for change)

   ```sh
   git clone https://github.com/FredrikOrheim/SSF.git
2. **Navigate to the Project Directory**  
   Change into the project directory.
   ```sh
   cd SSF
3. **Create a Virtual Environment**  
   Create a virtual environment to isolate the project dependencies.
   ```sh
   python -m venv venv
4. **Activate the Virtual Environment**  
   Activate the virtual environment using the following command:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```
5. **Install Dependencies**  
   Install the required dependencies using pip.
   ```sh
   pip install -r requirements.txt
6. **(Optional) Create and Configure a `.env` File**  
   A `.env` file will be included in the project, but you need to configure it with the correct database URL. 

   If you need to create the `.env` file, you can do so using the following command:
   ```sh
   echo DATABASE_URL=your_database_url > .env
7. **Run Migrations**  
   Apply the database migrations to set up the database schema.
   ```sh
   python manage.py migrate
8. **Run the Development Server**  
   Start the Django development server.
   ```sh
   python manage.py runserver
9. **Access the Application**  
   Open your web browser and go to `http://127.0.0.1:8000/` to access the SSF_app.


## Troubleshooting

If you encounter issues while setting up or running the SSF_app, here are some common problems and their solutions:

### 1. Database Connection Errors

**Symptom:** Unable to connect to the database, or receiving database-related error messages.

**Solutions:**
- Ensure your database server is running.
- Double-check that the `DATABASE_URL` in your `.env` file is correct.
- Verify that the database user has the necessary permissions.

### 2. Missing Dependencies

**Symptom:** ImportError or ModuleNotFoundError when trying to run the application.

**Solution:**
- Run `pip install -r requirements.txt` to ensure all dependencies are installed.
- If using a virtual environment, make sure it's activated before installing dependencies.

### 3. Migration Issues

**Symptom:** Errors when running migrations or database-related operations.

**Solutions:**
- Try running `python manage.py makemigrations` followed by `python manage.py migrate`.
- If problems persist, you can try resetting the migrations:
  1. Delete all migration files in each app's migrations folder (except `__init__.py`).
  2. Delete the database or drop all tables.
  3. Run `python manage.py makemigrations` and `python manage.py migrate` again.

### 4. Server Won't Start

**Symptom:** Error messages when trying to start the development server.

**Solutions:**
- Check the console output for specific error messages.
- Ensure no other process is using port 8000 (or whichever port you're trying to use).
- Try running the server on a different port: `python manage.py runserver 8080`

### 5. Admin Interface Issues

**Symptom:** Unable to access the admin interface or seeing unexpected behavior.

**Solutions:**
- Ensure you've created a superuser: `python manage.py createsuperuser`
- Check that your models are properly registered in the `admin.py` file.

### 6. Static Files Not Loading

**Symptom:** CSS, JavaScript, or images not loading properly in the browser.

**Solutions:**
- Run `python manage.py collectstatic`
- Check that `DEBUG = True` in your settings file (for development only).
- Verify that `STATIC_URL` and `STATIC_ROOT` are correctly set in your settings file.

### 7. Email Sending Failures

**Symptom:** Unable to send emails from the application.

**Solutions:**
- Check your email settings in the settings file.
- If using Gmail, make sure to allow less secure apps or use an app password.
- Verify your internet connection and email server accessibility.

### 8. Performance Issues

**Symptom:** The application is running slowly or timing out.

**Solutions:**
- Check your database queries for inefficiencies.
- Consider adding database indexes for frequently queried fields.
- Implement caching where appropriate.
- Monitor your server resources to ensure you have sufficient CPU and memory.

If you encounter any issues not covered here, or if the suggested solutions don't resolve your problem, please refer to our GitHub issues page or contact our support team for further assistance.


## API Documentation 

[Back to Table of Contents](#table-of-contents)

# SSF_app API Documentation

## Introduction

Welcome to the SSF_app API documentation. This API provides programmatic access to SSF_app functionality, allowing you to manage powerlifting competitions, participants, clubs, and more.

**Base URL:** `https://api.ssf-app.com/v1`

**Authentication:** All API requests require a valid Bearer Token in the Authorization header.

**Rate Limiting:** API calls are limited to 1000 requests per hour per API key.

**Versioning:** The current API version is v1. Include the version in the URL as shown in the Base URL.

# SSF_app API Documentation

## Table of Contents



1. [Community API](#community-api)
   - [Person](#person)
   - [District](#district)
   - [Club](#club)
   - [Lifter License](#lifter-license)
   - [Referee License](#referee-license)
   - [Violation](#violation)
   - [Filtered Clubs](#filtered-clubs)
   - [Club Detail](#club-detail)
   - [District Detail](#district-detail)
   - [Person Info](#person-info)

2. [Competition API](#competition-api)
   - [Age Categories](#age-categories)
   - [Competition Types](#competition-types)
   - [Competitions](#competitions)
   - [Disciplines](#disciplines)
   - [Groups](#groups)
   - [Past Competitions](#past-competitions)
   - [Past Competition Results](#past-competition-results)
   - [Past Lifter Results](#past-lifter-results)
   - [Qualifying Weights](#qualifying-weights)
   - [Rankings](#rankings)
   - [Referee Assignments](#referee-assignments)
   - [Upcoming Competition Detail](#upcoming-competition-detail)
   - [Upcoming Competitions](#upcoming-competitions)
   - [Weight Classes](#weight-classes)

3. [Scoring API](#scoring-api)

    - [Lifts](#lift)
    - [Result](#result)

4. [Serie API](#serie-api)
   - [Current_series](#current_series)
   - [Division Detail](#division_detail)
   - [Divisions](#divisions)
   - [Past Series Results](#past_series_results)
   - [Round_results](#round_results)
   - [Rounds](#rounds)
   - [Series](#series)
   - [Series Divisions](#series_divisions)
   - [Teams](#teams)
   - [Preliminary Round Results](#preliminary_round_results)

## Error Handling

The API uses conventional HTTP response codes to indicate the success or failure of an API request. In general:

- 2xx range indicate success
- 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.)
- 5xx range indicate an error with our servers

Error responses will include a JSON object with more information:

```json
{
  "error": {
    "code": "invalid_request",
    "message": "A detailed error message"
  }
}
```

## Pagination

List endpoints use cursor-based pagination via the `cursor` and `limit` parameters. `cursor` is an opaque string, and `limit` is a number between 1 and 100 (default 20).

Example: `GET /api/api_community/persons?cursor=abc123&limit=50`

The response will include `next_cursor` if there are more results available.

Now, let's dive into the specific API endpoints.

# Community API

[Return to API Overview](#table-of-contents-1)
## Person

### Get Person Details

Retrieves details of a specific person.

**Endpoint:** `GET /api/api_community/persons/{person_id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `person_id` (path parameter): The unique identifier of the person

**Response:**

```json
{
  "person_id": "12345",
  "first_name": "John",
  "last_name": "Doe",
  "gender": "male",
  "email": "john.doe@example.com",
  "social_security_nr": "900101-1234"
}
```

**Possible Errors:**
- 404 Not Found: If the person with the given ID doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

### Create a New Person

Creates a new person record.

**Endpoint:** `POST /api/api_community/persons/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "first_name": "Jane",
  "last_name": "Smith",
  "gender": "female",
  "email": "jane.smith@example.com",
  "social_security_nr": "910202-5678"
}
```

**Response:**

```json
{
  "person_id": "67890",
  "first_name": "Jane",
  "last_name": "Smith",
  "gender": "female",
  "email": "jane.smith@example.com",
  "social_security_nr": "910202-5678"
}
```

**Validations:**
- `social_security_nr`: Must be in the format "YYMMDD-XXXX"
- `first_name` and `last_name`: Cannot be the same

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## District

### Get District Details

Retrieves details of a specific district.

**Endpoint:** `GET /api/api_community/districts/{RF_nr}/`

**Authentication:** Bearer Token required

**Parameters:**
- `RF_nr` (path parameter): The unique identifier of the district

**Response:**

```json
{
  "RF_nr": "12345",
  "district_name": "Stockholm District",
  "district_orgnr": 123456789,
  "district_phone": "+46123456789",
  "district_email": "stockholm@example.com",
  "district_website": "https://stockholm-district.com"
}
```

**Possible Errors:**
- 404 Not Found: If the district with the given RF_nr doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Club

### Get Club Details

Retrieves details of a specific club.

**Endpoint:** `GET /api/api_community/clubs/{club_nr}/`

**Authentication:** Bearer Token required

**Parameters:**
- `club_nr` (path parameter): The unique identifier of the club

**Response:**

```json
{
  "club_nr": 12345,
  "club_orgnr": 987654321,
  "club_phone": "+46987654321",
  "club_email": "club@example.com",
  "club_website": "https://example-club.com",
  "name": "Example Powerlifting Club",
  "active": true,
  "paid": true,
  "district": {
    "RF_nr": "67890",
    "district_name": "Stockholm District"
  }
}
```

**Possible Errors:**
- 404 Not Found: If the club with the given club_nr doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

### Create a New Club

Creates a new club record.

**Endpoint:** `POST /api/api_community/clubs/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "club_nr": 12345,
  "club_orgnr": 987654321,
  "club_phone": "+46987654321",
  "club_email": "club@example.com",
  "club_website": "https://example-club.com",
  "name": "New Powerlifting Club",
  "district": "67890"
}
```

**Response:**

```json
{
  "club_nr": 12345,
  "club_orgnr": 987654321,
  "club_phone": "+46987654321",
  "club_email": "club@example.com",
  "club_website": "https://example-club.com",
  "name": "New Powerlifting Club",
  "active": true,
  "paid": false,
  "district": {
    "RF_nr": "67890",
    "district_name": "Stockholm District"
  }
}
```

**Validations:**
- `club_nr`: Must be a 5-digit number between 10000 and 99999
- `club_orgnr`: Must be a positive integer
- `club_phone`: Must be in a valid format (e.g., +46123456789)
- `club_website`: Must be a valid URL
- `name`: Must be at least 3 characters long

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials
- 409 Conflict: If a club with the given club_nr already exists

[Return to API Overview](#table-of-contents-1)

## Lifter License

### Get Lifter License Details

Retrieves details of a specific lifter license.

**Endpoint:** `GET /api/community/lifterlicenses/{id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `id` (path parameter): The unique identifier of the lifter license

**Response:**

```json
{
  "license_nr": "jd12345L",
  "person": {
    "person_id": "67890",
    "first_name": "John",
    "last_name": "Doe"
  },
  "status": "active",
  "requested": "2023-01-01",
  "terminates": "2023-12-31",
  "activated_date": "2023-01-15",
  "paid": true,
  "para": false,
  "ifn": false,
  "club": {
    "club_nr": 12345,
    "name": "Example Powerlifting Club"
  },
  "club_membership_date": "2022-12-01",
  "requested_year": 2023
}
```

**Possible Errors:**
- 404 Not Found: If the lifter license with the given license_nr doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

### Create a New Lifter License

Creates a new lifter license record.

**Endpoint:** `POST /api/api_community/lifterlicenses/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "person": "67890",
  "club": 12345,
  "requested": "2023-01-01",
  "terminates": "2023-12-31",
  "para": false,
  "ifn": false
}
```

**Response:**

```json
{
  "license_nr": "jd12345L",
  "person": {
    "person_id": "67890",
    "first_name": "John",
    "last_name": "Doe"
  },
  "status": "pending",
  "requested": "2023-01-01",
  "terminates": "2023-12-31",
  "activated_date": null,
  "paid": false,
  "para": false,
  "ifn": false,
  "club": {
    "club_nr": 12345,
    "name": "Example Powerlifting Club"
  },
  "club_membership_date": "2023-01-01",
  "requested_year": 2023
}
```

**Validations:**
- `license_nr`: Automatically generated in the format "initials" + "5 digits" + "L"
- `activated_date`: Cannot be before the requested date or after the termination date

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials
- 409 Conflict: If a lifter license for the given person and year already exists

[Return to API Overview](#table-of-contents-1)

## Referee License

### Get Referee License Details

Retrieves details of a specific referee license.

**Endpoint:** `GET /api/api_community/refereelicenses/{id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `id` (path parameter): The unique identifier of the referee license

**Response:**

```json
{
  "referee_license_nr": "js12345D",
  "person": {
    "person_id": "67890",
    "first_name": "Jane",
    "last_name": "Smith"
  },
  "authority": "Swedish Powerlifting Federation",
  "referee_category": "förbundsdomare",
  "status": "active",
  "requested": "2023-01-01",
  "terminates": "2023-12-31",
  "activated_date": "2023-01-15",
  "paid": true,
  "club": {
    "club_nr": 12345,
    "name": "Example Powerlifting Club"
  },
  "club_membership_date": "2022-12-01",
  "requested_year": 2023,
  "judged_competitions": [
    {
      "id": 1,
      "title": "Swedish Nationals 2023"
    }
  ],
  "number_of_missions": 1
}
```

**Possible Errors:**
- 404 Not Found: If the referee license with the given referee_license_nr doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

### Create a New Referee License

Creates a new referee license record.

**Endpoint:** `POST /api/api_community/refereelicenses/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "person": "67890",
  "authority": "Swedish Powerlifting Federation",
  "referee_category": "förbundsdomare",
  "requested": "2023-01-01",
  "terminates": "2023-12-31",
  "club": 12345
}
```

**Response:**

```json
{
  "referee_license_nr": "js12345D",
  "person": {
    "person_id": "67890",
    "first_name": "Jane",
    "last_name": "Smith"
  },
  "authority": "Swedish Powerlifting Federation",
  "referee_category": "förbundsdomare",
  "status": "pending",
  "requested": "2023-01-01",
  "terminates": "2023-12-31",
  "activated_date": null,
  "paid": false,
  "club": {
    "club_nr": 12345,
    "name": "Example Powerlifting Club"
  },
  "club_membership_date": "2023-01-01",
  "requested_year": 2023,
  "judged_competitions": [],
  "number_of_missions": 0
}
```

**Validations:**
- `referee_license_nr`: Enforced in the format "initials" + "5 digits" + "D"
- `activated_date`: Cannot be before the requested date or after the termination date
- `referee_category`: Must be one of 'distriksdomare', 'förbundsdomare', 'internationell domare kat 1', 'internationell domare kat 2'

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials
- 409 Conflict: If a referee license for the given person and year already exists

[Return to API Overview](#table-of-contents-1)

## Violation

### Get Violation Details

Retrieves details of a specific violation.

**Endpoint:** `GET /api/api_community/violations/{report_id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `report_id` (path parameter): The unique identifier of the violation report

**Response:**

```json
{
  "report_id": 12345,
  "violation": "Unsportsmanlike conduct",
  "repeal_start": "2023-06-01",
  "repeal_end": "2023-12-31",
  "author_first_name": "Admin",
  "author_last_name": "User",
  "description": "Detailed description of the violation",
  "person": {
    "person_id": "67890",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```

**Possible Errors:**
- 404 Not Found: If the violation with the given report_id doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

### Create a New Violation Report

Creates a new violation report.

**Endpoint:** `POST /api/api_community/violations/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "violation": "Unsportsmanlike conduct",
  "repeal_start": "2023-06-01",
  "repeal_end": "2023-12-31",
  "description": "Detailed description of the violation",
  "person": "67890"
}
```

**Response:**

```json
{
  "report_id": 12346,
  "violation": "Unsportsmanlike conduct",
  "repeal_start": "2023-06-01",
  "repeal_end": "2023-12-31",
  "author_first_name": "Admin",
  "author_last_name": "User",
  "description": "Detailed description of the violation",
  "person": {
    "person_id": "67890",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```

**Validations:**
- `violation`: Must not be empty
- `repeal_start`: Must be a valid date
- `repeal_end`: Must be a valid date and after the repeal_start date
- `person`: Must be a valid person_id

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials
- 404 Not Found: If the person with the given person_id doesn't exist


[Return to API Overview](#table-of-contents-1)

## Filtered Clubs

Retrieves a filtered and ordered list of clubs.

**Endpoint:** `GET /api_community/FilteredClub/`

**Authentication:** Bearer Token required

**Query Parameters:**
- `district` (optional): Filter clubs by district name (case-insensitive, partial match)
- `club_name` (optional): Filter clubs by club name (case-insensitive, partial match)
- `order_by` (optional): Order results by 'name' or 'district_name'. Prefix with '-' for descending order (e.g., '-name')

**Response:**

```json
[
  {
    "club_nr": 12345,
    "club_orgnr": 987654321,
    "name": "Example Powerlifting Club",
    "active": true,
    "paid": true,
    "district": {
      "RF_nr": "67890",
      "district_name": "Stockholm District"
    },
    "district_name": "Stockholm District"
  },
  {
    "club_nr": 12346,
    "club_orgnr": 987654322,
    "name": "Another Powerlifting Club",
    "active": false,
    "paid": true,
    "district": {
      "RF_nr": "67891",
      "district_name": "Gothenburg District"
    },
    "district_name": "Gothenburg District"
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Club Detail

Retrieves detailed information about a specific club.

**Endpoint:** `GET /api_community/ClubDetail/{club_nr}/`

**Authentication:** Bearer Token required

**Parameters:**
- `club_nr` (path parameter): The unique identifier of the club

**Response:**

```json
{
  "name": "Example Powerlifting Club",
  "district_name": "Stockholm District",
  "club_phone": "+46123456789",
  "club_email": "example@club.com",
  "club_website": "https://example-club.com",
  "club_orgnr": 987654321,
  "lifters": [
    {
      "license_nr": "jd12345L",
      "person": {
        "person_id": "67890",
        "first_name": "John",
        "last_name": "Doe"
      }
    }
  ],
  "referees": [
    {
      "referee_license_nr": "js12345D",
      "person": {
        "person_id": "67891",
        "first_name": "Jane",
        "last_name": "Smith"
      }
    }
  ],
  "number_of_lifters": 1,
  "number_of_referees": 1
}
```

**Notes:**
- Results are ordered by club name in ascending order.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials
- 404 Not Found: If the club with the given club_nr doesn't exist

[Return to API Overview](#table-of-contents-1)

## District Detail

Retrieves detailed information about a specific district.

**Endpoint:** `GET /api_community/DistrictDetail/{RF_nr}/`

**Authentication:** Bearer Token required

**Parameters:**
- `RF_nr` (path parameter): The unique identifier of the district

**Response:**

```json
{
  "district_name": "Stockholm District",
  "district_phone": "+46987654321",
  "district_email": "stockholm@district.com",
  "district_website": "https://stockholm-district.com",
  "district_orgnr": 123456789,
  "clubs": [
    {
      "club_nr": 12345,
      "name": "Example Powerlifting Club"
    }
  ],
  "associated_referees": [
    {
      "referee_license_nr": "js12345D",
      "person": {
        "person_id": "67891",
        "first_name": "Jane",
        "last_name": "Smith"
      }
    }
  ]
}
```

**Notes:**
- Results are ordered by district name in ascending order.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials
- 404 Not Found: If the district with the given RF_nr doesn't exist

[Return to API Overview](#table-of-contents-1)

## Person Info

Retrieves detailed information about a person, including their competition results.

**Endpoint:** `GET /api_community/PersonInfo/{person_id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `person_id` (path parameter): The unique identifier of the person

**Response:**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "age_category": "Senior",
  "active_lifter_license": true,
  "active_referee_license": false,
  "lifter_licenses": [
    {
      "license_nr": "jd12345L",
      "requested": "2023-01-01",
      "activated_date": "2023-01-15",
      "club_name": "Example Powerlifting Club"
    }
  ],
  "referee_licenses": [],
  "results": [
    {
      "competition_name": "Swedish Nationals 2023",
      "competition_type": "National",
      "competition_date": "2023-06-15",
      "lifter_bodyweight": 82.5,
      "squat": 200,
      "benchpress": 150,
      "deadlift": 250,
      "total": 600,
      "WILKS_score": 400.5,
      "IPFGL_score": 80.2,
      "DOTS_score": 395.8
    }
  ]
}
```

**Notes:**
- Results are ordered by person_id in ascending order.
- The `results` field uses the `Community_Lifter_Result_List_Serializer` to provide detailed competition results.
- WILKS, IPFGL, and DOTS scores are calculated based on the lifter's gender.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials
- 404 Not Found: If the person with the given person_id doesn't exist



<br>  


# Competition API

[Return to API Overview](#table-of-contents-1)

## Age Categories

Retrieves a list of age categories.

**Endpoint:** `GET /api_competition/age_categories/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "title": "Junior",
    "lower_limit_age": 14,
    "upper_limit_age": 23
  },
  {
    "id": 2,
    "title": "Senior",
    "lower_limit_age": 24,
    "upper_limit_age": 39
  }
]
```

**Notes:**
- Results are ordered by lower_limit_age in ascending order.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials


## Competition Types

Retrieves a list of competition types.

**Endpoint:** `GET /api_competition/competition_types/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "competition_type_title": "Swedish Championship",
    "competition_type_nickname": "SM"
  },
  {
    "id": 2,
    "competition_type_title": "District Championship",
    "competition_type_nickname": "DM"
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Competitions

Retrieves a list of all competitions.

**Endpoint:** `GET /api_competition/competitions/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "title": "Swedish Powerlifting Championship 2023",
    "competition_category": "National",
    "start": "2023-09-15T10:00:00Z",
    "end": "2023-09-17T18:00:00Z",
    "location": "Stockholm"
  },
  {
    "id": 2,
    "title": "Gothenburg Open 2023",
    "competition_category": "Regional",
    "start": "2023-08-20T09:00:00Z",
    "end": "2023-08-20T17:00:00Z",
    "location": "Gothenburg"
  }
]
```

**Notes:**
- Results are ordered by start date and competition category.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Disciplines

Retrieves a list of disciplines.

**Endpoint:** `GET /api_competition/disciplines/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "title": "Powerlifting"
  },
  {
    "id": 2,
    "title": "Bench Press"
  }
]
```

**Notes:**
- Results are ordered by discipline name in ascending order.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Groups

Retrieves a list of competition groups.

**Endpoint:** `GET /api_competition/groups/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "title": "Men's 59kg",
    "competition": 1
  },
  {
    "id": 2,
    "title": "Women's 47kg",
    "competition": 1
  }
]
```

**Notes:**
- Results are ordered by competition.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Past Competitions

Retrieves a list of past competitions.

**Endpoint:** `GET /api_competition/past_competitions/`

**Authentication:** Bearer Token required

**Query Parameters:**
- `past` (optional): Filter for past competitions (true/false)
- `competition_category` (optional): Filter by competition category
- `start` (optional): Filter by start date
- `end` (optional): Filter by end date
- `ordering` (optional): Order results by 'title', 'competition_category', 'start', 'end', or 'competition_type__nickname'

**Response:**

```json
[
  {
    "title": "Swedish Powerlifting Championship 2022",
    "competition_category": "National",
    "start": "2022-09-15T10:00:00Z"
  },
  {
    "title": "Gothenburg Open 2022",
    "competition_category": "Regional",
    "start": "2022-08-20T09:00:00Z"
  }
]
```

**Notes:**
- Only includes competitions with a start date before the current date.
- Results are ordered by start date by default.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Past Competition Results

Retrieves detailed results for a specific past competition.

**Endpoint:** `GET /api_competition/past_competition_results/{id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `id` (path parameter): The unique identifier of the competition

**Response:**

```json
{
        "title": "SL tävling",
        "competition_category": "Aja",
        "start": "2024-06-03",
        "results": [
            {
                "id": 20,
                "group": 1,
                "license_nr": 13,
                "weight_class": 7,
                "age_category": "Senior",
                "body_weight": "92.450",
                "date": "2024-07-03",
                "lot_nr": 2,
                "placement": 2,
                "WILKS_female_score": "609.093649",
                "WILKS_male_score": "448.854727",
                "IPFGL_male_score": "93.480420",
                "IPFGL_female_score": "130.048649",
                "DOTS_male_score": "454.629097",
                "DOTS_female_score": "627.832237",
                "WILKS_female_BP_score": "128.230242",
                "WILKS_male_BP_score": "94.495732",
                "IPFGL_male_BP_score": "71.373414",
                "IPFGL_female_BP_score": "109.656702",
                "DOTS_male_BP_score": "95.711389",
                "DOTS_female_BP_score": "132.175208",
                "squat": "262.50",
                "benchpress": "150.00",
                "deadlift": "300.00",
                "total": "712.50"
            },
            {
                "id": 21,
                "group": 1,
                "license_nr": 13,
                "weight_class": 7,
                "age_category": "Senior",
                "body_weight": "92.450",
                "date": "2024-07-03",
                "lot_nr": 2,
                "placement": 2,
                "WILKS_female_score": "0.000000",
                "WILKS_male_score": "0.000000",
                "IPFGL_male_score": "0.000000",
                "IPFGL_female_score": "0.000000",
                "DOTS_male_score": "0.000000",
                "DOTS_female_score": "0.000000",
                "WILKS_female_BP_score": "0.000000",
                "WILKS_male_BP_score": "0.000000",
                "IPFGL_male_BP_score": "0.000000",
                "IPFGL_female_BP_score": "0.000000",
                "DOTS_male_BP_score": "0.000000",
                "DOTS_female_BP_score": "0.000000",
                "squat": "0.00",
                "benchpress": "0.00",
                "deadlift": "0.00",
                "total": "0.00"
            }
        ]
```

**Notes:**
- Only includes competitions with a start date before the current date.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials
- 404 Not Found: If the competition with the given id doesn't exist or is not a past competition

[Return to API Overview](#table-of-contents-1)

## Past Lifter Results

Retrieves detailed results for lifters in past competitions.

**Endpoint:** `GET /api_competition/past_lifter_results/`

**Authentication:** Bearer Token required

**Query Parameters:**
- `weight_class` (optional): Filter by weight class (comma-separated for multiple)
- `age_category` (optional): Filter by age category (comma-separated for multiple)

**Response:**

```json
[
    {
        "placement": 1,
        "lifter_name": "John",
        "lifter_club": "Skånes klubb",
        "lifter_body_weight": "63.000",
        "lifts": [
            {
                "id": 14,
                "result": 18,
                "discipline": "Squat",
                "try_nr": 3,
                "weight": "110.00",
                "goodlift": true
            }
        ],
        "knäböj": "110.00",
        "bänkpress": "0.00",
        "marklyft": "0.00",
        "total_weight": "110.00",
        "WILKS_score": 89.831076,
        "IPFGL_score": 17.575735,
        "DOTS_score": 89.290419
    },
]
```

**Notes:**
- Only includes results from competitions with a start date before the current date.
- Results are ordered by weight class, age category, and placement.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Qualifying Weights

Retrieves a list of qualifying weights for competitions.

**Endpoint:** `GET /api_competition/qualifying_weights/`

**Authentication:** Bearer Token required

**Response:**

```json
[
    {
        "id": 1,
        "minimum": 130,
        "qualifying_period_start": "2024-06-23",
        "qualifying_period_end": "2024-06-24",
        "competition": 1,
        "age_category": "En åldersklass",
        "weight_class": 2
    }
]
```

**Notes:**
- Results are ordered by minimum, weight_class, and age_category.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Rankings

Retrieves rankings based on competition results.

**Endpoint:** `GET /api_competition/rankings/`

**Authentication:** Bearer Token required

**Query Parameters:**
- `start_date` (optional): Filter results from this date onwards
- `end_date` (optional): Filter results up to this date
- `age_category` (optional): Filter by age category
- `gender` (optional): Filter by gender
- `discipline` (optional): Filter by discipline (squat, benchpress, deadlift)

**Response:**

```json
[
    {
        "id": 18,
        "group": 1,
        "license_nr": 7,
        "weight_class": "-93KG",
        "age_category": "Senior",
        "body_weight": "63.000",
        "date": "2024-06-23",
        "lot_nr": 1,
        "placement": 1,
        "WILKS_female_score": "118.135318",
        "WILKS_male_score": "89.831076",
        "IPFGL_male_score": "17.575735",
        "IPFGL_female_score": "24.066148",
        "DOTS_male_score": "89.290419",
        "DOTS_female_score": "118.306645",
        "WILKS_female_BP_score": "0.000000",
        "WILKS_male_BP_score": "0.000000",
        "IPFGL_male_BP_score": "0.000000",
        "IPFGL_female_BP_score": "0.000000",
        "DOTS_male_BP_score": "0.000000",
        "DOTS_female_BP_score": "0.000000",
        "squat": "110.00",
        "benchpress": "0.00",
        "deadlift": "0.00",
        "total": "110.00"
    }
]
```

**Notes:**
- Results are ordered by competition start date, weight class, age category, and placement.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Referee Assignments

Retrieves a list of referee assignments for competitions.

**Endpoint:** `GET /api_competition/referee_assignments/`

**Authentication:** Bearer Token required

**Response:**

```json
[
    {
        "id": 2,
        "service": "Distriktstävling",
        "referee_license": 3,
        "group": 4
    },
    {
        "id": 3,
        "service": "Dömning",
        "referee_license": 3,
        "group": 6
    }
]
```

**Notes:**
- Results are ordered by group.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Upcoming Competition Detail

Retrieves detailed information about an upcoming competition.

**Endpoint:** `GET /api_competition/upcoming_competition_detail/{id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `id` (path parameter): The unique identifier of the competition

**Response:**

```json
{
  "id": 1,
  "title": "Swedish Powerlifting Championship 2023",
  "competition_category": "National",
  "location": "Stockholm",
  "description": "Annual national powerlifting championship",
  "start": "2023-09-15T10:00:00Z",
  "end": "2023-09-17T18:00:00Z",
  "reg_deadline": "2023-08-31T23:59:59Z",
  "location_address": "Stockholm Olympic Stadium, 114 33 Stockholm",
  "contact_phone": "+46123456789",
  "contact_email": "info@swedishpowerlifting.com",
  "contact_name": "Swedish Powerlifting Federation",
  "competition_type": 1,
  "club_orgnr": 123456789,
  "district_orgnr": 987654321,
  "invitation": "https://example.com/invitation.pdf",
  "registration_open": true,
  "live_stream": "https://example.com/livestream",
  "is_registration_open": true
}
```

**Notes:**
- Only includes competitions with a start date after the current date.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials
- 404 Not Found: If the competition with the given id doesn't exist or is not an upcoming competition

[Return to API Overview](#table-of-contents-1)

## Upcoming Competitions

Retrieves a list of upcoming competitions.

**Endpoint:** `GET /api_competition/upcoming-competitions/`

**Authentication:** Bearer Token required

**Query Parameters:**
- `upcoming` (optional): Filter for upcoming competitions (true/false)
- `competition_category` (optional): Filter by competition category
- `start` (optional): Filter by start date
- `end` (optional): Filter by end date
- `ordering` (optional): Order results by 'title', 'competition_category', 'start', 'end', or 'competition_type__nickname'

**Response:**

```json
[
  {
    "title": "Swedish Powerlifting Championship 2023",
    "competition_category": "National",
    "start": "2023-09-15T10:00:00Z"
  },
  {
    "title": "Gothenburg Open 2023",
    "competition_category": "Regional",
    "start": "2023-08-20T09:00:00Z"
  }
]
```

**Notes:**
- Only includes competitions with a start date after the current date.
- Results are ordered by start date by default.

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

## Weight Classes

Retrieves a list of weight classes.

**Endpoint:** `GET /api_competition/weight-classes/`

**Authentication:** Bearer Token required

**Response:**

```json
[
    {
        "id": 2,
        "upper_limit": "83.00",
        "lower_limit": "74.01",
        "title": "-83KG",
        "start_date": "2024-06-03",
        "end_date": "2024-11-03",
        "gender": "male"
    },
    {
        "id": 5,
        "upper_limit": "50.00",
        "lower_limit": "30.00",
        "title": "-93KG",
        "start_date": "2024-06-05",
        "end_date": "2024-06-08",
        "gender": "male"
    }
]
```

**Notes:**
- Results are ordered by lower_limit and gender.
- Selection between male & female 

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)

# Scoring API

## Lift

Retrieves details of a specific lift.

**Endpoint:** `GET /api/scoring/lifts/{id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `id` (path parameter): The unique identifier of the lift

**Response:**

```json
{
  "id": 1,
  "result": 1,
  "discipline": 1,
  "try_nr": 1,
  "weight": 100.5,
  "goodlift": true
}
```

**Possible Errors:**
- 404 Not Found: If the lift with the given id doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

**Create a New Lift**

Creates a new lift record.

**Endpoint:** `POST /api/api_scoring/lifts/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "result": 1,
  "discipline": 1,
  "try_nr": 1,
  "weight": 100.5,
  "goodlift": true
}
```

**Response:**

```json
{
  "id": 1,
  "result": 1,
  "discipline": 1,
  "try_nr": 1,
  "weight": 100.5,
  "goodlift": true
}
```

**Validations:**
- `weight`: Must be a positive number
- `try_nr`: Must be a positive integer
- `result`: Must be a valid Result id
- `discipline`: Must be a valid Discipline id

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials
- 409 Conflict: If a lift with the same try_nr and discipline already exists for the given result

## Result

Retrieves details of a specific result.

**Endpoint:** `GET /api/api_scoring/results/{id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `id` (path parameter): The unique identifier of the result

**Response:**

```json
{
  "id": 1,
  "group": 1,
  "license_nr": "ABC123",
  "weight_class": 1,
  "age_category": 1,
  "body_weight": 82.5,
  "date": "2023-07-15",
  "lot_nr": 5,
  "placement": 3,
  "WILKS_female_score": 100.123456,
  "WILKS_male_score": 95.987654,
  "IPFGL_male_score": 98.765432,
  "IPFGL_female_score": 97.654321,
  "DOTS_male_score": 99.876543,
  "DOTS_female_score": 98.765432,
  "WILKS_female_BP_score": 50.123456,
  "WILKS_male_BP_score": 48.987654,
  "IPFGL_male_BP_score": 49.765432,
  "IPFGL_female_BP_score": 48.654321,
  "DOTS_male_BP_score": 49.876543,
  "DOTS_female_BP_score": 48.765432,
  "squat": 150.00,
  "benchpress": 100.00,
  "deadlift": 180.00,
  "total": 430.00,
  "lifts": [
    {
      "id": 1,
      "result": 1,
      "discipline": 1,
      "try_nr": 1,
      "weight": 150.00,
      "goodlift": true
    },
    {
      "id": 2,
      "result": 1,
      "discipline": 2,
      "try_nr": 1,
      "weight": 100.00,
      "goodlift": true
    },
    {
      "id": 3,
      "result": 1,
      "discipline": 3,
      "try_nr": 1,
      "weight": 180.00,
      "goodlift": true
    }
  ]
}
```

**Possible Errors:**
- 404 Not Found: If the result with the given id doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

**Create a New Result**

Creates a new result record.

**Endpoint:** `POST /api/scoring/results/`

**Authentication:** Bearer Token required

**Request Body:**

```json
{
  "group": 1,
  "license_nr": "ABC123",
  "weight_class": 1,
  "age_category": 1,
  "body_weight": 82.5,
  "date": "2023-07-15",
  "lot_nr": 5
}
```

**Response:**

```json
{
  "id": 1,
  "group": 1,
  "license_nr": "ABC123",
  "weight_class": 1,
  "age_category": 1,
  "body_weight": 82.5,
  "date": "2023-07-15",
  "lot_nr": 5,
  "placement": null,
  "WILKS_female_score": 0,
  "WILKS_male_score": 0,
  "IPFGL_male_score": 0,
  "IPFGL_female_score": 0,
  "DOTS_male_score": 0,
  "DOTS_female_score": 0,
  "WILKS_female_BP_score": 0,
  "WILKS_male_BP_score": 0,
  "IPFGL_male_BP_score": 0,
  "IPFGL_female_BP_score": 0,
  "DOTS_male_BP_score": 0,
  "DOTS_female_BP_score": 0,
  "squat": 0,
  "benchpress": 0,
  "deadlift": 0,
  "total": 0,
  "lifts": []
}
```

**Validations:**
- `body_weight`: Must be a positive number
- `lot_nr`: Must be a positive integer
- `group`: Must be a valid Group id
- `license_nr`: Must be a valid LifterLicense id
- `weight_class`: Must be a valid WeightClass id
- `age_category`: Must be a valid AgeCategory id

**Possible Errors:**
- 400 Bad Request: If the request body is invalid or validation fails
- 401 Unauthorized: If the request lacks valid authentication credentials
- 409 Conflict: If a result for the given license_nr and competition already exists

[Return to API Overview](#table-of-contents-1)


# Serie API

[Return to API Overview](#table-of-contents-1)

## Current_series

Retrieves a list of ongoing series.

**Endpoint:** `GET /api/api_serie/current_series/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "title": "Powerlifting Series 2023",
    "series_type": "National",
    "year": 2023
  },
  {
    "title": "Regional Bench Press Series 2023",
    "series_type": "Regional",
    "year": 2023
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Division_detail

Retrieves detailed information about a specific division.

**Endpoint:** `GET /api/api_serie/division_detail/{division_id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `division_id` (path parameter): The unique identifier of the division

**Response:**

```json
{
  "title": "First Division",
  "teams": [
    {
      "title": "Team A",
      "paid": true,
      "club": "Club X",
      "round_results": [
        {
          "round": 1,
          "score": 1000.5
        }
      ],
      "total_score": 1000.5
    }
  ],
  "limit_teams": 10,
  "teams_moving_up": 2,
  "teams_moving_down": 2
}
```

**Possible Errors:**
- 404 Not Found: If the division with the given division_id doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

## Divisions

Retrieves a list of all divisions.

**Endpoint:** `GET /api/api_serie/divisions/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "division_id": "DIV2023A",
    "title": "First Division",
    "limit_teams": 10,
    "limit_team_members": 5,
    "series": "SER2023",
    "teams_moving_up": 2,
    "teams_moving_down": 2
  },
  {
    "division_id": "DIV2023B",
    "title": "Second Division",
    "limit_teams": 12,
    "limit_team_members": 5,
    "series": "SER2023",
    "teams_moving_up": 2,
    "teams_moving_down": 2
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Past_series_results

Retrieves results from past series.

**Endpoint:** `GET /api/api_serie/past_series_results/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "title": "Powerlifting Series 2022",
    "series_type": "National",
    "year": 2022,
    "results": [
      {
        "id": 1,
        "group": 1,
        "license_nr": "ABC123",
        "weight_class": 1,
        "age_category": "Senior",
        "body_weight": 82.5,
        "date": "2022-07-15",
        "lot_nr": 5,
        "placement": 3,
        "WILKS_score": 100.123456,
        "total": 430.00
      }
    ]
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Round_results

Retrieves results for a specific round.

**Endpoint:** `GET /api/api_serie/round_results/{round_id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `round_id` (path parameter): The unique identifier of the round

**Response:**

```json
[
  {
    "id": 1,
    "team": 1,
    "round": 1,
    "included_results": [
      {
        "id": 1,
        "group": 1,
        "license_nr": "ABC123",
        "weight_class": 1,
        "age_category": "Senior",
        "body_weight": 82.5,
        "date": "2023-07-15",
        "lot_nr": 5,
        "placement": 3,
        "WILKS_score": 100.123456,
        "total": 430.00
      }
    ],
    "score": 1000.5
  }
]
```

**Possible Errors:**
- 404 Not Found: If the round with the given round_id doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

## Rounds

Retrieves a list of all rounds.

**Endpoint:** `GET /api/api_serie/rounds/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "start": "2023-01-01",
    "end": "2023-01-31",
    "division": "DIV2023A"
  },
  {
    "id": 2,
    "start": "2023-02-01",
    "end": "2023-02-28",
    "division": "DIV2023A"
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Series

Retrieves a list of all series.

**Endpoint:** `GET /api/api_serie/series/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "serie_id": "SER2023",
    "title": "Powerlifting Series 2023",
    "series_type": "National",
    "year": 2023,
    "scoring_system": "WILKS",
    "gender": "male",
    "competition_type_nickname": 1,
    "age_categories": [1, 2, 3]
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Series_divisions

Retrieves series with their associated divisions.

**Endpoint:** `GET /api/api_serie/series_divisions/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "title": "Powerlifting Series 2023",
    "series_type": "National",
    "year": 2023,
    "divisions": [
      {
        "division_id": "DIV2023A",
        "title": "First Division",
        "limit_teams": 10,
        "limit_team_members": 5,
        "series": "SER2023",
        "teams_moving_up": 2,
        "teams_moving_down": 2
      }
    ]
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Teams

Retrieves a list of all teams.

**Endpoint:** `GET /api/api_serie/teams/`

**Authentication:** Bearer Token required

**Response:**

```json
[
  {
    "id": 1,
    "title": "Team A",
    "paid": true,
    "division": "DIV2023A",
    "club": "CLUB001"
  },
  {
    "id": 2,
    "title": "Team B",
    "paid": false,
    "division": "DIV2023B",
    "club": "CLUB002"
  }
]
```

**Possible Errors:**
- 401 Unauthorized: If the request lacks valid authentication credentials

## Preliminary_round_results

Retrieves preliminary results for a round.

**Endpoint:** `GET /api/api_serie/preliminary_round_results/{round_id}/`

**Authentication:** Bearer Token required

**Parameters:**
- `round_id` (path parameter): The unique identifier of the round

**Response:**

```json
[
  {
    "id": 1,
    "team": 1,
    "round": 1,
    "included_results": [
      {
        "id": 1,
        "group": 1,
        "license_nr": "ABC123",
        "weight_class": 1,
        "age_category": "Senior",
        "body_weight": 82.5,
        "date": "2023-07-15",
        "lot_nr": 5,
        "placement": 3,
        "WILKS_score": 100.123456,
        "total": 430.00
      }
    ],
    "score": 1000.5
  }
]
```

**Possible Errors:**
- 404 Not Found: If the round with the given round_id doesn't exist
- 401 Unauthorized: If the request lacks valid authentication credentials

[Return to API Overview](#table-of-contents-1)



# Home Views Documentation

[Back to Table of Contents](#table-of-contents)

The SSF application uses several home view functions to generate HTML pages that serve as landing pages for different API categories. These views follow a similar structure but use different routers specific to their API category.


## Common Structure

Each home view function:
1. Imports the specific router for its API category.
2. Builds a base URL for the API endpoints.
3. Generates an HTML page with:
   - A header for the specific API category
   - A list of available API endpoints based on the router's registry
   - Buttons to navigate to other API category pages

## Specific Home Views

### community_home_view

This view generates the landing page for the Community API. It uses the `community_router` to list all available Community API endpoints.

### competition_home_view

This view creates the landing page for the Competition API. It utilizes the `competition_router` to display all Competition API endpoints.

### scoring_home_view

This view produces the landing page for the Scoring API. It employs the `scoring_router` to show all Scoring API endpoints.

### serie_home_view

This view builds the landing page for the Serie API. It uses the `serie_router` to list all Serie API endpoints.

## Key Features

- Dynamic endpoint listing: The views automatically generate links to all registered endpoints in their respective routers.
- Consistent styling: All pages use Bootstrap for a clean, responsive design.
- Inter-API navigation: Each page includes buttons to easily switch between different API categories.
- SEO-friendly: The pages include proper HTML structure and meta tags.

## Usage

These views are typically mapped to URLs like `/home/`, `/home2/`, `/home3/`, and `/home4/` for Community, Competition, Scoring, and Serie APIs respectively. More about URLs and the routing in point 12 of the documentation.


# Community API Viewsets

[Back to Table of Contents](#table-of-contents)

## Community_Person_ViewSet

**Purpose:** Manages Person objects in the system.

**Queryset:** All Person objects, ordered by last name and then first name.

**Serializer:** `Community_Person_Serializer`

**Custom Actions:**
- `search`: Allows searching for persons by first name and/or last name.
  - **HTTP Method:** GET
  - **URL:** `/api/community/persons/search/`
  - **Query Parameters:** 
    - `first_name`: Filter by first name (case-insensitive, partial match)
    - `last_name`: Filter by last name (case-insensitive, partial match)

## Community_District_ViewSet

**Purpose:** Manages District objects in the system.

**Queryset:** All District objects, ordered by RF_nr.

**Serializer:** `Community_District_Serializer`

## Community_Club_ViewSet

**Purpose:** Manages Club objects in the system.

**Queryset:** All Club objects, ordered by club_nr.

**Serializer:** `Community_Club_Serializer`

## Community_Lifter_License_ViewSet

**Purpose:** Manages LifterLicense objects in the system.

**Queryset:** All LifterLicense objects, ordered by license_nr.

**Serializer:** `Community_Lifter_License_Serializer`

## Community_Referee_License_ViewSet

**Purpose:** Manages RefereeLicense objects in the system.

**Queryset:** All RefereeLicense objects, ordered by referee_license_nr.

**Serializer:** `Community_Referee_License_Serializer`

## Community_Violation_ViewSet

**Purpose:** Manages Violation objects in the system.

**Queryset:** All Violation objects.

**Serializer:** `Community_Violation_Serializer`

## Community_Filtered_Clubs_ViewSet

**Purpose:** Provides filtered view of Club objects.

**Queryset:** All Club objects.

**Serializer:** `Community_Club_List_Serializer`

**Filters:** Uses `Filter_Club_District_ClubName` for filtering and ordering.
- **district_name**: Filters clubs by district name (case-insensitive, partial match)
- **club_name**: Filters clubs by club name (case-insensitive, partial match)
- **order_by**: Allows ordering by 'name' or 'district_name'

**Filter Usage:**
- To filter by district: `/api/api_community/FilteredClub/?district_name=Stockholm`
- To filter by club name: `/api/api_community/FilteredClub/?club_name=Power`
- To order by club name ascending: `/api/api_community/FilteredClub/?order_by=name`
- To order by district name descending: `/api/api_community/FilteredClub/?order_by=-district_name`

## Community_Detail_Clubs_ViewSet

**Purpose:** Provides detailed view of Club objects.

**Queryset:** All Club objects, ordered by name.

**Serializer:** `Community_Club_Detail_Serializer`

## Community_Detail_District_ViewSet

**Purpose:** Provides detailed view of District objects.

**Queryset:** All District objects, ordered by district_name.

**Serializer:** `Community_District_Detail_Serializer`

## Community_Person_Information_ViewSet

**Purpose:** Provides detailed information about Person objects.

**Queryset:** All Person objects, ordered by person_id.

**Serializer:** `Community_Person_Info_Serializer`

[Back to Table of Contents](#table-of-contents)

# Competition API Viewsets

## Age_categories API

**Endpoint:** `GET /api/api_competition/age_categories/`

**Purpose:** Retrieves a list of age categories.

**Serializer:** `Competition_Age_Category_Serializer`

**Queryset:** All AgeCategory objects, ordered by lower_limit_age.

## Competition_types API

**Endpoint:** `GET /api/api_competition/competition_types/`

**Purpose:** Retrieves a list of competition types.

**Serializer:** `Competition_Competition_Type_Serializer`

**Queryset:** All CompetitionType objects.

## Competitions API

**Endpoint:** `GET /api/api_competition/competitions/`

**Purpose:** Retrieves a list of all competitions.

**Serializer:** `Competition_Competition_Serializer`

**Queryset:** All Competition objects, ordered by start date and then competition category.

## Disciplines API

**Endpoint:** `GET /api/api_competition/disciplines/`

**Purpose:** Retrieves a list of disciplines.

**Serializer:** `Competition_Discipline_Serializer`

**Queryset:** All Discipline objects, ordered by discipline name.

## Groups API

**Endpoint:** `GET /api/api_competition/groups/`

**Purpose:** Retrieves a list of competition groups.

**Serializer:** `Competition_Group_Serializer`

**Queryset:** All Group objects, ordered by competition.

## Past_competitions API

**Endpoint:** `GET /api/api_competition/past_competitions/`

**Purpose:** Retrieves a list of past competitions.

**Serializer:** `Competition_Past_List_Serializer`

**Queryset:** All Competition objects with start date in the past, ordered by start date.

**Filters:** Uses `Filter_Past_Competition` for filtering and ordering.
- **past**: Filters for past competitions (boolean)
- **competition_category**: Filters by competition category
- **start**: Filters by start date
- **end**: Filters by end date
- **ordering**: Allows ordering by 'title', 'competition_category', 'start', 'end', or 'competition_type__nickname'

**Filter Usage:**
- To filter past competitions: `/api/api_competition/past_competitions/?past=true`
- To filter by category: `/api/api_competition/past_competitions/?competition_category=Regional`
- To order by end date descending: `/api/api_competition/past_competitions/?ordering=-end`

## Past_competition_results API

**Endpoint:** `GET /api/api_competition/past_competition_results/{id}/`

**Purpose:** Retrieves detailed results for a specific past competition.

**Serializer:** `Competition_Past_Detail_Serializer`

**Queryset:** Specific Competition object with start date in the past.

## Past_lifter_results API

**Endpoint:** `GET /api/api_competition/past_lifter_results/`

**Purpose:** Retrieves results of lifters from past competitions.

**Serializer:** `Competition_Lifter_Result_Serializer`

**Queryset:** All Result objects from past competitions, ordered by weight class, age category, and placement.

**Filters:** Uses `Filter_Result_WeightClass_Age` for filtering.
- **weight_class**: Filters by weight class (comma-separated for multiple)
- **age_category**: Filters by age category (comma-separated for multiple)

**Filter Usage:**
- To filter by weight class: `/api/api_competition/past_lifter_results/?weight_class=82.5,90`
- To filter by age category: `/api/api_competition/past_lifter_results/?age_category=Senior,Junior`

## Qualifying_weights API

**Endpoint:** `GET /api/api_competition/qualifying_weights/`

**Purpose:** Retrieves a list of qualifying weights for competitions.

**Serializer:** `Competition_Qualifying_Weight_Serializer`

**Queryset:** All QualifyingWeight objects, ordered by minimum weight, weight class, and then age category.

## Rankings API

**Endpoint:** `GET /api/api_competition/rankings/`

**Purpose:** Retrieves rankings based on competition results.

**Serializer:** `Scoring_Result_Serializer`

**Queryset:** All Result objects, ordered by competition start date, weight class, age category, and placement.

**Filters:** Uses `Filter_Ranking_Date_Age_Gender` for filtering.
- **start_date**: Filters results from this date onwards
- **end_date**: Filters results up to this date
- **age_category**: Filters by age category
- **gender**: Filters by gender
- **discipline**: Filters by discipline (squat, benchpress, deadlift)

**Filter Usage:**
- To filter by date range: `/api/api_competition/rankings/?start_date=2023-01-01&end_date=2023-12-31`
- To filter by gender and age category: `/api/api_competition/rankings/?gender=female&age_category=Senior`
- To filter by discipline: `/api/api_competition/rankings/?discipline=benchpress`

## Referee_assignments API

**Endpoint:** `GET /api/api_competition/referee_assignments/`

**Purpose:** Retrieves a list of referee assignments for competitions.

**Serializer:** `Competition_Referee_Assignment_Serializer`

**Queryset:** All RefereeAssignment objects, ordered by group.

## Upcoming_competition_detail API

**Endpoint:** `GET /api/api_competition/upcoming_competition_detail/{id}/`

**Purpose:** Retrieves detailed information about a specific upcoming competition.

**Serializer:** `Competition_Upcoming_Detail_Serializer`

**Queryset:** Specific Competition object with start date in the future.

## Upcoming_competitions API

**Endpoint:** `GET /api/api_competition/upcoming_competitions/`

**Purpose:** Retrieves a list of upcoming competitions.

**Serializer:** `Competition_Upcoming_List_Serializer`

**Queryset:** All Competition objects with start date in the future, ordered by start date.

**Filters:** Uses `Filter_Upcoming_Competition` for filtering and ordering.
- **upcoming**: Filters for upcoming competitions (boolean)
- **competition_category**: Filters by competition category
- **start**: Filters by start date
- **end**: Filters by end date
- **ordering**: Allows ordering by 'title', 'competition_category', 'start', 'end', or 'competition_type__nickname'

**Filter Usage:**
- To filter upcoming competitions: `/api/api_competition/upcoming_competitions/?upcoming=true`
- To filter by category: `/api/api_competition/upcoming_competitions/?competition_category=National`
- To order by start date: `/api/api_competition/upcoming_competitions/?ordering=start`

## Weight_classes API

**Endpoint:** `GET /api/api_competition/weight_classes/`

**Purpose:** Retrieves a list of weight classes.

**Serializer:** `Competition_Weight_Class_Serializer`

**Queryset:** All WeightClass objects, ordered by lower_limit and then gender.


# Serie API Viewsets

[Back to Table of Contents](#table-of-contents)

## Series API

**Endpoint:** `GET /api/api_serie/series/`

**Purpose:** Retrieves a list of all series.

**Serializer:** `Series_Serie_Serializer`

**Queryset:** All Series objects.

## Divisions API

**Endpoint:** `GET /api/api_serie/divisions/`

**Purpose:** Retrieves a list of all divisions.

**Serializer:** `Series_Division_Serializer`

**Queryset:** All Division objects.

## Teams API

**Endpoint:** `GET /api/api_serie/teams/`

**Purpose:** Retrieves a list of all teams.

**Serializer:** `Series_Team_Serializer`

**Queryset:** All Team objects.

## Rounds API

**Endpoint:** `GET /api/api_serie/rounds/`

**Purpose:** Retrieves a list of all rounds.

**Serializer:** `Series_Round_Serializer`

**Queryset:** All Round objects.

## Round_results API

**Endpoint:** `GET /api/api_serie/round_results/`

**Purpose:** Manages round results.

**Serializer:** `Series_RoundScoring_Result_Serializer`

**Queryset:** All RoundResult objects.

**Custom Actions:**
- `add_competitors`: Adds competitors to a round result.
  - **HTTP Method:** POST
  - **URL:** `/api/api_serie/round_results/{id}/add_competitors/`
  - **Data:** `results_ids` (list of Result IDs to add)

- `remove_competitors`: Removes competitors from a round result.
  - **HTTP Method:** POST
  - **URL:** `/api/api_serie/round_results/{id}/remove_competitors/`
  - **Data:** `results_ids` (list of Result IDs to remove)

## Preliminary_round_results API

**Endpoint:** `GET /api/api_serie/preliminary_round_results/`

**Purpose:** The `Series_PreliminaryRoundResultsViewSet` is a viewset that handles the retrieval of preliminary round results for the period of a specific round in a series. It processes the request to fetch preliminary results, calculates these results, and serializes the data for the response.


**Query Parameters:**
- `round_id`: ID of the round to calculate preliminary results for.

## Current_series API

**Endpoint:** `GET /api/api_serie/current_series/`

**Purpose:** Retrieves a list of current (ongoing or future) series.

**Serializer:** `Series_Current_Serializer`

**Queryset:** All Series objects with year greater than or equal to the current year.

## Past_series_results API

**Endpoint:** `GET /api/api_serie/past_series_results/`

**Purpose:** Retrieves results from past series.

**Serializer:** `Series_Past_Serializer`

**Queryset:** All Series objects with year less than the current year.

## Series_divisions API

**Endpoint:** `GET /api/api_serie/series_divisions/`

**Purpose:** Retrieves series with their associated divisions.

**Serializer:** `Series_With_Divisions_Serializer`

**Queryset:** All Series objects.

## Division_detail API

**Endpoint:** `GET /api/api_serie/division_detail/`

**Purpose:** Retrieves detailed information about divisions.

**Serializer:** `Series_Division_Detail_Serializer`

**Queryset:** All Division objects.


# Scoring API Viewsets

[Back to Table of Contents](#table-of-contents)

## Results API

**Endpoint:** `GET /api/api_scoring/results/`

**Purpose:** Manages Result objects in the system.

**Serializer:** `Scoring_Result_Serializer`

**Queryset:** All Result objects, ordered by date, weight class, and age category.

## Lifts API

**Endpoint:** `GET /api/api_scoring/lifts/`

**Purpose:** Manages Lift objects in the system.

**Serializer:** `Scoring_Lift_Serializer`

**Queryset:** All Lift objects, ordered by result, discipline, and try number.

[Back to Table of Contents](#table-of-contents)

# Miscellaneous Viewsets

**DISCLAIMER: The code presented in this section is intended for testing purposes only and is not suitable for production use. It may lack necessary security measures and optimizations required for a live environment. Please ensure proper security practices are implemented before deploying any authentication or authorization code in a production setting.**

These viewsets were used for testing roles and permissions tied to the APIs in the Django admin page.

## Login View

**Purpose:** Handles user authentication and redirects based on user groups.

**Function:** `login_view(request)`

**Behavior:**
- Authenticates user credentials
- If authentication is successful:
  - Redirects to 'föreningsadmin_landing' for users in the 'föreningsadministratör' group
  - Redirects to 'domaradmin_landing' for users in the 'domaradmin' group
  - Redirects to 'home' for users not in either group
- If authentication fails, renders the login page with an error message

## Home View

**Purpose:** Redirects authenticated users to the home page.

**Function:** `home_view(request)`

**Behavior:**
- Requires user to be logged in (uses `@login_required` decorator)
- Redirects to the root URL ('/')

## Föreningsadmin Landing Page

**Purpose:** Renders the landing page for föreningsadministratör (club administrator) users.

**Function:** `föreningsadmin_landing_page(request)`

**Behavior:**
- Requires user to be logged in
- Checks if the user is in the 'Föreningsadministratör' group
- If yes, renders 'föreningsadmin_landing.html'
- If no, renders 'no_permission.html'

## Domaradmin Landing Page

**Purpose:** Renders the landing page for domaradministratör (referee administrator) users.

**Function:** `domaradmin_landing_page(request)`

**Behavior:**
- Requires user to be logged in
- Checks if the user is in the 'Domaradministratör' group
- If yes, renders 'domaradministratör_landing.html'
- If no, renders 'no_permission.html'

## No Permission View

**Purpose:** Renders a page indicating lack of permission.

**Function:** `no_permission_view(request)`

**Behavior:**
- Requires user to be logged in
- Renders 'no_permission.html'

These views are crucial for implementing role-based access control in the SSF application. They ensure that users are directed to appropriate pages based on their roles and permissions, and provide a mechanism for handling unauthorized access attempts.

**Remember:** This code is for testing purposes only. In a production environment, you should implement more robust authentication and authorization mechanisms, use secure password handling, protect against common web vulnerabilities, and follow Django's security best practices.

[Back to Table of Contents](#table-of-contents)

# Business Logic

## prel_results.py

**Purpose**

The Preliminary Round Results is designed to calculate scores for teams participating in a serie and suggest team constellations and competitors. This system allows teams to be evaluated based on their performance in multiple competitions across divisions, ensuring that competitors are optimally and legally assigned to teams within divisions and their rounds. The primary goal is to provide accurate and fair scoring, while also allowing for manual adjustments by the client before making the call.

**Overview**

The system includes functionality for:
- Retrieving eligible competitors for a given team.
- Calculating the top competitors based on specific scoring fields.
- Calculating the total score for a team.
- Fetching competitions that match certain criteria for a given round.
- Calculating preliminary round results, for every team in every division, within the dates of the round.

**Key Functions and Methods**

### `get_eligible_competitors(team, competitions)`

Retrieves eligible competitors for a given team and competitions.

**Args:**
- `team (Team)`: The team for which to retrieve competitors.
- `competitions (QuerySet)`: The competitions to consider.

**Returns:**
- `QuerySet`: A queryset of eligible competitors for the team.

### `get_top_competitors(competitors, limit_team_members, score_field)`

Fetches the top competitors based on the score field and limit of team members.

**Args:**
- `competitors (QuerySet)`: The competitors to select from.
- `limit_team_members (int)`: The maximum number of team members allowed.
- `score_field (str)`: The field used to order competitors by score.

**Returns:**
- `QuerySet`: A queryset of the top competitors.

### `calculate_team_score(team, competitions)`

Calculates the total score for a team based on eligible competitors.

**Args:**
- `team (Team)`: The team to calculate the score for.
- `competitions (QuerySet)`: The competitions to consider.

**Returns:**
- `tuple`: A tuple containing the total score and a queryset of the top competitors.

### `get_competitions_for_round(round_obj)`

Retrieves competitions that overlap with the round's date range and match the competition type.

**Args:**
- `round_obj (Round)`: The round object containing the date range and division information.

**Returns:**
- `QuerySet`: A queryset of competitions that match the criteria.

### `calculate_preliminary_round_results(round_obj)`

Calculates preliminary round results for a given round. Combines all previous functions to achieve this, but they can be used individually for other means.

**Args:**
- `round_obj (Round)`: The round object for which to calculate preliminary results.

**Returns:**
- `list`: A list of dictionaries containing the team, their score, and their competitors.



## insert_competitors.py

### `add_competitors_to_round_results(round_result_id, competitor_ids)`

This function is designed to add competitors to the `included_results` of a `RoundResult` and update the score accordingly. This is useful for dynamically managing the competitors contributing to a team's score in a specific round.

**Args:**
- `round_result_id (int)`: The ID of the `RoundResult` to update.
- `competitor_ids (list)`: A list of competitor IDs to add to the `included_results`.

**Usage Example:**

To add competitors to a round result and update the score, call the function with the appropriate round result ID and competitor IDs. This example is done with the browser console:

    fetch('http://127.0.0.1:8000/api/api_series/round_results/22/add_competitors/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        results_ids: []
      })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));


## utils.py

### `is_bench_only(competition_type)`

This function determines whether a given competition type is bench press only. It checks the disciplines associated with the competition type and returns `True` if there is only one discipline and that discipline is either 'bänkpress' or 'benchpress'.

**Args:**
- `competition_type (CompetitionType)`: The competition type to check.

**Returns:**
- `bool`: `True` if the competition type is for bench press only, `False` otherwise.

### `get_score_field(series, is_bench_press_only, gender)`
This function constructs the name of the score field to be used based on the series, whether the competition is bench press only, and the gender of the competitors.

**Args:**

- `series (Series)`: The series object containing the scoring system.
- `is_bench_press_only (bool)`: A flag indicating if the competition is bench press only.
- `gender (str)`: The gender of the competitors.
- `Returns`: str: The name of the score field to be used.





<br>
<br>
<br>
<br>

# Models

## Community Models 

[Back to Table of Contents](#table-of-contents)

## Model: Person


Represents an individual in the system.

**Fields:**
- `person_id` (CharField): Primary key, auto-generated UUID
- `first_name` (CharField): Person's first name
- `last_name` (CharField): Person's last name
- `gender` (CharField): Person's gender (choices: 'male', 'female')
- `email` (EmailField): Person's email address
- `social_security_nr` (CharField): Social security number in format "YYMMDD-XXXX"

**Methods:**
- `clean()`: Validates social security number format and date
- `age` (property): Calculates age based on social security number
- `license_nrs` (property): Returns list of associated lifter license numbers

**Validations:**
- Social security number must be in "YYMMDD-XXXX" format
- Date in social security number must be valid

## Model: Club

Represents a sports club.

**Fields:**
- `club_nr` (IntegerField): Primary key, 5-digit unique identifier
- `club_orgnr` (IntegerField): Unique organization number
- `club_phone` (CharField): Club's phone number
- `club_email` (EmailField): Club's email address
- `club_website` (CharField): Club's website URL
- `name` (CharField): Club's name
- `active` (BooleanField): Club's active status
- `paid` (BooleanField): Club's payment status
- `district` (ForeignKey): Associated District

**Validations:**
- Club number must be 5 digits between 10000 and 99999
- Organization number must be a positive integer
- Phone number must be in valid format
- Website must be a valid URL
- Club name must be at least 3 characters long

## Model: LifterLicense

Represents a lifter's license.

**Fields:**
- `license_nr` (CharField): Unique license number in format "initials + 5 digits + L"
- `person` (ForeignKey): Associated Person
- `status` (CharField): License status (choices: 'active', 'non-active', 'pending')
- `requested` (DateField): Date of license request
- `terminates` (DateField): Date of license expiry/termination
- `activated_date` (DateField): Date of license activation
- `paid` (BooleanField): Payment status
- `para` (BooleanField): Para-athlete status
- `ifn` (BooleanField): IFN status
- `club` (ForeignKey): Associated Club
- `club_membership_date` (DateField): Date of club membership
- `requested_year` (IntegerField): Year of license request

**Validations:**
- License number must be in correct format
- Activated date must be after requested date and before termination date
- Unique constraint on person, license number, and requested year

## Model: RefereeLicense

Represents a referee's license.

**Fields:**
- `referee_license_nr` (CharField): Unique referee license number
- `person` (ForeignKey): Associated Person
- `authority` (CharField): Licensing authority
- `referee_category` (CharField): Referee category
- `status` (CharField): License status (choices: 'active', 'non-active', 'pending')
- `requested` (DateField): Date of license request
- `terminates` (DateField): Date of license expiry/termination
- `activated_date` (DateField): Date of license activation
- `paid` (BooleanField): Payment status
- `club` (ForeignKey): Associated Club
- `club_membership_date` (DateField): Date of club membership
- `requested_year` (IntegerField): Year of license request

**Validations:**
- Unique constraint on person, referee license number, and requested year

## Model: District

Represents a district or region.

**Fields:**
- `RF_nr` (CharField): Primary key, unique identifier
- `district_name` (CharField): Name of the district
- `district_orgnr` (IntegerField): Unique organization number
- `district_phone` (CharField): District's phone number
- `district_email` (EmailField): District's email address
- `district_website` (CharField): District's website URL

## Model: Violation

Represents a violation report.

**Fields:**
- `report_id` (AutoField): Primary key, auto-incrementing ID
- `violation` (CharField): Description of the violation
- `repeal_start` (DateField): Start date of the repeal
- `repeal_end` (DateField): End date of the repeal
- `author_first_name` (CharField): First name of the report author
- `author_last_name` (CharField): Last name of the report author
- `description` (CharField): Detailed description of the violation
- `person` (ForeignKey): Associated Person (violator)

# Competition Models 

[Back to Table of Contents](#table-of-contents)

## Model: Discipline

Represents a specific discipline in powerlifting competitions.

**Fields:**
- `discipline` (CharField): Primary key, name of the discipline

## Model: AgeCategory

Represents an age category for competitions.

**Fields:**
- `title` (CharField): Primary key, name of the age category
- `lower_limit_age` (IntegerField): Lower age limit for the category
- `upper_limit_age` (IntegerField): Upper age limit for the category

## Model: WeightClass

Represents a weight class for competitions.

**Fields:**
- `upper_limit` (DecimalField): Upper weight limit for the class
- `lower_limit` (DecimalField): Lower weight limit for the class
- `title` (CharField): Unique title for the weight class
- `start_date` (DateField): Start date of the weight class's validity
- `end_date` (DateField): End date of the weight class's validity
- `gender` (CharField): Gender for the weight class (choices: 'male', 'female')

**Validations:**
- Start date must be before end date
- Weight limits must be between 30 and 120
- Difference between lower and upper limit must be at least 4
- Lower limit must be less than upper limit

## Model: CompetitionType

Represents a type of competition.

**Fields:**
- `competition_type_nickname` (CharField): Primary key, short name for the competition type
- `title` (CharField): Full title of the competition type
- `classic` (BooleanField): Indicates if it's a classic competition
- `para` (BooleanField): Indicates if it's a para competition
- `ifn` (BooleanField): Indicates if it's an IFN competition
- `disciplines` (ManyToManyField): Associated disciplines
- `weightclasses` (ManyToManyField): Associated weight classes

## Model: Competition

Represents a specific competition event.

**Fields:**
- `title` (CharField): Title of the competition
- `competition_category` (CharField): Category of the competition (e.g., SM, DM)
- `location` (CharField): Location of the competition
- `description` (CharField): Description of the competition
- `start` (DateField): Start date of the competition
- `end` (DateField): End date of the competition
- `reg_deadline` (DateField): Registration deadline
- `location_address` (CharField): Detailed address of the competition
- `contact_phone` (CharField): Contact phone number
- `contact_email` (EmailField): Contact email address
- `contact_name` (CharField): Name of the contact person
- `competition_type` (ForeignKey): Associated CompetitionType
- `club_orgnr` (ForeignKey): Associated Club
- `district_orgnr` (ForeignKey): Associated District
- `invitation` (FileField): Uploaded invitation file
- `registration_open` (BooleanField): Indicates if registration is open
- `live_stream` (URLField): URL for live stream of the competition

**Properties:**
- `is_registration_open`: Checks if registration is currently open

## Model: QualifyingWeight

Represents qualifying weights for a competition.

**Fields:**
- `minimum` (IntegerField): Minimum qualifying weight
- `qualifying_period_start` (DateField): Start of qualifying period
- `qualifying_period_end` (DateField): End of qualifying period
- `competition` (ForeignKey): Associated Competition
- `age_category` (ForeignKey): Associated AgeCategory
- `weight_class` (ForeignKey): Associated WeightClass

## Model: Group

Represents a group within a competition.

**Fields:**
- `title` (CharField): Title of the group
- `speaker` (CharField): Name of the group's speaker
- `secretary` (CharField): Name of the group's secretary
- `competition` (ForeignKey): Associated Competition

## Model: RefereeAssignment

Represents the assignment of a referee to a group.

**Fields:**
- `service` (CharField): Type of service provided
- `referee_license` (ForeignKey): Associated RefereeLicense
- `group` (ForeignKey): Associated Group

# Scoring Models 

[Back to Table of Contents](#table-of-contents)

## Model: Result

Represents the result of a lifter in a competition.

**Fields:**
- `body_weight` (DecimalField): The body weight of the lifter
- `date` (DateField): Date of the result
- `lot_nr` (IntegerField): Lot number of the lifter
- `placement` (IntegerField): Placement of the lifter in the competition
- `group` (ForeignKey): Associated Group
- `license_nr` (ForeignKey): Associated LifterLicense
- `weight_class` (ForeignKey): Associated WeightClass
- `age_category` (ForeignKey): Associated AgeCategory
- Various score fields for WILKS, IPFGL, and DOTS calculations (DecimalField)
- `squat` (DecimalField): Best squat weight
- `benchpress` (DecimalField): Best bench press weight
- `deadlift` (DecimalField): Best deadlift weight
- `total` (DecimalField): Total weight lifted

**Methods:**
- `calculate_scores()`: Calculates and updates all score fields based on the lifts

## Model: Lift

Represents an individual lift attempt in a competition.

**Fields:**
- `try_nr` (IntegerField): Attempt number
- `result` (ForeignKey): Associated Result
- `discipline` (ForeignKey): Associated Discipline
- `weight` (DecimalField): Weight lifted
- `goodlift` (BooleanField): Indicates if the lift was successful

**Methods:**
- `validate()`: Performs validation checks on the lift
- `get_previous_lifts()`: Retrieves all previous lifts in the same discipline for the same result

**Signals:**
- `update_result_scores`: Updates the associated Result's scores when a Lift is saved

# Serie Models

[Back to Table of Contents](#table-of-contents)

## Model: Series

Represents a series of competitions.

**Fields:**
- `serie_id` (CharField): Primary key, unique identifier for the series
- `title` (CharField): Title of the series
- `series_type` (CharField): Type of the series
- `year` (IntegerField): Year of the series
- `scoring_system` (CharField): Scoring system used (WILKS, IPF2020, IPFGL, DOTS)
- `gender` (CharField): Gender category (male, female)
- `competition_type_nickname` (ForeignKey): Associated CompetitionType
- `age_categories` (ManyToManyField): Associated AgeCategories

## Model: Division

Represents a division within a series.

**Fields:**
- `division_id` (CharField): Primary key, unique identifier for the division
- `title` (CharField): Title of the division
- `limit_teams` (IntegerField): Maximum number of teams allowed
- `limit_team_members` (IntegerField): Maximum number of members per team
- `series` (ForeignKey): Associated Series
- `teams_moving_up` (IntegerField): Number of teams moving up from this division
- `teams_moving_down` (IntegerField): Number of teams moving down from this division

## Model: Team

Represents a team participating in a division.

**Fields:**
- `title` (CharField): Name of the team
- `paid` (BooleanField): Indicates if the team has paid
- `division` (ForeignKey): Associated Division
- `club` (ForeignKey): Associated Club

## Model: Round

Represents a round of competition within a division.

**Fields:**
- `start` (DateField): Start date of the round
- `end` (DateField): End date of the round
- `division` (ForeignKey): Associated Division

## Model: RoundResult

Represents the results of a team in a specific round.

**Fields:**
- `team` (ForeignKey): Associated Team
- `round` (ForeignKey): Associated Round
- `included_results` (ManyToManyField): Associated Results
- `score` (DecimalField): Total score for the round

**Methods:**
- `update_score()`: Updates the score based on included results

**Signals:**
- `update_score_on_change`: Updates the score when included_results are changed

# URLs, views & routing
This bulletpoint explains how views in the project are connected to routers/urls and how to add new views step-by-step.

### Structure
SSF/urls.py: Imports
- home views from SSF_app/views, collected in the init file of the folder
- routers with urls for api calls from SSF_app.routers. Each router, containing views, is collected and given its own path in the init file of the folder.
- landing and login views from SSF_app/urls
   
### How It Works Together
**Request Flow:**
 When a user navigates to /community/, the SSF/urls.py file directs the request to the included URL patterns from SSF_app. The imported views and routers matches the path and calls the views. The view will execute, process the request and return a response. 

### Example of Adding a view and give it a URL
To add a new URL to your project, follow these steps:

1. Define a New View: Create a new view in the views folder.
In the project, we have divided our views into their own files, and imported them to the init file instead. In the example, we define our new view in a new file, but it is fine to include your new view in the existing view file and include the new view in its corresponding router. However, be mindful of the route that is given in step 3 (and skip steps thereafter).

```python
# SSF_app/views/new_view.py
from django.shortcuts import render

def new_view(request):
    return render(request, 'new_template.html')
```
2. Import the New View in views/__init__.py (might not be needed, see bulletpoint 2.11. in TO-DO):

```python
# SSF_app/views/__init__.py
from .new_view import new_view
```
3. Define a URL Pattern for the New View: Add a new URL pattern in the router file.

```python
# SSF_app/router/new_urls.py
from rest_framework.routers import DefaultRouter
from SSF_app.views.new_view import new_view

a_router = DefaultRouter()
a_router.register(r'our_new_view', new_view)
urlpatterns = a_router.urls
```
4. Gather the New Router in __init__.py: Include the new router in the __init__.py file of the router folder.

```python
# SSF_app/router/__init__.py
from SSF_app.routers.new_urls import a_router
urlpatterns = [
    path('choose_a_slug/', include(a_router.urls))
]
```
5. Include the New Router in the Main urls.py: Ensure the new URL pattern is included in the project's main urls.py file.

```python
# SSF_project/urls.py
from django.contrib import admin
from django.urls import path, include
from SSF_app.router import all_urlpatterns as SSF_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('some_slug/', include(SSF_app_urls)),
]
```
