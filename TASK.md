# A rate limiter for the API (example task)

The API in front of you is being hammered by a handful of clients, and the
team has settled on the crudest fix that works: **no client gets more than
`limit` requests in any `window` seconds.** Everything else — what a client
is, what happens to the requests you turn away, how the limit is configured —
is already decided and is not your problem.

Your problem is `limiter.py`, and one method in it.

## What to do

1. **`RateLimiter.allow(client)`** — return `True` if this request is within
   the client's allowance and `False` if it is not. A rejected request does
   not count against the client's allowance.
2. Two clients must not share an allowance.
3. `python3 test_limiter.py` must pass. It drives a fake clock, so the tests
   run instantly and do not sleep.

The class takes the clock as an argument (`now`) rather than reading it
directly. That is what lets the tests wind time forward — treat it as given,
but do notice which clock the default is.

## What you are marked on

Not that the tests pass — they run on cases you have already seen. You are
marked on whether you can explain what you built, in a viva, against the
commit you hand in.

Three things worth being able to answer before you sit it:

- A client sends its whole allowance at the very end of one window, then its
  whole allowance again at the start of the next. How many requests did it
  actually get through, and over what stretch of time?
- Which clock are you reading, and what happens to a client the next time the
  machine's time is corrected by a few seconds?
- What does your limiter hold in memory after a million different clients have
  each sent one request?

## Handing in

Work in your own private copy, and commit as you go — the examiner reads your
history and asks how the work evolved, so one squashed commit gives it much
less to ask about. Then sit the viva against the commit you want marked.
