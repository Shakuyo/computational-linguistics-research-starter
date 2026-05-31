# Research Plan

## Working Title

Lexical Patterns Across Short Text Registers: A Reproducible Computational Linguistics Starter Study

## Research Question

How do basic lexical patterns differ across short text registers in a small corpus?

## Motivation

Computational linguistics often begins with a carefully prepared text dataset and a reproducible analysis pipeline. This starter project demonstrates that workflow at a small scale. It is designed to be easy to inspect, extend, and publish as a first GitHub repository.

## Data

The demonstration dataset is `data/sample_corpus.csv`.

Each row represents one short text document with:

- `doc_id`: unique document identifier
- `register`: broad text type
- `text`: document content

The current registers are:

- academic
- news
- conversation

## Measures

The first analysis calculates:

- document count by register
- token count
- type count
- type-token ratio
- hapax ratio
- lexical density
- frequent bigrams

## Method

1. Load the corpus from CSV.
2. Tokenize each document with a transparent regex tokenizer.
3. Group documents by register.
4. Calculate descriptive lexical measures.
5. Export reproducible result files.

## Limitations

The sample corpus is too small for real claims. The goal is to demonstrate a clean research workflow. For actual research, replace the sample data with a larger corpus and document data collection, preprocessing, annotation, and ethical considerations.

## Next Steps

- Add a larger corpus.
- Add POS tagging or dependency parsing.
- Add visualizations.
- Add a Jupyter notebook for exploratory analysis.
- Add tests for the analysis script.

