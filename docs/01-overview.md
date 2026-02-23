# Overview: Financial Network Science and Knowledge Graphs

## 1. History of Financial Network Science

### 1.1 Foundations (Late 1990s)

The application of network science to finance traces its origins to **Mantegna (1999)**, who constructed a **Minimum Spanning Tree (MST)** from stock return correlations on the NYSE. This work demonstrated that hierarchical clustering of financial assets reveals meaningful economic taxonomy — sector structures emerged naturally from price co-movements. Mantegna's approach borrowed directly from statistical physics, applying graph-theoretic methods to correlation matrices, and is widely regarded as the founding contribution of financial network science.

Around the same period, **Vandewalle, Brisbois & Trevisan (1998)** and **Bonanno, Lillo & Mantegna (2001)** extended correlation-based network analysis to foreign exchange markets and broader asset classes, establishing the Random Matrix Theory (RMT) + network filtering pipeline that remains influential today.

### 1.2 Early 2000s: Contagion and Complex Networks

The early 2000s saw two parallel developments:

**Financial contagion theory:**
- **Allen & Gale (2000)** published "Financial Contagion" in the *Journal of Political Economy*, providing the first formal model of contagion spreading through interbank network structures. They showed that network topology — complete vs. incomplete — determines system resilience.
- **Freixas, Parigi & Rochet (2000)** modeled systemic risk in interbank payment systems.
- **Eisenberg & Noe (2001)** introduced the clearing payment vector framework for interbank obligations, enabling computation of losses in networked financial systems.

**Complex network theory applied to economics:**
- **Caldarelli (2007)** and collaborators applied scale-free network models to financial systems.
- **Boss, Elsinger, Summer & Thurner (2004)** produced one of the first empirical mappings of a national interbank network (Austria), revealing heavy-tailed degree distributions.
- **Iori, De Masi, Precup, Gabbi & Caldarelli (2008)** analyzed the Italian overnight money market as a complex network.

### 1.3 The 2008 Financial Crisis: A Turning Point

The Global Financial Crisis (GFC) of 2007–2009 was a watershed moment for financial network science. The crisis exposed how interconnections — through derivatives, repo markets, and cross-holdings — could amplify and propagate shocks in ways that traditional risk models completely missed.

**Key intellectual responses:**

- **Andrew Haldane's "Rethinking the Financial Network" speech (2009)** at the Bank of England drew explicit parallels between financial networks and ecological/epidemiological networks. Haldane argued that regulators had focused on individual institution risk while ignoring the network topology that determined systemic fragility. This speech became a rallying call for network-based financial regulation.

- **Haldane & May (2011)**, published in *Nature*, formalized this argument by applying May's (1972) ecological stability results to banking ecosystems, showing that increasing complexity and connectivity can destabilize financial networks beyond a critical threshold.

- **Basel III and macroprudential regulation** emerged partly from this network-aware thinking. The designation of **Global Systemically Important Banks (G-SIBs)** explicitly incorporated interconnectedness metrics alongside size, complexity, and substitutability.

- **Battiston, Puliga, Kaushik, Tasca & Caldarelli (2012)** introduced **DebtRank**, a recursive algorithm inspired by feedback centrality that measures the systemic importance of financial institutions by propagating distress through the network. DebtRank became one of the most widely adopted tools in macroprudential network analysis.

- **Cont, Moussa & Santos (2013)** provided a detailed simulation-based study of contagion in the Brazilian banking system, distinguishing between credit and funding contagion channels.

### 1.4 2010s: Expansion and Maturation

The post-crisis decade saw an explosion of research across multiple dimensions:

**Interbank and payment networks:**
- Network topology of TARGET2 (ECB), Fedwire (Fed), and other large-value payment systems
- **Craig & von Peter (2014)**: Tiered structure of interbank networks
- **in 't Veld & van Lelyveld (2014)**: Reconstructing interbank networks from incomplete data

**Production and trade networks:**
- **Acemoglu, Carvalho, Ozdaglar & Tahbaz-Salehi (2012)**: Network origins of aggregate economic fluctuations — showed that heavy-tailed input-output networks prevent diversification of idiosyncratic shocks
- **Carvalho (2014)**: Survey on micro-origins of macroeconomic fluctuations through production networks
- **Barrot & Sauvagnat (2016)**: Propagation of natural disaster shocks through supply chains

