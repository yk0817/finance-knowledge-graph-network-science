# Mathematical Foundations

This chapter provides the mathematical underpinnings for financial network science — from classical graph theory through spectral methods, random matrix theory, knowledge graph formalisms, graph neural networks, and the theory of dynamic and multilayer networks.

---

## 1. Graph Theory Fundamentals

### Basic Definitions

- **Graph**: $G = (V, E)$ where $V$ is a set of vertices (nodes) and $E \subseteq V \times V$ is a set of edges (links).
- **Undirected graph**: Edges are unordered pairs $\{u, v\}$; the relationship is symmetric.
- **Directed graph (digraph)**: Edges are ordered pairs $(u, v)$; direction matters (e.g., lending flows, ownership stakes).
- **Weighted graph**: Each edge carries a weight $w_{ij} \in \mathbb{R}$ (e.g., correlation strength, exposure size).
- **Bipartite graph**: $V = V_1 \cup V_2$ with $V_1 \cap V_2 = \emptyset$ and edges only between $V_1$ and $V_2$ (e.g., banks and assets, firms and directors).
- **Hypergraph**: Edges (hyperedges) can connect any number of nodes simultaneously (e.g., a syndicated loan involving multiple banks).

### Matrix Representations

- **Adjacency matrix** $\mathbf{A}$: $A_{ij} = 1$ (or $w_{ij}$) if edge $(i,j) \in E$, else 0. Symmetric for undirected graphs.
- **Degree matrix** $\mathbf{D}$: Diagonal matrix with $D_{ii} = \sum_j A_{ij}$ (the degree of node $i$).
- **Laplacian matrix** $\mathbf{L} = \mathbf{D} - \mathbf{A}$: Positive semidefinite for undirected graphs; encodes diffusion dynamics.
  - **Normalized Laplacian**: $\mathcal{L} = \mathbf{D}^{-1/2}\mathbf{L}\mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$
  - **Random walk Laplacian**: $\mathbf{L}_{rw} = \mathbf{D}^{-1}\mathbf{L} = \mathbf{I} - \mathbf{D}^{-1}\mathbf{A}$
- **Incidence matrix** $\mathbf{B}$: $N \times M$ matrix (N nodes, M edges); $B_{ie} = \pm 1$ indicating endpoints of edge $e$. Relates to the Laplacian via $\mathbf{L} = \mathbf{B}\mathbf{B}^T$.

### Paths, Walks, Cycles, and Connectivity

- **Walk**: A sequence of adjacent vertices (vertices and edges may repeat).
- **Path**: A walk with no repeated vertices.
- **Cycle**: A closed walk with no repeated vertices except start = end.
- **Connected graph**: There exists a path between every pair of vertices. For digraphs: **strongly connected** (directed path in both directions) vs. **weakly connected** (connected when ignoring edge direction).
- **Connected components**: Maximal connected subgraphs.
- **Shortest path distance** $d(u,v)$: Minimum number of edges (or minimum total weight) on any path from $u$ to $v$.
- **Diameter**: $\max_{u,v} d(u,v)$ — the longest shortest path in the graph.

### Trees and Spanning Trees

- **Tree**: A connected acyclic graph. A tree on $N$ nodes has exactly $N-1$ edges.
- **Spanning tree**: A subgraph that is a tree and includes all vertices of $G$.
- **Minimum Spanning Tree (MST)**: The spanning tree minimizing total edge weight. Algorithms: Kruskal's $O(E \log E)$, Prim's $O(E + V \log V)$.
- **Cayley's formula**: The complete graph $K_n$ has $n^{n-2}$ spanning trees.

### Planarity and Graph Embeddings

- **Planar graph**: Can be drawn in the plane without edge crossings.
- **Kuratowski's theorem**: A graph is planar iff it contains no subdivision of $K_5$ or $K_{3,3}$.
- **Euler's formula**: For connected planar graphs, $V - E + F = 2$ (where $F$ = number of faces).
- **Graph embeddings**: Representing graphs on surfaces of higher genus. Relevant to PMFG and TMFG construction in financial networks.

---

## 2. Centrality Measures

Centrality quantifies the "importance" of a node within a network. Different centrality measures capture different notions of importance.

### Degree Centrality

- **Definition**: $C_D(i) = k_i = \sum_j A_{ij}$
- **In-degree** (directed): $k_i^{in} = \sum_j A_{ji}$ — how many edges point to $i$.
- **Out-degree** (directed): $k_i^{out} = \sum_j A_{ij}$ — how many edges originate from $i$.
- **Weighted degree** (strength): $s_i = \sum_j w_{ij}$
- Simple and fast ($O(N)$); captures local importance but not global position.

### Betweenness Centrality

