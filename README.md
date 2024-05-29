# Re-Ranker API

## Overview

The Re-Ranker API is a simple API for ranking documents based on their relevance to a given question. As a
note of importance, this project assumes a secure environment where sensitive data will not be handled.

**No additional security measures are included in this API**, as it is designed to operate within a trusted
perimeter.

This project uses FastAPI and Sentence Transformers to rank documents using a cross-encoder model.

## How to use

### Prerequisites

* Python 3.11 or greater
* pip
* virtual environment (recommended)
* A secure environment

To get started with the Re-Ranker API, you'll need to have Python 3.11 or greater installed on your system.
Once you have Python set up, follow these steps:

### Step 1: Create and activate a Virtual Environment

The best way to manage dependencies for this project is by using a virtual environment (venv). To create a
new venv, run the following command in your terminal:

```shell
python -m venv myenv
```

Replace `myenv` with the name you want to give your virtual environment. Then, activate it:

```
source myenv/bin/activate
```

### Step 2: Install dependencies

With your venv activated, install the required packages by running:

```shell
pip install -r requirements.txt
```

This will install all the necessary dependencies for the project.

### Step 3: Start the API

Once you have the dependencies installed, start the API by running:

```
python3 -m uvicorn main:app --host localhost --port 8000
```

This will start the API on port 8000 and make it available at `http://localhost:8000`.

### Step 4: Send a POST request to rank documents

To send a POST request to the `/rank` endpoint, you can use any HTTP client tool such as curl or Postman.
Here's an example of how you could do this using curl:

```shell
curl -X POST \
  http://localhost:8000/rank \
   -H 'Content-Type: application/json' \
   -d '{"question": "What is the capital of France?", "documents": ["The Eiffel Tower is located in Paris,
France.", "Montreal is the capital of Canada."]}''
```
When you send a POST request to the `/rank` endpoint, you can expect to receive a JSON object in the
following format sorted on the scores, higher is better:
```json
[
  {"corpus_id": 0, "score": "0.843489"},
  {"corpus_id": 2, "score": "0.725346"},
  {"corpus_id": 1, "score": "0.435645"}
]
```
This JSON object contains an array of objects, each representing a document with its corresponding relevance
score. The `corpus_id` field is the ID of the document sent in the request, and the `score` field is the
calculated relevance score between 0 and 1.
