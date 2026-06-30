from time import perf_counter

from fastapi import Request, Response


async def add_process_time_header(request: Request, call_next) -> Response:
    start_time = perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{perf_counter() - start_time:.3f}"
    return response
