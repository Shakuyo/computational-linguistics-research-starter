from collections import Counter
from csv import DictReader
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "literature_seed.csv"
OUTPUT_FILE = ROOT / "results" / "literature_matrix.md"


def load_rows():
    with INPUT_FILE.open("r", encoding="utf-8", newline="") as file:
        return list(DictReader(file))


def value(row, key):
    return row.get(key, "").strip()


def main():
    rows = load_rows()
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    publication_counts = Counter(value(row, "publication_type") or "unspecified" for row in rows)

    lines = [
        "# Literature Matrix",
        "",
        "This file is generated from `data/literature_seed.csv`.",
        "",
        "## Coverage",
        "",
    ]

    for publication_type, count in sorted(publication_counts.items()):
        lines.append(f"- {publication_type}: {count}")

    lines.extend(
        [
            "",
            "## Sources",
            "",
            "| Stage | Area | Publication | Source | Core Idea | Researcher Action | Link |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for row in rows:
        publication = ", ".join(
            item
            for item in [value(row, "journal_or_venue"), value(row, "year"), value(row, "publication_type")]
            if item
        )
        lines.append(
            "| {stage} | {area} | {publication} | {source} | {idea} | {action} | [source]({url}) |".format(
                stage=value(row, "workflow_stage") or "general",
                area=value(row, "area"),
                publication=publication,
                source=value(row, "short_citation"),
                idea=value(row, "core_idea"),
                action=value(row, "researcher_action") or value(row, "why_it_matters_for_this_repo"),
                url=value(row, "url"),
            )
        )

    lines.extend(
        [
            "",
            "## How to Use This Matrix",
            "",
            "- Start with `theory` and `method_design` rows before adding computational models.",
            "- Use `annotation_design` rows when defining labels and decision rules.",
            "- Use `method_validation` rows before reporting model or script outputs as evidence.",
            "- Use `domain_context` rows to interpret BRI and Southeast Asian media findings cautiously.",
        ]
    )

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} literature entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

