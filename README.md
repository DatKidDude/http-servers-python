# Minimal HTTP Servers in Python

This repository contains three minimal HTTP server implementations in Python, organized by abstraction level and complexity. The goal is to explore how different layers of Python's standard library build up from raw sockets to higher-level HTTP handling.

## Project Structure

<pre><code>
├── http-servers-python/
│   ├── http_server/
|   |     └── server.py/
│   ├── socketserver_server/
|   |     └── server.py/
│   ├── raw_socket_server/
|   |     └── server.py/
</code></pre>

---

## Server Implementations

### 1. `http_server/`

- Uses Python's built-in `http.server` module.
- Easiest to set up, minimal code.
- Automatically handles request parsing and basic HTTP response formatting.

### 2. `socketserver_server/`

- Uses `socketserver.TCPServer` and `BaseRequestHandler`.
- Manual response formatting.
- Teaches how to work closer to the socket layer while keeping the event loop abstracted.

### 3. `raw_socket_server/`

- Uses the `socket` module directly.
- Full control over connections, request parsing, and HTTP response structure.
- Best for understanding how HTTP works over TCP.

---

## Purpose

This project is educational in nature. It's designed to:

- Practice reading and applying Python standard library documentation.
- Understand the layers of abstraction in network programming.
- Build progressively deeper understanding of how HTTP works over sockets.

---

## Running the Servers

Navigate into each folder and run the `server.py` file:

```bash
cd http_server
python server.py
```

---

## Credits

This challenge is inspired by [CodingChallenges](https://www.codingchallenges.com) "Build Your Own Web Server"

This repository is my implementation and learning journey through those challenges.

Link to challenge: [Build Your Own Web Server](https://codingchallenges.fyi/challenges/challenge-webserver)
