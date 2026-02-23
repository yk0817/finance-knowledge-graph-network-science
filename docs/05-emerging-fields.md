# Emerging Fields in Financial Network Science

This document surveys the frontier domains where network science, knowledge graphs, and graph analytics are being applied to financial systems. These emerging fields represent the next wave of innovation—from decentralized finance and climate risk to CBDC payment networks and regulatory technology.

---

## 1. DeFi and Cryptocurrency Networks

### 1.1 Key Projects and Platforms

#### GraphSense (AIT Vienna)

**GraphSense** is an open-source cryptocurrency analytics platform developed by Bernhard Haslhofer and colleagues at the Austrian Institute of Technology (AIT).

- **Core Capabilities:**
  - Multi-currency blockchain analysis (Bitcoin, Ethereum, Litecoin, Zcash).
  - Address clustering: linking addresses to real-world entities through heuristic analysis.
  - Transaction flow visualization: interactive graph exploration of fund flows.
  - Cross-chain analytics: tracking value transfers across multiple blockchains.
- **Architecture:** Apache Spark-based backend, Cassandra database, REST API, web dashboard.
- **Open Source:** Freely available for academic research and compliance use.
- **Reference:** Haslhofer, B. et al. (2016). "O Bitcoin Where Art Thou? Insight into Large-Scale Transaction Graphs." SEMANTiCS.
- **URL:** https://graphsense.info

#### Chainalysis

- **Position:** Leading blockchain analytics company, serving government agencies, exchanges, and financial institutions.
- **Products:**
  - **KYT (Know Your Transaction):** Real-time transaction monitoring for compliance.
  - **Reactor:** Investigation tool for tracing cryptocurrency flows across addresses and entities.
  - **Kryptos:** Risk scoring for cryptocurrency addresses and transactions.
- **Network Analysis:** Builds and maintains one of the largest cryptocurrency entity graphs, mapping addresses to real-world identities.
- **Data Coverage:** Bitcoin, Ethereum, 100+ other blockchains.
- **Use Cases:** AML compliance, sanctions screening, law enforcement investigations.

#### Elliptic

- **Position:** ML-based crypto risk scoring and compliance platform.
- **Elliptic Dataset:** Publicly available Bitcoin transaction dataset with labeled illicit/licit transactions—widely used benchmark for GNN-based fraud detection.
  - 203,769 transactions, 234,355 edges.
  - 4,545 illicit, 42,019 licit, 157,205 unlabeled transactions.
  - Used in 100+ academic papers.
- **Network Analysis:**
  - Temporal transaction graph analysis for identifying money laundering patterns.
  - Cross-chain tracing through bridge protocols and DEXs.
- **Reference:** Weber, M. et al. (2019). "Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics." KDD Workshop.

### 1.2 DeFi Composability Graphs

DeFi protocols are inherently composable—they interact with each other like building blocks, creating complex dependency networks.

- **Protocol Interaction Networks:** Nodes are DeFi protocols (Aave, Compound, Uniswap, MakerDAO), edges represent interactions (flash loans, collateral, liquidity provision).
- **Liquidity Flow Networks:** Tracking how liquidity moves between protocols, identifying systemic liquidity risks.
- **Composability Risk:** The "DeFi Lego" concept means a failure in one protocol can cascade through the network. Network analysis quantifies these contagion risks.
- **Smart Contract Dependency Graphs:** Mapping which contracts call which other contracts, identifying critical infrastructure protocols.
- **Reference:** Gudgeon, L. et al. (2020). "DeFi Protocols for Loanable Funds: Interest Rates, Liquidity and Market Efficiency." AFT.

### 1.3 Token Transfer Networks

- **ERC-20 Flow Analysis:** Constructing directed weighted graphs from token transfer events on Ethereum. Node = address, edge = token transfer, weight = transfer volume.
- **Network Properties:**
  - Power-law degree distributions (few addresses handle most volume).
  - Small-world properties in token transfer networks.
  - Community structure corresponding to protocol ecosystems.
