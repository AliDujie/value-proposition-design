# Installation Guide / 安装指南 — Value Proposition Design Skill

## Prerequisites / 前置要求

- Python 3.9 or higher / Python 3.9 或更高版本
- Git

## Installation Steps / 安装步骤

### Option 1: OpenClaw Skills Directory (Recommended) / 方式一：OpenClaw 技能目录（推荐）

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/value-proposition-design.git

# Copy to your OpenClaw skills directory / 复制到 OpenClaw 技能目录
cp -r value-proposition-design ~/.openclaw/skills/
```

### Option 2: Custom Skills Directory / 方式二：自定义技能目录

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/value-proposition-design.git

# Copy to your agent's skills directory / 复制到你的 Agent 技能目录
cp -r value-proposition-design /your/agent/skills/
```

### Option 3: As a Python Package / 方式三：作为 Python 包安装

```bash
cd value-proposition-design
pip install -e .
```

## Verify Installation / 验证安装

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

# Quick test / 快速测试
skill = VPDSkill("Test Product", "Test Audience")
print("Value Proposition Design Skill installed successfully! ✓")
# 价值主张设计技能安装成功！✓
```

## Dependencies / 依赖

- Python >= 3.9
- **No external dependencies** (pure standard library) / **无外部依赖**（纯标准库）
- Compatible with macOS, Linux, and Windows / 兼容 macOS、Linux 和 Windows

## Troubleshooting / 故障排查

| Issue / 问题 | Solution / 解决方案 |
|-------|----------|
| `ModuleNotFoundError: No module named 'vpd'` | Ensure the skill directory is in your Python path / 确保技能目录在 Python 路径中 |
| Import errors / 导入错误 | Verify Python version is 3.9+ / 确认 Python 版本为 3.9+ |
| Permission denied / 权限被拒绝 | Check file permissions on the skill directory / 检查技能目录的文件权限 |

## Related Skills / 相关技能

This skill is part of the AliDujie UX Research ecosystem:
本技能是 AliDujie UX 研究生态系统的一部分：

- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — JTBD 发现的"工作"映射到 VPD 价值主张画布
- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — UDM 生成阶段方法可与 VPD 画布结合
- [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — VPD 价值假设可用 QuantUX 实验验证
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — Persona 客户画像可直接用于 VPD 画布
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — VPD 实验结果可交给 SWD 进行数据叙事
