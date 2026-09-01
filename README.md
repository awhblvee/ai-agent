# AI Agent

This is a toy version of Claude Code.

> **WARNING:** This is not meant to be run like Claude Code — it does not have the same guardrails. **Run this with caution.**

## Requirements

- [uv](https://docs.astral.sh/uv/) installed
- Python 3.13+ (pinned in `.python-version` and `pyproject.toml`'s `requires-python`) — uv will fetch this automatically if you don't already have it

## Dependencies

Declared in `pyproject.toml`, installed automatically by `uv run` / `uv sync`:

- `openai==2.44.0` — used as a generic client pointed at OpenRouter's API, not OpenAI directly
- `python-dotenv==1.1.0`

## Setup

Create a `.env` file in the project root with your OpenRouter API key:

```
OPENROUTER_API_KEY='your openrouter api key'
```

## How to run

```
uv run main.py "your prompt here"
uv run main.py "your prompt here" --verbose
```

## Scope / working directory

The agent's working directory is set to `./calculator` — it can only read, write, list, and execute files inside that directory, and can't touch anything else on your filesystem. If you want it to operate somewhere else, change `WORKING_DIRECTORY` in `config.py`.

## The `calculator/` directory

`calculator/` is a test dummy for the agent to work against. For example, you can break something in `calculator/pkg/calculator.py` and ask the agent to fix it — it'll inspect, diagnose, and edit files within whatever directory you've set as its working directory.