- **Shortest-path betweenness**: $C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$ where $\sigma_{st}$ is the number of shortest paths from $s$ to $t$ and $\sigma_{st}(v)$ is the number passing through $v$.
- Identifies **bottleneck** nodes: removal of high-betweenness nodes disrupts information/risk flow.
- **Flow betweenness**: Uses maximum flow instead of shortest paths — captures all possible routes, not just geodesics.
- Computational cost: $O(NE)$ for unweighted, $O(NE + N^2 \log N)$ for weighted (Brandes' algorithm).

### Closeness Centrality

- **Definition**: $C_C(i) = \frac{N-1}{\sum_{j \neq i} d(i,j)}$ — inverse of average distance to all other nodes.
- **Harmonic closeness**: $C_H(i) = \frac{1}{N-1}\sum_{j \neq i} \frac{1}{d(i,j)}$ — handles disconnected graphs (infinite distances become zero contribution).
- **Information centrality**: Based on information contained in all paths (not just shortest), using the graph's effective resistance.

### Eigenvector Centrality

- **Definition**: $\mathbf{A}\mathbf{x} = \lambda_1 \mathbf{x}$ — the eigenvector corresponding to the largest eigenvalue of the adjacency matrix.
- A node is important if it is connected to other important nodes (self-referential definition resolved by eigenvalue decomposition).
- **Bonacich power index**: $c_i(\alpha, \beta) = \sum_j (\alpha + \beta c_j) A_{ij}$ — parameterized centrality that interpolates between degree ($\beta = 0$) and eigenvector centrality.
- Converges via power iteration; requires the graph to be connected (by Perron-Frobenius theorem, the leading eigenvector is positive).

### PageRank

- Introduced by **Brin & Page (1998)** for ranking web pages.
- **Random walk interpretation**: PageRank is the stationary distribution of a random walker who, at each step, follows a random outgoing link with probability $\alpha$ and teleports to a uniformly random node with probability $1-\alpha$.
$$\mathbf{p} = \alpha \mathbf{D}^{-1}\mathbf{A}^T \mathbf{p} + \frac{1-\alpha}{N}\mathbf{1}$$
- **DebtRank as financial analogue**: Battiston et al. (2012) adapted the recursive centrality logic of PageRank to quantify systemic importance of financial institutions — a node's systemic impact depends on the impact of those it is connected to.
- Damping factor $\alpha$ (typically 0.85) controls the balance between local and global importance.

### Katz Centrality

- **Definition**: $C_{Katz}(i) = \sum_{k=1}^{\infty} \sum_{j} \alpha^k (A^k)_{ji}$
- Counts **all walks** of all lengths from other nodes to $i$, with attenuation factor $\alpha^k$ for walks of length $k$.
- Requires $\alpha < 1/\lambda_1$ for convergence.
- Closed form: $\mathbf{c} = ((\mathbf{I} - \alpha\mathbf{A}^T)^{-1} - \mathbf{I})\mathbf{1}$

### HITS (Hub and Authority Scores)

- **Kleinberg (1999)**: Hyperlink-Induced Topic Search.
- Two scores per node:
  - **Authority score** $a_i$: high if pointed to by good hubs.
  - **Hub score** $h_i$: high if pointing to good authorities.
- Mutual reinforcement: $\mathbf{a} = \mathbf{A}^T\mathbf{h}$, $\mathbf{h} = \mathbf{A}\mathbf{a}$
- Converges to leading eigenvectors of $\mathbf{A}^T\mathbf{A}$ (authorities) and $\mathbf{A}\mathbf{A}^T$ (hubs).
- Financial application: In directed ownership or lending networks, authorities are key borrowers/investees and hubs are key lenders/investors.

### Applications in Finance

| Centrality | Financial Application |
|---|---|
| Degree | Identifying most-connected banks in interbank networks |
| Betweenness | Finding critical intermediaries whose failure disrupts the system |
| Closeness | Assessing how quickly shocks propagate from a given institution |
| Eigenvector | Identifying systemically important institutions (connected to other important ones) |
| PageRank / DebtRank | Quantifying cascading systemic impact |
| HITS | Distinguishing key lenders (hubs) from key borrowers (authorities) |

---

## 3. Community Detection

### Modularity Optimization

- **Modularity** $Q$: Measures the fraction of edges within communities minus the expected fraction under a null model:
$$Q = \frac{1}{2m}\sum_{ij}\left[A_{ij} - \frac{k_i k_j}{2m}\right]\delta(c_i, c_j)$$
  where $m = \frac{1}{2}\sum_{ij} A_{ij}$, $k_i$ is the degree of node $i$, and $\delta(c_i, c_j) = 1$ if $i$ and $j$ are in the same community.

- **Newman-Girvan algorithm**: Iteratively remove edges with highest betweenness; dendrogram yields community structure. $O(N^2 E)$ — slow for large networks.
- **Louvain algorithm** (Blondel et al., 2008): Fast greedy modularity optimization. Two phases: (1) local node moves to maximize modularity gain, (2) aggregate communities into super-nodes. Repeat. Near-linear time.
- **Leiden algorithm** (Traag et al., 2019): Improved version of Louvain that guarantees well-connected communities and avoids poorly connected or disconnected communities.

### Spectral Methods

- **Spectral clustering**: Use the eigenvectors of the graph Laplacian $\mathbf{L}$ (or normalized Laplacian) to embed nodes in a low-dimensional space, then apply k-means.
- The **Fiedler vector** (eigenvector of second-smallest Laplacian eigenvalue) provides the optimal 2-way graph cut (continuous relaxation of the NP-hard minimum cut problem).
- Multi-way partitioning: use the $k$ smallest non-trivial eigenvectors for $k$-community detection.

### Stochastic Block Models (SBM)

- **Planted partition model**: Nodes divided into groups; edge probability depends only on group membership. Edges within groups with probability $p$, between groups with probability $q$.
- **Degree-corrected SBM**: Accounts for heterogeneous degree distributions within communities — more realistic for real-world networks.
- **Inference**: Maximum likelihood or Bayesian estimation. Avoids the resolution limit of modularity.
- **Detectability threshold**: Information-theoretic limit below which community structure cannot be detected (Decelle et al., 2011).

### Label Propagation

- Each node adopts the label most common among its neighbors; iterate until convergence.
- Very fast ($O(E)$ per iteration) but non-deterministic — results vary across runs.
- Useful for very large networks where modularity optimization is too slow.

### Overlapping Communities

- **BigCLAM** (Yang & Leskovec, 2013): Community detection via matrix factorization allowing nodes to belong to multiple communities.
- **DEMON** (Coscia, Rossetti, Giannotti, Pedreschi, 2012): Democratic Estimate of the Modular Organization of a Network — bottom-up label propagation for overlapping communities.
- Important for finance: a bank can belong to multiple communities (by geography, asset class, counterparty type).

### Financial Applications

| Method | Financial Application |
|---|---|
| Modularity (Louvain/Leiden) | Identifying market sectors from correlation networks |
| Spectral clustering | Segmenting banking systems by structural role |
| SBM | Modeling interbank lending community structure |
| Overlapping communities | Banks in multiple functional groups (lending, derivatives, payments) |
| All methods | Ownership cluster detection, supply chain community identification |

---

## 4. Network Models

### Erdos-Renyi (ER) Random Graph

- $G(N, p)$: Each of $\binom{N}{2}$ possible edges exists independently with probability $p$.
- **Phase transitions**: Giant connected component emerges at $p = 1/N$. At $p = \ln(N)/N$, the graph becomes almost surely connected.
- Degree distribution: Binomial → Poisson for large $N$.
- Clustering coefficient: $C = p$ — no excess clustering (unlike real networks).
- Used as a null model for comparison but unrealistic for financial networks.

### Barabasi-Albert (BA) Model

- **Preferential attachment**: New nodes connect to existing nodes with probability proportional to their degree.
- Produces **scale-free networks** with power-law degree distribution: $P(k) \sim k^{-3}$.
- "Rich get richer" — captures the emergence of hub nodes.
- Financial relevance: some financial networks show heavy-tailed degree distributions (major banks with many counterparties), though true power laws are debated.

### Watts-Strogatz (WS) Model

- Start with a regular ring lattice; rewire each edge with probability $\beta$.
- Produces **small-world networks**: high clustering coefficient (like lattices) + short average path length (like random graphs).
- Captures the "six degrees of separation" phenomenon observed in many social and financial networks.

### Configuration Model

- **Preserves an arbitrary degree sequence**: Given a degree sequence $\{k_1, k_2, \ldots, k_N\}$, generate a random graph uniformly from all graphs with that sequence.
- Used as a null model that preserves degree heterogeneity — tests whether observed properties (clustering, communities) go beyond what degree distribution alone explains.
- Can produce multi-edges and self-loops; variants correct for this.

### Stochastic Block Model (SBM)

- Generative model for community structure: assign each node to a group; edge probability depends on group pair.
- The most principled framework for community detection (avoids modularity resolution limit).
- **Degree-corrected SBM**: More realistic — allows within-group degree variation.
- **Hierarchical SBM**: Nested community structure at multiple scales.

### Exponential Random Graph Models (ERGM)

- **Maximum entropy models** with constraints: specify sufficient statistics (edge count, triangle count, degree sequence) and find the maximum entropy distribution over graphs consistent with those statistics.
$$P(G) = \frac{1}{Z}\exp\left(\sum_k \theta_k s_k(G)\right)$$
  where $s_k(G)$ are graph statistics and $\theta_k$ are parameters.
- Fit via MCMC (Markov Chain Monte Carlo).
- Financial applications: modeling interbank networks with prescribed properties (reciprocity, clustering, core-periphery structure).

### Financial Applications

| Model | Financial Application |
|---|---|
| ER | Null model benchmark for financial network properties |
| BA | Modeling emergence of hub banks and concentrated counterparty relationships |
| WS | Small-world structure of ownership and directorship networks |
| Configuration model | Testing significance of financial network patterns beyond degree effects |
| SBM | Inferring latent group structure in interbank and trading networks |
| ERGM | Modeling formation of OTC derivative networks, trade networks |

---

## 5. Spectral Graph Theory

### Graph Laplacian and Its Eigenvalues

The Laplacian $\mathbf{L} = \mathbf{D} - \mathbf{A}$ is central to spectral graph theory. For an undirected graph:

- $\mathbf{L}$ is positive semidefinite: all eigenvalues $0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_N$.
- Multiplicity of the zero eigenvalue equals the number of connected components.
- The eigenvectors form an orthonormal basis for "graph signals."

### Algebraic Connectivity (Fiedler Value)

- $\lambda_2$ is the **algebraic connectivity** or **Fiedler value** — the smallest non-zero Laplacian eigenvalue.
- Larger $\lambda_2$ → better connected graph (harder to disconnect by removing edges).
- The corresponding eigenvector (Fiedler vector) provides the optimal bipartition of the graph.
- Financial application: $\lambda_2$ of an interbank network measures systemic robustness — a low Fiedler value suggests the network can be easily fragmented.

### Cheeger Inequality and Graph Partitioning

- **Cheeger constant** $h(G) = \min_S \frac{|\partial S|}{\min(\text{vol}(S), \text{vol}(\bar{S}))}$ measures the "bottleneck" of a graph.
- **Cheeger inequality**: $\frac{\lambda_2}{2} \leq h(G) \leq \sqrt{2\lambda_2}$
- Links the spectral gap to combinatorial graph partitioning — spectral clustering has provable approximation guarantees.

### Spectral Gap and Mixing Time

- The **spectral gap** $\lambda_2$ (or $1 - \lambda_2$ for normalized Laplacian) controls the mixing time of random walks on the graph.
- Larger spectral gap → faster mixing → shocks dissipate more quickly.
- Financial application: a well-connected financial network (large spectral gap) distributes shocks rapidly, while a poorly connected one (small spectral gap) traps shocks locally.

### Applications in Financial Networks

- **Diffusion processes**: The heat equation on graphs, $\frac{d\mathbf{x}}{dt} = -\mathbf{L}\mathbf{x}$, models risk propagation; the Laplacian spectrum determines diffusion speed.
- **Stability analysis**: Eigenvalues of the network Laplacian determine the stability of equilibria in coupled dynamical systems on networks (e.g., synchronized market behavior).
- **Graph signal processing**: Fourier analysis on graphs using Laplacian eigenvectors — filtering financial signals on network domains.

---

## 6. Random Matrix Theory for Networks

### Marchenko-Pastur Law

For an $N \times T$ random matrix $\mathbf{X}$ with i.i.d. entries and $Q = N/T$, the eigenvalue distribution of $\frac{1}{T}\mathbf{X}\mathbf{X}^T$ converges to:

$$\rho(\lambda) = \frac{Q}{2\pi\sigma^2} \frac{\sqrt{(\lambda_+ - \lambda)(\lambda - \lambda_-)}}{\lambda}$$

where $\lambda_{\pm} = \sigma^2(1 \pm \sqrt{1/Q})^2$.

This provides the **null hypothesis** for correlation matrix eigenvalues — deviations from the Marchenko-Pastur bulk indicate genuine structure.

### Tracy-Widom Distribution

- Describes the fluctuations of the **largest eigenvalue** of random matrices.
- Used to test whether the largest eigenvalue of a financial correlation matrix is significantly above the Marchenko-Pastur edge (i.e., whether there is a detectable "market factor").
- Three universality classes: $\text{TW}_1$ (real symmetric), $\text{TW}_2$ (complex Hermitian), $\text{TW}_4$ (quaternion self-dual).

### Spiked Covariance Models

- **Model**: True covariance $\boldsymbol{\Sigma} = \mathbf{I} + \sum_{k=1}^{r} \theta_k \mathbf{v}_k\mathbf{v}_k^T$ — identity plus rank-$r$ perturbation.
- **BBP transition** (Baik, Ben Arous, Peche, 2005): A spike $\theta_k$ is detectable iff $\theta_k > \sqrt{Q}$. Below this threshold, the spike eigenvalue merges with the Marchenko-Pastur bulk.
- Financial implication: weak factors (e.g., small sector effects) become undetectable when $N/T$ is not small enough.

### Free Probability Theory

- Non-commutative probability theory developed by Voiculescu.
- **Free convolution**: Determines the eigenvalue distribution of sums or products of random matrices when they are "freely independent."
- Enables analytical computation of eigenvalue distributions for structured random matrices (e.g., signal + noise).
- Applied to optimal estimation of covariance matrices (Bun, Bouchaud, Potters, 2017).

### Applications

| Application | RMT Tool |
|---|---|
| Denoising correlation matrices | Marchenko-Pastur bulk removal, eigenvalue clipping |
| Factor detection | Spiked model, BBP transition |
| Community detection | Eigenvalue separation from bulk indicates group structure |
| Dynamic network estimation | Time-varying RMT for evolving correlation structure |
| Covariance estimation | Free probability-based optimal shrinkage (RIE) |

---

## 7. Knowledge Graph Formalisms

### RDF (Resource Description Framework)

- Data model based on **subject-predicate-object triples**: `(JPMorgan, hasExposureTo, GoldmanSachs)`.
- Global identifiers via URIs/IRIs.
- Can be stored as directed labeled graphs.
- Foundation of the Semantic Web.
- Schema: RDFS (RDF Schema) provides class hierarchies and domain/range constraints.

### Property Graphs

- Nodes and edges carry **key-value property dictionaries**.
- More flexible than RDF for real-world modeling: edges can have multiple attributes (exposure amount, maturity date, seniority).
- Native model for graph databases (Neo4j, Amazon Neptune, TigerGraph).
- No built-in schema enforcement (schema-optional).

### OWL (Web Ontology Language)

- Built on RDF; adds **ontological reasoning** capabilities.
- **Description Logic (DL) expressivity**: OWL profiles (EL, QL, RL, DL) trade off expressiveness vs. computational complexity.
- Enables automated inference: if "BankA isSubsidiaryOf BankB" and "BankB isRegulatedBy FED", infer "BankA isIndirectlyRegulatedBy FED".
- Financial ontologies: FIBO (Financial Industry Business Ontology) is OWL-based.

### SPARQL

- **Query language for RDF** data.
- Pattern matching on triple patterns: `SELECT ?bank WHERE { ?bank rdf:type fin:Bank . ?bank fin:hasExposureTo fin:GoldmanSachs . }`
- Supports aggregation, optional patterns, subqueries, federated queries across endpoints.

### Cypher / Gremlin

- **Cypher**: Declarative query language for property graphs (Neo4j). Pattern: `MATCH (a:Bank)-[:LENDS_TO]->(b:Bank) RETURN a, b`
- **Gremlin**: Imperative/functional traversal language for property graphs (Apache TinkerPop). Pattern: `g.V().hasLabel('Bank').out('LENDS_TO')`
- Both support path queries, aggregation, and complex traversals essential for financial network analysis.

### Knowledge Graph Embeddings

- Map entities and relations into continuous vector spaces for link prediction, entity alignment, and reasoning.

| Model | Scoring Function | Key Feature |
|---|---|---|
| **TransE** (Bordes et al., 2013) | $\|\mathbf{h} + \mathbf{r} - \mathbf{t}\|$ | Translation-based, simple, effective |
| **TransR** (Lin et al., 2015) | $\|\mathbf{M}_r\mathbf{h} + \mathbf{r} - \mathbf{M}_r\mathbf{t}\|$ | Relation-specific projection spaces |
| **RotatE** (Sun et al., 2019) | $\|\mathbf{h} \circ \mathbf{r} - \mathbf{t}\|$ | Rotation in complex space; models symmetry, inversion, composition |
| **ComplEx** (Trouillon et al., 2016) | $\text{Re}(\langle\mathbf{h}, \mathbf{r}, \bar{\mathbf{t}}\rangle)$ | Complex-valued; handles asymmetric relations |

- Financial applications: predicting missing financial relationships, supply chain link prediction, ownership chain completion.

### Financial KG Representation Choices

| Aspect | RDF/OWL | Property Graph |
|---|---|---|
| Standards compliance | W3C standards, FIBO ontology | Vendor-specific |
| Reasoning | Built-in inference via DL reasoners | Limited (application-level) |
| Flexibility | Schema-heavy | Schema-light |
| Query performance | SPARQL can be slow on complex queries | Optimized for traversals |
| Typical use | Regulatory reporting, data integration | Analytics, real-time queries |

---

## 8. Graph Neural Network Architectures

### GCN (Graph Convolutional Network)

- **Kipf & Welling (2017)**: Semi-supervised classification with graph convolutional networks.
- Layer-wise propagation: $\mathbf{H}^{(l+1)} = \sigma(\tilde{\mathbf{D}}^{-1/2}\tilde{\mathbf{A}}\tilde{\mathbf{D}}^{-1/2}\mathbf{H}^{(l)}\mathbf{W}^{(l)})$
  where $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}$ (self-loops) and $\tilde{\mathbf{D}}$ is its degree matrix.
