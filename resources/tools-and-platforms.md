# Tools and Platforms for Financial Network Analysis and Knowledge Graphs

This document catalogs software tools, libraries, platforms, and services for building and analyzing financial networks and knowledge graphs.

---

## Graph Databases

| Tool | Type | Description | License | URL |
|------|------|-------------|---------|-----|
| Neo4j | Native graph database (labeled property graph) | Most popular graph database; Cypher query language; ACID compliant; strong ecosystem (APOC, GDS library) | Community (GPLv3) / Enterprise (Commercial) | https://neo4j.com/ |
| TigerGraph | Native parallel graph database | High-performance distributed graph analytics; GSQL query language; real-time deep link analytics | Commercial (free tier available) | https://www.tigergraph.com/ |
| Amazon Neptune | Managed graph database (AWS) | Supports both property graph (Gremlin/openCypher) and RDF (SPARQL); serverless option | Commercial (AWS) | https://aws.amazon.com/neptune/ |
| ArangoDB | Multi-model (document, graph, key-value) | Native graph + document store; AQL query language; Pregel-based graph analytics | Apache 2.0 / Commercial | https://www.arangodb.com/ |
| JanusGraph | Distributed graph database | Supports multiple backends (Cassandra, HBase, BerkeleyDB); Gremlin/TinkerPop compatible | Apache 2.0 | https://janusgraph.org/ |
| Dgraph | Native distributed graph database | GraphQL-native; horizontal scaling; ACID transactions | Apache 2.0 / Commercial | https://dgraph.io/ |
| Stardog | Enterprise knowledge graph platform | RDF/OWL triple store with reasoning; SPARQL + GraphQL; virtual graph federation | Commercial | https://www.stardog.com/ |
| Ontotext GraphDB | RDF triple store with reasoning | OWL 2 reasoning; SPARQL 1.1; semantic inference; SHACL validation | Commercial (free edition available) | https://www.ontotext.com/products/graphdb/ |
| Ultipa | Real-time graph database | High-performance parallel graph traversal; HDFS-like distributed architecture | Commercial | https://www.ultipa.com/ |
| Memgraph | In-memory graph database | Cypher-compatible; streaming graph analytics; Kafka integration | BSL / Community (free) | https://memgraph.com/ |
| NebulaGraph | Distributed graph database | Horizontal scaling; nGQL query language; designed for super-large graphs | Apache 2.0 | https://www.nebula-graph.io/ |

---

## Graph Analytics Libraries

| Tool | Language | Description | License | URL |
|------|----------|-------------|---------|-----|
| NetworkX | Python | De facto standard for network analysis in Python; rich algorithm library; easy to use | BSD | https://networkx.org/ |
| igraph | R / Python / C | High-performance network analysis; fast community detection, centrality, visualization | GPL-2.0 | https://igraph.org/ |
| graph-tool | Python (C++ core) | High-performance network analysis with Bayesian inference; stochastic block models | LGPL-3.0 | https://graph-tool.skewed.de/ |
| SNAP | C++ / Python | Stanford large-scale network analysis; billions of edges; PageRank, motifs, communities | BSD | https://snap.stanford.edu/snap/ |
| DGL (Deep Graph Library) | Python (PyTorch/TensorFlow) | Flexible framework for GNNs; message passing; heterogeneous graphs | Apache 2.0 | https://www.dgl.ai/ |
| PyG (PyTorch Geometric) | Python (PyTorch) | GNN library; extensive model zoo; mini-batch training; heterogeneous graphs | MIT | https://pyg.org/ |
| StellarGraph | Python (TensorFlow/Keras) | GNNs for node/edge/graph tasks; GraphSAGE, GAT, GCN implementations | Apache 2.0 | https://stellargraph.readthedocs.io/ |
| cuGraph (NVIDIA RAPIDS) | Python (CUDA) | GPU-accelerated graph analytics; PageRank, BFS, Louvain on GPU | Apache 2.0 | https://github.com/rapidsai/cugraph |
| Networkit | Python (C++ core) | Large-scale network analysis; parallel algorithms; community detection | MIT | https://networkit.github.io/ |
| GraphFrames | Python/Scala (Apache Spark) | Distributed graph processing on Spark; motif finding; connected components | Apache 2.0 | https://graphframes.github.io/graphframes/ |
| Tulip | C++ / Python | Large graph visualization and analysis framework | LGPL | https://tulip.labri.fr/ |
| PowerGraph (GraphLab) | C++ | Distributed graph computation; vertex-cut partitioning | Apache 2.0 | https://github.com/jegonzal/PowerGraph |

---

## Knowledge Graph Construction and Management Tools

