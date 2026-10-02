# 《立体化学》v5.2：可复现源码及原始归档

此目录来自本项目对话中用户提供的 **《记忆默写复习回顾06 · 立体化学》v5.2 原始 LaTeX 源码 ZIP**，不是《烷烃与环烷烃》。按**文件实际内容**归档。压缩包中包含主源码、练习/答案两个入口和课堂 A–D 图片。另在 `../reference/` 保存此前用户提供的两版 PDF 成品。

## 目录与原件
- [立体化学_master_v5.2.tex](立体化学_master_v5.2.tex)：原始主源码，练习/答案共用。
- [练习版入口](记忆默写复习回顾06_立体化学_练习版_v5.2.tex)：对主文件的 `\input`。
- [答案版入口](记忆默写复习回顾06_立体化学_答案版_v5.2.tex)：设置 `\ANSWERS` 后加载主文件。
- `assets/p20_A.png`～`p20_D.png`：四张课件课堂题图片，来自用户上传包；请核实分享权限后再迁移到其他公开项目。
- [original-source-v5.2.zip](original-source-v5.2.zip)：**字节完全一致**的原始上传压缩包。

## 编译

需安装 XeLaTeX、ctex 中文字体、`mhchem`、`chemfig`、TikZ 等包。在本目录（即源码及 `assets` 的共同父目录）执行：

```bash
xelatex -interaction=nonstopmode -halt-on-error 记忆默写复习回顾06_立体化学_练习版_v5.2.tex
xelatex -interaction=nonstopmode -halt-on-error 记忆默写复习回顾06_立体化学_答案版_v5.2.tex
```

交叉引用或书签若有变动，各再运行一次。仓库内已有真实参考成品：
- [练习版 PDF](../reference/v5.2-practice.pdf)（15 页）
- [答案版 PDF](../reference/v5.2-answers.pdf)（16 页）

## 验证与使用范围

- 本次实际解包、从源码编译练习与答案，两版均成功；重编译 PDF 的逐页提取文本与存档成品匹配。
- **保留原件不改动**：这次只做归档，不替用户改写上一章化学内容。
- 后续新章应同时阅读实际 PDF 配对页与这份可编辑源码，观察 `\Fischer`/`\FischerTwo`/`\Newman` 自定义宏、题目表格、答案条件编译和高分辨率课堂图布局。不要机械照搬颜色和短横线；以 [烯烃失败经验](../../../docs/FAILURE_ANALYSIS_ALKENES.md) 的防回归要求为准。

原始上传 ZIP SHA256：`9963c8ba1ec404460f6a5af46d49da5989f32583d139025f3e66b48ea43ebf4b`