- **Spectral interpretation**: Approximation of spectral graph convolutions using first-order Chebyshev polynomials.
- **Spatial interpretation**: Each node aggregates features from its immediate neighbors.
- Financial application: credit risk prediction on bank-firm networks, fraud detection.

### GAT (Graph Attention Network)

- **Velickovic et al. (2018)**: Graph Attention Networks.
- **Attention-weighted aggregation**: Different neighbors contribute differently to a node's representation.
$$\alpha_{ij} = \frac{\exp(\text{LeakyReLU}(\mathbf{a}^T[\mathbf{W}\mathbf{h}_i \| \mathbf{W}\mathbf{h}_j]))}{\sum_{k \in \mathcal{N}(i)} \exp(\text{LeakyReLU}(\mathbf{a}^T[\mathbf{W}\mathbf{h}_i \| \mathbf{W}\mathbf{h}_k]))}$$
- Multi-head attention for stability and expressiveness.
- Financial application: learning which financial relationships matter most for a given prediction task.

### GraphSAGE

- **Hamilton, Ying & Leskovec (2017)**: Inductive Representation Learning on Large Graphs.
- **Inductive learning**: Can generalize to unseen nodes (unlike transductive methods like GCN).
- **Sampling**: Samples a fixed number of neighbors at each layer, enabling scalability to large graphs.
- Aggregator variants: mean, LSTM, pooling.
- Financial application: new entity classification (e.g., newly listed companies), dynamic portfolio universes.