- **Applications:**
  - Token velocity measurement for valuation models.
  - Wash trading detection through network pattern analysis.
  - Whale tracking: identifying large holders and their transaction patterns.

### 1.4 DEX/AMM Liquidity Networks

- **Automated Market Makers (AMMs):** Uniswap, Curve, Balancer create liquidity pools that form bipartite networks (tokens × pools).
- **Liquidity Network Analysis:**
  - Token reachability: which tokens can be swapped in how many hops.
  - Liquidity concentration risk: how concentrated liquidity is across pools.
  - Impermanent loss networks: how correlated pool exposures propagate losses.
- **DEX Aggregator Routing:** Optimal route finding through DEX liquidity networks (1inch, Paraswap use graph algorithms).

### 1.5 MEV (Maximal Extractable Value) Relay Networks

- **MEV Supply Chain:** A network of searchers, builders, and relayers competing to extract value from transaction ordering.
- **Network Analysis:**
  - Searcher-builder relationship networks.
  - MEV flow graphs: tracking value extraction across the MEV supply chain.
  - Censorship analysis: which builders/relayers censor certain transactions.
- **Reference:** Flashbots research on MEV ecosystem network structure.

### 1.6 NFT Transfer and Pricing Networks

- **NFT Transfer Graphs:** Tracking ownership transfer networks for NFT collections.
- **Applications:**
  - Wash trading detection: circular transfer patterns in NFT markets.
  - Price manipulation networks: coordinated bidding patterns.
  - Social network effects on NFT pricing: influence propagation from notable collectors.
- **Network Properties:** Highly clustered, with hub addresses (marketplaces, whales) dominating.

### 1.7 Key Papers on Blockchain Network Analysis

| Year | Paper | Focus | Method |
|------|-------|-------|--------|
| 2013 | Ron & Shamir, "Quantitative Analysis of the Full Bitcoin Transaction Graph" | Bitcoin network topology | Graph statistics |
| 2014 | Kondor et al., "Do the Rich Get Richer? Wealth Distribution in Bitcoin" | Wealth distribution | Network analysis |
| 2016 | Haslhofer et al., "O Bitcoin Where Art Thou?" | Cryptocurrency analytics | GraphSense platform |
| 2018 | Chen et al., "Understanding Ethereum via Graph Analysis" | Ethereum network | Multi-graph analysis |
| 2019 | Weber et al., "AML in Bitcoin" | Fraud detection | GCN on Bitcoin graph |
| 2020 | Gudgeon et al., "DeFi Protocols for Loanable Funds" | DeFi composability | Protocol interaction graphs |
| 2020 | Victor & Weintraud, "Detecting DeFi Securities Violations" | DeFi regulation | Transaction graph analysis |
| 2021 | Ao et al., "Temporal Analysis of the Entire Ethereum Blockchain Network" | Ethereum temporal | Dynamic network analysis |
| 2022 | Flashbots, "MEV and Me" | MEV ecosystem | MEV supply chain network |
| 2023 | Heimbach et al., "DeFi Lending During The Merge" | DeFi systemic risk | Liquidity network analysis |

---

## 2. ESG and Climate Finance Networks

### 2.1 NGFS (Network for Greening the Financial System)

The **NGFS** is a coalition of central banks and financial supervisors working to integrate climate risk into financial stability monitoring.

- **Membership:** 141 central banks and supervisors, 22 observers (as of 2025).
- **Climate Scenarios:**
  - Orderly transition (Net Zero 2050).
  - Disorderly transition (Delayed Transition).
  - Hot house world (Current Policies, Nationally Determined Contributions).
- **Network Relevance:**
  - Climate scenarios propagate through financial networks: physical risk → asset devaluation → portfolio losses → counterparty defaults → systemic contagion.
  - NGFS scenarios are used as inputs for network-based climate stress testing.
- **Reference:** NGFS (2022). "Climate Scenarios for Central Banks and Supervisors."
- **URL:** https://www.ngfs.net

### 2.2 Battiston et al.: Climate Stress Testing Through Financial Networks

