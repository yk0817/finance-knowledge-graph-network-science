# Quantitative Methods for Financial Networks

This chapter covers the core quantitative techniques used to construct, filter, and analyze financial networks — from correlation-based graph construction and portfolio optimization to random matrix theory, multilayer networks, and market microstructure.

---

## 1. Minimum Spanning Tree and Correlation Networks

### Foundational Framework: Mantegna (1999)

The modern era of correlation-based financial networks begins with Mantegna's seminal paper "Hierarchical structure in financial markets" (1999). The construction pipeline is:

1. **Cross-correlation matrix**: Compute pairwise Pearson correlations $\rho_{ij}$ of log-returns for $N$ assets over a rolling window.
2. **Distance matrix**: Transform correlations into a metric distance:
$$d_{ij} = \sqrt{2(1 - \rho_{ij})}$$
   This satisfies the three axioms of a metric (non-negativity, symmetry, triangle inequality).
3. **Minimum Spanning Tree (MST)**: Apply Kruskal's or Prim's algorithm to extract the MST — a connected acyclic subgraph with $N-1$ edges that minimizes total distance.

The resulting MST reveals **hierarchical clustering of stocks by sector and industry**, providing a parsimonious representation of market structure from $O(N^2)$ correlations down to $O(N)$ edges.

### Planar Maximally Filtered Graph (PMFG)

Tumminello, Aste, Di Matteo & Mantegna (2005) introduced the PMFG as a richer alternative to the MST:

- Retains $3(N-2)$ edges (vs. $N-1$ for MST) while remaining **planar** (embeddable on a sphere without edge crossings).
- Always contains the MST as a subgraph.
- Captures additional topological features: **cliques** (3-cliques and 4-cliques) and **loops** that encode higher-order correlation structure.
- Better preserves local neighborhood information compared to the MST.

### Triangulated Maximally Filtered Graph (TMFG)

Massara, Di Matteo & Aste (2016) proposed the TMFG:

- Efficient $O(N^2)$ construction algorithm based on iterative vertex insertion.
- Produces a chordal (triangulated) planar graph.
- Better captures **local clustering structure** and produces positive-definite filtered correlation matrices.
- Particularly useful when a sparse but information-rich graph representation is needed.

### Applications

| Application | Method | Key Insight |
|---|---|---|
| Portfolio diversification | MST topology analysis | Peripheral assets on the MST are less correlated → better diversification |
| Market regime detection | Dynamic MST tracking | MST topology changes (normalized tree length, degree distribution) signal regime shifts |
| Crisis detection | MST shrinkage | During market stress, MST contracts as correlations spike — the "ultrametric shrinkage" effect |
| Sector rotation | Time-varying MST | Changing hub structure and cluster membership reveal sector leadership rotation |
| Risk management | PMFG/TMFG filtering | Cleaner correlation structure for downstream covariance estimation |

### Key Papers

| Paper | Authors | Year | Contribution |
|---|---|---|---|
| Hierarchical structure in financial markets | Mantegna | 1999 | MST from correlation distance — founding paper |
| A tool for filtering information in complex systems | Tumminello, Aste, Di Matteo, Mantegna | 2005 | PMFG construction and properties |
| Network filtering for big data: TMFG | Massara, Di Matteo, Aste | 2016 | TMFG algorithm and positive-definiteness |
| Dynamics of the MST of the US stock market | Onnela, Chakraborti, Kaski, Kertesz, Kanto | 2003 | Dynamic MST analysis, crisis detection |
| Clustering and information in correlation-based financial networks | Tumminello, Lillo, Mantegna | 2010 | Comparison of MST, PMFG, thresholded networks |

---

## 2. Network-Based Portfolio Optimization

### Hierarchical Risk Parity (HRP)

Marcos Lopez de Prado (2016) introduced HRP in "Building Diversified Portfolios that Outperform Out-of-Sample":

1. **Tree clustering**: Compute a hierarchical clustering (single linkage) of the correlation matrix.
2. **Quasi-diagonalization**: Reorder the covariance matrix according to the dendrogram to place correlated assets adjacent.
3. **Recursive bisection**: Allocate risk top-down by splitting the sorted assets and allocating inversely proportional to cluster variance.

