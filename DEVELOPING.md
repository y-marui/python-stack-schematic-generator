# Developing

This guide is for developers working on the library itself.
For contribution rules and PR/Issue process, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Setup

```bash
git clone https://github.com/y-marui/python-stack-schematic-generator.git
cd python-stack-schematic-generator
uv sync
```

## Development Commands

| Command | Description |
|---|---|
| `uv run pytest` | Run tests |
| `uv run ruff check .` | Lint |
| `uv run ruff format .` | Format |
| `uv run mypy stack_schematic_generator/` | Type check |

## Code Style

Follow [docs/dev-charter/CODE_STYLE.md](docs/dev-charter/CODE_STYLE.md).

- Linting and formatting: **ruff** (`pyproject.toml` `[tool.ruff]`)
- Type checking: **mypy** (`pyproject.toml` `[tool.mypy]`) — all public functions and methods must have type annotations

## Conventions

- Tests run headless: `tests/conftest.py` sets `matplotlib.use("Agg")`. Do not add tests that call `plt.show()`.
- `stack_schematic_generator/test_stack.py` is a usage example script, not a pytest target.
- Commit messages: [Conventional Commits](https://www.conventionalcommits.org/) format (`fix: ...`, `feat: ...`).