### GIN (Graph Isomorphism Network)

- **Xu et al. (2019)**: How Powerful are Graph Neural Networks?
- **Maximally expressive** among message-passing GNNs — as powerful as the Weisfeiler-Leman graph isomorphism test.
- Update: $\mathbf{h}_v^{(k)} = \text{MLP}^{(k)}\left((1 + \epsilon^{(k)}) \cdot \mathbf{h}_v^{(k-1)} + \sum_{u \in \mathcal{N}(v)} \mathbf{h}_u^{(k-1)}\right)$
- Financial application: graph-level classification tasks (e.g., classifying entire corporate structures as risky/safe).

### Message Passing Neural Networks (MPNN)

- **Gilmer et al. (2017)**: Neural Message Passing for Quantum Chemistry.
- **General framework** unifying most GNN architectures:
  1. **Message**: $\mathbf{m}_v^{(t+1)} = \sum_{w \in \mathcal{N}(v)} M_t(\mathbf{h}_v^{(t)}, \mathbf{h}_w^{(t)}, \mathbf{e}_{vw})$
  2. **Update**: $\mathbf{h}_v^{(t+1)} = U_t(\mathbf{h}_v^{(t)}, \mathbf{m}_v^{(t+1)})$
  3. **Readout**: $\hat{y} = R(\{\mathbf{h}_v^{(T)} | v \in G\})$