**Theoretical advances:**
- **Acemoglu, Ozdaglar & Tahbaz-Salehi (2015)**: "Systemic Risk and Stability in Financial Networks" in *AER* — showed phase transitions between diversification (dense networks absorb small shocks) and contagion (dense networks amplify large shocks)
- **Elliott, Golub & Jackson (2014)**: "Financial Networks and Contagion" in *AER* — cross-holdings and integration vs. diversification
- **Glasserman & Young (2016)**: Contagion in financial networks, bounding default cascades

**Regulatory adoption:**
- Central banks worldwide developed network-based stress testing tools
- ECB's NATkit, OFR's financial stability monitor
- Network metrics integrated into supervisory frameworks

### 1.5 2020s: Knowledge Graphs, GNNs, and LLMs

The current frontier integrates modern AI with financial network analysis:

- **Graph Neural Networks (GNNs)** applied to financial networks: credit risk prediction, fraud detection, stock movement prediction using relational data (Wang et al., 2021; Cheng et al., 2022)
- **Knowledge Graphs (KGs)** for financial regulation, compliance, and risk analysis
- **Large Language Models (LLMs)** combined with KGs for financial text analysis, event extraction, and reasoning (GraphRAG approaches)
- **FinDKG (Cheng, Xu & Farmer, 2024)**: Dynamic knowledge graph construction from financial news for macro-financial forecasting
- **Temporal financial networks**: Time-varying topology analysis with dynamic community detection
- **Climate-finance networks**: Battiston et al.'s work on climate stress testing through financial network transmission

---

## 2. Knowledge Graphs in Finance

### 2.1 Semantic Web Origins

Knowledge graphs build on decades of work in knowledge representation:

- **RDF (Resource Description Framework)**: W3C standard for representing information as subject-predicate-object triples. Provides the foundational data model for knowledge graphs.
- **OWL (Web Ontology Language)**: Enables formal ontological reasoning — class hierarchies, property constraints, logical inference.
- **SPARQL**: Query language for RDF data, allowing complex graph pattern matching.
- **The original "Knowledge Graph"**: Google (2012) popularized the term, but the underlying technology draws from the Semantic Web, description logics, and earlier AI knowledge representation work (Cyc, WordNet, etc.).

### 2.2 The FIBO Ontology

The **Financial Industry Business Ontology (FIBO)**, developed by the **EDM Council** (now a program of GLEIF), is the most significant domain ontology for finance:

- Covers: financial instruments, business entities, corporate actions, indices, market data, loans, derivatives
- Built on OWL/RDF standards with formal semantics
- Enables interoperability across institutions and regulatory bodies
- Adopted by regulators (e.g., OFR, GLEIF) for entity identification and data harmonization
- Continuously maintained and extended by industry working groups

### 2.3 Industry Adoption

| Organization | KG Application | Scale / Notes |
|---|---|---|
| **Bloomberg** | Enterprise KG linking companies, people, securities, events | Billions of triples; powers Bloomberg Terminal analytics |
| **Refinitiv (LSEG)** | Permid entity graph, relationship extraction from news | Open identifiers for financial entities |
| **JPMorgan** | Internal KG for regulatory compliance, AML | Connects transaction data with entity relationships |
| **Goldman Sachs** | KG for market intelligence and research | Links financial data with alternative data sources |
| **Moody's Analytics** | Orbis company network, ownership chains | ~400M company records with beneficial ownership |
| **IHS Markit (S&P Global)** | Supply chain and corporate hierarchy mapping | Used in supply chain risk analytics |
| **Central Banks** | GLEIF LEI graph, regulatory reporting KGs | Entity identification and systemic risk mapping |

### 2.4 Financial NLP to KG Construction Pipeline

A typical pipeline for constructing financial knowledge graphs from text:

