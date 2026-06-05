# Multi-threaded Downloader

A simple Python project demonstrating multithreading by downloading multiple files simultaneously.

## Concepts Covered

- threading module
- Thread creation
- start()
- join()
- Concurrent execution
- File handling
- I/O-bound tasks

## Project Structure

```text
mini_project_multithreaded_downloader/
│
├── downloader.py
├── urls.txt
├── downloads/
└── README.md
```

## How It Works

1. Read URLs from urls.txt
2. Create one thread per URL
3. Start all threads
4. Download files concurrently
5. Wait for all downloads to finish

## Run

```bash
python downloader.py
```

## Sample Output

```text
Downloading file1...
Downloading file2...
Downloading file3...

Completed file1
Completed file2
Completed file3

All downloads completed
```

## What I Learned

- Creating threads
- Running concurrent tasks
- Using join()
- Managing I/O-bound operations
- Building a real-world multithreaded application