- Provides a vocabulary for describing and comparing GNN variants.

### Heterogeneous GNNs

- **HAN (Heterogeneous Attention Network)**: Wang et al. (2019) — hierarchical attention over meta-paths in heterogeneous graphs.
- **HGT (Heterogeneous Graph Transformer)**: Hu et al. (2020) — transformer-based message passing with type-specific parameters.
- Handle multi-type node/edge graphs naturally — essential for financial KGs with diverse entity and relationship types (banks, firms, regulators; lending, ownership, derivatives).

### Temporal GNNs

- **TGAT (Temporal Graph Attention)**: Xu et al. (2020) — attention over temporal neighborhoods with time encoding.
- **TGN (Temporal Graph Network)**: Rossi et al. (2020) — memory module for tracking node states over time.
- **DyRep**: Trivedi et al. (2019) — representation learning over dynamic graphs via temporal point processes.
- Financial application: modeling evolving financial networks (e.g., interbank lending patterns, time-varying correlations, governance structure changes).

### Financial Applications Summary

| Architecture | Financial Application |
|---|---|
| GCN | Credit scoring, fraud detection on transaction graphs |
| GAT | Identifying important financial relationships via attention |
| GraphSAGE | Inductive inference for new financial entities |
| GIN | Classification of corporate group structures |
| MPNN | General framework for financial network prediction |
| Heterogeneous GNNs | Multi-type financial knowledge graph reasoning |
| Temporal GNNs | Dynamic risk assessment, evolving network modeling |

