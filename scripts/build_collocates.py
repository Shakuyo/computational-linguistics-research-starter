from argparse import ArgumentParser
from collections import Counter, defaultdict
from csv import DictReader, DictWriter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "demo_bri_media_corpus.csv"
DEFAULT_OUTPUT = ROOT / "results" / "collocates_bri_terms.csv"
TOKEN_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "may",
    "of",
    "on",
    "or",
    "the",
    "to",
    "was",
    "were",
    "with",
}


def tokenize(text):
    return [match.group(0).lower() for match in TOKEN_PATTERN.finditer(text)]


def parse_terms(value):
    return [term.strip().lower() for term in value.split(",") if term.strip()]


def collocate_rows(documents, terms, text_column, window, min_count, include_stopwords):
    counts = defaultdict(Counter)
    examples = defaultdict(lambda: defaultdict(set))

    for document in documents:
        tokens = tokenize(document[text_column])
        doc_id = document.get("doc_id", "")
        for index, token in enumerate(tokens):
            if token not in terms:
                continue
            start = max(0, index - window)
            end = min(len(tokens), index + window + 1)
            for context_index in range(start, end):
                if context_index == index:
                    continue
                collocate = tokens[context_index]
                if collocate == token:
                    continue
                if not include_stopwords and collocate in STOPWORDS:
                    continue
                counts[token][collocate] += 1
                examples[token][collocate].add(doc_id)

    rows = []
    for target in sorted(counts):
        for collocate, count in counts[target].most_common():
            if count < min_count:
                continue
            rows.append(
                {
                    "target": target,
                    "collocate": collocate,
                    "count": count,
                    "example_doc_ids": ";".join(sorted(examples[target][collocate])),
                }
            )
    return rows


def parse_args():
    parser = ArgumentParser(description="Build simple collocate counts around target terms.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Input CSV file.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output CSV file.")
    parser.add_argument("--text-column", default="text", help="Name of the text column.")
    parser.add_argument(
        "--terms",
        default="bri,initiative,china,chinese,beijing,asean,rules,risk,governance",
        help="Comma-separated target terms.",
    )
    parser.add_argument("--window", type=int, default=5, help="Context window on each side.")
    parser.add_argument("--min-count", type=int, default=1, help="Minimum collocate count.")
    parser.add_argument(
        "--include-stopwords",
        action="store_true",
        help="Include common function words in the collocate table.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_file = Path(args.input)
    output_file = Path(args.output)
    terms = parse_terms(args.terms)

    with input_file.open("r", encoding="utf-8", newline="") as file:
        documents = list(DictReader(file))

    rows = collocate_rows(
        documents,
        terms,
        args.text_column,
        args.window,
        args.min_count,
        args.include_stopwords,
    )
    output_file.parent.mkdir(exist_ok=True)

    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = DictWriter(file, fieldnames=["target", "collocate", "count", "example_doc_ids"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} collocate rows to {output_file}")


if __name__ == "__main__":
    main()
