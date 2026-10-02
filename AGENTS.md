# Agent instructions — Chemistry Review Notes

These instructions apply to every future code/LaTeX editing agent working in this repository.

1. Read `SKILL.md` and `PROMPT.md` first. The **2026-10-02 priority additions** take precedence over older conflicting advice.
2. Then read `docs/FAILURE_ANALYSIS_ALKENES.md`, `docs/EXERCISE_DESIGN_REACTIONS.md`, `docs/DRAWING_AND_LATEX_PIPELINE.md`, `docs/PROVENANCE_AND_ASSETS.md` and `docs/REVIEW_CHECKLIST.md`.
3. Study `examples/alkanes-cycloalkanes/CASE_STUDY.md`, `examples/stereochemistry/CASE_STUDY.md`, and `examples/alkenes/README.md`; **open actual paired legacy practice/answer PDFs if and only if actually available**. A descriptive README cannot substitute for visual review of real pages.
4. Treat the supplied **course PPT as the chemistry-content scope**, and the user's latest confirmed chapter version as the **layout/content baseline**. Avoid changing successful pages for stylistic imitation of another chapter.
5. Every important rule must be complete enough for the exercise and adjacent to specific chemical structures. No all-text lecture; no too-sparse one-sentence/giant-blank question.
6. Exercise vs answers is a hard separation. Never put an answered PPT screenshot in student exercises. For reaction recall, provide a concrete substrate and goal/class and let the learner write reagents, conditions, intermediates and final products; also include separate migration questions where reagents are supplied.
7. Use uniform black-and-white vector molecule drawings (RDKit for ordinary 2D, Ketcher/manual for atypical ring/stereochemical diagrams, chemfig/TikZ for reaction layout/explicit electron arrows). Put reagents and conditions **on arrows**, draw requested structures/mechanisms for real.
8. Use tables only when appropriate. Leave real handwriting space for entire equations; repeat table headers only when materially useful. No decorative colored boxes or duplicated rectangles nested inside blank table cells.
9. Same source controls practice+answer. For every task, audit source PPT page, corresponding exercise/answer task ID, actual chemical answer, and visible PDF rendering. Render **every page**; compiler success is not a visual or chemistry proof.
10. Maintain internal chapter-plan/coverage/QA records **outside** student-facing PDFs. When chemistry is uncertain, record `needs independent verification`, not an invented teacher answer.
11. Do not silently claim missing reference PDF or generated assets exist; see `docs/PROVENANCE_AND_ASSETS.md`. Do not copy unvetted third-party repositories or proprietary fonts.
12. Finalize a chapter only with the user's explicit approval. In every new revision, compare changed pages with the last user-approved baseline and preserve the stable knowledge architecture.