**Key advantages**:
- Does not require matrix inversion (unlike Markowitz mean-variance optimization).
- Robust to estimation error in the covariance matrix — a machine learning approach to portfolio construction.
- Consistently outperforms traditional mean-variance in out-of-sample tests.
- Exploits the **hierarchical structure of asset correlations** rather than treating the covariance matrix as unstructured.

### Hierarchical Equal Risk Contribution (HERC)

Raffinot (2017) extended HRP with **risk budgeting**:

- Combines hierarchical clustering with equal risk contribution (ERC) within clusters.
- More flexible risk allocation — can target equal risk contribution at each level of the hierarchy.
- Bridges between HRP and traditional risk parity approaches.

### Network Risk Parity

- Uses **graph centrality measures** (degree, eigenvector, betweenness) to inform risk allocation.
- Penalizes highly connected assets: nodes with high centrality contribute more to systemic risk and receive lower portfolio weight.
- Variants:
  - Degree-weighted risk parity: allocate inversely to weighted degree.
  - Betweenness-penalized allocation: reduce weight of assets that serve as "bridges" between clusters.
  - Eigenvector centrality-adjusted risk budgeting.

### Signed Network Portfolios

- Financial correlation networks have both **positive and negative correlations** — naturally modeled as **signed edges**.
- **Community detection on signed networks**: Group assets such that intra-community edges are positive (correlated) and inter-community edges are negative (hedging).
- **Balance theory applications**: Heider's balance theory — "the enemy of my enemy is my friend" — provides structural constraints on portfolio grouping.
- Frustrated edges (violations of balance) signal arbitrage or mispricing opportunities.

### Graph Neural Network Portfolios

- **GNN-based asset allocation**: Construct a financial relation graph (correlation, supply chain, sector membership) and learn portfolio weights end-to-end.
- The GNN learns both the **optimal network structure** (via attention or learnable adjacency) and **portfolio weights** jointly.
- Architectures: GAT for attention-weighted neighbor aggregation, GraphSAGE for inductive learning across varying asset universes.
- Advantages: can incorporate heterogeneous financial relationships (fundamental, technical, alternative data) in a unified graph framework.

### Key Papers

| Paper | Authors | Year | Contribution |
|---|---|---|---|
| Building Diversified Portfolios that Outperform Out-of-Sample | Lopez de Prado | 2016 | HRP algorithm |
| Hierarchical clustering-based asset allocation | Raffinot | 2017 | HERC extension |
| Network-based risk parity | Various | 2018+ | Centrality-informed allocation |
| Portfolio optimization with graph neural networks | Various | 2020+ | End-to-end GNN portfolio learning |
| Signed networks in finance | Harary (balance theory), applications in finance | — | Signed graph portfolio grouping |

---

## 3. Random Matrix Theory

### Foundational Work: Laloux, Cizeau, Bouchaud & Potters (1999)

"Noise Dressing of Financial Correlation Matrices" — a landmark paper from **CFM (Capital Fund Management)** research:

- The empirical correlation matrix $\mathbf{C}$ of $N$ asset returns over $T$ observations contains substantial noise when $N/T = Q$ is not negligible.
- **Marchenko-Pastur distribution**: For a purely random matrix (i.i.d. returns), the eigenvalue density follows:
$$\rho(\lambda) = \frac{Q}{2\pi\sigma^2} \frac{\sqrt{(\lambda_+ - \lambda)(\lambda - \lambda_-)}}{\lambda}$$
  where $\lambda_{\pm} = \sigma^2(1 \pm \sqrt{1/Q})^2$.
- Eigenvalues within the Marchenko-Pastur bulk are **noise**; those exceeding $\lambda_+$ carry genuine signal (market factor, sector factors).
- This provides a principled method for **separating signal from noise** in correlation matrices.

### Denoising Methods

| Method | Description | Reference |
|---|---|---|
| Eigenvalue clipping | Replace bulk eigenvalues with their average (or zeros), preserving trace | Laloux et al. (1999) |
| Rotationally Invariant Estimator (RIE) | Optimal shrinkage of each eigenvalue using free probability theory | Bun, Bouchaud & Potters (2017) |
| Ledoit-Wolf shrinkage | Linear shrinkage toward structured target (identity, constant correlation) | Ledoit & Wolf (2004) |
| Oracle Approximating Shrinkage (OAS) | Improved shrinkage with better bias-variance tradeoff | Chen, Wiesel, Eldar & Hero (2010) |
| Nonlinear shrinkage | Analytically optimal nonlinear shrinkage using Stieltjes transform | Ledoit & Wolf (2012, 2020) |

