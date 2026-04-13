# Stack Schematic Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/ci.yml)
[![Charter Check](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/dev-charter-check.yml/badge.svg)](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/dev-charter-check.yml)

Python library for generating schematic diagrams of multilayer (stack) structures using matplotlib.

## Requirements

- Python 3.12+
- matplotlib 3.10+

## Setup

```bash
pip install git+https://github.com/y-marui/python-stack-schematic-generator.git
```

For development:

```bash
git clone https://github.com/y-marui/python-stack-schematic-generator.git
cd python-stack-schematic-generator
uv sync
```

## Usage

```python
from stack_schematic_generator.stack import Stack
from stack_schematic_generator.layer import Layer
import matplotlib.pyplot as plt

with plt.style.context(['matplotlib_extension.article', 'stack_schematic_generator.stack_schematic']):
    stack = Stack([
        Layer("Si Sub.", "lightgray"),
        Layer("SiO$_2$ (100)", "lightgray"),
        Layer("W (3)", "dodgerblue"),
        Layer("CoFeB (1)", "orangered"),
        Layer("MgO (2)", "lightgray"),
        Layer("Ta (1)", "lightgray"),
    ])
    stack.plot()
    plt.show()
```

<div align="center">
    <img src="docs/W_CoFeB.png" width="200">
</div>

Wedge-shaped layers using the `slope` parameter:

```python
with plt.style.context(['matplotlib_extension.article', 'stack_schematic_generator.stack_schematic']):
    stack = Stack([
        Layer("Si Sub.", "lightgray"),
        Layer("SiO$_2$ (100)", "lightgray"),
        Layer("W (1-5)", "dodgerblue", height=0.5, slope=1),
        Layer("CoFeB (1)", "orangered"),
        Layer("MgO (2)", "lightgray"),
        Layer("Ta (1)", "lightgray"),
    ])
    stack.plot()
    plt.show()
```

<div align="center">
    <img src="docs/W_CoFeB_grad.png" width="200">
</div>

### Development Commands

| Command | Description |
|---|---|
| `uv run pytest` | Run tests |
| `uv run ruff check .` | Lint |
| `uv run ruff format .` | Format |
| `uv run mypy stack_schematic_generator/` | Type check |

## License

[MIT](LICENSE)
