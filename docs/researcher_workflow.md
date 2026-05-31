# Researcher Workflow

This workflow is designed for corpus-assisted critical discourse analysis, media framing research, and computational-linguistics projects that still need close reading.

## 1. Define the Research Object

Start with a narrow object:

- outlet or corpus source
- date range
- search terms
- language
- genre or register
- inclusion and exclusion rules

For a BRI media project, define whether the object is "BRI coverage" broadly, Singapore-based coverage specifically, or comparative regional coverage.

## 2. Build a Corpus Log

Keep a table with:

- document id
- date
- outlet
- author if available
- section
- headline
- source database
- search query
- licensing status

Do not publish copyrighted article text unless the license allows it. Public repos can include scripts, metadata templates, synthetic examples, and derived non-sensitive summaries.

## 3. Clean Text Transparently

Record every cleaning decision:

- boilerplate removal
- duplicate handling
- headline/body separation
- quote normalization
- punctuation handling
- tokenization rules

The goal is not perfect cleaning. The goal is cleaning that another researcher can inspect.

## 4. Generate Corpus Views

Use corpus outputs to guide close reading:

- wordlists
- bigrams and collocates
- keyword-in-context lines
- register or time-period comparisons
- actor naming patterns
- source attribution patterns
- modality and hedging patterns

This repo currently includes simple scripts for lexical metrics, collocates, KWIC lines, and literature-to-method outputs.

## 5. Annotate Interpretable Categories

Use `data/annotation_codebook.csv` as a starter. For each label, keep:

- definition
- decision rule
- positive and negative examples
- disagreements and revisions

For multi-coder work, add inter-annotator agreement before model training.

## 6. Combine Quantitative and Qualitative Evidence

A good corpus-assisted CDA claim should usually connect:

- a measurable pattern
- a concordance or document-level example
- a discourse interpretation
- a limitation

Avoid treating frequency as meaning by itself.

## 7. Move Toward Computational Modeling Carefully

Good next computational steps include:

- frame annotation on a small gold set
- stance labels for target-specific claims
- quotation/source attribution
- temporal comparison
- cross-outlet comparison
- retrieval-augmented close reading

Keep human-readable outputs in `results/` so qualitative interpretation remains auditable.

## 8. Tie Each Step to Literature

Use `data/literature_seed.csv` and `results/method_blueprint.md` as a method audit trail.

- Use framing theory before inventing labels.
- Use corpus-assisted discourse studies before interpreting collocates.
- Use content-analysis literature before coding frames.
- Use text-as-data validation literature before making automated claims.
- Use BRI and ASEAN context literature before interpreting regional strategy.

This is especially important for public research repos: the repository should show not only what the scripts do, but why those operations are methodologically defensible.