| Tool | Type | Description | License | URL |
|------|------|-------------|---------|-----|
| Protégé | Ontology editor | Stanford's OWL/RDF ontology editor; visual class hierarchy; plugin ecosystem | BSD-2-Clause | https://protege.stanford.edu/ |
| Apache Jena | RDF framework (Java) | RDF/SPARQL framework; TDB triple store; Fuseki SPARQL server; OWL reasoning | Apache 2.0 | https://jena.apache.org/ |
| RDFLib | RDF library (Python) | Python RDF manipulation; SPARQL query; serialization (Turtle, JSON-LD, N-Triples) | BSD | https://rdflib.readthedocs.io/ |
| Owlready2 | Ontology library (Python) | Load/modify OWL ontologies in Python; HermiT reasoning; SPARQL queries | LGPL-3.0 | https://owlready2.readthedocs.io/ |
| PyKEEN | KG embedding library (Python) | Knowledge graph embedding models (TransE, RotatE, ConvE, etc.); hyperparameter search | MIT | https://pykeen.readthedocs.io/ |
| AmpliGraph | KG embedding library (Python) | Knowledge graph embeddings; link prediction; model evaluation | Apache 2.0 | https://docs.ampligraph.org/ |
| OpenKE | KG embedding framework | Open-source KG embedding toolkit; efficient C++ backend with Python interface | MIT | https://github.com/thunlp/OpenKE |
| spaCy + REL | NER + Entity Linking | Named entity recognition with entity linking to knowledge bases | MIT | https://spacy.io/ |
| DeepKE | Knowledge extraction (Python) | Low-resource knowledge graph construction; NER, RE, attribute extraction | MIT | https://github.com/zjunlp/DeepKE |
| OpenIE / Stanford KG | Information extraction | Open information extraction for triple generation from text | Apache 2.0 | https://stanfordnlp.github.io/CoreNLP/ |

---

## Financial NLP Tools

| Tool | Type | Description | License | URL |
|------|------|-------------|---------|-----|
| FinBERT | Pre-trained language model | BERT fine-tuned on financial text; sentiment analysis; financial NER | Apache 2.0 | https://github.com/ProsusAI/finBERT |
| BloombergGPT | Large language model | 50B parameter LLM trained on Bloomberg financial data; financial NLP tasks | Commercial (Bloomberg) | — |
| FinGPT | Open-source financial LLM | Open framework for financial LLMs; RLHF with financial data | MIT | https://github.com/AI4Finance-Foundation/FinGPT |
| spaCy (finance pipelines) | NLP library (Python) | Industrial-strength NLP; custom financial NER models; fast tokenization | MIT | https://spacy.io/ |
| Stanza | NLP library (Python) | Stanford NLP toolkit; multilingual support; biomedical/financial models | Apache 2.0 | https://stanfordnlp.github.io/stanza/ |
| AllenNLP | NLP framework (Python) | Deep learning NLP framework; semantic role labeling; coreference | Apache 2.0 | https://allennlp.org/ |
| FinRL | Deep RL for finance (Python) | Reinforcement learning library for quantitative finance | MIT | https://github.com/AI4Finance-Foundation/FinRL |
| Hugging Face Transformers | Model hub / framework | Access to FinBERT, financial GPT models, and fine-tuning pipelines | Apache 2.0 | https://huggingface.co/ |
| SEC-API | SEC filing parser | Programmatic access to SEC EDGAR filings with full-text search | Freemium | https://sec-api.io/ |

---

## Visualization Tools

| Tool | Type | Description | License | URL |
|------|------|-------------|---------|-----|
| Gephi | Desktop application | Open-source network visualization and exploration; ForceAtlas2 layout; large graphs | GPL-3.0 / CDDL | https://gephi.org/ |
| Cytoscape | Desktop application | Network visualization originally for biology; extensive plugin ecosystem; large graphs | LGPL-2.1 | https://cytoscape.org/ |
| D3.js | JavaScript library | Low-level data visualization; force-directed layouts; highly customizable | ISC | https://d3js.org/ |
| vis.js (vis-network) | JavaScript library | Interactive network visualization; physics-based layouts; browser-based | Apache 2.0 / MIT | https://visjs.org/ |
| Sigma.js | JavaScript library | Web-based graph visualization for large graphs; WebGL rendering | MIT | https://www.sigmajs.org/ |
| Linkurious | Commercial platform | Graph visualization and investigation platform; Neo4j/Cosmos integration | Commercial | https://linkurious.com/ |
| Graphistry | Commercial platform | GPU-accelerated visual graph analytics; large-scale exploration | Commercial (free tier) | https://www.graphistry.com/ |
| yFiles | Commercial library | Professional graph visualization SDK (Java, JS, .NET); automatic layouts | Commercial | https://www.yworks.com/products/yfiles |
| Plotly/Dash + NetworkX | Python framework | Interactive web-based network visualizations using Plotly + Python | MIT | https://plotly.com/ |
| Pyvis | Python library | Interactive network visualization in Jupyter; vis.js wrapper | BSD | https://pyvis.readthedocs.io/ |
| Cosmograph | JavaScript library | GPU-powered large-scale graph visualization (WebGL) | — | https://cosmograph.app/ |
| Flourish | Web platform | No-code interactive data visualization; network diagram templates | Freemium | https://flourish.studio/ |

