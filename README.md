# API Deployment

FastAPI is a modern web framework for building APIs with Python. To deploy this FastAPI application, you have several options depending on your needs and infrastructure. Here are some common deployment methods:

## 1. Local Development and Testing

1 Install dependencies: Make sure you have installed all the required dependencies by creating a virtual environment and installing the necessary packages. You can use the `pip` for this.

```bash
pip install -r requirements.txt
```

Run the application: In your terminal, navigate to the root directory of your FastAPI application and use `uvicorn` to run the application.

```bash

uvicorn main:app --reload

```

The `main` is the name of the Python file containing the FastAPI application, and `app` is the instance of the FastAPI application.

3\. Test the API: With the application running, open your web browser or API client (e.g., Postman) and access the API at `http://localhost:8000` (or a different port if specified). Test the API endpoints to ensure everything is working as expected.
