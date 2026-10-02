# 化学结构绘图及 LaTeX 排版技术路线

## 工具分工：不要用一个工具画所有东西

| 内容 | 首选 | 注意 |
|---|---|---|
| 普通链状、环状、支链底物与产物 | [RDKit](https://github.com/rdkit/rdkit) 的 MolDraw2DSVG，输出 SVG，再转 PDF | 统一黑白线条、固定字号、显式甲基；输入 SMILES 必须核对碳骨架和连接 |
| 桥环、螺环、特殊立体结构 | [Ketcher](https://github.com/epam/ketcher) 人工调整后导出矢量文件 | 指定编号、键连位置、楔线必须对照课件；自动结构清理不能替代人工核查 |
| 化学式、离子、试剂和箭头标签 | [mhchem](https://ctan.org/pkg/mhchem) `\ce{...}` | 不用一行缩小字号的分子式冒充二维结构 |
| 箭头、机理曲箭头、Fischer/Newman/楔线专项 | [chemfig](https://ctan.org/pkg/chemfig) / TikZ | 电子箭头用**正确的起点和终点锚点**；自由基鱼钩与双电子箭头区分 |
| 实在难以准确重画的特殊课堂题 | 精准 PPT 裁图 | 只裁题目结构；练习版严禁截入红字答案、优先级着色、最终产物 |

> 参考外部开源项目的**用法与文档链接**，不整库拷贝第三方源码/字体/未核实许可素材。README 的工具资源清单是本仓库离线导航入口，后续无需重新搜索。

## 规范执行顺序

1. 扫描课件并建立结构资源清单：题号、页码、底物、条件、关键立体关系。
2. 所有明确结构先在化学对象层建模（SMILES、Molfile 或人工绘图）；不要先随手画 SVG 再猜结构。
3. 生成 SVG（可编辑）和 PDF（给 XeLaTeX 嵌入）；普通结构全章统一黑白，分子图大小只在明确类型层级差异时变化。
4. **化学审查一**：通过 RDKit 分子读取/立体标记提示排查，人工核对 SMILES 的连接、环大小、键序及原料/产物。
5. **立体审查二**：几何 E/Z、R/S、meso、楔/虚楔及 syn/anti 是否与课件和机理一致；镜像关系不能仅凭缩略图判别。
6. 在 LaTeX 里把底物、带条件反应箭头、产物排在**同一反应表达式**里；中间体另以明确步骤连接。
7. 按“命名/画结构/完整反应式/多步机理”**分别**设计行高和留白。答案版测量左右两列最高内容。
8. XeLaTeX 编译后整份渲染到 PNG：检查图中文字大小、键线深浅、条件在箭头上、注释不碰分隔线，尤其分页前后。
9. 对没有自动可验证化学含义的特殊结构，记录人工审查人/依据；不把“SMILES 可解析”误认为结构一定正确。

## 可复现的绘图参数（供起步，实际仍需按 PDF 视觉调节）

```python
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

m = Chem.MolFromSmiles("CC=C")       # 丙烯，仅为示例
assert m is not None
Chem.AssignStereochemistry(m, cleanIt=True, force=True)
rdDepictor.Compute2DCoords(m)
d = rdMolDraw2D.MolDraw2DSVG(310, 190)
o = d.drawOptions()
o.useBWAtomPalette()
o.bondLineWidth = 2.0
o.explicitMethyl = True
o.fixedFontSize = 23
o.padding = 0.10
d.DrawMolecule(m)
d.FinishDrawing()
open("propene.svg", "w", encoding="utf-8").write(d.GetDrawingText())
```

`cairosvg.svg2pdf(url="propene.svg", write_to="propene.pdf")` 可生成 LaTeX 用的 PDF（在脚本中导入 cairosvg）。
实际脚本及可编译范例见 `examples/alkenes/`。

## 化学反应的正确排布（不要“结构在上，试剂散落下方”）

```tex
\begin{tabular}{@{}c@{\;}c@{\;}c@{}}
\includegraphics[width=2.6cm]{assets/propene.pdf}
& $\xrightarrow{\substack{\ce{Br2 / H2O}}}$
& \includegraphics[width=2.7cm]{assets/bromohydrin.pdf}
\end{tabular}
```

一般模板只保证图形对齐，**不保证**该反应的化学选择性；答案结构须另行复核。条件太长时采用 `\substack` 或上下两行但必须属于箭头标签。

## 常见不可接受的出图 bug

- PPT 原图印着答案却放在练习版。
- 左图浅灰小得看不清，右图大黑粗：必须使用同一输出风格和视觉校准。
- 写“应画出反式产物”而没有真实楔线产物。
- “浓热酸性 KMnO₄”散放在图下而没有指向的反应箭头。
- table 只测答案高度，不测左侧题干图及其条件，线与字重叠。
- 一页缩略图看上去没问题，放大 200% 后发现化学键、甲基或箭头相撞。
