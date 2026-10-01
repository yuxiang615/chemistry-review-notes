# Chemistry Review Notes

一套用于把**课程 PPT + 逐页讨论**整理成 LaTeX 化学复习资料的长期工作规范。

目标不是“把 PPT 重新写一遍”，而是把课件重构成：

- **练习版**：结构识别、命名、判断、转换、画图、反应与综合题，强调主动回忆。
- **答案版**：与练习版一一对应，给出答案与必要的短解释。
- **LaTeX 源码**：可持续修改、复用、版本化。
- **覆盖核对**：保证 PPT 中有价值的结构、分子、课堂题、命名、老师强调的形式不因重组而遗漏。

## 新对话怎么开始

新章节建议第一句话直接使用：

> 请先读取 GitHub 仓库 `yuxiang615/chemistry-review-notes` 中的 `SKILL.md`、`PROMPT.md` 和 `docs/REVIEW_CHECKLIST.md`，按其中规范整理我接下来上传的化学 PPT。我们会先逐页讨论并记录保留/删除/补充/易错点，再生成 LaTeX 练习版和答案版。不要把 PPT 复述成讲义。

然后上传新的 PPT 即可。

## 仓库结构

```text
chemistry-review-notes/
├── README.md
├── SKILL.md                     # 总规范：以后优先读这个
├── PROMPT.md                    # 新对话可直接复制的启动提示词
├── docs/
│   ├── WORKFLOW.md              # 从 PPT 到最终 PDF 的完整工作流
│   ├── REVIEW_CHECKLIST.md      # 多轮审查与最终收尾门槛
│   ├── STYLE_GUIDE.md           # 题型、文字、LaTeX 与化学结构排版规范
│   ├── EXAMPLE_STUDY.md         # 新章节如何学习旧章例子而不机械复制
│   └── LESSONS_LEARNED.md       # 从已完成章节总结出的经验与反例
├── templates/
│   ├── chapter-plan.md          # 每章讨论/设计记录模板
│   └── coverage-checklist.md    # PPT 逐页覆盖核对模板
└── examples/
    ├── alkanes-cycloalkanes/
    │   └── README.md
    └── stereochemistry/
        ├── README.md
        └── layout-snippets.tex   # Fischer/Newman/表格等可复用排版片段
```

## 当前基准

已完成并验证过的两类范式：

1. **烷烃与环烷烃**  
   强项：结构→命名、规则表格、画图区、反应式完整输出、练习版/答案版一致。

2. **立体化学 v5.2**  
   强项：Fischer / Newman / 锯架 / 椅式结构，CIP 与 R/S 完整命名，易错点嵌入对应题目，结构图逐页渲染检查，经过多轮从“讲义式”重构为“主动回忆式”。

核心原则：

> **少复述，多输出；少抽象定义，多具体结构；少花哨框，多清晰表格；不怕页数长，只怕结构看不清。**


## 使用原则

这个仓库是后续化学整理的**权威规范来源**。新对话不需要依赖聊天记忆，也不需要重新解释以前的要求；先读取这里的规范和例子，再处理新 PPT。