Stefano Battiston (University of Zurich) and colleagues have pioneered the integration of climate science and financial network analysis.

- **Key Contributions:**
  - **CLIMAFIN model:** Climate stress testing framework that propagates climate shocks through financial networks (banks, funds, insurance companies).
  - **Climate VaR:** Network-enhanced climate Value-at-Risk that accounts for contagion effects.
  - **Carbon stranded assets:** Quantifying how unburnable carbon reserves create losses that propagate through ownership and lending networks.
  - **Green Swan:** Concept of climate-related systemic financial crises (with BIS).
- **Network Methodology:**
  - Bipartite networks: financial institutions × climate-sensitive assets.
  - Contagion cascades: fire sales triggered by climate-related asset devaluation.
  - Multi-layer networks: physical risk + transition risk propagating through different financial channels.
- **Key References:**
  - Battiston, S. et al. (2017). "A Climate Stress-Test of the Financial System." Nature Climate Change.
  - Battiston, S. et al. (2021). "The Price of Complexity in Financial Networks." PNAS.

### 2.3 ESG Knowledge Graphs

- **Concept:** Linking companies to ESG (Environmental, Social, Governance) factors through knowledge graph structures.
- **Architecture:**
  - Entities: Companies, ESG factors, UN SDGs, regulatory frameworks, emissions data.
  - Relations: emits_CO2, violates_regulation, supplies_to, operates_in, scores_on.
  - Temporal dimension: tracking ESG score evolution over time.
- **Applications:**
  - ESG scoring with network context: a company's ESG risk is influenced by its supply chain's ESG performance.
  - Greenwashing detection: identifying inconsistencies between ESG claims and KG-derived facts.
  - Impact investment screening: multi-hop KG queries for sustainable investment identification.
- **Data Sources:** CDP (Carbon Disclosure Project), SASB standards, GRI reports, TCFD disclosures.

### 2.4 Carbon Credit Trading Networks

- **Network Structure:** Participants (companies, countries, intermediaries) connected by carbon credit trades.
- **Analysis:**
  - Price discovery through network structure.
  - Market concentration and liquidity in carbon markets.
  - Fraud detection: identifying circular trading patterns in voluntary carbon markets.
- **Platforms:** EU ETS, voluntary carbon markets (Verra, Gold Standard).

### 2.5 Green Bond Networks and Taxonomy Alignment

- **Green Bond Issuer-Investor Networks:** Who finances whom for green projects.
- **Taxonomy Alignment:** Mapping bonds to EU Taxonomy, CBI (Climate Bonds Initiative) standards through KG.
- **Network Analysis:**
  - Green bond market structure and concentration.
  - Contagion risk in green bond portfolios.
  - Investor network effects on green bond pricing.

### 2.6 Climate Risk Transmission Through Supply Chain Networks

- **Physical Risk Propagation:** Climate events (floods, droughts, storms) impact specific geographic regions, propagating through supply chain networks.
- **Network Models:**
  - Supply chain graphs + climate hazard maps → impact propagation models.
  - Multi-hop propagation: Tier 1, Tier 2, Tier N supplier risk.
  - Geographic concentration risk: supply chain bottlenecks in climate-vulnerable regions.
- **Reference:** Pichler, A. et al. (2022). "Forecasting the Propagation of Pandemic Shocks with a Dynamic Input-Output Model." Journal of Economic Behavior & Organization.

### 2.7 TCFD Reporting and Network-Based Climate Risk Assessment

- **TCFD (Task Force on Climate-related Financial Disclosures):** Framework for climate risk disclosure.
- **Network Enhancement:**
  - KG-based TCFD compliance checking: mapping company disclosures to TCFD requirements.
  - Scenario analysis with network models: combining NGFS scenarios with financial network contagion.
  - Peer comparison networks: benchmarking climate disclosure quality across industry networks.

---

## 3. Supply Chain Finance Networks

### 3.1 GNN for Supply Chain Finance Risk Assessment

