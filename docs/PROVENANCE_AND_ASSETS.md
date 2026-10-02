# 来源、成品与素材归档规则

## 资料的权威顺序

1. 当前课程 PPT、教师课堂题原始结构和条件（课程范围主干）。
2. 用户在该章的明确保留/删除/重点/误区/排版反馈。
3. 经用户认可的**当前章冻结基线**（修改必须以它为起点）。
4. 已完成章节的 PDF 成品（只学题型与视觉标准；不是新章的化学事实来源）。
5. 必要的化学知识与绘图工具资料；**补充/更正与 PPT 原句清楚区分**。

## 2026-10-02 已完成归档：立体化学 v5.2

`examples/stereochemistry/source_v5.2/` 已实际上传用户提供的**原 ZIP 与拆开的 LaTeX 源码、练习/答案入口和全部 4 张课堂图**；`examples/stereochemistry/reference/` 已实际上传用户早先提供的 15 页练习版和 16 页答案版 PDF。存储状态已用 Git blob SHA 与本地 `git hash-object` 对照。详见 `examples/stereochemistry/source_v5.2/README.md`。

**尚未完成的其他项目归档**：烷烃 v5.1 PDF、烯烃 v0.5/v0.7 完整 PDF/资源包仍需分别核实 GitHub 的实际文件存在性。本条只改变立体化学 v5.2 的状态，不代表所有参考资料已存齐。

## 第三章当前基线

- **v0.5** 获得明确正向确认：章节骨架、黑白矢量图、按动作留空白；后续 v0.6/0.7 只能在其基础上修订，不能“为追求新版本”推倒既有好页。
- **v0.7 仍需逐题复核**复杂立体化学与跨章答案；它是修改史与可复用技术来源，不可假装“通过编译=化学最终正确”。
- 本仓库的 `examples/alkenes/` 提供原创、可重跑的绘图和双版本演示；**它不是 v0.7 全本 PDF 的复制品**。

## 为什么要保存“真实旧章 PDF”，而不是只留文字 README

旧版《烷烃与环烷烃》v5.1、《立体化学》v5.2 的练习/答案配对页，在**结构大小、题位是否泄露答案、规则紧贴实图、机理分步空间、长名称留空与图线粗细**方面包含 README 无法呈现的隐性约束。新章如果拿不到这些真实成品，就必须先申报缺口，禁止声称已实物对照。

### 建议固定路径（只在文件实际上传并核对后才称已归档）

- `examples/alkanes-cycloalkanes/reference/v5.1-practice.pdf`
- `examples/alkanes-cycloalkanes/reference/v5.1-answers.pdf`
- `examples/stereochemistry/reference/v5.2-practice.pdf`
- `examples/stereochemistry/reference/v5.2-answers.pdf`
- `examples/alkenes/reference/v0.5-practice.pdf` 与 `v0.5-answers.pdf`（获认可的版式基线）
- `examples/alkenes/reference/v0.7-practice.pdf`、`v0.7-answers.pdf`、`v0.7-source.zip`（历史工作稿，需化学复核）

**状态约定**：在本路径下文件实际存在前不得在 README 中写成“已上传”。保留来源、日期、版权和化学验证状态。存放源 PPT 之前先确认使用许可，公开仓库不自动上传课程原件。

## 体积/权限与文件检查

优先保存 .tex/.py/.md/可编辑矢量资产与必要的参考 PDF；禁止上传临时渲染、反复重复版本或第三方项目完整源码。提交后通过 GitHub 文件目录和 SHA 实际核实。完整二进制 PDF 若当前连接只能直接接收 UTF-8 文件，不能凭聊天中的 sandbox 路径伪造 GitHub 归档；另行利用已授权的 Git 终端或支持二进制的提交方式上传，文件列表须在上传成功后更新。

## 官方工具导航

- RDKit：<https://github.com/rdkit/rdkit>；绘图 API：<https://www.rdkit.org/docs/source/rdkit.Chem.Draw.rdMolDraw2D.html>
- Ketcher：<https://github.com/epam/ketcher>
- chemfig：<https://ctan.org/pkg/chemfig>
- mhchem：<https://ctan.org/pkg/mhchem>
- TikZ/PGF：<https://ctan.org/pkg/pgf>
- PDF 人工检查：整份渲染成图后逐页放大，复杂结构不能凭仅有文字提取进行核对。

这些是**外部工具指引**，不是把外部仓库的代码或文件未经许可复制进本项目。
