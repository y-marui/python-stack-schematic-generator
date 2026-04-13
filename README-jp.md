# Stack Schematic Generator

> **このファイルは正本（日本語版）です。**
> 英語版（参照）は [README.md](README.md) を参照してください。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/ci.yml)
[![Charter Check](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/dev-charter-check.yml/badge.svg)](https://github.com/y-marui/python-stack-schematic-generator/actions/workflows/dev-charter-check.yml)

matplotlib を使って多層膜（スタック）構造の模式図を簡単に生成するための Python ライブラリ。

## Requirements

- Python 3.12+
- matplotlib 3.10+

## Setup

```bash
pip install git+https://github.com/y-marui/python-stack-schematic-generator.git
```

開発環境のセットアップ：

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

`slope` パラメータを使ったくさび形レイヤー：

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

| コマンド | 説明 |
|---|---|
| `uv run pytest` | テスト実行 |
| `uv run ruff check .` | リント |
| `uv run ruff format .` | フォーマット |
| `uv run mypy stack_schematic_generator/` | 型チェック |

## License

[MIT](LICENSE)

---
*この文書には英語版 [README.md](README.md) があります。編集時は同一コミットで更新してください。*