- **Problem:** Assess credit risk of supply chain participants considering network position and dependency structure.
- **Approach:**
  - Construct supply chain graph (buyer-supplier edges, weighted by trade volume).
  - Apply GNNs to learn node embeddings incorporating network structure.
  - Predict default probability, late payment risk, or creditworthiness.
- **Key Insight:** A company's risk is not just determined by its own financials but by its network position—central nodes in supply chains face different risks than peripheral ones.
- **Models:** GraphSAGE for inductive prediction on new supply chain participants, GAT for attention-weighted risk aggregation.

### 3.2 Bloomberg Supply Chain Data and Momentum Factor

- **Bloomberg SPLC (Supply Chain):** Comprehensive dataset of disclosed supplier-customer relationships.
- **Supply Chain Momentum Factor:**
  - Customer returns predict supplier returns (information flows through supply chains with delay).
  - Network-based alpha: constructing trading signals from supply chain graph structure.
  - Lead-lag relationships identified through network topology.
- **Reference:** Cohen, L. & Frazzini, A. (2008). "Economic Links and Predictable Returns." Journal of Finance.

### 3.3 Trade Finance Networks

- **Letters of Credit Networks:** Banks, importers, exporters connected through LC issuance and confirmation.
- **Factoring/Reverse Factoring Networks:** Financial institutions, anchor buyers, SME suppliers.
- **Network Analysis:**
  - Credit risk propagation through trade finance chains.
  - Fraud detection: duplicate financing, phantom invoices identified through network patterns.
  - Trade-based money laundering: unusual trade price/volume patterns in transaction networks.

### 3.4 Supply Chain Disruption Propagation Models

- **Network Contagion Models:**
  - Cascade failures in supply chain networks when critical nodes (suppliers) fail.
  - Epidemic models (SIR/SIS) adapted for disruption propagation.
  - Percolation theory applied to supply chain resilience.
- **Metrics:**
  - Network robustness: how many node/edge removals before network fragments.
  - Criticality scores: identifying the most systemically important supply chain nodes.
  - Recovery dynamics: how fast do supply chain networks reconstitute after disruption.

### 3.5 COVID-19 and Supply Chain Network Resilience

- **Impact:** COVID-19 exposed vulnerabilities in global supply chain networks, driving massive interest in network-based resilience analysis.
- **Key Findings:**
  - Concentrated supply chains (few dominant suppliers) are fragile to targeted disruptions.
  - Geographic clustering creates correlated failure risk.
  - Multi-tier visibility (beyond Tier 1) is critical for risk assessment.
- **Network Responses:**
  - Diversification strategies guided by network analysis.
  - Nearshoring decisions informed by supply chain graph restructuring.
  - Digital twin supply chain networks for scenario simulation.
- **Reference:** Inoue, H. & Todo, Y. (2020). "The Propagation of the Economic Impact through Supply Chains: The Case of a Mega-City Lockdown." PLoS ONE.

### 3.6 Dual-Use: Physical Supply Chain x Financial Supply Chain Networks

- **Concept:** Physical goods flow networks and financial flow networks are intertwined—combining both provides richer risk analysis.
- **Multi-Layer Network:**
  - Layer 1: Physical supply chain (goods flow).
  - Layer 2: Financial supply chain (payment flow, trade finance).
  - Layer 3: Information flow (orders, forecasts, contracts).
- **Applications:** Integrated risk assessment, trade-based money laundering detection, working capital optimization.

---

## 4. Insurance and Reinsurance Networks

### 4.1 BoE Working Paper No. 1000

The **Bank of England Working Paper No. 1000** provides a landmark analysis of network structure in reinsurance markets.

- **Title:** "Network structure and fragility of the UK reinsurance market."
- **Key Findings:**
  - The reinsurance market exhibits a core-periphery network structure.
  - A small number of large reinsurers form a densely connected core.
  - Failure of core reinsurers can cascade through the network, amplifying losses.
  - Network structure affects market pricing and capacity.
- **Methodology:** Bilateral reinsurance contract data analyzed using network science tools (degree distribution, betweenness centrality, core-periphery decomposition).
- **Implications:** Regulatory focus on systemically important reinsurers (G-SIIs).
- **Reference:** Bank of England Staff Working Paper No. 1000 (2022).

