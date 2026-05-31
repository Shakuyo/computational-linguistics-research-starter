# Computational Linguistics Research Starter

This repository is a reproducible starter project for computational linguistics, corpus linguistics, and corpus-assisted discourse analysis.

It began as a small register-comparison demo and has been expanded toward a more research-oriented use case: media discourse, framing, stance, source attribution, and lexical pattern analysis.

## Thesis-Inspired Direction

The project is inspired by an undergraduate graduation thesis titled:

> A Critical Discourse Analysis of The Straits Times' Narratives on the Belt and Road Initiative

The thesis examined The Straits Times' Belt and Road Initiative coverage from 2021 to 2024 using corpus-assisted analysis and close reading. This public repository does not include the private thesis file, copyrighted news articles, or local research data. Instead, it provides reusable open scaffolding for similar research workflows.

## What This Repo Helps With

- Build a clean small corpus workflow.
- Generate descriptive lexical metrics.
- Generate keyword-in-context lines for close reading.
- Generate simple collocate tables around target terms.
- Keep a literature seed table with journal-backed research anchors.
- Convert literature metadata into a method blueprint.
- Use a starter annotation codebook for media framing and discourse analysis.
- Document corpus-assisted CDA decisions clearly enough for another researcher to reproduce.

## Repository Structure

```text
.
|-- data/
|   |-- annotation_codebook.csv
|   |-- demo_bri_media_corpus.csv
|   |-- literature_seed.csv
|   `-- sample_corpus.csv
|-- docs/
|   |-- literature_review_notes.md
|   |-- research_plan.md
|   |-- researcher_workflow.md
|   `-- thesis_extension_ideas.md
|-- results/
|   |-- collocates_bri_terms.csv
|   |-- literature_matrix.md
|   |-- method_blueprint.md
|   |-- metrics.csv
|   |-- kwic_bri_terms.csv
|   |-- summary.md
|   `-- top_bigrams.csv
|-- scripts/
|   |-- analyze_corpus.py
|   |-- build_collocates.py
|   |-- build_kwic.py
|   |-- build_method_blueprint.py
|   `-- build_literature_matrix.py
|-- CITATION.cff
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Quick Start

Run the lexical metrics demo:

```bash
python scripts/analyze_corpus.py
```

Generate keyword-in-context lines for the demo BRI media corpus:

```bash
python scripts/build_kwic.py
```

Generate collocates around target terms:

```bash
python scripts/build_collocates.py
```

Generate the literature matrix:

```bash
python scripts/build_literature_matrix.py
```

Generate the method blueprint:

```bash
python scripts/build_method_blueprint.py
```

## Useful Starting Points

- `docs/researcher_workflow.md`: a practical workflow for corpus-assisted CDA and media-framing research.
- `docs/literature_review_notes.md`: a short review-style guide to the expanded bibliography.
- `docs/thesis_extension_ideas.md`: research ideas grounded in the thesis direction and authoritative literature.
- `data/annotation_codebook.csv`: starter labels for framing, actor naming, source attribution, modality, and evaluation.
- `data/literature_seed.csv`: selected journal articles, review articles, conference resources, and books to orient future extensions.
- `results/method_blueprint.md`: generated guidance that maps the literature to workflow stages.

## Notes

The included corpus files are synthetic demos. They are suitable for testing scripts and explaining method, not for drawing substantive claims about real media coverage.
