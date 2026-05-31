from collections import defaultdict
from csv import DictReader
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "literature_seed.csv"
OUTPUT_FILE = ROOT / "results" / "method_blueprint.md"

STAGE_ORDER = [
    "theory",
    "literature_review",
    "domain_context",
    "method_design",
    "workflow_design",
    "feature_design",
    "annotation_design",
    "source_attribution",
    "method_validation",
    "modeling",
]


def load_rows():
    with INPUT_FILE.open("r", encoding="utf-8", newline="") as file:
        return list(DictReader(file))


def value(row, key):
    return row.get(key, "").strip()


def stage_title(stage):
    return stage.replace("_", " ").title()


def main():
    rows = load_rows()
    by_stage = defaultdict(list)
    for row in rows:
        by_stage[value(row, "workflow_stage") or "general"].append(row)

    ordered_stages = [stage for stage in STAGE_ORDER if stage in by_stage]
    ordered_stages.extend(sorted(stage for stage in by_stage if stage not in ordered_stages))

    lines = [
        "# Method Blueprint",
        "",
        "This file turns the literature seed table into practical design guidance.",
        "",
        "Use it as a checklist when moving from a thesis-style question to a reproducible computational-linguistics workflow.",
        "",
    ]

    for stage in ordered_stages:
        lines.extend([f"## {stage_title(stage)}", ""])
        for row in by_stage[stage]:
            publication = ", ".join(
                item for item in [value(row, "journal_or_venue"), value(row, "year")] if item
            )
            lines.extend(
                [
                    f"### {value(row, 'short_citation')}",
                    "",
                    f"- Publication: {publication}",
                    f"- Method signal: {value(row, 'method_signal')}",
                    f"- Why it matters: {value(row, 'why_it_matters_for_this_repo')}",
                    f"- Researcher action: {value(row, 'researcher_action')}",
                    "",
                ]
            )

    lines.extend(
        [
            "## Minimum Viable Research Upgrade",
            "",
            "A researcher can turn the current demo into a stronger study by completing these steps:",
            "",
            "1. Replace the synthetic demo corpus with licensed or private corpus data.",
            "2. Keep a corpus log with source, date, query, and licensing fields.",
            "3. Generate wordlists, collocates, and KWIC lines before close reading.",
            "4. Annotate a small gold sample with the codebook.",
            "5. Validate any automated labels against the gold sample.",
            "6. Report representative concordance lines together with aggregate metrics.",
            "",
        ]
    )

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote method blueprint to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