### 4.2 Reinsurance Network Topology and Systemic Risk

- **Network Structure:**
  - Bipartite: insurers × reinsurers.
  - Layered: primary insurance → reinsurance → retrocession.
  - Multi-line: property, casualty, life reinsurance as different edge types.
- **Systemic Risk Analysis:**
  - Contagion through shared reinsurance exposures (common reinsurer problem).
  - Spiral effects: losses trigger reinsurance calls, reducing capacity, increasing premiums, triggering further losses.
  - Network-based stress testing for reinsurance sector.
- **Key Metric:** Reinsurance dependency ratio—how concentrated an insurer's cession is across reinsurers.

### 4.3 Insurance-Linked Securities (ILS) Networks

- **ILS Market Network:**
  - Sponsors (insurers/reinsurers) → SPVs → investors.
  - Catastrophe bonds, industry loss warranties, collateralized reinsurance.
- **Network Analysis:**
  - Investor concentration risk in ILS markets.
  - Trigger correlation networks: how cat bond triggers are correlated across deals.
  - ILS fund interconnectedness and systemic risk.

### 4.4 Cyber Risk Aggregation Through Network Models

- **Problem:** Cyber risk is highly correlated—a single vulnerability can affect many organizations simultaneously.
- **Network Approach:**
  - Technology dependency networks: which organizations share software, cloud providers, IT infrastructure.
  - Cyber supply chain risk: propagation of breaches through vendor networks.
  - Accumulation risk: estimating correlated cyber losses through network structure.
- **Insurance Implications:**
  - Pricing cyber insurance with network-based correlation models.
  - Portfolio aggregation risk for cyber insurers.
  - Cyber catastrophe modeling using network contagion.

### 4.5 Catastrophe Risk and Geographic Correlation Networks

- **Natural Catastrophe Networks:**
  - Exposure networks: which insurers/reinsurers are exposed to the same geographic perils.
  - Correlation networks: correlation of losses across perils and regions.
  - Retrocession chains: how catastrophe risk is distributed through the reinsurance network.
- **Climate Change Impact:** Increasing correlation in catastrophe networks as climate change creates more simultaneous extreme events across regions.

---

## 5. CBDC and Payment Networks

### 5.1 Fedwire Topology (Soramaki et al., 2007)

A pioneering study that applied network science to payment systems for the first time.

- **Paper:** Soramaki, K. et al. (2007). "The topology of interbank payment flows." Physica A.
- **Key Findings:**
  - Fedwire exhibits a small-world network structure.
  - Highly skewed degree distribution: a few banks process most payments.
  - Core-periphery structure: a small core of major banks connects the entire network.
  - Network topology is remarkably stable over time despite daily variation in individual flows.
- **Impact:** Launched the field of payment network analysis and influenced central bank network monitoring worldwide.
- **Data:** 9,500 participants, 700,000 daily transfers, $1.3 trillion daily value (at time of study).

### 5.2 TARGET2 (ECB)

- **System:** Trans-European Automated Real-time Gross settlement Express Transfer system.
- **Network Analysis:**
  - Tiered structure: direct and indirect participants create a layered network.
  - Liquidity recycling: how payment flows create liquidity efficiency through network cycles.
  - Intraday dynamics: network topology changes throughout the trading day.
  - Stress testing: simulating participant failures and measuring network-wide liquidity impact.
- **References:**
  - ECB Occasional Paper Series on TARGET2 network analysis.
  - Arciero, L. et al. (2009). "How to Measure the Unsecured Money Market? The Eurosystem's Implementation and Validation."

### 5.3 CBDC Network Effects

- **Retail CBDC:**
  - Network effects of adoption: critical mass dynamics on payment networks.
  - Two-sided network analysis: merchants and consumers adoption interdependence.
  - Privacy-preserving network analytics: analyzing payment patterns without revealing identities.
- **Wholesale CBDC:**
  - Interbank settlement network restructuring.
  - DvP (Delivery versus Payment) atomic settlement through smart contracts.
  - Cross-border CBDC corridors: bilateral and multilateral network topologies.
