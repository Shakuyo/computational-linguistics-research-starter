from csv import DictReader
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "literature_seed.csv"
OUTPUT_FILE = ROOT / "results" / "literature_matrix.md"


def load_rows():
    with INPUT_FILE.open("r", encoding="utf-8", newline="") as file:
        return list(DictReader(file))


def main():
    rows = load_rows()
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    lines = [
        "# Literature Matrix",
        "",
        "This file is generated from `data/literature_seed.csv`.",
        "",
        "| Area | Source | Core Idea | Use in This Repo | Link |",
        "| --- | --- | --- | --- | --- |",
    ]

    for row in rows:
        lines.append(
            "| {area} | {source} | {idea} | {use} | [source]({url}) |".format(
                area=row["area"],
                source=row["short_citation"],
                idea=row["core_idea"],
                use=row["why_it_matters_for_this_repo"],
                url=row["url"],
            )
        )

    OUTPUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} literature entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

