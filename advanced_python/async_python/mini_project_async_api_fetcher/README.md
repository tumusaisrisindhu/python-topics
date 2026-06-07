# Async API Fetcher

A mini project built while learning:

- Async Python
- asyncio
- await
- Event Loop
- aiohttp
- Concurrent API Requests

## Features

- Fetch multiple APIs concurrently
- Faster than sequential requests
- Error handling
- Clean modular structure

## Project Structure

```text
async_api_fetcher/
│
├── app.py
├── fetcher.py
├── urls.py
├── requirements.txt
└── notes.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Example Output

```text
FETCHED DATA

ID: 1
TITLE: sunt aut facere repellat provident

ID: 2
TITLE: qui est esse

ID: 3
TITLE: ea molestias quasi exercitationem
```

## Concepts Practiced

- async
- await
- asyncio.gather()
- Event Loop
- aiohttp ClientSession
- Concurrent Execution
