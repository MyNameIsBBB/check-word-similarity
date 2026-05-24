# FastAPI backend

## Install

```bash
py -m pip install -r requirements.txt
```

## Run

```bash
py main.py
```

The API will be available at `http://127.0.0.1:8000`.

Alternative:

```bash
py -m uvicorn main:app --reload
```

## Endpoints

- `GET /`
- `GET /health`
- `GET /api/hello/{name}`
- `GET /api/check-word/similarity?word1=cat&word2=kitten`
- `POST /api/check-word/similarity`

## Semantic similarity API

This endpoint uses the Hugging Face model `sentence-transformers/all-MiniLM-L6-v2`
to compare two words or short phrases and return how related they are as a percentage.

If you cannot send headers, use the `GET` version with query parameters:

```text
http://127.0.0.1:8000/api/check-word/similarity?word1=cat&word2=kitten
```

If you want to use `POST`, you can send either JSON body or query parameters.

Example POST with query params:

```text
POST http://127.0.0.1:8000/api/check-word/similarity?word1=cat&word2=kitten
```

Example POST body:

```json
{
  "word1": "cat",
  "word2": "kitten"
}
```

Example response:

```json
{
  "word1": "cat",
  "word2": "kitten",
  "model": "sentence-transformers/all-MiniLM-L6-v2",
  "similarity_score": 0.82,
  "similarity_percent": 82.0
}
```

The first request may take longer because the model is downloaded from Hugging Face.

Interactive docs:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`
