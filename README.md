# An example assignment, and what makes it examinable

The half of a worked example that **students copy**: an ordinary IT assignment — a
per-client rate limiter — set up so that [viva-cologna][viva] can examine a
submission of it. The other half, [viva-example-solution][solution], is what the course
keeps to itself — it is private, so that link is a 404 unless you set the assignment.

[viva]: https://github.com/Interactions-HSG/viva-cologna
[solution]: https://github.com/Interactions-HSG/viva-example-solution

| | |
|---|---|
| **[`ASSIGNMENT.md`](ASSIGNMENT.md)** | What to build. The examiner reads it as the brief you were given. |
| **[`limiter.py`](limiter.py)** | Where the work goes. One method, one decision in it. |
| **[`test_limiter.py`](test_limiter.py)** | The examples you develop against. They are not where the marks come from. |
| **[`viva.yml`](viva.yml)** | What you are examined on — the learning objectives, and the name of the brief the exam server holds. What it deliberately does not hold is listed in it, with the reason. |

## What you do

1. **Use this template**, into your own account, private.
2. Give the examiner **Read** access.
3. Work, and **commit as you go**. The examiner reads `git log`, `diff` and
   `show` and asks how the work evolved — one squashed commit gives it much
   less to ask about, and gives you much less to talk about.
4. Sit the viva at <https://wiser-sp4.interactions.ics.unisg.ch> against the
   commit you want marked. Everything it reads — your code, your history and
   `viva.yml` — is read **at that commit**, not at the tip of your branch.
5. The viva commits its own record — `.viva/token.json`, `.viva/turns.json`,
   `.viva/transcript.md` — on top of the commit you defended. Hand in **that
   commit**, not the repository.

```bash
python3 test_limiter.py     # no dependencies, no toolchain
```

## What the viva is actually about

Not whether the tests pass. They run on cases you have already seen, and
passing them is the beginning of the exercise rather than the end of it.

`allow` has a decision in it that the tests here do not reach, a clock behind
it that no test can catch, and it accumulates something per client that nobody
ever clears. A viva is a conversation about decisions like those: what you
chose, what you rejected, and what your code does in the case you did not
write a test for. It is much easier to have that conversation about code you
understand than about code that merely passes.

## Why the brief is in two halves

`viva.yml` is in your copy, so anything written in it is something you can read
before you are asked it. That is fine for the **learning objectives** — knowing
what you are examined on is not knowing what you will be asked, and it is only
fair that you can see it — so they are here, and you can check them yourself:

```bash
node app/src/lint.js .        # from a viva-cologna checkout
```

Everything else would spoil the exam. What the examiner is told to steer at,
the questions it always puts word for word, and the reference solution live on
the exam server instead, in a **solution** named by the `assignment:` line. The
solution wins field by field, so editing this file changes nothing about the viva
you sit — it only stops it finding the right brief.

[viva-example-solution][solution] is that other half, and it exercises every field the
interface has. [viva-cologna's README][viva] is the interface as a whole.
