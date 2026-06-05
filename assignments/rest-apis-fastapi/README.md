# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework in Python, including defining routes, handling request data with Pydantic models, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI App

#### Description
Set up a FastAPI application with a root endpoint and run it locally using Uvicorn.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define a `GET /` endpoint that returns a JSON welcome message
- Be runnable with `uvicorn main:app --reload`
- Example response:
  ```json
  { "message": "Welcome to the FastAPI assignment!" }
  ```

### 🛠️ Add CRUD Endpoints for a Resource

#### Description
Expand the API by adding endpoints to create, retrieve, and delete items from an in-memory list.

#### Requirements
Completed program should:

- Define a `GET /items` endpoint that returns the full list of items
- Define a `POST /items` endpoint that adds a new item to the list and returns it
- Define a `DELETE /items/{item_id}` endpoint that removes an item by its ID
- Return appropriate status codes (e.g., `404` if item not found)

### 🛠️ Validate Requests with Pydantic Models

#### Description
Use Pydantic to define a data model for items and enforce input validation on the `POST /items` endpoint.

#### Requirements
Completed program should:

- Define a `Pydantic` `BaseModel` class called `Item` with at least `id` (int), `name` (str), and `description` (str) fields
- Use the `Item` model as the request body type for `POST /items`
- Return a `422 Unprocessable Entity` error automatically when required fields are missing or have the wrong type
- Example request body:
  ```json
  { "id": 1, "name": "Notebook", "description": "A lined paper notebook" }
  ```
