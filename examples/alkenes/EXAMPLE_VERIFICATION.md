# 可复现最小样张：验证范围与非验证范围

当前 GitHub 实际包含 `draw_molecules.py` 和 `dual_mode_sample.tex`，前者为 5 个常规分子输出黑白 SVG/PDF，后者通过同一源码的 `\ifanswers` 切换形成一张**结构→名称**和一张**起始物+目标→独立写完整两步反应式**的示例页面。

2026-10-02 已在准备环境中做过真实运行：5 张 SVG/PDF 可生成，XeLaTeX 两种模式各编译出 1 页；PDF 已渲染检查结构与留白。这个小样只证明普通分子可矢量绘制、答案在相同题位、整体反应留空，**不是**烯烃全部机理与复杂立体结构的校验。

运行：

```sh
cd examples/alkenes
python -m pip install rdkit cairosvg
python draw_molecules.py
xelatex -interaction=nonstopmode -halt-on-error -jobname=practice dual_mode_sample.tex
xelatex -interaction=nonstopmode -halt-on-error -jobname=answers '\def\ANSWERS{1}\input{dual_mode_sample.tex}'
pdftoppm -png -r 180 practice.pdf practice
pdftoppm -png -r 180 answers.pdf answers
```

视觉验收：两版都确实显示具体分子；练习版**没有目标反应试剂和中间体答案**，只留全宽空白；答案版显示带试剂条件的两个连续反应箭头。根据纸张实际打印尺寸放大或缩小图像宽度。

完整第三章原工作稿：`source_v0.7/master_v0.7.tex`、`source_v0.7/build_assets.py`、`source_v0.7/postprocess_assets.py`。此源码包需要额外课堂环系 PNG 和未完全核实的答案审查；**不能把示例成功推定为全章正确**。