---

## Commercial Financial Platforms

| Platform | Provider | Description | Key Features | URL |
|----------|----------|-------------|--------------|-----|
| Refinitiv Workspace | LSEG (London Stock Exchange Group) | Financial data terminal; corporate relationships; ownership data | Company trees, supply chains, ownership networks | https://www.refinitiv.com/ |
| Bloomberg Terminal | Bloomberg L.P. | Comprehensive financial data; SPLC (supply chain); OWNS (ownership) | Supply chain maps, ownership analysis, corporate structure | https://www.bloomberg.com/professional/ |
| Sayari | Sayari | Trade and corporate records for supply chain and risk analysis | Beneficial ownership, trade networks, entity resolution | https://sayari.com/ |
| Palantir Foundry | Palantir Technologies | Data integration and analytics platform; graph-based investigation | Entity resolution, link analysis, financial crime detection | https://www.palantir.com/ |
| Chainalysis | Chainalysis | Blockchain analytics and investigation platform | Crypto transaction tracing, compliance, network visualization | https://www.chainalysis.com/ |
| Elliptic | Elliptic | Crypto compliance and risk management | Transaction scoring, wallet screening, network analysis | https://www.elliptic.co/ |
| GraphAware Hume | GraphAware (now Neo4j) | Knowledge graph platform with NLP and graph analytics | Entity extraction, relationship discovery, knowledge management | https://graphaware.com/hume/ |
| Diffbot | Diffbot | AI-powered web scraping and knowledge graph construction | 20B+ entity Knowledge Graph; relationship extraction from web | https://www.diffbot.com/ |
| Moody's Analytics / RiskCalc | Moody's | Credit risk and financial network analysis | Interbank exposure, counterparty risk, network stress testing | https://www.moodysanalytics.com/ |
| FactSet | FactSet Research Systems | Financial data, analytics, supply chain relationships | Supply chain mapping, ownership data, entity relationships | https://www.factset.com/ |
| S&P Capital IQ Pro | S&P Global | Financial data platform with corporate relationship data | Corporate hierarchy, key relationships, supply chain intel | https://www.spglobal.com/marketintelligence/ |

---

## Cloud Graph Services

| Service | Provider | Description | Graph Model | URL |
|---------|----------|-------------|-------------|-----|
| Amazon Neptune | AWS | Managed graph database service; serverless option | Property Graph (Gremlin/openCypher) + RDF (SPARQL) | https://aws.amazon.com/neptune/ |
| Amazon Neptune Analytics | AWS | Graph analytics with vector search; Neptune ML for GNN-based predictions | Property Graph + ML | https://aws.amazon.com/neptune/neptune-analytics/ |
| Google Cloud Knowledge Graph / Spanner | Google Cloud | Enterprise knowledge graph and distributed graph database capabilities | Multi-model | https://cloud.google.com/spanner |
| Azure Cosmos DB (Gremlin API) | Microsoft Azure | Globally distributed multi-model database with graph API | Property Graph (Gremlin) | https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/ |
| Databricks (GraphFrames) | Databricks | Distributed graph processing on Spark; Lakehouse architecture | GraphFrames (Spark) | https://docs.databricks.com/ |
| Neo4j AuraDB | Neo4j | Fully managed cloud Neo4j; graph data science as a service | Labeled Property Graph (Cypher) | https://neo4j.com/cloud/aura/ |
| TigerGraph Cloud | TigerGraph | Managed TigerGraph instance with ML workbench | Property Graph (GSQL) | https://www.tigergraph.com/cloud/ |

---

## Development and Integration Tools

| Tool | Type | Description | License | URL |
|------|------|-------------|---------|-----|
| Apache Kafka + Graph Sink | Stream processing | Real-time graph construction from streaming financial data | Apache 2.0 | https://kafka.apache.org/ |
| Apache Airflow | Workflow orchestration | Schedule and monitor financial data pipeline DAGs | Apache 2.0 | https://airflow.apache.org/ |
| dbt | Data transformation | SQL-based transformation for graph feature engineering | Apache 2.0 | https://www.getdbt.com/ |
| LangChain (Graph modules) | LLM framework | LLM-powered knowledge graph construction and querying | MIT | https://www.langchain.com/ |
| LlamaIndex (Knowledge Graph) | LLM framework | KG-augmented retrieval; graph stores; structured queries | MIT | https://www.llamaindex.ai/ |
| Jupyter + Graph Extensions | Notebook environment | Interactive graph analysis with yFiles, nxviz, pyvis integrations | BSD | https://jupyter.org/ |

---

*Last updated: 2026-02-23*
