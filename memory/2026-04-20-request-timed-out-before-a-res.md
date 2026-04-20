# Session: 2026-04-20 06:04:25 UTC

- **Session Key**: agent:main:main
- **Session ID**: 751939d6-46fe-4885-87a5-0f02e6c300ea
- **Source**: webchat

## Conversation Summary

user: System: [2026-04-20 14:00:38 GMT+8] Gateway restart update ok (npm)
System: Run: openclaw doctor --non-interactive

Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Mon 2026-04-20 14:01 GMT+8] https://github.com/AliDujie/jtbd-knowledge-skill 请完整下载并安装一下这个skill，以后跟JTBD相关的任务，都调用这个skill来完成任务。
assistant: ✅ **JTBD Skill 安装完成！**

已成功下载并安装 `jtbd-knowledge` skill 到 `~/.openclaw/skills/jtbd-knowledge/`。

## 📦 技能概览

这是一个基于 Alan Klement《When Coffee and Kale Compete》的 **JTBD（Jobs to Be Done）理论与实践执行技能**，包含：

### 🔧 8 大执行能力
1. **生成 JTBD 访谈提纲** - 结构化用户深度访谈框架
2. **设计 JTBD 调查问卷** - 筛选型/验证型/竞争型问卷模板
3. **计算 JTBD 机会分数** - 四维度评估模型（挣扎强度/替代方案满意度/市场规模/预算可获取性）
4. **输出优先级矩阵** - 多 Job/需求排序与行动建议
5. **JTBD 竞争分析** - 识别真正竞争对手 + 四力对比
6. **生成 JTBD 营销文案** - 基于挣扎/进步/焦虑/惯性的文案框架
7. **增长与留存策略** - 流失原因分类 + 习惯设计
8. **JTBD 描述生成与验证** - 标准化 Job 描述 + 质量验证

### 📚 知识库
- 11 份 Markdown 文档覆盖理论基础→研究方法→分析框架→创新指南→案例研究
- 完整的 Python API（`jtbd` 包）：`JTBDAnalyzer`、`InterviewBuilder`、`ForcesProfile`、`InnovationFinder`

---

**以后所有 JTBD 相关任务**（用户访谈、问卷设计、机会评估、竞争分析、营销文案、增长策略等），我都会调用这个skill 来执行。

需要我现在测试一下吗？比如帮你生成一个 JTBD 访谈提纲？
