# Multithreading

## Concepts

### What is Multithreading?

Multithreading allows multiple tasks to run concurrently inside a single process.

Example:

- Downloading files
- Handling multiple users in a server
- Background notifications
- File uploads

---

## Thread

A thread is the smallest unit of execution within a process.

Example:

Browser Process
├── UI Thread
├── Network Thread
└── Rendering Thread

---

## Thread Lifecycle

1. New
2. Runnable
3. Running
4. Waiting / Blocked
5. Terminated

Example:

Create Thread
    ↓
Start Thread
    ↓
Running
    ↓
Waiting (sleep)
    ↓
Finished

---

## Creating Threads

```python
import threading

def task():
    print("Running")

t = threading.Thread(target=task)
t.start()
t.join()