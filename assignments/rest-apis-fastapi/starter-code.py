from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Define a Pydantic model called `Item` with id (int), name (str), and description (str) fields


# In-memory list to store items
items = []


# TODO: Define a GET / endpoint that returns a welcome message


# TODO: Define a GET /items endpoint that returns all items


# TODO: Define a POST /items endpoint that adds a new item to the list


# TODO: Define a DELETE /items/{item_id} endpoint that removes an item by its ID