- **Interoperability:**
  - Multi-CBDC platform network design (mBridge, Project Dunbar).
  - Hub-and-spoke vs. peer-to-peer network architectures.
  - Foreign exchange settlement: reducing Herstatt risk through network design.
- **References:**
  - BIS (2022). "Project mBridge: Connecting economies through CBDC."
  - Auer, R. et al. (2021). "Multi-CBDC arrangements and the future of cross-border payments." BIS Papers.

### 5.4 Cross-Border Payment Networks

#### SWIFT Network

- **Network Structure:** ~11,000 financial institutions in 200+ countries connected through messaging network.
- **Analysis:**
  - Correspondent banking network topology.
  - Payment corridor analysis: volume and value flows between country pairs.
  - De-risking effects: how correspondent banking relationship termination reshapes the network.
  - Geopolitical risk: network fragmentation scenarios (sanctions, geopolitical tensions).

#### Correspondent Banking

- **Network Challenges:**
  - Declining number of correspondent banking relationships (de-risking trend).
  - Increased concentration: fewer but larger correspondent banks.
  - Financial inclusion implications: remote/small economies losing network connectivity.
- **Network-Based Solutions:**
  - Hub optimization: identifying optimal correspondent banking hub placement.
  - Payment routing efficiency through network analysis.
  - Risk-based approach to correspondent banking using network metrics.

### 5.5 Real-Time Gross Settlement (RTGS) Network Optimization

- **Liquidity Optimization:**
  - Netting algorithms: reducing gross liquidity needs through network-based netting.
  - LSM (Liquidity Saving Mechanisms): offsetting queues based on bilateral/multilateral netting.
  - Gridlock resolution: detecting and resolving circular payment dependencies.
- **Network Design:**
  - Tiered participation: direct vs. indirect access and network implications.
  - Operational resilience: network robustness to participant outages.
  - Migration strategies: how RTGS modernization programs (UK, Euro area, US) redesign network architecture.

### 5.6 Stablecoin Payment Networks

- **Network Analysis:**
  - USDT, USDC, DAI transfer networks on Ethereum and other chains.
  - Cross-chain stablecoin flow networks (bridging between L1s and L2s).
  - Stablecoin in DeFi: liquidity provision networks, lending protocol integration.
- **Regulatory Implications:**
  - Systemic importance assessment through network centrality analysis.
  - Reserve backing network: which assets back stablecoins and through what custody chains.
  - Run risk: network contagion from stablecoin de-pegging events (Terra/UST case study).
- **Reference:** Lyons, R. & Viswanath-Natraj, G. (2023). "What Keeps Stablecoins Stable?" Journal of International Money and Finance.

---

## 6. RegTech Knowledge Graphs

### 6.1 FIBO (Financial Industry Business Ontology)

- **Developers:** EDM Council and OMG (Object Management Group).
- **Purpose:** Standard ontology for financial industry concepts, enabling semantic interoperability.
- **Structure:**
  - **Foundations:** Basic financial concepts (parties, contracts, dates).
  - **Business Entities:** Legal entities, corporate structures.
  - **Financial Instruments:** Securities, derivatives, loans.
  - **Indices and Indicators:** Market indices, economic indicators.
  - **Corporate Actions:** Dividends, splits, mergers.
- **Network Relevance:**
  - Provides the ontological backbone for financial knowledge graphs.
  - Enables cross-institution KG interoperability.
  - Standard edge types for financial entity relationships.
- **Adoption:** Major banks (Goldman Sachs, JP Morgan), regulators (SEC, BoE), data providers.
- **URL:** https://spec.edmcouncil.org/fibo/

### 6.2 FinRegOnt (Financial Regulation Ontology)

- **Purpose:** Ontology for representing financial regulations as structured, machine-readable knowledge.
- **Coverage:**
  - Regulatory rules and requirements.
  - Regulatory entities (supervisors, regulated entities).
  - Compliance obligations and reporting requirements.
  - Regulatory changes and their effective dates.
