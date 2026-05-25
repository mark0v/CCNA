from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ARTICLES = ROOT / "articles"
ENGLISHE = ROOT / "englishe"
QUALITY_ASSURANCE = ROOT / "quality-assurance"
KUBERNETES = ROOT / "kubernetes"

CCNA_DOCS = DOCS / "ccna"
ENGLISHE_DOCS = DOCS / "englishe"
QUALITY_ASSURANCE_DOCS = DOCS / "quality-assurance"
KUBERNETES_DOCS = DOCS / "kubernetes"
OLD_KUBERNATES_DOCS = DOCS / "kubernates"


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def clean_generated_docs() -> None:
    generated_paths = [
        DOCS / "articles",
        DOCS / "study-plan.md",
        CCNA_DOCS / "articles",
        CCNA_DOCS / "index.md",
        CCNA_DOCS / "study-plan.md",
        ENGLISHE_DOCS,
        QUALITY_ASSURANCE_DOCS,
        KUBERNETES_DOCS,
        OLD_KUBERNATES_DOCS,
    ]

    for generated_path in generated_paths:
        if generated_path.is_dir():
            shutil.rmtree(generated_path)
        elif generated_path.exists():
            generated_path.unlink()


def copy_study_plan() -> None:
    CCNA_DOCS.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "STUDY_PLAN.md", CCNA_DOCS / "index.md")


def copy_articles() -> None:
    target_root = CCNA_DOCS / "articles"
    target_root.mkdir(parents=True, exist_ok=True)

    for source_dir in sorted(path for path in ARTICLES.glob("*/*") if path.is_dir()):
        relative = source_dir.relative_to(ARTICLES)
        (target_root / relative).mkdir(parents=True, exist_ok=True)

    for source in ARTICLES.rglob("*.md"):
        if source.name == ".gitkeep":
            continue
        relative = source.relative_to(ARTICLES)
        target = target_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def copy_englishe() -> None:
    ENGLISHE_DOCS.mkdir(parents=True, exist_ok=True)

    for source in sorted(ENGLISHE.glob("*.md")):
        target_name = "index.md" if source.name.lower() == "readme.md" else source.name
        shutil.copy2(source, ENGLISHE_DOCS / target_name)


def copy_quality_assurance() -> None:
    QUALITY_ASSURANCE_DOCS.mkdir(parents=True, exist_ok=True)

    for source in sorted(QUALITY_ASSURANCE.rglob("*.md")):
        relative = source.relative_to(QUALITY_ASSURANCE)
        target_name = "index.md" if relative.name.lower() == "readme.md" else relative.name
        target = QUALITY_ASSURANCE_DOCS / relative.parent / target_name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def copy_kubernetes() -> None:
    KUBERNETES_DOCS.mkdir(parents=True, exist_ok=True)

    for source in sorted(KUBERNETES.rglob("*.md")):
        relative = source.relative_to(KUBERNETES)
        target_name = "index.md" if relative.name.lower() == "readme.md" else relative.name
        target = KUBERNETES_DOCS / relative.parent / target_name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def article_link(path: Path, base: Path) -> str:
    relative = path.relative_to(base).as_posix()
    title = title_from_markdown(path)
    number_match = re.match(r"^(\d+)-", path.name)
    prefix = f"{number_match.group(1)}. " if number_match else ""
    return f"- [{prefix}{title}]({relative})"


def write_articles_index() -> None:
    docs_articles = CCNA_DOCS / "articles"
    weeks = sorted(path for path in docs_articles.glob("*/*") if path.is_dir())

    lines = [
        "# Статьи CCNA",
        "",
        "Материалы сгруппированы по месяцу и неделе. Внутри каждой недели файлы пронумерованы в порядке чтения.",
        "",
    ]

    for week in weeks:
        month = week.parent.name
        week_name = week.name
        lines.append(f"- [{month} / {week_name}]({month}/{week_name}/index.md)")

    (docs_articles / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_week_indexes() -> None:
    docs_articles = CCNA_DOCS / "articles"
    for week in sorted(path for path in docs_articles.glob("*/*") if path.is_dir()):
        articles = sorted(path for path in week.glob("*.md") if path.name != "index.md")
        month = week.parent.name
        week_number = week.name.replace("week-", "Week ")

        lines = [
            f"# {week_number} ({month})",
            "",
            "Статьи этой недели в порядке прохождения:",
            "",
        ]
        lines.extend(article_link(path, week) for path in articles)
        lines.append("")

        (week / "index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    clean_generated_docs()
    copy_study_plan()
    copy_articles()
    copy_englishe()
    copy_quality_assurance()
    copy_kubernetes()
    write_articles_index()
    write_week_indexes()


if __name__ == "__main__":
    main()
