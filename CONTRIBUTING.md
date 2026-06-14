# Contributing Guide / 贡献指南

Thank you for your interest in contributing to Value Proposition Design Skill!
感谢你对价值主张设计技能的贡献！

## How to Contribute / 如何贡献

### 📚 Content Contributions / 内容贡献

- **Add new VPD tools**: Customer profile templates, value map frameworks / 添加新的 VPD 工具：客户画像模板、价值地图框架
- **Improve method descriptions**: Clarify usage scenarios, prerequisites, or outputs / 改进方法描述：澄清使用场景、前提条件或产出
- **Add real-world examples**: Practical case studies for VPD canvas creation / 添加真实案例：VPD 画布创建的实践案例
- **Translate content**: Help make this skill accessible in more languages / 翻译内容：帮助本技能支持更多语言

### 🔧 Code Contributions / 代码贡献

- **Fix bugs**: Report and fix issues in the `vpd/` module / 修复 bug：报告和修复 vpd/ 模块中的问题
- **Add features**: New canvas generators, fit assessment tools / 添加功能：新的画布生成器、契合度评估工具
- **Improve performance**: Optimize value proposition analysis / 提升性能：优化价值主张分析
- **Add tests**: Ensure reliability of the toolkit / 添加测试：确保工具包的可靠性

### 📝 Documentation / 文档贡献

- **Improve README**: Clearer instructions, better examples / 改进 README：更清晰的说明，更好的示例
- **Add tutorials**: Step-by-step guides for VPD canvas creation / 添加教程：VPD 画布创建的分步指南
- **Update references**: Keep VPD frameworks current and accurate / 更新参考文档：保持 VPD 框架的准确性和时效性

## Development Setup / 开发环境

```bash
# Clone the repository / 克隆仓库
git clone https://github.com/AliDujie/value-proposition-design.git
cd value-proposition-design

# Install in development mode / 安装开发模式
pip install -e ".[dev]"

# Run tests / 运行测试
pytest

# Lint code / 代码检查
ruff check .
```

## Pull Request Process / PR 流程

1. Fork the repository / Fork 仓库
2. Create a feature branch (`git checkout -b feature/amazing-feature`) / 创建功能分支
3. Make your changes / 进行修改
4. Run tests and linting / 运行测试和代码检查
5. Commit with descriptive messages / 使用描述性的提交信息
6. Push to your fork and submit a PR / 推送到你的 Fork 并提交 PR

## Code Style / 代码规范

- Follow PEP 8 guidelines / 遵循 PEP 8 规范
- Use type hints for new code / 新代码使用类型标注
- Add docstrings for all public functions / 为所有公共函数添加文档字符串
- Keep line length under 100 characters / 行长度不超过 100 字符

## Related Skills / 相关技能

When contributing, consider how VPD fits into the broader AliDujie UX Research ecosystem:

- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — JTBD 发现的"工作"映射到 VPD 价值主张画布
- [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — UDM 生成阶段方法可与 VPD 画布结合
- [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — VPD 价值假设可用 QuantUX 实验设计验证
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — Persona 客户画像可直接用于 VPD 画布
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — VPD 实验结果可交给 SWD 进行数据叙事
- [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — VPD 商业决策可用 STM 战略框架支撑

---

*By contributing, you agree that your contributions will be licensed under the MIT License.*
*通过贡献，你同意你的贡献将在 MIT 许可下授权。*
