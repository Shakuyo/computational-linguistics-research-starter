# Computational Linguistics Research Starter

This repository is a small, reproducible starter project for computational linguistics research.

The example study asks:

> How do simple lexical patterns differ across short text registers?

The project includes a tiny sample corpus, a documented research plan, and a Python analysis script that calculates basic corpus-linguistic measures such as token counts, type-token ratio, lexical density, hapax ratio, and frequent bigrams.

## Repository Structure

```text
.
├── data/
│   └── sample_corpus.csv
├── docs/
│   └── research_plan.md
├── results/
│   └── .gitkeep
├── scripts/
│   └── analyze_corpus.py
├── .gitignore
├── CITATION.cff
├── LICENSE
├── README.md
└── requirements.txt
```

## Quick Start

Run the analysis from the repository root:

```bash
python scripts/analyze_corpus.py
```

The script writes:

- `results/metrics.csv`
- `results/top_bigrams.csv`
- `results/summary.md`

## Research Use

This starter can be expanded into a more serious project by:

- replacing the demo corpus with a larger annotated corpus;
- adding metadata such as date, source, genre, speaker, or proficiency level;
- comparing registers, authors, learners, or time periods;
- adding statistical tests and visualizations;
- documenting data collection and annotation decisions.

## Notes

The sample corpus is intentionally tiny. It is useful for testing the workflow, not for drawing real linguistic conclusions.

