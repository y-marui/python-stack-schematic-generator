# AI_CONTEXT.md

## Project Overview

Python library for generating schematic diagrams of multilayer (stack) structures using matplotlib.

- **Language:** Python 3.12+
- **Build:** hatchling / uv
- **Linting:** ruff
- **Type checking:** mypy
- **Testing:** pytest

### Key Directories

| Path | Contents |
|---|---|
| `stack_schematic_generator/` | Library source: `stack.py`, `layer.py`, `coordinate.py` |
| `tests/` | pytest tests |
| `docs/dev-charter/` | Shared dev charter (git subtree from y-marui/dev-charter) |

## Applied Charter Principles

憲章参照: `docs/dev-charter/CHARTER_INDEX.md` でトピックを特定してから該当ファイルのみ読む

- Code style: `docs/dev-charter/CODE_STYLE.md`
- AI collaboration rules: `docs/dev-charter/AI_COLLABORATION_RULES.md`
- Security: `docs/dev-charter/SECURITY_POLICY.md`
- Python dev env: `docs/dev-charter/topics/PYTHON_DEV_ENV.md`
- CI policy: `docs/dev-charter/topics/CI_POLICY.md`
- GitHub settings: `docs/dev-charter/topics/GITHUB_SETTINGS.md`

## Project-Specific Rules

- テストは `tests/conftest.py` で `matplotlib.use("Agg")` を設定し、ディスプレイなしで実行する
- `matplotlib-extension` は PyPI 未公開のため git URL で直接参照する
- `stack_schematic_generator/test_stack.py` は使用例スクリプト（pytest 対象外）

## AI Tool Assignments

- **Claude Code:** 機能追加・リファクタリング・CI 設定
- **GitHub Copilot:** 補完・微修正

## Prohibited Actions

- シークレット・認証情報のコミット
- `plt.show()` を含むテストの追加（ヘッドレス環境で失敗する）
