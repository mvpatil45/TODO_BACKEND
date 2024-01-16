# Todo Backend

This is the backend for a Todo List application built using Django and Django Rest Framework. It provides API endpoints for managing tasks, including CRUD (Create, Read, Update, Delete) operations.

## Features

1. **Task Validation:** Ensure proper validation for tasks to meet specified criteria.

2. **Avoiding Duplicate Tasks:** Implement measures to prevent the creation of duplicate tasks.

3. **Automatic Refreshing of APIs:** Ensure that APIs automatically refresh after performing CRUD operations to reflect the latest changes.

4. **Responsive Design:** The backend supports responsiveness, catering to both laptop and mobile users.

5. **Video Player with Playback Support:** Integrate a video player within the application that supports playback functionalities.

## Setup

To set up the backend, follow these steps:

1. Install required Python packages:

    ```bash
    pip install django djangorestframework django-cors-headers
    ```

2. Run database migrations:

    ```bash
    python manage.py migrate
    ```

## API Endpoints

- **Create Todo:**
  - Endpoint: `http://127.0.0.1:8000/api/create`
  - Method: POST

- **Read All Todos:**
  - Endpoint: `http://127.0.0.1:8000/api`
  - Method: GET

- **Detail/Update Todo:**
  - Endpoint: `http://127.0.0.1:8000/api/${ID}`
  - Method: GET, PUT

- **Delete Todo:**
  - Endpoint: `http://127.0.0.1:8000/api/delete/${ID}`
  - Method: DELETE

Replace `${ID}` with the specific ID of the todo you want to retrieve, update, or delete.

## Frontend Repository

Check out the [Todo Frontend Repository](https://github.com/mvpatil45/TODO_FRONTEND) for the frontend code.

Feel free to customize and expand the backend according to your project requirements.