### Applications in Network Construction

- **Cleaned correlation matrices → better network topology**: Denoised matrices produce more stable and meaningful MSTs and PMFGs.
- **Improved MST construction**: MSTs from denoised matrices show more consistent sector clustering and less temporal instability.
- **Dynamic RMT for time-varying network estimation**: Track the evolution of the eigenvalue spectrum and eigenvectors to detect structural breaks in the network.

### Spiked Models and Factor Structure

- **Spiked covariance model**: A few large eigenvalues (spikes) emerge above the Marchenko-Pastur sea, corresponding to market-wide and sector factors.
- **BBP transition** (Baik, Ben Arous & Peche, 2005): Phase transition in detectability of spikes — below a critical SNR, spikes merge into the bulk and become undetectable.
- Connection to **factor models**: The top eigenvectors correspond to PCA factors (market, value, size, momentum), linking RMT to asset pricing.

### Key Papers

| Paper | Authors | Year | Contribution |
|---|---|---|---|
| Noise dressing of financial correlation matrices | Laloux, Cizeau, Bouchaud, Potters | 1999 | RMT applied to finance — foundational |
| Universal and non-universal properties of cross-correlations | Plerou, Gopikrishnan, Rosenow, Amaral, Guhr, Stanley | 1999 | Empirical eigenvalue analysis of stock correlations |
| Cleaning large correlation matrices | Bun, Bouchaud, Potters | 2017 | RIE and optimal estimation |
| A well-conditioned estimator for large-dimensional covariance matrices | Ledoit, Wolf | 2004 | Shrinkage estimators |
| Nonlinear shrinkage estimation of large-dimensional covariance matrices | Ledoit, Wolf | 2012 | Analytically optimal nonlinear shrinkage |

---

## 4. Multiplex and Multilayer Networks

### Motivation

Financial institutions are connected through **multiple types of relationships simultaneously**: equity cross-holdings, debt claims, derivatives exposures, interbank lending, and payment flows. Analyzing any single layer in isolation misses critical cross-layer interactions.

### BIS Working Paper No. 603

The Bank for International Settlements published a key working paper on **multilayer network analysis of financial interconnectedness**, demonstrating that systemic risk assessments based on single-layer analysis can be severely misleading.

### Multilayer Systemic Risk

- **Different layers**:
  - Equity layer: cross-shareholdings, stock return correlations
  - Debt layer: bond holdings, credit exposures
  - Derivatives layer: OTC and exchange-traded counterparty networks
  - Interbank layer: overnight lending, repo markets
  - Payment layer: real-time gross settlement flows

- **Cross-layer contagion and amplification**: Distress in one layer (e.g., interbank defaults) spills over to other layers (e.g., derivatives counterparty risk, fire sales in equity).
- **DebtRank on multiplex networks**: Extended DebtRank algorithm that accounts for cascading losses across multiple exposure types simultaneously.

### Bipartite Networks

- **Bank-asset networks**: Banks connected to assets they hold — a bipartite (two-mode) graph.
- **Investor-asset overlap**: Overlapping portfolios create indirect connections between institutions through common asset holdings.
- Bipartite projection yields the one-mode network of institutions (weighted by portfolio overlap), which drives fire-sale contagion.

### Temporal Multiplex

- Adding the **time dimension** to multilayer structure: each layer evolves independently with cross-layer coupling.
- Enables analysis of how multilayer financial networks rewire during crises.

### Key Concepts

| Concept | Description |
|---|---|
| Interlayer coupling | Strength of dependencies between layers (e.g., equity-debt feedback) |
| Layer aggregation | Combining layers into a single network — information loss vs. tractability |
| Multiplex centrality | Centrality measures that account for node importance across all layers |
| Layer reducibility | Quantifying redundancy between layers — are they structurally similar? |

### Key Papers

| Paper | Authors | Year | Contribution |
|---|---|---|---|
| The multiplex structure of interbank networks | Bargigli, di Iasio, Infante, Lillo, Pierobon | 2015 | Multiplex analysis of Italian interbank market |
| Multilayer network analysis of financial interconnectedness | BIS Working Paper No. 603 | 2016 | Systemic risk in multilayer financial networks |
| Multiplexity and systemic risk | Poledna, Molina-Borboa, Martinez-Jaramillo, van der Leij, Thurner | 2015 | DebtRank on multiplex interbank networks |
| Leveraging the network: a stress-test framework | Cont, Moussa, Santos | 2013 | Bipartite bank-asset stress testing |
| Fire sales, indirect contagion and systemic risk | Cont, Schaanning | 2017 | Overlapping portfolios and fire-sale spirals |

