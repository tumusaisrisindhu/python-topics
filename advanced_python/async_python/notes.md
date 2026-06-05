# Async Python Notes

## What is Async Programming?

Async programming allows Python to perform other work while waiting for a task to finish.

Example:

Waiting for:

- API Response
- Database Query
- File Download

Instead of sitting idle, Python can execute another task.

---

## async

Creates a coroutine function.

```python
async def hello():
    print("Hello")
```

---

## await

Pauses execution until a task finishes.

```python
await asyncio.sleep(2)
```

Unlike:

```python
time.sleep(2)
```

await does not block the whole program.

---

## Coroutine

A function created using:

```python
async def
```

Example:

```python
async def fetch_data():
    pass
```

---

## Event Loop

The brain of async programming.

Responsibilities:

- Start tasks
- Pause tasks
- Resume tasks
- Complete tasks

Python uses:

```python
asyncio.run()
```

to start the event loop.

---

## asyncio.gather()

Runs multiple tasks concurrently.

```python
await asyncio.gather(
    task1(),
    task2(),
    task3()
)
```

All tasks start together.

---

## asyncio.create_task()

Runs a task in background.

```python
task = asyncio.create_task(send_email())
```

Useful when other work should continue.

---

## When to Use Async

✓ API Calls

✓ Web Scraping

✓ Database Queries

✓ Chat Applications

✓ Real-time Systems

✓ Network Requests

---

## When NOT to Use Async

✗ Heavy CPU Calculations

Example:

```python
for i in range(100000000):
    pass
```

Use:

- Multiprocessing
- Parallel Processing

instead.

---

## Interview Questions

### What is async?

A way to write non-blocking code.

### What is await?

Waits for an async task to complete.

### What is a coroutine?

A function defined using async def.

### What is an event loop?

A manager that schedules async tasks.

### What is asyncio.gather()?

Runs multiple coroutines concurrently.

### What is asyncio.create_task()?

Starts a task in the background.

---

## Quick Revision

async → Create coroutine

await → Wait for coroutine

asyncio.run() → Start event loop

gather() → Run many tasks together

create_task() → Background task

aiohttp → Async API requests