1. **Corpus collection**: Financial news (Reuters, Bloomberg), SEC filings (10-K, 10-Q, 8-K), earnings call transcripts, analyst reports, central bank communications
2. **Named Entity Recognition (NER)**: Identifying financial entities — companies, people, instruments, monetary amounts, dates (FinBERT, domain-adapted NER models)
3. **Relation Extraction (RE)**: Extracting relationships — acquisitions, partnerships, supply relationships, executive appointments (supervised & distant supervision approaches)
4. **Entity Linking / Resolution**: Mapping extracted entities to canonical identifiers (LEI, ISIN, CUSIP, Permid)
5. **Knowledge Graph Construction**: Populating RDF/property graph stores with extracted triples
6. **Temporal enrichment**: Adding timestamps, validity periods, and provenance metadata
7. **Reasoning & inference**: Applying ontological rules to derive implicit knowledge

**Key research:**
- **Ding, Zhang, Liu & Duan (2019)**: Knowledge graph construction for financial text
- **Chen, Wei & Huang (2018)**: FinKG — financial knowledge graph from SEC filings
- **Cheng, Xu & Farmer (2024)**: FinDKG — dynamic KG from financial news with temporal link prediction

### 2.5 Recent Advances: GraphRAG and LLM Integration

- **GraphRAG (Microsoft Research, 2024)**: Combines knowledge graphs with retrieval-augmented generation for structured reasoning over large document collections
- **KG-enhanced financial LLMs**: Using knowledge graphs to ground LLM outputs, reduce hallucination, and enable structured financial reasoning
- **Automated KG construction with LLMs**: Using GPT-4, Claude, and similar models for zero-shot relation extraction and ontology learning
- **Multi-modal financial KGs**: Integrating structured data (financial statements), unstructured text, and temporal market data into unified graph representations

---

## 3. Intersection of Economics and Computer Science

### 3.1 Methodological Traditions

| Dimension | Economics | Computer Science |
|---|---|---|
| **Epistemology** | Theory-driven, deductive | Data-driven, inductive |
| **Causality** | Causal identification (IV, RDD, DiD) | Prediction-focused, correlation-based |
| **Models** | Equilibrium models, optimization | Machine learning, scalable algorithms |
| **Agents** | Representative agent / heterogeneous agents with micro-foundations | Nodes in networks, features in ML |
| **Validation** | Econometric hypothesis testing | Train/test splits, benchmarks |
| **Data** | Panel data, national accounts, surveys | Web-scale data, alternative data |
| **Publication** | Top-5 journals, long review cycles | Conference papers (NeurIPS, ICML, KDD), fast cycles |

### 3.2 Convergence Areas

**Graph Neural Networks for Economic Prediction:**
- GNNs applied to supply chain networks for macro forecasting (Brintrup et al., 2020)
- Stock prediction using company relationship graphs (Feng et al., 2019)
- Credit risk assessment with borrower-lender network features (Wang et al., 2021)

**Knowledge Graphs for Financial Regulation:**
- Regulatory compliance checking via ontological reasoning
- Anti-money laundering through entity resolution and graph analytics
- Beneficial ownership networks for tax transparency (e.g., OpenCorporates, GLEIF)

**NLP for Economic Text:**
- Central bank communication analysis (Hansen & McMahon, 2016; Shapiro et al., 2022)
- Measuring economic sentiment and uncertainty (Baker, Bloom & Davis, 2016)
- Extracting supply chain relationships from earnings calls (Barrot & Sauvagnat, 2016)

**Agent-Based Computational Economics:**
- Multi-agent simulation of financial markets (Farmer & Foley, 2009)
- Combining ABM with network topology (Thurner, Farmer & Geanakoplos, 2012)
- Reinforcement learning agents in economic environments

### 3.3 Complementarities and Tensions

**Where economics strengthens CS:**
- Causal reasoning and identification strategies prevent spurious ML predictions
- Equilibrium thinking provides structural constraints on models
- Welfare analysis and mechanism design offer normative frameworks
- Domain knowledge prevents "garbage in, garbage out" in financial ML

**Where CS strengthens economics:**
- Scalable computation for large-scale network analysis
- Flexible non-parametric models that capture complex patterns
- Knowledge representation for organizing vast institutional knowledge
- NLP and information extraction from unstructured economic text at scale