---

## 9. Temporal and Dynamic Networks

### Time-Varying Graphs

- **Snapshot representation**: A sequence of static graphs $G_1, G_2, \ldots, G_T$ at discrete time steps. Simple but loses inter-snapshot dynamics.
- **Continuous-time representation**: Edges are events with timestamps — $(u, v, t)$. Preserves fine-grained temporal information.
- **Interval representation**: Edges active over intervals $[t_s, t_e]$.
- Tradeoff: snapshot models are simpler to analyze; continuous-time models are more expressive.

### Temporal Motifs and Causal Paths

- **Temporal motifs**: Subgraph patterns that respect time ordering. E.g., $A \to B$ at $t_1$, then $B \to C$ at $t_2 > t_1$ forms a temporal two-hop path.
- **Causal paths**: Sequences of edges where each subsequent edge occurs after the previous one (time-respecting paths). The set of causal paths can be much smaller than the set of static paths.
- **Temporal reachability**: Node $v$ is temporally reachable from $u$ if there exists a causal path from $u$ to $v$.
- Financial application: contagion can only follow causal paths — analyzing only static paths overestimates systemic risk.

### Dynamic Community Detection

- **Evolutionary clustering**: Balance between current snapshot quality and consistency with previous time step.
- **Temporal SBM**: Stochastic block model with time-varying community memberships and transition probabilities.
- **Change point detection**: Identify times when community structure undergoes significant reorganization.
- Financial application: detecting regime shifts in market sector structure, identifying emerging banking communities.

