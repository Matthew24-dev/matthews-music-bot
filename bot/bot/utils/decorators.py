from functools import wraps


def errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] {func.__name__}: {e}")

    return wrapper


def authorized_only(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        # Add authorization checks here later if needed.
        return await func(client, message, *args, **kwargs)

    return wrapper