**Ongoing tensions:**
- Interpretability vs. predictive power
- Structural models vs. reduced-form ML
- Causal inference vs. pattern recognition
- Small-sample econometric rigor vs. large-scale data mining
- Publication culture and incentive differences

### 3.4 Emerging Synthesis

A productive synthesis is emerging in several areas:

- **Causal ML**: Combining ML flexibility with econometric causal identification (Athey & Imbens, 2019; Chernozhukov et al., 2018)
- **Structural estimation + ML**: Using ML within structural economic models for estimation
- **Network econometrics**: Rigorous statistical inference on network data (de Paula, 2017; Graham, 2017)
- **Economics-informed GNNs**: Incorporating economic theory (equilibrium, no-arbitrage) as inductive biases in graph neural networks
- **LLMs as economic agents**: Simulating economic behavior with language models (Horton, 2023)

---

## References

- Acemoglu, D., Carvalho, V.M., Ozdaglar, A. & Tahbaz-Salehi, A. (2012). The network origins of aggregate fluctuations. *Econometrica*, 80(5), 1977–2016.
- Acemoglu, D., Ozdaglar, A. & Tahbaz-Salehi, A. (2015). Systemic risk and stability in financial networks. *American Economic Review*, 105(2), 564–608.
- Allen, F. & Gale, D. (2000). Financial contagion. *Journal of Political Economy*, 108(1), 1–33.
- Athey, S. & Imbens, G.W. (2019). Machine learning methods that economists should know about. *Annual Review of Economics*, 11, 685–725.
- Baker, S.R., Bloom, N. & Davis, S.J. (2016). Measuring economic policy uncertainty. *Quarterly Journal of Economics*, 131(4), 1593–1636.
- Barrot, J.N. & Sauvagnat, J. (2016). Input specificity and the propagation of idiosyncratic shocks in production networks. *Quarterly Journal of Economics*, 131(3), 1543–1592.
- Battiston, S., Puliga, M., Kaushik, R., Tasca, P. & Caldarelli, G. (2012). DebtRank: Too central to fail? *Scientific Reports*, 2, 541.
- Bonanno, G., Lillo, F. & Mantegna, R.N. (2001). High-frequency cross-correlation in a set of stocks. *Quantitative Finance*, 1(1), 96–104.
- Boss, M., Elsinger, H., Summer, M. & Thurner, S. (2004). Network topology of the interbank market. *Quantitative Finance*, 4(6), 677–684.
- Caldarelli, G. (2007). *Scale-Free Networks: Complex Webs in Nature and Technology*. Oxford University Press.
- Carvalho, V.M. (2014). From micro to macro via production networks. *Journal of Economic Perspectives*, 28(4), 23–48.
- Cheng, M., Xu, M. & Farmer, J.D. (2024). FinDKG: Dynamic knowledge graphs with large language models for detecting global trends in financial markets. Working paper.
- Cont, R., Moussa, A. & Santos, E.B. (2013). Network structure and systemic risk in banking systems. In *Handbook on Systemic Risk*, Cambridge University Press.
- Craig, B. & von Peter, G. (2014). Interbank tiering and money center banks. *Journal of Financial Intermediation*, 23(3), 322–347.
- Eisenberg, L. & Noe, T.H. (2001). Systemic risk in financial systems. *Management Science*, 47(2), 236–249.
- Elliott, M., Golub, B. & Jackson, M.O. (2014). Financial networks and contagion. *American Economic Review*, 104(10), 3115–3153.
- Farmer, J.D. & Foley, D. (2009). The economy needs agent-based modelling. *Nature*, 460, 685–686.
- Glasserman, P. & Young, H.P. (2016). Contagion in financial networks. *Journal of Economic Literature*, 54(3), 779–831.
- Haldane, A.G. (2009). Rethinking the financial network. Speech at the Financial Student Association, Amsterdam.
- Haldane, A.G. & May, R.M. (2011). Systemic risk in banking ecosystems. *Nature*, 469, 351–355.
- Mantegna, R.N. (1999). Hierarchical structure in financial markets. *European Physical Journal B*, 11, 193–197.
- Wang, J. et al. (2021). Graph neural networks for credit risk. Various venues.