---

## 5. Market Microstructure Networks

### Limit Order Book (LOB) Networks

- **Order flow networks**: Reconstructing "who trades with whom" from order book data.
  - Nodes: market participants (identifiable in some markets via trader IDs).
  - Edges: bilateral trades, weighted by volume or frequency.
- **Information flow through order book dynamics**: Lead-lag relationships between order book events across assets or venues reveal information propagation paths.
- **High-frequency trading network effects**:
  - HFT firms act as hubs in the trading network, providing liquidity but also transmitting shocks.
  - Co-location and latency arbitrage create asymmetric network structures.
  - Flash crash propagation follows network topology.

### OTC Dealer Networks

- **Interdealer broker networks** in fixed income, FX, and derivatives markets:
  - OTC markets lack a central limit order book — trades occur bilaterally through dealer intermediation.
  - The resulting network exhibits strong **core-periphery structure**: a dense core of large dealers connected to a sparse periphery of smaller participants.

- **Li & Schurhoff (2019)**: "Dealer Networks" — analysis of municipal bond markets:
  - Documented intermediation chains: bonds pass through multiple dealers before reaching end investors.
  - Network position determines transaction costs: peripheral clients pay higher markups.
  - Central dealers earn rents from their network position.

- **Network effects on pricing and liquidity**:
  - Bid-ask spreads depend on the dealer's centrality in the trading network.
  - Liquidity is not a property of an asset alone but of the network through which it trades.
  - Network fragility: removal of core dealers can cause liquidity to evaporate.

### Dark Pool Networks

- **Fragmented equity markets**: Trading occurs across lit exchanges, dark pools, and internalizers — creating a networked market ecosystem.
- **Information leakage across venues**: Order flow in one venue signals to informed traders in others; the topology of this information network affects execution quality.
- **Optimal execution in networked markets**: Smart order routing as a network optimization problem — how to split orders across interconnected venues to minimize market impact.

### Market Maker Networks and Liquidity Provision

- Market makers form networks through their overlapping obligations and inventory management.
- Intermarket maker information sharing and competitive dynamics shape bid-ask spreads.
- Network effects in market making: failure of one market maker propagates through inventory imbalances to connected makers.

### Key Papers

| Paper | Authors | Year | Contribution |
|---|---|---|---|
| Dealer Networks | Li, Schurhoff | 2019 | Municipal bond dealer network structure and pricing |
| The network of interdealer trades | Iori, de Masi, Precup, Gabbi, Caldarelli | 2008 | Italian interbank e-MID network |
| Core-periphery structure in OTC markets | Craig, von Peter | 2014 | Core-periphery model for interbank markets |
| High-frequency trading and market quality | Various | 2010s | HFT network effects on market microstructure |
| Fragmentation and market quality | O'Hara, Ye | 2011 | Effects of market fragmentation |
| The network origins of aggregate fluctuations | Acemoglu, Carvalho, Ozdaglar, Tahbaz-Salehi | 2012 | Network propagation of microstructural shocks |

---

## Summary

The quantitative methods surveyed in this chapter form the analytical backbone of financial network science:

- **Correlation networks** (MST, PMFG, TMFG) provide principled ways to extract meaningful structure from noisy correlation matrices.
- **Network-based portfolio optimization** (HRP, HERC, network risk parity, GNN portfolios) leverages graph structure for more robust asset allocation.
- **Random matrix theory** enables signal-noise separation, improving both network construction and covariance estimation.
- **Multiplex and multilayer networks** capture the multi-faceted nature of financial interconnections and their cross-layer contagion dynamics.
- **Market microstructure networks** reveal the hidden topology of trading relationships and their impact on pricing, liquidity, and systemic stability.

These methods are not isolated — they interact synergistically. RMT-cleaned correlations produce better MSTs; MST topology informs HRP clustering; multiplex analysis reveals contagion channels invisible in single-layer networks; microstructure networks provide the empirical substrate on which macro-level financial networks rest.
