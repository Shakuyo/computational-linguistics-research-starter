# Research Plan

## Working Title

Corpus-Assisted Analysis of Media Framing and Stance

## Research Question

How can corpus methods and close reading be combined to study media framing, source attribution, stance, and actor naming in a reproducible way?

## Motivation

This starter project is shaped by a thesis-style research problem: how a news outlet constructs narratives around the Belt and Road Initiative through lexical choices, sources, modality, and evaluative framing.

The repository turns that problem into an open and reusable computational-linguistics scaffold. It provides synthetic demo data, scripts, codebook templates, and literature anchors without publishing private thesis files or copyrighted news texts.

## Demonstration Data

The repo includes two small demo corpora:

- `data/sample_corpus.csv`: a generic register-comparison corpus for lexical metrics.
- `data/demo_bri_media_corpus.csv`: a synthetic BRI media-discourse corpus for KWIC examples.

The demo texts are not evidence for real-world claims. They exist to test and explain the workflow.

## Current Measures

The current scripts produce:

- document count by register
- token count
- type count
- type-token ratio
- hapax ratio
- lexical density
- frequent bigrams
- keyword-in-context lines
- a literature matrix

## Method

1. Start with a corpus log and explicit inclusion rules.
2. Clean text with recorded preprocessing decisions.
3. Generate descriptive corpus views.
4. Use KWIC lines to select close-reading evidence.
5. Annotate framing, actor naming, source attribution, modality, and evaluation.
6. Treat computational outputs as aids to interpretation rather than automatic proof.

## Research Extensions

The most natural extensions are:

- source-mediated framing analysis;
- actor naming comparison such as China, Chinese, and Beijing;
- conditional opportunity frames around rules and safeguards;
- target-specific stance analysis;
- cross-outlet or cross-period comparison.

See `docs/thesis_extension_ideas.md` for details.

## Limitations

The included data is tiny and synthetic. Any real study should replace it with licensed or private corpus data, document the source database and search terms, and keep close-reading evidence tied to reproducible corpus outputs.

