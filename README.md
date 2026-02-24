# Finance × Knowledge Graph × Network Science: Research Landscape

**金融 × 知識グラフ × ネットワーク科学：研究領域マップ**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Purpose

This repository provides a structured survey of the research landscape at the intersection of **Finance**, **Knowledge Graphs**, and **Network Science**. It is designed as a reference for researchers, practitioners, and students working across finance, computer science, and economics who want to understand how graph-based and network-based methods are transforming financial analysis, risk management, and corporate governance.

## Target Audience

- **Researchers** in financial economics, computational finance, and network science
- **Practitioners** in fintech, risk management, and regulatory compliance
- **Students** in finance, CS, economics, and related interdisciplinary programs

## Field Map

```
                    ┌─────────────────────┐
                    │      Finance        │
                    │  (Risk, Markets,    │
                    │   Regulation)       │
                    └────────┬────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
   ┌──────────────┐  ┌────────────┐  ┌──────────────┐
   │  Knowledge   │  │ Corporate  │  │   Network    │
   │   Graphs     │◄─┤ Governance ├─►│   Science    │
   │  (Ontology,  │  │  ★ Focus   │  │  (Graphs,    │
   │   NLP, LLM)  │  │   Area     │  │   Topology)  │
   └──────┬───────┘  └────────────┘  └──────┬───────┘
          │                                  │
          │        ┌──────────────┐          │
          └───────►│ Quantitative │◄─────────┘
                   │   Methods    │
                   │ (Math, Stats,│
                   │  ML/AI)      │
                   └──────────────┘
```

## Table of Contents

### Documents

| # | Document | Description |
|---|----------|-------------|
| 01 | [Overview & History](docs/01-overview.md) | Historical development and landscape overview |
| 02 | [Economics Perspective](docs/02-economics.md) | Economic theory and financial network analysis |
| 03 | [Computer Science Perspective](docs/03-computer-science.md) | KG construction, NLP, GNNs, and LLM approaches |
| 04 | [Corporate Governance × KG/Network](docs/04-corporate-governance.md) | ★ **Focus Area** — Ownership networks, board interlocks, ESG |
| 05 | [Emerging Fields](docs/05-emerging-fields.md) | DeFi, climate finance, supply-chain graphs, and more |
| 06 | [Quantitative Methods](docs/06-quantitative-methods.md) | Statistical and computational methods for financial networks |
| 07 | [Japan & Asia Research](docs/07-japan-asia.md) | Region-specific research themes and datasets |
| 08 | [Mathematical Foundations](docs/08-mathematical-foundations.md) | Graph theory, topology, and algebraic methods |

### Resources

| Resource | Description |
|----------|-------------|
| [Key Researchers](docs/resources/researchers.md) | Leading scholars and research groups |
| [Datasets](docs/resources/datasets.md) | Public and commercial datasets for financial networks |
| [Tools & Platforms](docs/resources/tools-and-platforms.md) | Software, libraries, and platforms |
| [Conferences & Workshops](docs/resources/conferences.md) | Relevant venues and events |
| [Key Papers](docs/resources/papers.md) | Curated reading list of seminal and recent papers |
| [Ontologies & Standards](docs/resources/ontologies.md) | Financial ontologies, taxonomies, and data standards |

### Tutorials (Jupyter Notebooks)

| # | Notebook | Theme | Data Source |
|---|----------|-------|-------------|
| 01 | [Correlation Network](docs/notebooks/01-correlation-network.ipynb) | Stock correlation network & MST | Yahoo Finance |
| 02 | [Ownership Network](docs/notebooks/02-ownership-network.ipynb) | Corporate ownership network analysis | Wikidata / GLEIF LEI |
| 03 | [Board Interlocks](docs/notebooks/03-board-interlocks.ipynb) | Board interlock network | Sample CSV |
| 04 | [GNN Fraud Detection](docs/notebooks/04-gnn-fraud-detection.ipynb) | GNN-based fraud detection | Elliptic Bitcoin Dataset |
| 05 | [KG Construction](docs/notebooks/05-kg-construction.ipynb) | KG construction from financial text | SEC EDGAR |

## Web Site

Documentation is also available as a website via GitHub Pages:

**[https://yk0817.github.io/finance-knowledge-graph-network-science/](https://yk0817.github.io/finance-knowledge-graph-network-science/)**

## Contributing

Contributions are welcome! If you'd like to add references, correct information, or expand coverage:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/add-topic`)
3. Commit your changes (`git commit -m 'Add new topic'`)
4. Push to the branch (`git push origin feature/add-topic`)
5. Open a Pull Request

Please ensure that:
- References follow a consistent citation format
- New documents fit within the existing structure
- Content is relevant to the intersection of finance, knowledge graphs, and/or network science

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
