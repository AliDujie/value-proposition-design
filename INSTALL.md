# Installation Guide — Value Proposition Design Skill

## Prerequisites

- Python 3.9 or higher
- Git

## Installation Steps

### Option 1: OpenClaw Skills Directory (Recommended)

```bash
# Clone the repository
git clone https://github.com/AliDujie/value-proposition-design.git

# Copy to your OpenClaw skills directory
cp -r value-proposition-design ~/.openclaw/skills/
```

### Option 2: Custom Skills Directory

```bash
# Clone the repository
git clone https://github.com/AliDujie/value-proposition-design.git

# Copy to your agent's skills directory
cp -r value-proposition-design /your/agent/skills/
```

### Option 3: As a Python Package

```bash
cd value-proposition-design
pip install -e .
```

## Verify Installation

```python
import sys
sys.path.insert(0, "/path/to/value-proposition-design")
from vpd import VPDSkill

# Quick test
skill = VPDSkill("Test Product", "Test Audience")
print("Value Proposition Design Skill installed successfully! ✓")
```

## Dependencies

- Python >= 3.9
- **No external dependencies** (pure standard library)
- Compatible with macOS, Linux, and Windows

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'vpd'` | Ensure the skill directory is in your Python path |
| Import errors | Verify Python version is 3.9+ |
| Permission denied | Check file permissions on the skill directory |