### Temporal Centrality Measures

- **Temporal betweenness**: Based on time-respecting shortest paths.
- **Temporal closeness**: Average temporal distance (earliest arrival time) rather than shortest-hop distance.
- **Temporal PageRank**: Random walk with temporal constraints — can only follow edges forward in time.
- **Katz centrality on temporal graphs**: Count time-respecting walks with temporal attenuation.

### Applications in Finance

- **Evolving financial networks**: Interbank lending topology changes before, during, and after crises.
- **Governance structure changes**: Corporate board interlocks, ownership networks that rewire over time.
- **Dynamic correlation networks**: Time-varying MSTs and filtered graphs track market regime evolution.
- **Temporal arbitrage**: Time-respecting paths in cross-market networks reveal arbitrage opportunities that static analysis misses.

---

## 10. Multilayer and Multiplex Networks

### Mathematical Formulation

- A multiplex network consists of $L$ layers sharing the same node set $V$:
$$\mathcal{G} = (V, E_1, E_2, \ldots, E_L)$$
- **Supra-adjacency matrix**: Block matrix representation:
$$\mathcal{A} = \begin{pmatrix} \mathbf{A}_1 & \mathbf{C}_{12} & \cdots & \mathbf{C}_{1L} \\ \mathbf{C}_{21} & \mathbf{A}_2 & \cdots & \mathbf{C}_{2L} \\ \vdots & \vdots & \ddots & \vdots \\ \mathbf{C}_{L1} & \mathbf{C}_{L2} & \cdots & \mathbf{A}_L \end{pmatrix}$$
  where $\mathbf{A}_\alpha$ is the adjacency matrix of layer $\alpha$ and $\mathbf{C}_{\alpha\beta}$ encodes interlayer coupling.
- For multiplex networks (same nodes across layers), the interlayer coupling is typically diagonal: $\mathbf{C}_{\alpha\beta} = \omega_{\alpha\beta}\mathbf{I}$.

### Interlayer Coupling and Dependencies

- **Coupling strength** $\omega$: Controls the degree of interaction between layers.
- Limits: $\omega \to 0$ yields independent layers; $\omega \to \infty$ yields an aggregate single-layer network.
- **Asymmetric coupling**: Layer $\alpha$ may influence layer $\beta$ more than vice versa (e.g., equity volatility spilling into credit markets).

### Multiplex Centrality Measures

- **Multiplex degree**: $k_i^{multi} = \sum_\alpha k_i^\alpha$ — total degree across all layers.
- **Multiplex PageRank**: PageRank on the supra-adjacency matrix, with interlayer teleportation.
- **Versatility**: Identifies nodes that are central in many layers simultaneously (De Domenico et al., 2015).
- **Layer-weighted centrality**: Weight layers by importance before aggregation.

### Layer Reducibility

- **Structural reducibility** (De Domenico et al., 2015): Quantifies when two layers are structurally redundant and can be merged without information loss.
- Uses **Jensen-Shannon divergence** between layers' von Neumann entropy.
- Financial application: determine whether equity and debt exposure layers provide non-redundant information for systemic risk.

### Diffusion on Multiplex Networks

- **Supra-Laplacian**: $\mathcal{L} = \mathcal{D} - \mathcal{A}$ — the Laplacian of the supra-adjacency matrix.
- Diffusion governed by $\frac{d\mathbf{x}}{dt} = -\mathcal{L}\mathbf{x}$ — shocks propagate both within and across layers.
- **Super-diffusion**: Diffusion on the multiplex can be faster than on any individual layer (Gomez et al., 2013).
- Financial implication: systemic risk propagation through multiplex financial networks can be faster and more destructive than single-layer analysis suggests.

### Applications in Finance

- **Multi-type financial relationships**: Equity cross-holdings, debt claims, derivatives exposures, and interbank lending as separate layers.
- **Cross-layer amplification**: Distress in the interbank layer triggers fire sales in the asset layer, which feeds back to the equity layer.
- **Systemic risk on multiplex**: Poledna et al. (2015) showed that single-layer DebtRank underestimates systemic risk by up to 90% compared to multiplex DebtRank.

---

## 11. Network Robustness and Cascading Failures

### Percolation Theory

- **Site percolation**: Each node is removed independently with probability $1-p$. At what $p_c$ does a giant connected component exist?
- **Bond percolation**: Each edge is removed independently with probability $1-p$.
- **Percolation threshold** $p_c$: Depends on network topology. For ER graphs, $p_c = 1/\langle k \rangle$. For scale-free networks with $\gamma \leq 3$, $p_c \to 0$ (robust to random removal but vulnerable to targeted attack).
- Financial analogy: bank failures (site percolation) or relationship severing (bond percolation) and the resulting network fragmentation.

