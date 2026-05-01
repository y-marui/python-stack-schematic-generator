## How to Contribute

For large changes (new features, design changes), please open an issue before submitting a PR.
Small bug fixes and typos can be submitted directly as a PR.

## Development Setup

See [DEVELOPING.md](DEVELOPING.md) for build, test, and code style instructions.

## Pull Request Checklist

- [ ] No secrets or credentials included
- [ ] Lint passes (`uv run ruff check .`)
- [ ] Type checks pass (`uv run mypy stack_schematic_generator/`)
- [ ] Tests pass (`uv run pytest`)
- [ ] New features include tests
- [ ] User-facing changes are documented
