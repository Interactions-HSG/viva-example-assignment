"""The examples you develop against. The marks do not come from these."""

from limiter import RateLimiter


class Clock:
    """A clock the test moves by hand, so nothing has to sleep."""

    def __init__(self, t: float = 1000.0) -> None:
        self.t = t

    def __call__(self) -> float:
        return self.t

    def tick(self, seconds: float) -> None:
        self.t += seconds


def test_the_allowance_is_spent_and_then_refused():
    limiter = RateLimiter(limit=3, window=60, now=Clock())
    assert [limiter.allow("alice") for _ in range(4)] == [True, True, True, False]


def test_a_refusal_does_not_cost_the_client_anything():
    clock = Clock()
    limiter = RateLimiter(limit=1, window=60, now=clock)
    limiter.allow("alice")
    for _ in range(10):
        limiter.allow("alice")          # refused, over and over
    clock.tick(61)
    assert limiter.allow("alice") is True


def test_the_allowance_comes_back():
    clock = Clock()
    limiter = RateLimiter(limit=2, window=60, now=clock)
    assert limiter.allow("alice") and limiter.allow("alice")
    assert limiter.allow("alice") is False
    clock.tick(61)
    assert limiter.allow("alice") is True


def test_clients_do_not_share_an_allowance():
    limiter = RateLimiter(limit=1, window=60, now=Clock())
    assert limiter.allow("alice") is True
    assert limiter.allow("bob") is True
    assert limiter.allow("alice") is False


if __name__ == "__main__":
    for name, case in sorted(globals().items()):
        if name.startswith("test_"):
            case()
            print(f"ok  {name}")