### Cascading Failure Models

- **Sandpile model**: Nodes have capacity thresholds; exceeding capacity causes load redistribution to neighbors, potentially triggering further failures.
- **Load redistribution**: When a node fails, its load is redistributed to remaining nodes (proportional to capacity or connectivity), potentially overloading them.
- **Threshold models**: A node fails when the fraction of its failed neighbors exceeds a threshold $\phi$ — Watts' cascade model.
- Financial analogy: bank failure redistributes obligations to counterparties, who may then fail under the additional burden.

### Network Resilience: Targeted vs. Random Attack

- **Random failure**: Remove nodes uniformly at random. Scale-free networks are highly robust (due to the abundance of low-degree nodes).
- **Targeted attack**: Remove nodes in decreasing order of degree (or betweenness). Scale-free networks are extremely vulnerable — removal of a few hub nodes shatters the network.
- **Financial implication**: The financial system may be robust to random small-bank failures but catastrophically vulnerable to the failure of a few systemically important institutions ("too-big-to-fail").

### Core-Periphery Structure and "Too-Interconnected-to-Fail"

- Many financial networks exhibit **core-periphery structure**: a dense core of large, interconnected institutions surrounded by a sparse periphery.
- Core nodes are **too-interconnected-to-fail**: their removal disconnects periphery nodes from the system.
- **Craig & von Peter (2014)**: Formal statistical model for core-periphery structure in interbank networks.
- Policy implication: systemic importance depends not just on size but on network position.

### DebtRank as Cascade Model

- **Battiston, Puliga, Kaushik, Tasca & Caldarelli (2012)**: DebtRank — a recursive cascade model for financial distress.
- Each node $i$ has a distress level $h_i \in [0, 1]$ and equity $E_i$.
- Distress propagates: $h_j(t+1) = \min\left(1, h_j(t) + \sum_i W_{ij} h_i(t)\right)$ where $W_{ij} = \frac{A_{ij}}{E_j}$ is the relative exposure.
- Unlike simple contagion, DebtRank captures **continuous distress propagation** (not just binary default/no-default).
- Extensions: multi-round DebtRank, nonlinear DebtRank, multiplex DebtRank.

### Contagion Models: SIR/SIS on Financial Networks

- **SIR (Susceptible-Infected-Recovered)**: A solvent bank (S) can become distressed (I) through exposure to distressed neighbors, and eventually defaults or is resolved (R). One-time contagion.
- **SIS (Susceptible-Infected-Susceptible)**: Banks can recover and become susceptible again — models recurring financial stress.
- **Epidemic threshold**: $\beta/\gamma > 1/\lambda_1(\mathbf{A})$ where $\beta$ is infection rate, $\gamma$ is recovery rate, and $\lambda_1$ is the spectral radius. Below this threshold, contagion dies out.
- **Heterogeneous mean-field**: Accounts for degree heterogeneity — highly connected banks are more likely to be infected and to spread contagion.

### Stress Testing Through Network Failure Analysis

- **Scenario-based stress testing**: Apply an external shock (e.g., sovereign default, interest rate spike) and simulate cascade through the network.
- **Sequential default algorithm**: Process defaults one at a time, checking after each whether additional banks breach their solvency/liquidity thresholds.
- **Multi-round simulations**: Allow for feedback loops — asset fire sales depress prices, causing further losses, triggering more defaults.
- **Network-enhanced stress tests**: Combine traditional balance-sheet stress testing with network contagion models (Cont, Moussa & Santos, 2013).
- **Regulatory applications**: EBA/ECB stress tests increasingly incorporate network effects. Identify which initial shocks cause the largest cascades.

---

## Summary

The mathematical foundations presented in this chapter provide the formal toolkit for financial network science:

- **Graph theory** provides the language and structural concepts.
- **Centrality measures** identify systemically important nodes.
- **Community detection** reveals the modular organization of financial systems.
- **Network models** provide null models and generative mechanisms.
- **Spectral graph theory** connects network structure to dynamical properties.
- **Random matrix theory** enables principled signal-noise separation in financial correlation matrices.
- **Knowledge graph formalisms** structure heterogeneous financial data for reasoning and querying.
- **Graph neural networks** learn from network-structured financial data end-to-end.
- **Temporal network theory** captures the evolving nature of financial relationships.
- **Multilayer network theory** models the multi-faceted interconnections in the financial system.
- **Robustness and cascade theory** provides the framework for understanding and stress-testing systemic fragility.

These foundations are interconnected: spectral theory underlies both community detection and GNNs; RMT informs network construction from correlation matrices; cascade models build on percolation theory and network robustness. Mastery of these foundations enables rigorous analysis of financial networks across all scales and domains.
