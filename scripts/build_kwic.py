from argparse import ArgumentParser
from csv import DictReader, DictWriter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "demo_bri_media_corpus.csv"
DEFAULT_OUTPUT = ROOT / "results" / "kwic_bri_terms.csv"
TOKEN_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def tokenize(text):
    return [match.group(0) for match in TOKEN_PATTERN.finditer(text)]


def kwic_rows(documents, terms, text_column, window):
    normalized_terms = {term.lower() for term in terms}
    for document in documents:
        tokens = tokenize(document[text_column])
        lowered = [token.lower() for token in tokens]
        for index, token in enumerate(lowered):
            if token in normalized_terms:
                left = " ".join(tokens[max(0, index - window) : index])
                right = " ".join(tokens[index + 1 : index + window + 1])
                yield {
                    "doc_id": document.get("doc_id", ""),
                    "date": document.get("date", ""),
                    "outlet": document.get("outlet", ""),
                    "keyword": tokens[index],
                    "left_context": left,
                    "right_context": right,
                }


def parse_args():
    parser = ArgumentParser(description="Build keyword-in-context lines for a CSV corpus.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Input CSV file.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output CSV file.")
    parser.add_argument("--text-column", default="text", help="Name of the text column.")
    parser.add_argument(
        "--terms",
        default="belt,road,initiative,china,chinese,beijing,asean,rules,risk,governance",
        help="Comma-separated keywords to search.",
    )
    parser.add_argument("--window", type=int, default=6, help="Number of tokens on each side.")
    return parser.parse_args()


def main():
    args = parse_args()
    input_file = Path(args.input)
    output_file = Path(args.output)
    terms = [term.strip() for term in args.terms.split(",") if term.strip()]

    with input_file.open("r", encoding="utf-8", newline="") as file:
        documents = list(DictReader(file))

    rows = list(kwic_rows(documents, terms, args.text_column, args.window))
    output_file.parent.mkdir(exist_ok=True)

    with output_file.open("w", encoding="utf-8", newline="") as file:
        writer = DictWriter(
            file,
            fieldnames=["doc_id", "date", "outlet", "keyword", "left_context", "right_context"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} KWIC rows to {output_file}")


if __name__ == "__main__":
    main()

