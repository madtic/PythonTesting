# Fork of PythonTesting
by S2510828014 | Thomas.Schaetz  & S2510828016|Tichelmann Michael

## Branches:
- [main] fork of [PythonTesting](https://github.com/V3RO/PythonTesting)
- [Vorlesung] code aus der Vorlesung
- [Hausaufgabe] Hausaufgabe Connect 4 Pair Programming Lösen

# Testing and TDD with Python

Exercises for learning unit testing and test-driven development with [pytest](https://docs.pytest.org).

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```bash
uv sync
uv run pytest
```

## Layout

| Exercise | Code | Tests |
|---|---|---|
| Exploration (pytest, mocks, fakes) | `src/testing_course/exploration/` | `tests/exploration/` |
| Bowling kata | `src/testing_course/bowling/` | `tests/bowling/` |
| Connect Four (TDD) | `src/testing_course/connect_four/` | `tests/connect_four/` |

## Useful commands

```bash
uv run pytest tests/bowling      # one exercise
uv run pytest -k spare           # tests matching a name
uv run pytest --cov              # coverage
uv run ruff check                # lint
uv run ruff format               # format
uv run ty check                  # type check
uv run connect-four              # play Connect Four
```
