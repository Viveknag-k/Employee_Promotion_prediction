# Architecure

![Architecture](https://github.com/user-attachments/assets/4afb45cf-f9cc-402e-b5dc-69a5f4e1ba7b)
'''diff
The architecture for the Employee Promotion Prediction system integrates multiple technologies, including FastAPI for the backend and Streamlit for the frontend, effectively combining machine learning and modern web frameworks to deliver a scalable solution. At the core of the system lies a Machine Learning (ML) model that has been trained on employee data, including features like employee ID, number of trainings, age, previous year’s performance rating, length of service, awards won, and average training score. This model is loaded in the FastAPI backend, which acts as the server-side API responsible for receiving client requests, processing the data, and returning predictions.

## Backend - +FastAPI :
FastAPI, a modern, high-performance web framework for building APIs with Python, serves as the API backend. When a client, in this case, the Streamlit frontend, sends a HTTP request (typically a POST or GET request with employee details), FastAPI processes the input and passes the data to the machine learning model. The prediction is packaged into a JSON response and returned to the Streamlit app through the same API request-response pipeline. FastAPI's ability to handle asynchronous requests efficiently ensures low-latency responses even when handling multiple client requests simultaneously.

## Frontend - -Streamlit:
On the frontend, Streamlit acts as the user interface for the Employee Promotion Prediction application. Streamlit is highly popular for quickly building and deploying data science and ML web apps. The interface collects user inputs (e.g., employee details) and sends the data to the FastAPI server through an HTTP request. Streamlit interacts with the backend by sending API calls to the FastAPI server’s URL. The FastAPI server, after processing the request, sends a JSON response back, containing the model's prediction on whether the employee will be promoted.

### Communication:
The system is designed to follow a clear client-server architecture. The Streamlit app (client) makes an API call to FastAPI (server) via a request URL, sending data using HTTP methods like GET or POST. Upon receiving the request, FastAPI processes the data and returns a response in the form of response.json, which Streamlit parses and displays to the user. This separation of concerns ensures that the machine learning logic is encapsulated in the backend (FastAPI), while the frontend focuses solely on interacting with the end-user, making the system modular, scalable, and easy to maintain.'''