- **Applications:**
  - Automated compliance checking: mapping regulations to business processes.
  - Regulatory change management: tracking how rule changes affect compliance requirements.
  - Cross-jurisdiction comparison: mapping equivalent regulations across jurisdictions.

### 6.3 GraphRAG for Compliance

**GraphRAG** (Graph-enhanced Retrieval Augmented Generation) applies knowledge graphs to improve LLM-based regulatory interpretation.

- **Architecture:**
  - Regulatory corpus → KG construction (entities: regulations, requirements, entities, obligations).
  - User query → graph traversal + text retrieval → LLM generation with KG context.
- **Advantages Over Standard RAG:**
  - Multi-hop reasoning: "Which regulations apply to a bank that also offers insurance products in the EU?"
  - Relationship-aware retrieval: understanding regulatory hierarchies and cross-references.
  - Provenance tracking: every answer linked to specific regulatory sources through KG edges.
- **Applications:**
  - Automated regulatory interpretation for compliance teams.
  - Regulatory gap analysis: identifying missing compliance coverage.
  - Regulatory impact assessment: tracing how proposed rules affect existing compliance.

### 6.4 KYC/AML Knowledge Graphs

- **KYC (Know Your Customer) KG:**
  - Entity resolution: linking customer records across systems.
  - Beneficial ownership graphs: tracing ultimate beneficial owners through complex corporate structures.
  - PEP (Politically Exposed Persons) networks: relationship networks connecting customers to PEPs.
  - Sanctions screening with network context: identifying indirect sanctions exposure through relationships.
- **AML (Anti-Money Laundering) KG:**
  - Transaction pattern KGs: encoding suspicious transaction patterns as graph structures.
  - Typology networks: representing known money laundering typologies as subgraph patterns.
  - Alert investigation graphs: providing investigators with contextual relationship information.
  - Cross-institution AML: federated KGs for sharing risk signals across institutions.

### 6.5 Regulatory Reporting Networks

- **Reporting Topology:**
  - Regulated entities → regulators reporting relationships form a directed network.
  - Multi-regulator reporting: entities reporting to multiple supervisors (prudential, conduct, market).
  - Cross-border reporting: international reporting networks (CRS, FATCA, EMIR).
- **Network Optimization:**
  - Reducing reporting burden through network-based deduplication.
  - Identifying reporting gaps through network analysis.
  - Standardizing reporting through shared ontologies (FIBO, XBRL).

### 6.6 Legal Entity Identification

#### LEI (Legal Entity Identifier)

- **System:** Global system of 20-character codes uniquely identifying legally distinct entities in financial transactions.
- **GLEIF (Global LEI Foundation):** Manages the LEI system, maintains the LEI database.
- **Network Application:**
  - LEI relationship data: parent-child, fund-manager, branch relationships form a global corporate ownership network.
  - Ultimate parent mapping: tracing ownership chains to identify ultimate controlling entities.
  - LEI as the node identifier: standardized entity identification across financial knowledge graphs.
- **Statistics:** 2.5M+ active LEIs (as of 2025), covering entities in 200+ jurisdictions.

#### BODS (Beneficial Ownership Data Standard)

- **Purpose:** Open data standard for publishing beneficial ownership information.
- **Network Relevance:**
  - Structured format for ownership chains: person → company → company → etc.
  - Enables construction of global beneficial ownership networks.
  - Cross-border ownership tracing for AML and tax compliance.

### 6.7 SupTech (Supervisory Technology) and Network Monitoring

- **Concept:** Technology used by financial supervisors to enhance their regulatory and supervisory capabilities.
- **Network Monitoring Applications:**
  - Real-time financial network visualization for supervisors.
  - Early warning systems based on network structure changes.
  - Automated systemic risk assessment through network metrics.
  - Interconnectedness monitoring: tracking how financial institution networks evolve.
- **Examples:**
  - **BIS Innovation Hub:** SupTech projects for network-based supervision.
  - **ECB SupTech Lab:** AI and network analytics for banking supervision.
  - **MAS (Singapore):** Network analytics for financial stability monitoring.
  - **FCA (UK):** Market surveillance using network analysis of trading patterns.
