# issues-tracker

FastAPI backend for tracking issues.

## Middleware

Middleware setup is kept in `app/middlewares/`:

- `cors.py` configures CORS for local frontend origins.
- `process_time.py` adds the `X-Process-Time` response header.

`app/main.py` imports and registers these middlewares before including API routes.
