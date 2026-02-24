#!/usr/bin/env python3
"""Build PDF from all markdown documents."""

import subprocess
import tempfile
import os

PROJECT = "/Users/yamamtoken/finance-knowledge-graph-network-science"

# Order of files to include
DOC_FILES = [
    "docs/01-overview.md",
    "docs/02-economics.md",
    "docs/03-computer-science.md",
    "docs/04-corporate-governance.md",
    "docs/05-emerging-fields.md",
    "docs/06-quantitative-methods.md",
    "docs/07-japan-asia.md",
    "docs/08-mathematical-foundations.md",
]

RESOURCE_FILES = [
    "docs/resources/researchers.md",
    "docs/resources/datasets.md",
    "docs/resources/tools-and-platforms.md",
    "docs/resources/conferences.md",
    "docs/resources/papers.md",
    "docs/resources/ontologies.md",
]

CSS = """
@page {
    size: A4;
    margin: 2cm 1.8cm;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #666;
    }
}
body {
    font-family: "Hiragino Kaku Gothic Pro", "Hiragino Sans", sans-serif;
    font-size: 10pt;
    line-height: 1.7;
    color: #222;
}
h1 {
    font-size: 20pt;
    border-bottom: 2px solid #333;
    padding-bottom: 6px;
    margin-top: 40px;
    page-break-before: always;
}
h1:first-of-type {
    page-break-before: avoid;
}
h2 {
    font-size: 15pt;
    border-bottom: 1px solid #999;
    padding-bottom: 4px;
    margin-top: 28px;
}
h3 { font-size: 12pt; margin-top: 20px; }
h4 { font-size: 11pt; margin-top: 16px; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 8.5pt;
}
th, td {
    border: 1px solid #ccc;
    padding: 4px 6px;
    text-align: left;
    word-wrap: break-word;
}
th {
    background: #f0f0f0;
    font-weight: bold;
}
tr:nth-child(even) { background: #fafafa; }
code {
    font-family: "SF Mono", "Menlo", monospace;
    font-size: 8.5pt;
    background: #f4f4f4;
    padding: 1px 3px;
    border-radius: 2px;
}
pre {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 4px;
    font-size: 8pt;
    overflow-x: auto;
    white-space: pre-wrap;
}
blockquote {
    border-left: 3px solid #ccc;
    padding-left: 12px;
    color: #555;
}
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 24px 0;
}
.cover {
    text-align: center;
    padding-top: 200px;
}
.cover h1 {
    font-size: 28pt;
    border: none;
    page-break-before: avoid;
}
.cover p {
    font-size: 12pt;
    color: #666;
}
.toc h1 {
    page-break-before: always;
}
"""

COVER = """
<div class="cover">
<h1>金融 × 知識グラフ × ネットワーク科学<br>研究領域マップ</h1>
<p style="font-size: 14pt; margin-top: 20px;">Finance × Knowledge Graph × Network Science:<br>Research Landscape</p>
<p style="margin-top: 60px;">2026年2月</p>
</div>
"""


def md_to_html(md_path):
    """Convert markdown to HTML using pandoc."""
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html5", "--wrap=none", md_path],
        capture_output=True, text=True
    )
    return result.stdout


def build():
    # Build HTML
    html_parts = [COVER]

    # Docs
    for f in DOC_FILES:
        path = os.path.join(PROJECT, f)
        html_parts.append(md_to_html(path))

    # Resources separator
    html_parts.append("<h1>リソース</h1>")

    for f in RESOURCE_FILES:
        path = os.path.join(PROJECT, f)
        html_parts.append(md_to_html(path))

    full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{"".join(html_parts)}
</body>
</html>"""

    # Write HTML
    html_path = os.path.join(PROJECT, "output.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    # Convert to PDF
    pdf_path = os.path.join(PROJECT, "finance-kg-network-science.pdf")
    subprocess.run(
        ["python3", "-m", "weasyprint", html_path, pdf_path],
        check=True
    )

    # Clean up
    os.remove(html_path)
    print(f"PDF generated: {pdf_path}")


if __name__ == "__main__":
    build()