- **Key Metrics Monitored:**
  - Interconnectedness indices (degree, betweenness, eigenvector centrality).
  - Concentration ratios in interbank networks.
  - Contagion simulation results under stress scenarios.
  - Cross-border exposure network dynamics.

### SupTech Network Monitoring Summary

| Supervisor | Tool/Platform | Network Focus |
|-----------|--------------|--------------|
| BIS Innovation Hub | Various SupTech projects | Cross-border network analysis |
| ECB | SupTech Lab | Banking network supervision |
| MAS Singapore | FEAT principles + analytics | Financial stability networks |
| FCA UK | Market surveillance | Trading network patterns |
| Fed (US) | Fedwire monitoring | Payment network topology |
| ESMA | EMIR data analytics | Derivatives network monitoring |

---

## Cross-Cutting Themes

### Convergence of Emerging Fields

The emerging fields described in this document are increasingly interconnected:

| Connection | Description |
|-----------|-------------|
| DeFi × ESG | Green DeFi protocols, carbon credit tokenization on blockchain |
| Supply Chain × ESG | Scope 3 emissions tracking through supply chain networks |
| CBDC × DeFi | Programmable money, DeFi-like functionality on CBDC platforms |
| Insurance × Climate | Climate risk modeling through insurance/reinsurance networks |
| RegTech × All Fields | Knowledge graphs for regulatory compliance across all emerging domains |
| Supply Chain × CBDC | Trade finance on programmable payment networks |

### Shared Methodological Challenges

1. **Data Availability:** Many emerging networks lack comprehensive, standardized data.
2. **Temporal Dynamics:** All networks evolve—requiring dynamic network analysis methods.
3. **Multi-Layer Integration:** Combining physical, financial, and information networks.
4. **Privacy-Preserving Analytics:** Analyzing sensitive financial networks without revealing individual data.
5. **Scalability:** Emerging networks (DeFi, payment systems) generate billions of transactions.
6. **Regulatory Uncertainty:** Rapidly evolving regulatory landscape for DeFi, CBDC, ESG.

---

## References

1. Soramaki, K. et al. (2007). "The topology of interbank payment flows." Physica A, 379(1), 317-333.
2. Ron, D. & Shamir, A. (2013). "Quantitative Analysis of the Full Bitcoin Transaction Graph." Financial Cryptography.
3. Haslhofer, B. et al. (2016). "O Bitcoin Where Art Thou? Insight into Large-Scale Transaction Graphs." SEMANTiCS.
4. Battiston, S. et al. (2017). "A Climate Stress-Test of the Financial System." Nature Climate Change, 7, 283-288.
5. Cohen, L. & Frazzini, A. (2008). "Economic Links and Predictable Returns." Journal of Finance, 63(4), 1977-2011.
6. Weber, M. et al. (2019). "Anti-Money Laundering in Bitcoin." KDD Workshop on Anomaly Detection in Finance.
7. Gudgeon, L. et al. (2020). "DeFi Protocols for Loanable Funds." AFT.
8. Inoue, H. & Todo, Y. (2020). "The Propagation of Economic Impact through Supply Chains." PLoS ONE.
9. Pichler, A. et al. (2022). "Forecasting the Propagation of Pandemic Shocks." Journal of Economic Behavior & Organization.
10. NGFS (2022). "Climate Scenarios for Central Banks and Supervisors."
11. BIS (2022). "Project mBridge: Connecting economies through CBDC."
12. Auer, R. et al. (2021). "Multi-CBDC arrangements and the future of cross-border payments." BIS Papers.
13. Bank of England Staff Working Paper No. 1000 (2022). "Network structure and fragility of the UK reinsurance market."
14. Battiston, S. et al. (2021). "The Price of Complexity in Financial Networks." PNAS.
15. Lyons, R. & Viswanath-Natraj, G. (2023). "What Keeps Stablecoins Stable?" Journal of International Money and Finance.
