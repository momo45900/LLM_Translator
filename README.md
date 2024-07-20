# Flask Groq Translation App

## Description

A Flask application that uses LangChain and Groq to provide translation services via a RESTful API.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Setup


    

1. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Obtain an API Key**:
   - Visit the [Groq website](https://www.groq.com/) to sign up and obtain your API key.

5. **Create a `.env` file** in the root directory and add your API key:
    ```plaintext
    GROQ_API_KEY=your_api_key_here
    ```

6. **Run the application**:
    ```bash
    python app.py
    ```

## Using Postman to Test the API

1. **Open Postman** and create a new request.

2. **Set the request type** to `POST`.

3. **Enter the URL** for your local API:
    ```
    http://127.0.0.1:5000/tran
    ```

4. **In the request body**, select `raw` and `JSON` format, then enter the following JSON data:
    ```json
    {
        "language": "en",
        "text": "Hello, world!"
    }
    ```

5. **Send the request** and observe the response. You should receive a JSON response with the translated text.

## Example Response

- **Success Response**:
    ```json
    {
        "status": 200,
        "translation": "Your translation here",
        "msg": "Translation successful"
    }
    ```

- **Error Response** (e.g., missing fields):
    ```json
    {
        "status": 400,
        "msg": "Missing 'language' or 'text' in request body"
    }
    ```


