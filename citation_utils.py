import re


def split_references_section(report_text: str):
    """Split a Markdown report into body and References section.

    Returns:
        tuple[str, str]: body text and references text. If no References
        section exists, the full report is returned as body and references is empty.
    """
    match = re.search(r"(?im)^#{1,3}\s*references\s*$", report_text)

    if not match:
        return report_text.rstrip(), ""

    body = report_text[: match.start()].rstrip()
    references = report_text[match.end() :].strip()
    return body, references


def clean_reference_line(line: str) -> str:
    """Normalize one reference line."""
    cleaned = line.strip()

    # Remove Markdown bullets or numbering.
    cleaned = re.sub(r"^[-*]\s+", "", cleaned)
    cleaned = re.sub(r"^\d+\.\s+", "", cleaned)

    return cleaned.strip()


def extract_reference_lines(references_text: str):
    """Extract candidate APA references from a References section."""
    lines = []

    for raw_line in references_text.splitlines():
        line = clean_reference_line(raw_line)

        if not line:
            continue

        # Keep lines that look like references or contain URLs.
        if "http://" in line or "https://" in line or re.search(r"\(\d{4}\)", line):
            lines.append(line)

    return lines


def normalize_references(references_text: str) -> list[str]:
    """Remove duplicate references and sort them alphabetically."""
    references = extract_reference_lines(references_text)
    seen = set()
    unique_references = []

    for reference in references:
        key = reference.lower().strip().rstrip(".")

        if key not in seen:
            seen.add(key)
            unique_references.append(reference)

    return sorted(unique_references, key=lambda item: item.lower())


def extract_in_text_citations(report_body: str) -> list[str]:
    """Extract simple APA-style in-text citations from the report body."""
    pattern = r"\((?:[A-Z][A-Za-z&.\s-]+,\s*\d{4})(?:;\s*[A-Z][A-Za-z&.\s-]+,\s*\d{4})*\)"
    return sorted(set(re.findall(pattern, report_body)))


def build_citation_quality_note(report_body: str, references: list[str]) -> str:
    """Create a short quality note for the end of the report."""
    in_text_citations = extract_in_text_citations(report_body)

    notes = []

    if not references:
        notes.append("No APA references with URLs were detected.")

    if not in_text_citations:
        notes.append("No APA-style in-text citations were detected in the report body.")

    if not notes:
        notes.append(
            "APA-style in-text citations and a References section were detected. "
            "Review source details manually before formal publication."
        )

    note_text = "\n".join(f"- {note}" for note in notes)

    return f"\n\n## Citation Quality Note\n\n{note_text}\n"


def process_report(report_text: str) -> str:
    """Post-process a generated report.

    This function:
    - keeps URLs only in the References section when the model follows instructions,
    - removes duplicate references,
    - sorts references alphabetically,
    - adds a citation-quality note.
    """
    body, references_text = split_references_section(report_text)
    references = normalize_references(references_text)

    final_parts = [body.rstrip()]

    final_parts.append("\n\n## References\n")

    if references:
        final_parts.extend(f"\n{reference}" for reference in references)
    else:
        final_parts.append("\nNo references were detected. Please regenerate the report or add APA references manually.")

    final_parts.append(build_citation_quality_note(body, references))

    return "".join(final_parts).strip() + "\n"
