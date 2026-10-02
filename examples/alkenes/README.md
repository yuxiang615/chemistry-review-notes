# Example — 烯烃：从多轮返工到稳定的结构/反应版式

**状态**：这是设计、绘图与训练范例；v0.7 全章仍有复杂立体产物与跨章题需要进一步验证，不应被当作化学答案标准库。

## 本例提供的可迁移资产

- `draw_molecules.py`：独立原创的 RDKit 黑白 SVG/PDF 生成器，普通分子统一输出参数；运行后得到 `assets/`。
- `dual_mode_sample.tex`：XeLaTeX 双版本最小范例：**真实结构→命名；给定真实底物+目标→独立默写整条反应式；答案在同一题位**。不引入 PPT 截图。
- `docs/FAILURE_ANALYSIS_ALKENES.md`：v0.2–v0.7 的反例（更重要的是说明失败原因）。
- `docs/DRAWING_AND_LATEX_PIPELINE.md` 与 `docs/EXERCISE_DESIGN_REACTIONS.md`：绘图、反应式、机理题和 PDF 验收。

## 正确学习方法

1. 首先对比旧章练习/答案的**实际页面**，不要只看本 README。
2. 保留第三章的结构→异构→命名→稳定性→HX/水合/卤素/硼氢化→氧化→烯丙位→制备→综合主线。
3. 练习版给真实底物和目标/反应任务；答案版同题位补**带条件箭头、实际产物和必要中间体**。
4. 普通分子黑白矢量画法统一；复杂几何/立体结构人工修图并核对。
5. 对用户认可的前一版本只做局部补丁，检查分页改变后的相邻页；没必要大改成功的版式。

## 独立运行最小例子

```sh
python -m pip install rdkit cairosvg
python draw_molecules.py
xelatex dual_mode_sample.tex
xelatex -jobname=answers "\\def\\ANSWERS{1}\\input{dual_mode_sample.tex}"
```

在本目录中运行；第二次会生成答案版。XeLaTeX 需已安装 `ctex`、`mhchem`、`graphicx`、`amsmath` 和标准中文字体。环境不同需设置可用 CJK 字体。
