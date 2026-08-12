"""Per-client rate limiting for the API.

The plumbing is not the exercise. Configuration, what a client id is, and what
the caller does with a refusal are all settled; `allow` is the part that has a
decision in it.
"""

from time import time


class RateLimiter:
    """No more than `limit` requests per client in any `window` seconds."""

    def __init__(self, limit: int, window: float, now=time) -> None:
        self.limit = limit
        self.window = window
        # Injected so the tests can wind the clock forward instead of sleeping.
        self.now = now
        self.seen: dict[str, object] = {}

    def allow(self, client: str) -> bool:
        """True if this request is within the client's allowance."""
        raise NotImplementedError
