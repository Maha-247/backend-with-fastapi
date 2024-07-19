# Virtual Candy Store

As a owner of the virtual candy store, I want customers to taste different varieties of candies and give us their feedback.
I do that by handing them a random set of candies and track their level of enjoyment
Level of enjoyment is predicted by how quickly they lick through and finish the candy or bite into it.

## Project Setup

1. Fork and then clone the repository
2. The project has two broad folders:
   - `frontend` : Contains the frontend code (ReactJS)
   - `backend` : Contains the backend code (FastAPI)

## Frontend

1. Navigate to the `cd frontend` folder
2. Install the dependencies using `npm install`
3. Run the frontend server using `npm start`

> For this session we are not worried about frontend. We will focus on the backend part of the application.

## Backend

1. Navigate to the `cd backend` folder
2. create a virtual environment using `python3 -m venv venv`
3. Activate the virtual environment using `source venv/bin/activate`
4. Install the dependencies using `pip install -r requirements.txt`
5. Run the backend server using `fastapi dev main.py`

## Accessing the Application

Once you have both running, hit `http://localhost:3000/` in your browser and start playing around

## Concepts

# What is CORS?

Imagine you've built a backend with data collected with hours of effort, you write a UI and expose the APIs. It all goes well until your competitor decides to use your APIs in their application.

You might ask "What about Authentication?". When you go to browser's network tab and explore the requests, you see the tokens/headers used to make the request. Your competitor can easily copy the headers and use them in their application.

This is where CORS comes into play. CORS stands for Cross-Origin Resource Sharing. This feature helps backend APIs restrict access based on the origin of the request aka the URL.

For example, if your backend is hosted at `http://localhost:8000` and your frontend is hosted at `http://localhost:3000`, the backend can restrict access to only requests coming from `http://localhost:3000`.

## How to handle CORS in FastAPI?

FastAPI provides a middleware to handle CORS. You can enable CORS by adding the following code to your FastAPI application.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

In the above code, we are allowing requests from `http://localhost:3000` with credentials, methods `GET` and `POST` and headers `*` (everything).
