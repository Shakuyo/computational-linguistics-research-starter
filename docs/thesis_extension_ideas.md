# Thesis Extension Ideas

This note turns the thesis direction into reusable computational-linguistics research ideas.

## Thesis Anchor

The project is inspired by an undergraduate thesis titled "A Critical Discourse Analysis of The Straits Times' Narratives on the Belt and Road Initiative." The thesis studied The Straits Times' BRI-related reports from 2021 to 2024 with a corpus-assisted CDA design: wordlists, collocates, KWIC lines, and close reading of selected representative texts.

The public repository intentionally does not include the thesis file, private local analysis files, or copyrighted news articles.

## Research Extension 1: Source-Mediated Framing

Question: When BRI coverage evaluates risk, opportunity, or governance, who is allowed to say it?

Method:

- extract quotation and reported-speech contexts;
- classify sources as official, expert, institution, document, business, or journalist voice;
- compare source type with frame label;
- inspect whether evaluation is outsourced to experts or documents.

Why useful: This extends close reading into a reproducible source-attribution analysis.

Literature anchors: Pareti et al. on quotation attribution; Entman on framing.

## Research Extension 2: Actor Naming and Geopolitical Distance

Question: How do names such as China, Chinese, and Beijing distribute across development, risk, and strategic frames?

Method:

- generate KWIC lines for actor terms;
- annotate nearby frame and evaluation labels;
- compare collocates across actor names;
- test whether Beijing clusters more strongly with strategic or state-action contexts.

Why useful: It operationalizes a thesis-style qualitative observation as a corpus question.

Literature anchors: Biber on distributional register comparison; Baker et al. on corpus-assisted CDA.

## Research Extension 3: Conditional Opportunity Frames

Question: How often is cooperation framed as beneficial only under rules, standards, safeguards, or institutional management?

Method:

- create a lexicon for conditional governance language;
- inspect KWIC lines around rules, standards, transparency, safeguards, arbitration, ASEAN, and governance;
- annotate whether opportunity is unconditional, risk-dominant, or managed/conditional;
- compare across time periods.

Why useful: This is a strong bridge between policy interpretation and measurable discourse patterns.

Literature anchors: Entman on salience and selection; Card et al. on media-frame annotation.

## Research Extension 4: Stance Beyond Sentiment

Question: Is an article's stance toward BRI, China, ASEAN, rules-based governance, or risk the same?

Method:

- define stance targets explicitly;
- annotate target-specific stance rather than document-level positivity;
- compare stance with frame labels and source types;
- train only after a reliable human-coded seed set exists.

Why useful: News discourse often has mixed stance. A text may be positive toward infrastructure, cautious toward debt, and supportive of governance safeguards.

Literature anchor: Mohammad et al. on target-sensitive stance detection.

## Research Extension 5: Cross-Outlet or Cross-Period Comparison

Question: Are the same frames distributed differently across outlets, regions, or years?

Method:

- use matched search terms and inclusion criteria;
- separate training and evaluation by outlet or time period;
- report where models fail across sources;
- combine aggregate metrics with close-reading examples.

Why useful: This can turn a thesis case study into a comparative computational-linguistics project.

Literature anchor: Baly et al. on media bias modeling and the risks of source-sensitive prediction.

## Immediate Repo Tasks

- Replace the demo corpus with licensed or private local data.
- Extend the codebook with examples from the actual corpus.
- Add a script for collocates and target-term comparison.
- Add a small hand-annotated gold sample.
- Add a notebook that links metrics, KWIC evidence, and close-reading notes.

