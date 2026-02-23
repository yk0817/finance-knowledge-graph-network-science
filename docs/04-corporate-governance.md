# Corporate Governance × Knowledge Graphs × Network Science

**コーポレートガバナンス × 知識グラフ × ネットワーク科学**

---

## A. Foundational Research

### A.1 The Network of Global Corporate Control

**Vitali, Glattfelder & Battiston (2011)**, "The Network of Global Corporate Control," *PLoS ONE*, 6(10), e25995.

This landmark study applied network science to the global ownership structure of transnational corporations (TNCs) and revealed a striking concentration of economic power:

- **Data**: 43,060 TNCs identified from the Orbis database (Bureau van Dijk), connected through 600,508 ownership relations (nodes represent firms; directed weighted edges represent shareholdings).
- **Methodology**:
  - Constructed a directed ownership network from Orbis data
  - Applied a recursive algorithm to compute *network control* — the fraction of a company's decision-making power attributable to each shareholder, accounting for indirect ownership paths through chains, pyramids, and cross-holdings
  - Identified the *strongly connected component (SCC)* — a tightly interwoven core where every member can reach every other member through ownership chains
- **Key Findings**:
  - The network exhibits a **"bow-tie" structure**: a small, densely connected core (SCC) of 1,318 companies, with in-components (firms owning the core) and out-components (firms owned by the core) radiating outward
  - A super-entity of **147 tightly-knit companies** (mostly financial institutions) collectively control ~40% of the total economic value of all TNCs in the network
  - **737 top holders** control 80% of the network's value
  - The top 50 controllers include Barclays PLC, Capital Group, FMR Corp (Fidelity), AXA, State Street, JPMorgan Chase, and other major financial institutions
  - The concentration is far greater than random network models predict — the ownership network is neither random nor merely hierarchical, but contains a superconnected core
- **Impact**: ~6,000+ citations; widely reported in mainstream media; sparked policy debates on concentration of economic power, systemic risk from ownership concentration, and the need for transparency in global corporate networks. The paper is a foundational reference for any study of corporate ownership through network methods.

### A.2 CORPNET Research Group (University of Amsterdam)

The **CORPNET** (Corporate Network Governance) research group, led by **Eelke Heemskerk**, is one of the most prolific academic groups studying corporate networks:

- **Scale**: Analysis of **77 million ownership relations** from the Orbis database, representing one of the most comprehensive mappings of global corporate ownership ever undertaken
- **Key Research Themes**:
  - **Global corporate ownership network topology**: extending the Vitali et al. analysis with richer data and more sophisticated methods
  - **Offshore financial center hierarchies**: identifying which jurisdictions function as conduits vs. sinks for corporate investment flows, revealing the architecture of global tax avoidance
  - **State-owned enterprise networks**: mapping how governments exert economic control through complex ownership chains
  - **Tax haven networks**: quantifying the role of specific jurisdictions (Netherlands, Luxembourg, Ireland, Cayman Islands, British Virgin Islands) as conduits in global corporate structures
  - **Elite networks**: studying how corporate directors, shareholders, and political actors form interconnected power structures
- **Notable Publications**:
  - Garcia-Bernardo, Fichtner, Takes & Heemskerk (2017). "Uncovering Offshore Financial Centers: Conduits and Sinks in the Global Corporate Ownership Network." *Scientific Reports*, 7, 6246.
  - Heemskerk, Takes & Fichtner (2017). "The Offshore-Intensity Ratio." European Tax Observatory working paper.
  - Fichtner, Heemskerk & Garcia-Bernardo (2017). "Hidden power of the Big Three? Passive index funds, re-concentration of corporate ownership, and new financial risk." *Business and Politics*, 19(2), 298–326.
- **Key Datasets**: Orbis Bureau van Dijk (now Moody's), GLEIF LEI, national corporate registries

### A.3 Stanford Corporate Governance Research Initiative (CGRI)

The **Stanford CGRI**, part of the Stanford Graduate School of Business and Stanford Law School, conducts influential research at the intersection of governance, networks, and economic outcomes:

- **Board diversity research**: systematic studies on how board composition — gender, ethnicity, expertise — relates to firm performance and governance quality
- **CEO compensation networks**: analysis of how CEO pay is influenced by board interlocks, peer benchmarking through shared directors, and compensation consultant networks
- **Governance ratings and network effects**: examining how governance quality scores (ISS, MSCI) propagate through corporate networks and whether improvements in governance at one firm spill over to connected firms
- **Director labor markets**: studying how the market for corporate directors operates as a network, with reputation, connections, and board experience determining appointments

---

## B. Board Interlocking Networks

### B.1 Theoretical Foundation

The study of **board interlocks** — connections formed when a single individual sits on the boards of two or more companies — is one of the oldest and most developed areas of corporate governance network analysis.

**Key theoretical frameworks:**

- **Social Network Analysis (SNA)**: The application of SNA to corporate boards treats the set of all publicly listed companies and their directors as a bipartite network. Projecting this bipartite network onto the company mode yields a company-interlock network; projecting onto the director mode yields a director co-membership network.

- **"Old Boys' Network" Hypothesis**: Corporate elites form a cohesive social network through shared board memberships, educational backgrounds (e.g., Ivy League, Oxbridge, Tokyo University), and club memberships. Board interlocks are seen as the structural manifestation of elite social cohesion, reinforcing shared worldviews and mutual interests.

- **Resource Dependence Theory** (Pfeffer & Salancik, 1978): Organizations create board interlocks strategically to manage environmental uncertainty and resource dependencies. A firm facing regulatory uncertainty might appoint a director with government connections; a firm seeking financing might appoint a banker to its board. Interlocks serve as **boundary-spanning mechanisms** that facilitate information flow, reduce transaction costs, and co-opt sources of uncertainty.

- **Class Hegemony Theory** (Domhoff, 1967; Useem, 1984): Board interlocks maintain the cohesion of a capitalist class by creating communication channels among corporate elites, enabling coordinated action on matters of shared interest (e.g., lobbying, political donations, labor policy). The interlock network functions as the structural backbone of an "inner circle" of business leaders who transcend individual firm interests.

- **Agency Theory and Monitoring**: Interlocks may weaken governance by creating mutual non-aggression pacts — "I won't challenge your CEO's pay if you don't challenge mine." Reciprocally interlocked boards (where directors of firm A sit on B's board and vice versa) are particularly suspect from an agency perspective.

### B.2 Methods

**Exponential Random Graph Models (ERGM):**
Statistical models for network formation that model the probability of observing a given network as a function of network statistics (e.g., density, reciprocity, transitivity, homophily). ERGMs enable researchers to test hypotheses about *why* interlocks form — do firms with similar industries, sizes, or geographies form more interlocks than expected by chance?

**Centrality Measures:**
- **Degree centrality**: Number of interlocks (for firms) or board seats (for directors). High-degree firms/directors are well-connected.
- **Betweenness centrality**: Frequency with which a node lies on shortest paths between other nodes. High-betweenness directors are "bridges" connecting otherwise separate clusters.
- **Closeness centrality**: Average distance to all other nodes. Measures speed of information access.
- **Eigenvector centrality**: Being connected to other well-connected nodes. Captures influence within the power structure.

**Community Detection:**
Algorithms (Louvain, Infomap, spectral methods, stochastic block models) applied to interlock networks to identify clusters of densely connected firms. These clusters often correspond to governance regimes, industry groups, geographic regions, or historical alliances (e.g., keiretsu in Japan, grupos in Latin America).

**Bipartite Network Analysis:**
The director-company affiliation network is naturally bipartite (two types of nodes: directors and companies). Bipartite-specific methods — such as bipartite modularity, bipartite projection with Newman weights, and two-mode centrality measures — preserve the structural information lost in one-mode projection.

**Temporal Network Analysis:**
Board networks evolve as directors join and leave boards, companies merge or dissolve, and governance norms shift. Temporal network methods track the evolution of interlock patterns over time, identifying structural breaks (e.g., post-crisis governance reforms), trends (e.g., declining interlock density), and path dependencies.

### B.3 Key Findings

Board interlocks have been shown to correlate with a wide range of corporate outcomes:

- **Executive compensation convergence**: Directors serving on multiple boards carry information about pay practices, leading to convergence in CEO compensation among interlocked firms (Hallock, 1997; Bizjak, Lemmon & Whitby, 2009)
- **Strategic similarity**: Interlocked firms adopt more similar strategies, including diversification patterns, capital structure choices, and market entry decisions (Haunschild & Beckman, 1998)
- **M&A patterns**: Board connections predict merger and acquisition activity — interlocked firms are more likely to pursue similar deal types and to merge with each other (Haunschild, 1993; Cai & Sevilir, 2012)
- **Poison pill adoption and defensive tactics**: Anti-takeover defenses spread through interlock networks, with firms adopting poison pills after their interlocked partners do (Davis, 1991)
- **Innovation diffusion**: New practices, technologies, and organizational forms diffuse through interlock ties (Westphal, Gulati & Shortell, 1997)
- **Financial reporting quality**: Board connections to firms involved in accounting scandals increase the likelihood of earnings management and restatements (Chiu, Teoh & Tian, 2013)
- **Gender diversity and network position**: Female directors tend to occupy different network positions than male directors, with implications for influence and information access. Women are often appointed to boards with existing female directors (network homophily), and their presence correlates with improved governance quality in some studies (Adams & Ferreira, 2009)
- **International variation**: The structure, density, and function of board interlock networks vary dramatically across countries. The US and UK exhibit relatively sparse networks dominated by financial institutions; Germany features denser networks structured around banks and industrial firms (the *Deutschland AG* model); Japan's networks are organized around keiretsu groups; South Korea features chaebol-centered networks with extensive family cross-board membership.

### B.4 Key Papers

| Authors | Year | Journal / Venue | Title | Key Finding |
|---------|------|-----------------|-------|-------------|
| Mizruchi | 1996 | *Annual Review of Sociology* | "What Do Interlocks Do? An Analysis, Critique, and Assessment of Research on Interlocking Directorates" | Comprehensive survey; interlocks facilitate diffusion of practices and information but their effect on firm behavior is more nuanced than class hegemony suggests |
| Davis, Yoo & Baker | 2003 | *Strategic Organization* | "The Small World of the American Corporate Elite, 1982–2001" | US corporate board network exhibits small-world properties; average path length ~4; network fragmented significantly from 1982 to 2001 as interlock density declined |
| Larcker, So & Wang | 2013 | *Journal of Accounting and Economics* | "Boardroom Centrality and Firm Performance" | Directors with higher network centrality (especially eigenvector centrality) are associated with better firm performance; well-connected boards make better-informed decisions |
| Hallock | 1997 | *Journal of Financial and Quantitative Analysis* | "Reciprocally Interlocking Boards of Directors and Executive Compensation" | Reciprocal interlocks (CEO of A on board of B, CEO of B on board of A) are associated with higher CEO compensation, suggesting mutual back-scratching |
| Davis | 1991 | *Administrative Science Quarterly* | "Agents Without Principles? The Spread of the Poison Pill through the Intercorporate Network" | Poison pill adoption spreads through board interlocks; firms are more likely to adopt after connected firms do |
| Haunschild | 1993 | *Administrative Science Quarterly* | "Interorganizational Imitation: The Impact of Interlocks on Corporate Acquisition Activity" | Firms imitate the acquisition strategies of companies to which they are connected through board interlocks |
| Cai & Sevilir | 2012 | *Journal of Financial Economics* | "Board Connections and M&A Transactions" | Mergers between firms sharing a board connection have higher announcement returns and better post-merger performance |
| Bizjak, Lemmon & Whitby | 2009 | *Journal of Financial Economics* | "Option Backdating and Board Interlocks" | Options backdating practices spread through board interlocks; connected firms exhibit correlated backdating behavior |
| Conyon & Muldoon | 2006 | *Journal of Business Finance & Accounting* | "The Small World of Corporate Boards" | UK board network exhibits small-world properties with high clustering and short path lengths; network structure reflects elite cohesion |
| Fracassi & Tate | 2012 | *Journal of Finance* | "External Networking and Internal Firm Governance" | Socially connected boards (through interlocks, education, and professional ties) exhibit weaker monitoring; CEO-board social ties reduce firm value |
| Santos, Silveira & Barros | 2012 | *Corporate Governance: An International Review* | "Board Interlocking in Brazil" | Mapping of Brazilian corporate governance network; concentrated ownership and family control shape interlock patterns |
| Kramarz & Thesmar | 2013 | *Journal of Finance* | "Social Networks in the Boardroom" | French CEOs connected to board members through social networks (grandes écoles) receive higher pay and their firms underperform |

---

## C. Ownership Networks

### C.1 Ultimate Beneficial Ownership (UBO)

**Definition**: Ultimate Beneficial Ownership (UBO) refers to the identification of the **natural person(s) who ultimately own or control a legal entity**, regardless of how many layers of corporate structure stand between them and the entity. UBO analysis is a core application of graph methods to corporate governance.

**Challenges in UBO Identification:**
- **Multi-layered structures**: Ownership chains may pass through dozens of intermediate holding companies, limited partnerships, and trusts across multiple jurisdictions
- **Nominee arrangements**: Legal owners may be nominees acting on behalf of undisclosed beneficial owners
- **Trust structures**: Trusts separate legal ownership (trustee) from beneficial interest (beneficiary), creating opacity
- **Bearer shares**: Shares with no registered owner (now banned or restricted in most jurisdictions, but still held historically)
- **Circular ownership**: Company A owns B, which owns C, which owns A — creating loops in the ownership graph that complicate control computation
- **Threshold ambiguity**: Different jurisdictions define "beneficial ownership" at different thresholds (25% in EU, 10% in some contexts)

**Graph Algorithms for UBO Computation:**
- **Path analysis**: Finding all directed paths from natural persons to target entities, computing effective ownership at each step by multiplying fractional holdings along the path
- **Control propagation**: Recursive algorithms (extending Vitali et al.'s approach) that propagate control from ultimate owners through intermediate entities, handling voting rights vs. cash flow rights separation
- **Cycle detection**: Identifying and resolving circular ownership structures using algorithms like Johnson's algorithm for elementary circuits in directed graphs
- **Shapley value computation**: Computing the voting power of shareholders in the presence of coalitions and complex structures, using cooperative game theory (Shapley-Shubik power index)

**Regulatory Framework:**
- **EU Anti-Money Laundering Directives**:
  - **4AMLD** (2015): Required member states to establish central beneficial ownership registers; defined UBO threshold at 25% ownership or control
  - **5AMLD** (2018): Made beneficial ownership registers publicly accessible; extended requirements to trusts and other arrangements
  - **6AMLD** (2020): Harmonized criminal offenses for money laundering; strengthened enforcement of beneficial ownership requirements
- **US Corporate Transparency Act** (2021): Requires reporting of beneficial ownership information to FinCEN; effective 2024
- **FATF Recommendations**: International standards for beneficial ownership transparency; the Financial Action Task Force drives global adoption

**AML Applications:**
Knowledge graphs and network analysis are central to modern Anti-Money Laundering (AML) systems. By constructing ownership networks and applying UBO algorithms, financial institutions can identify:
- Shell company structures used for money laundering or terrorist financing
- Sanctions evasion through complex corporate chains
- Politically Exposed Persons (PEPs) with hidden corporate interests
- Unusual patterns of ownership concentration or rapid structural changes

### C.2 Cross-Shareholding Analysis

**Circular ownership structures** arise when companies hold shares in each other, either directly (A↔B) or through longer cycles (A→B→C→A). These structures are common in certain governance regimes (Japan, South Korea, continental Europe) and serve various purposes:

- **Defensive mechanism**: Mutual shareholdings create a stable shareholder base resistant to hostile takeovers
- **Relationship cement**: Cross-holdings signal long-term commitment between business partners
- **Voting power amplification**: A company can increase its effective voting power through circular holdings

**Voting Power vs. Cash Flow Rights Separation:**
In complex ownership structures, the fraction of votes controlled by an owner (voting rights) can diverge significantly from the fraction of cash flows they receive (cash flow rights). This separation — measured by the ratio of voting rights to cash flow rights — is a key governance concern because it enables controllers to extract private benefits with minimal financial exposure. Network methods quantify this separation by tracing all ownership paths and computing both metrics.

**Shapley-Shubik Power Index in Ownership Networks:**
The Shapley-Shubik power index (from cooperative game theory) measures the *a priori* voting power of a shareholder by computing the probability of being the pivotal voter across all possible voting coalitions. In the context of ownership networks, this index accounts for indirect holdings, pyramidal structures, and cross-shareholdings to determine the true distribution of corporate control. Computing Shapley values for large ownership networks is computationally intensive and often requires Monte Carlo approximation.

**Network Metrics for Ownership Concentration:**
- **HHI (Herfindahl-Hirschman Index)** on the ownership network: measuring concentration among ultimate controllers
- **Network density and clustering**: higher density in ownership subgraphs indicates tighter control
- **Giant component analysis**: what fraction of listed firms are connected through ownership links?
- **Bow-tie decomposition**: following Vitali et al., decomposing the ownership network into core, in-component, out-component, and tendrils

### C.3 Pyramid Structures and Dual-Class Shares

**Pyramid Structures:**
A pyramid structure exists when a controlling shareholder owns a company (the apex) that in turn owns a subsidiary, which owns another subsidiary, and so on. The controller can maintain decision-making power over firms at the bottom of the pyramid while holding only a small fraction of cash flow rights. For example: if the controller owns 51% of company A, which owns 51% of company B, which owns 51% of company C — the controller has voting control over C but only ~13.3% of C's cash flow rights.

**Control-Enhancing Mechanisms:**
- Dual-class shares (different voting rights per share class)
- Pyramid structures
- Cross-shareholdings
- Voting caps and loyalty shares
- Golden shares (government veto power)

**Tunneling and Expropriation:**
Controlling shareholders with limited cash flow rights but extensive control may engage in "tunneling" — transferring value from controlled firms to entities where they have greater cash flow rights. This can occur through:
- Related-party transactions at non-arm's-length prices
- Transfer pricing manipulation within the group
- Selective dividend policies
- Asset stripping or favorable merger terms

**Family Business Groups Worldwide:**

| Structure | Region | Characteristics |
|-----------|--------|-----------------|
| **Chaebols** | South Korea | Family-controlled conglomerates (Samsung, Hyundai, SK, LG); extensive circular cross-shareholding; concentrated control despite dispersed cash flow rights |
| **Zaibatsu / Keiretsu** | Japan | Pre-WWII zaibatsu (family-held holding companies) dissolved post-war; succeeded by keiretsu (bank-centered, cross-shareholding); see Section D |
| **Grupos económicos** | Latin America | Family business groups (Grupo Slim, Grupo Votorantim); pyramid structures and dual-class shares common |
| **Business houses** | India | Family-controlled conglomerates (Tata, Reliance, Birla); promoter holdings through complex pyramids |
| **State-linked groups** | China | SOE groups with Communist Party committee influence; complex layered state ownership through SASAC |
| **Family holdings** | Southeast Asia | Dominant families control diversified conglomerates (Li Ka-shing, Salim Group, CP Group) |
| **Participações** | Continental Europe | Holding company structures (Agnelli family/Exor, Wallenberg family/Investor AB); dual-class shares and pyramid control |

### C.4 Data Sources for Ownership Networks

| Dataset | Provider | Coverage | Access | Key Features |
|---------|----------|----------|--------|--------------|
| **Orbis** | Bureau van Dijk (Moody's) | 400M+ entities globally | Commercial (WRDS, institutional) | Most comprehensive global ownership data; direct/indirect ownership chains; financial data; director information |
| **OpenOwnership Register** | Open Ownership | 27M+ records, 200+ jurisdictions | Open (API, bulk download) | Beneficial ownership declarations from national registers; standardized using BODS |
| **GLEIF LEI Database** | Global Legal Entity Identifier Foundation | 2.5M+ legal entities | Open (API, bulk download) | Legal Entity Identifiers with direct/ultimate parent information; standardized hierarchy |
| **OpenCorporates** | OpenCorporates | 170M+ companies | Freemium (API) | Company registrations from government registries worldwide; basic officer information |
| **BODS Data** | Open Ownership | Beneficial ownership data standard | Open | Standardized schema for beneficial ownership declarations; interoperable across jurisdictions |
| **SEC EDGAR** | US SEC | All US public companies | Open | Beneficial ownership filings (Schedule 13D/13G, Form 3/4/5); proxy statements (DEF 14A) |
| **ICIJ Offshore Leaks** | ICIJ | 800K+ offshore entities | Open | Panama Papers, Paradise Papers, Pandora Papers; offshore ownership structures |

---

## D. Keiretsu and Cross-Shareholding (Japan-Specific)

**系列・株式持ち合い**

### D.1 Historical Context

**From Zaibatsu to Keiretsu:**

The modern Japanese corporate governance landscape cannot be understood without its historical context:

- **Zaibatsu (財閥)**: Pre-WWII Japan was dominated by family-controlled industrial conglomerates — Mitsubishi (三菱), Mitsui (三井), Sumitomo (住友), and Yasuda (安田) were the "Big Four." These were pyramid structures with a family-held holding company at the apex, controlling banks, insurance companies, trading companies, and industrial firms through cascading ownership. The zaibatsu controlled approximately 25% of Japan's corporate assets by 1945.

- **Dissolution (1945–1952)**: The Allied Occupation's Supreme Commander (SCAP/GHQ) ordered the dissolution of zaibatsu holding companies under the belief that concentrated economic power had contributed to Japanese militarism. The Holding Company Liquidation Commission dissolved 83 holding companies, distributed their shares to the public, and purged zaibatsu family members from corporate management. The Anti-Monopoly Act (1947) initially prohibited holding companies (this prohibition was lifted in 1997).

- **Keiretsu Emergence (1950s–1960s)**: Former zaibatsu firms, now independently managed, gradually reformed their relationships through **cross-shareholding (株式持ち合い, kabushiki mochiiai)** — mutual stock ownership among group members without a holding company at the apex. Six major horizontal keiretsu emerged:

| Keiretsu | Core Bank | Trading Company | Origin |
|----------|-----------|-----------------|--------|
| **Mitsubishi (三菱)** | Mitsubishi UFJ | Mitsubishi Corp. | Mitsubishi zaibatsu |
| **Mitsui (三井)** | Sumitomo Mitsui | Mitsui & Co. | Mitsui zaibatsu |
| **Sumitomo (住友)** | Sumitomo Mitsui | Sumitomo Corp. | Sumitomo zaibatsu |
| **Fuyo (芙蓉)** | Mizuho | Marubeni | Yasuda zaibatsu |
| **DKB (第一勧銀)** | Mizuho | Itochu | Post-war formation |
| **Sanwa (三和)** | Mitsubishi UFJ | Nissho Iwai (now Sojitz) | Post-war formation |

- **Cross-Shareholding Functions**:
  - **Takeover defense**: Mutual holdings created a stable, "friendly" shareholder base that would not sell to hostile acquirers
  - **Relationship cement**: Cross-holdings signaled long-term commitment between business partners (supplier-customer, bank-borrower, joint venture partners)
  - **Information sharing**: President's councils (社長会, shachōkai) of keiretsu group members met regularly to exchange information and coordinate strategy
  - **Main bank system**: The main bank (メインバンク) served as both lender and monitor, holding equity in client firms and intervening in management during financial distress

- **Peak cross-shareholding**: Cross-shareholding ratios (percentage of listed shares held through cross-holding arrangements) peaked in the late 1980s–early 1990s at approximately **50–60%** of total listed shares on the Tokyo Stock Exchange. This represented one of the most densely interconnected corporate ownership networks in any major economy.

### D.2 Graph Theory Analysis of Keiretsu

**Network Topology of Major Keiretsu Groups:**
When represented as ownership networks, keiretsu groups exhibit distinctive topological features:

- **Horizontal keiretsu (水平的系列)**: Approximate **complete graph** or near-complete graph structures — every member holds shares in (nearly) every other member. The "Big Six" keiretsu groups exhibited this pattern, with the main bank and trading company typically having higher degree centrality (more connections and larger holdings).

- **Vertical keiretsu (垂直的系列)**: **Hub-and-spoke** or **tree-like** structures centered on a major manufacturer (e.g., Toyota, Nissan, Sony). The parent firm holds substantial stakes in first-tier suppliers, who in turn hold stakes in second-tier suppliers, creating a hierarchical supply chain network. Cross-holdings between non-adjacent tiers are less common.

**Case Study: Mazda Supply Chain Keiretsu:**
Mazda's supplier network provides a well-studied example of vertical keiretsu structure:
- Mazda holds equity stakes in ~200 suppliers (first-tier)
- First-tier suppliers (Mazda-group companies like Mazda Motor Parts, Kanzaki Kokyukoki) in turn hold stakes in second-tier suppliers
- Network analysis reveals a core-periphery structure with Mazda at the hub
- Sumitomo group membership adds horizontal connections to financial institutions and trading companies
- After Mazda's financial crisis (1970s), its network restructured — Ford's 33% equity stake introduced a cross-border dimension

**Community Detection Revealing Keiretsu Boundaries:**
Applying community detection algorithms (Louvain, Infomap, stochastic block models) to the full TSE ownership network recovers keiretsu group boundaries as distinct communities. Research shows:
- In the 1990s, community detection cleanly identified the Big Six groups as separate communities
- By the 2010s, boundaries had become blurred due to cross-shareholding unwinding, mega-bank mergers, and cross-group M&A
- Some "stubborn" communities persist, particularly among industrial firms with deep supply chain relationships (e.g., the Toyota group, the Nippon Steel group)

**Centrality Analysis Identifying Key Connectors:**
- **Main banks** (Mitsubishi UFJ, Sumitomo Mitsui, Mizuho) consistently exhibit the highest **eigenvector centrality** — they are connected to other highly connected firms
- **General trading companies** (総合商社: Mitsubishi Corp., Mitsui & Co., Itochu, Sumitomo Corp., Marubeni, Sojitz) rank highest on **betweenness centrality** — they bridge different industry sectors and keiretsu groups
- **Life insurance companies** (Nippon Life, Meiji Yasuda, Dai-ichi Life, Sumitomo Life) are high-degree nodes but lower betweenness — they hold shares widely but do not bridge distinct communities

### D.3 Japanese Cross-Shareholding Networks 2001–2023

**Structural Analysis:**

The Japanese corporate ownership network has undergone dramatic structural transformation over two decades:

- **Bow-tie structure analysis**: Applying the Vitali et al. (2011) bow-tie decomposition to TSE-listed companies reveals a shrinking strongly connected core as cross-shareholdings are unwound, but the core has not disappeared entirely
- **PageRank analysis**: Applying PageRank (treating ownership links as endorsements) reveals the most influential holders in the network. Financial institutions — particularly trust banks (Mitsubishi UFJ Trust, Sumitomo Mitsui Trust) and life insurers — rank consistently high, though their dominance has decreased as foreign institutional investors have grown
- **Power-law degree distribution**: The ownership network exhibits a heavy-tailed degree distribution — a few firms hold shares in hundreds of others while most firms have few ownership connections — consistent with scale-free network properties

**The Unwinding Trend: ~60% → 30.8% (2023):**

The most significant structural change in Japanese corporate governance is the secular decline of cross-shareholding:

| Period | Cross-Shareholding Ratio | Key Driver |
|--------|--------------------------|------------|
| Late 1980s–early 1990s | ~50–60% | Peak of bubble economy |
| 1990s–2000s | ~60% → ~45% | Banking crisis; banks forced to sell equity to meet capital requirements |
| 2000s–2010s | ~45% → ~35% | Foreign investor pressure; global financial crisis; insurance accounting changes |
| 2014 | ~33% | Stewardship Code introduced |
| 2015 | ~32% | Corporate Governance Code introduced; comply-or-explain on cross-holdings |
| 2022 | ~31% | TSE market restructuring: Prime, Standard, Growth market segments |
| 2023 | ~30.8% | TSE's "capital cost-aware management" (資本コスト経営) push |

**Key Drivers of Unwinding:**

1. **Banking crisis of the 1990s (バブル崩壊)**: The collapse of Japan's asset price bubble forced banks to sell cross-held equity to meet Basel capital adequacy requirements and absorb non-performing loan losses. This initiated the structural unwinding.

2. **Foreign investor pressure**: Foreign ownership of Japanese equities rose from ~4% in 1990 to ~30% by 2023. Foreign institutional investors (particularly US and European asset managers and activists) consistently pressured Japanese companies to reduce "unproductive" cross-shareholdings that tie up capital.

3. **Japan's Stewardship Code (2014)**: Modeled on the UK Stewardship Code, it encouraged institutional investors to engage with portfolio companies and exercise voting rights responsibly. This reduced the "silent partner" culture of cross-shareholding.

4. **Corporate Governance Code (2015, revised 2018, 2021)**: Requires listed companies to explain the rationale for holding cross-shareholdings and to reduce holdings that lack strategic justification. Each revision has strengthened disclosure requirements.

5. **TSE market restructuring (2022)**: The Tokyo Stock Exchange reorganized from five market segments (First Section, Second Section, Mothers, JASDAQ Standard, JASDAQ Growth) into three: **Prime** (highest governance standards), **Standard**, and **Growth**. Prime Market listing requires compliance with the Corporate Governance Code at the highest level, including meaningful explanation of cross-shareholding rationale.

6. **"Capital cost-aware management" push (2023, 資本コスト経営)**: In January 2023, the TSE issued a directive asking companies trading below book value (PBR < 1x) to disclose action plans for improving capital efficiency. Cross-shareholdings, which often earn below the cost of equity capital, became targets for divestiture. This was perhaps the most impactful recent catalyst.

**Network Evolution:**
The Japanese ownership network has evolved from **densely connected** (near-complete graphs within keiretsu groups) to **more sparse**, but a **stubborn core remains**:
- The number of edges (ownership links) in the TSE network has declined significantly
- Average clustering coefficient has decreased
- Network diameter has increased (the network is less tightly woven)
- However, certain bilateral cross-holdings — particularly among industrial firms with supply chain relationships — persist stubbornly
- Life insurance companies and trust banks remain high-degree nodes despite overall network thinning

**Sectoral Analysis:**

| Sector | Cross-Shareholding Trend | Notes |
|--------|--------------------------|-------|
| **Banking** | Dramatic reduction | Forced selling due to capital requirements; mega-bank mergers eliminated intra-group holdings |
| **Insurance** (life) | Gradual reduction | Accounting changes (mark-to-market) forced recognition of unrealized gains/losses; slow reduction due to long-term relationship culture |
| **Automotive** | Selective reduction | OEM-supplier relationships remain strong; Toyota group retains significant holdings; some OEMs (e.g., Nissan) have reduced dramatically |
| **Electronics** | Significant reduction | Industry restructuring (Sharp, Toshiba, Olympus scandals) accelerated unwinding |
| **Steel & Materials** | Moderate reduction | Nippon Steel group maintains some holdings; industry consolidation (Nippon Steel + Sumitomo Metal) restructured network |

### D.4 JPX Governance Code and Network Implications

**Corporate Governance Code (コーポレートガバナンス・コード):**

Japan's Corporate Governance Code, first issued in 2015 and revised in 2018 and 2021, is a principles-based code operating on a "comply-or-explain" basis. Its provisions directly affect corporate network structure:

- **Board independence requirements**: Companies (especially Prime Market-listed) are required to appoint at least one-third independent outside directors. This has dramatically increased the diversity of board networks by bringing in non-executive directors from outside traditional keiretsu circles.

- **Cross-shareholding disclosure requirements** (Principle 1-4): Companies must "examine whether or not to hold each individual cross-shareholding... on an annual basis," disclose the rationale for holding, and exercise voting rights on cross-held shares appropriately. This principle has been the primary regulatory driver of cross-shareholding unwinding.

- **Revised Principle 1-4 (2021)**: Strengthened requirements to disclose the "economic rationale" and "future outlook" for each cross-shareholding and to establish criteria for reducing holdings. Companies must also disclose the results of their annual review.

- **Stewardship Code alignment**: Institutional investors are expected to disclose voting policies and engagement activities, including their stance on portfolio companies' cross-shareholdings.

**Impact on Network Density and Structure:**
- Interlock network density has *increased* even as ownership density has decreased — because the Code pushes for independent director appointments, many independent directors serve on multiple boards, creating new interlocks
- Ownership network density has decreased steadily
- The "main bank" role in governance has weakened as banks reduce equity holdings and firms diversify financing sources
- New governance actors — activist investors, institutional shareholder services (ISS/Glass Lewis) — have entered the network as influential nodes

### D.5 Visualization and Data Tools

| Tool / Source | Description | Access |
|---------------|-------------|--------|
| **Nikkei cross-shareholding visualization (日経持ち合い調査)** | Annual survey of cross-shareholding among listed companies; visualizations of ownership networks | Nikkei (commercial) |
| **Toyo Keizai Shikiho (東洋経済四季報)** | Company relationship data including major shareholders, officer appointments, business connections | Commercial (Toyo Keizai) |
| **JPX Stock Distribution Survey (株式分布状況調査)** | Annual survey of share ownership distribution by investor type (individuals, corporations, foreigners, banks, etc.) | Open (JPX website) |
| **EDINET (Electronic Disclosure for Investors' NETwork)** | Electronic filing system for securities reports, quarterly reports, and ownership disclosures | Open (FSA Japan) |
| **TDnet (Timely Disclosure Network)** | Real-time disclosure of material corporate information | Open (JPX) |
| **Large Shareholding Reports (大量保有報告書)** | 5% threshold ownership disclosure filings | Open (EDINET) |
| **Academic visualization efforts** | Various research projects visualizing keiretsu networks using Gephi, NetworkX, D3.js | Academic papers |

---

## E. GNN × Governance

### E.1 Credit Rating with Graph Neural Networks

**CCR-GNN: Corporate Credit Rating with Graph Neural Networks**

Traditional credit rating relies on financial ratios, industry classification, and analyst judgment. GNN-based approaches incorporate the relational structure of corporate networks:

- **Architecture**: Constructs a multi-relational graph of companies connected by supply chain relationships, ownership links, industry co-membership, and geographic proximity. Node features include financial ratios (leverage, profitability, liquidity, coverage) and macroeconomic indicators. Graph convolutional layers aggregate information from neighbors, allowing a company's credit assessment to be influenced by the financial health of its suppliers, customers, and ownership partners.
- **Key insight**: A company's creditworthiness depends not just on its own financials but on the creditworthiness of its network neighbors — supply chain disruptions, ownership chain distress, and industry contagion all propagate through the corporate graph
- **Performance**: CCR-GNN outperforms traditional models (logistic regression, random forests, gradient boosting) and tabular deep learning (feedforward neural networks) on credit rating prediction benchmarks, demonstrating that network effects contain significant information about creditworthiness beyond what is captured in firm-level features
- **Practical application**: Banks and rating agencies can incorporate network features into credit risk models to better assess systemic and contagion risk

### E.2 Company-as-Tribe: Tree-guided Hierarchical GNN (TH-GNN)

**TH-GNN**, presented at **KDD 2022**, introduces a novel approach to modeling corporate group structures:

- **Metaphor**: "Company-as-Tribe" — companies are not isolated entities but members of tribal (group) structures with hierarchical organization. A company's behavior is shaped by its position within its corporate tribe (business group, keiretsu, chaebol, industrial cluster).
- **Architecture**: Tree-guided Hierarchical GNN that:
  1. Constructs a corporate hierarchy tree from ownership data (parent-subsidiary relationships)
  2. Uses tree-structured message passing to propagate information along hierarchical ownership chains
  3. Applies graph attention mechanisms at each hierarchy level to weight the influence of sibling entities, parent entities, and subsidiary entities
  4. Combines hierarchical embeddings with flat (non-hierarchical) graph representations
- **Applications**: Applied to stock prediction and credit risk assessment on Chinese A-share market data; demonstrates that hierarchical group structure contains predictive information not captured by flat graph representations
- **Relevance to governance**: The model explicitly captures the hierarchical ownership structures (pyramids, business groups) that governance research studies. It can be used to assess how governance quality at the group level (e.g., controlling family behavior) propagates through the corporate hierarchy.

### E.3 Hierarchical Heterogeneous GNN (HHGNN)

HHGNN extends graph neural network architectures to the full complexity of corporate governance data:

- **Multiple node types**: Companies, directors, shareholders (institutional investors, individuals, government entities), auditors, legal entities, regulatory bodies
- **Multiple edge types**: Ownership (direct, indirect, beneficial), board membership (executive, non-executive, independent), audit relationships, supply chain connections, advisory mandates, legal proceedings, joint ventures
- **Hierarchical aggregation**: Information is aggregated at multiple scales:
  1. *Local level*: Immediate neighbors (direct shareholders, board members)
  2. *Community level*: Keiretsu groups, industry clusters, geographic regions
  3. *Global level*: Entire market structure, systemic position
- **Heterogeneous attention**: Different attention mechanisms for different edge types — ownership links are weighted differently from board interlocks, which are weighted differently from supply chain relationships
- **Governance applications**: HHGNN can be used for multi-task learning across governance-related predictions (credit risk, fraud likelihood, governance quality, ESG scores) by exploiting the shared graph structure

### E.4 Corporate Fraud Detection

**"Corporate Fraud Detection in Rich-yet-Noisy Financial Graphs":**
Financial relationship data is inherently noisy — ownership records may be outdated, supply chain links may be partial, director appointments may be misrecorded. This paper addresses the challenge of detecting fraud signals in graphs with significant noise:

- **Noise handling**: Develops graph attention mechanisms that learn to downweight noisy edges while amplifying informative connections. The model estimates edge reliability as a latent variable.
- **Fraud signal propagation**: Fraud at one firm (e.g., accounting manipulation, insider trading) creates detectable signals in connected firms (unusual trading patterns, abnormal accruals, related-party transaction anomalies). The GNN propagates these signals through the corporate graph.
- **Feature selection**: Addresses the challenge of high-dimensional, noisy financial features by learning feature importance jointly with graph structure. Financial ratios, textual features (from filings), and market features are integrated.

**Know-GNN: Knowledge-guided GNN for Explainable Fraud Detection:**
- **Explainability**: Regulatory compliance requirements (MiFID II, Basel III, SEC guidelines) demand that fraud detection models provide interpretable explanations. Know-GNN integrates domain knowledge (known fraud patterns, regulatory rules, accounting standards) as constraints and priors in the GNN, producing explanations alongside predictions.
- **Architecture**: Combines a GNN backbone with a knowledge graph of regulatory rules and known fraud typologies. The knowledge graph provides structured prior knowledge (e.g., "circular trading typically involves entities connected through indirect ownership") that guides the GNN's attention mechanisms.
- **Output**: For each prediction, Know-GNN produces a subgraph explanation — the specific entities, relationships, and features that contributed to the fraud assessment — making it suitable for regulatory examination and legal proceedings.

### E.5 Other GNN Applications in Governance

| Application | Description | Relevance |
|-------------|-------------|-----------|
| **Predicting board appointments** | GNN trained on historical director-company bipartite network to predict future board appointments; captures homophily, triadic closure, and preferential attachment | Understanding director labor markets and governance network formation |
| **ESG score prediction from governance networks** | Using ownership and interlock networks as features for predicting ESG ratings; exploits the correlation between network position and governance quality | ESG integration in investment analysis |
| **Director effectiveness scoring** | GNN-based ranking of director influence and effectiveness using board interlock networks, company performance, and director biographical features | Board evaluation and composition optimization |
| **Governance risk early warning** | Temporal GNN monitoring governance network changes (sudden interlock changes, ownership restructuring, unusual director departures) for early risk detection | Regulatory surveillance and investor due diligence |
| **Shareholder activism prediction** | Predicting which firms are likely targets for activist investors based on governance quality, ownership concentration, and network position | Investment strategy and corporate preparedness |

---

## F. Knowledge Graph × Governance

### F.1 Enterprise KG for Company Ownership

**Bank of Italy Research (EDBT 2020):**
The Bank of Italy developed an ownership knowledge graph to support supervisory activities:

- **Motivation**: Italian banking regulators need to understand the complex ownership structures of banks and their controlling shareholders to assess governance risk, concentration risk, and related-party transactions
- **Methodology**:
  1. Integrating heterogeneous data sources: Orbis, Italian company registry (Registro Imprese), Bank of Italy internal databases, Consob (securities regulator) disclosures
  2. **Entity resolution**: Matching entities across databases with different identifiers, naming conventions, and update frequencies. Uses blocking strategies, string similarity, and graph-based matching to resolve entities across sources
  3. Constructing an OWL/RDF knowledge graph of ownership relationships, with semantic types for different entity categories (banks, insurance companies, holding companies, natural persons)
  4. **UBO computation on KG**: Running recursive control algorithms on the knowledge graph to compute ultimate beneficial ownership, handling cycles and threshold-based ownership definitions
- **Applications**: Supervisory monitoring of ownership changes, identifying potential conflicts of interest, assessing corporate group perimeters, and verifying regulatory compliance (e.g., qualified holdings approvals)
- **Technical stack**: RDF triple store, SPARQL queries for ownership path analysis, custom control propagation algorithms integrated with the KG

### F.2 Firmographica (2025)

**Firmographica** is a recent (2025) KG-based framework for financial risk assessment:

- **Focus**: Short-selling risk assessment — identifying firms at elevated risk of short-seller attacks (which often target governance weaknesses)
- **Architecture**:
  - Constructs a temporal knowledge graph linking companies to governance events (board changes, ownership transfers, audit committee compositions, regulatory actions), financial indicators (accruals quality, revenue recognition patterns), and market signals (short interest, options activity, analyst downgrades)
  - Links corporate governance factors to market risk through KG reasoning
  - **Temporal dimension**: Governance events have timestamps and durations; the KG captures governance state changes over time (e.g., "Company X added independent director Y on date D")
- **Multi-source data integration**: SEC filings, proxy statements, court records, news articles, social media (investor forums), patent filings, government contracts
- **Short-selling risk model**: Combines KG embeddings (TransE, RotatE, temporal KG embedding models) with financial time series to predict short-selling activity

### F.3 ESG Governance Knowledge Graphs

ESG (Environmental, Social, Governance) frameworks increasingly rely on structured data representations:

- **Mapping governance practices to ESG frameworks**: Knowledge graphs link specific corporate governance practices (board independence, audit committee composition, executive compensation structure) to ESG rating criteria (MSCI, Sustainalytics, ISS ESG, FTSE Russell)
- **Board composition KG**: Rich knowledge graph of directors including biographical data (education, career history, expertise, demographics), board roles (chair, lead independent, committee memberships), and network connections (shared boards, shared employers, shared education)
- **Compliance monitoring**: KG reasoning can automatically check governance compliance — e.g., "Does this company's board have at least one-third independent directors?" can be answered through SPARQL queries or rule-based reasoning on the governance KG
- **Regulatory alignment checking**: Mapping governance requirements across jurisdictions (US SOX, UK Corporate Governance Code, Japan CG Code, EU CSDDD) onto a unified ontological framework to identify gaps and conflicts

### F.4 LLM + GraphRAG for Governance Compliance

The combination of Large Language Models with graph-based retrieval-augmented generation (GraphRAG) opens new possibilities for governance compliance:

- **Retrieval-Augmented Generation on governance KGs**: LLMs can query a structured governance knowledge graph to retrieve relevant facts (board compositions, ownership chains, voting histories, regulatory requirements) before generating responses, dramatically reducing hallucination in governance analysis

- **Automated proxy statement analysis**: LLMs can parse proxy statements (DEF 14A filings) to extract structured governance data — director nominees, compensation tables, voting items, shareholder proposals — and populate a governance KG. GraphRAG then enables question-answering over the extracted data: "What percentage of the board is independent?" "Has executive compensation exceeded peer benchmarks?"

- **Board evaluation report generation**: Using a governance KG as the source of truth, LLMs can generate comprehensive board evaluation reports that incorporate director network analysis, peer benchmarking, skills matrix assessment, and diversity metrics

- **Regulatory change impact assessment**: When regulations change (e.g., new SEC rules on climate disclosure, new TSE governance requirements), GraphRAG can assess the impact on a portfolio of companies by reasoning over the governance KG: "Which companies in our portfolio do not currently comply with the new requirement?"

- **Multi-jurisdictional compliance checking**: For multinational corporations subject to governance requirements in multiple jurisdictions, GraphRAG can integrate jurisdiction-specific regulatory KGs to identify compliance gaps and conflicts: "Company X is listed in Tokyo, New York, and London — what are the combined independent director requirements?"

---

## G. Platforms and Tools

### G.1 Investigation and Compliance Platforms

| Platform | Focus | Key Features | Technology |
|----------|-------|--------------|------------|
| **Sayari** | Supply chain & ownership intelligence | Global corporate records from 250+ jurisdictions; UBO computation; risk scoring; sanctions screening; supply chain mapping | Proprietary graph database; ML-based entity resolution |
| **Linkurious** | Graph visualization for investigations | Connected to Neo4j and other graph databases; compliance investigation workflows; case management; visual link analysis | Frontend for graph databases; JavaScript-based visualization |
| **Neo4j** | General-purpose graph database | Financial services solutions for fraud detection, AML, and customer 360; Cypher query language; graph data science library | Native graph storage; ACID compliant; GDS plugin for graph algorithms |
| **GraphAware** | Neo4j-based analytics platform | **Hume**: NLP→KG pipeline for converting unstructured text into knowledge graphs; financial crime detection; entity resolution | NLP pipeline + Neo4j; NER and RE models |
| **Ultipa** | High-performance graph database | Real-time fraud detection; deep-link traversal for UBO; strong presence in Chinese financial market; HTAP graph engine | Custom graph engine; SQL-like query language (UQL) |
| **TigerGraph** | Scalable graph analytics | Anti-fraud and AML solutions; entity resolution at scale; real-time deep link analytics; graph-based machine learning | Distributed graph database; GSQL query language; native parallel computation |
| **PoolParty** | Semantic AI platform | Taxonomy and ontology management; knowledge graph construction from unstructured data; text mining | Semantic middleware; SKOS/OWL; text analytics |
| **Palantir** | Data integration and analytics | AML compliance (Gotham); corporate investigation (Metropolis); entity-centric data fusion | Proprietary platform; graph-based data model |

### G.2 Governance Data Providers

| Provider | Data Scope | Coverage | Key Offerings |
|----------|-----------|----------|---------------|
| **ISS (Institutional Shareholder Services)** | Governance ratings, proxy advisory, voting analytics | Global (~44,000 companies) | Governance QualityScore; proxy voting recommendations; ESG ratings; compensation analytics; board analytics |
| **Glass Lewis** | Proxy advisory, governance research | Global (~30,000 companies) | Independent proxy voting recommendations; governance analysis; ESG data; shareholder engagement |
| **Bloomberg** | Governance data, ESG, ownership, financials | Global | Bloomberg Governance Scores; board composition data; ownership analysis; executive compensation; ESG data |
| **MSCI** | ESG ratings, governance scores, climate data | Global (~8,500 companies) | ESG Ratings (AAA–CCC); Governance Pillar scores; controversy monitoring; climate metrics |
| **Orbis (BvD/Moody's)** | Ownership, financials, directors, compliance | 400M+ entities globally | Comprehensive ownership chains; UBO computation; director data; financial data; compliance risk indicators |
| **Equilar** | Executive compensation, board data | US focus (~5,000 companies) | Executive compensation analytics; board composition; peer group analysis; director network mapping |
| **BoardEx** | Director networks, biographical data | Global (~1.5M+ profiles) | Director relationship mapping; biographical profiles; board composition analytics; succession planning data |
| **Diligent** | Board management, governance intelligence | Global | Board portal software; entity management; governance data; ESG reporting; compliance management |
| **S&P Capital IQ** | Financials, ownership, key developments | Global | Company financials; ownership data; transaction data; key developments; supply chain mapping |

---

## H. Datasets

| Dataset | Records | Description | Access | URL / Notes |
|---------|---------|-------------|--------|-------------|
| **Open Ownership Register** | 27M+ | Beneficial ownership declarations from 200+ jurisdictions; standardized under BODS | Open (API, bulk) | register.openownership.org |
| **GLEIF LEI** | 2.5M+ | Legal Entity Identifiers with direct and ultimate parent relationship data; ISO 17442 standard | Open (API, bulk) | gleif.org |
| **Transparency Fabric 2.0** | — | Graph-based beneficial ownership data standard; extends BODS with additional relationship types | Open | Open Ownership initiative |
| **OpenCorporates** | 170M+ | Company registrations from government registries worldwide; officer data; gazette notices | Freemium (API) | opencorporates.com |
| **NRG Metrics** | — | Governance ratings, ESG data, corporate events for emerging market companies | Commercial | nrgmetrics.com |
| **ISS Governance Data** | — | Board composition, voting records, compensation data, governance ratings; available through WRDS | Commercial (WRDS) | issgovernance.com |
| **Orbis (BvD)** | 400M+ | Ownership chains, financial data, director data, compliance indicators; most comprehensive global source | Commercial (WRDS, institutional) | bvdinfo.com |
| **Harvard Law School Forum on Corporate Governance** | — | Research papers, datasets, and commentary on corporate governance topics | Open | corpgov.law.harvard.edu |
| **JPX Stock Distribution Survey (株式分布状況調査)** | — | Annual survey of share ownership distribution by investor type for all TSE-listed companies | Open (JPX) | jpx.co.jp |
| **BoardEx** | 1.5M+ profiles | Director biographical data, board memberships, network connections, employment history | Commercial | boardex.com |
| **SEC EDGAR Filings** | — | US company filings: 10-K (annual), 10-Q (quarterly), DEF 14A (proxy), Schedule 13D/13G (ownership), Form 3/4/5 (insider) | Open | sec.gov/edgar |
| **WRDS (Wharton Research Data Services)** | — | Multi-database platform: CRSP, Compustat, ISS, BoardEx, IBES, TAQ, Orbis, and many more | Academic (institutional subscription) | wrds-web.wharton.upenn.edu |
| **ICIJ Offshore Leaks Database** | 800K+ | Entities from Panama Papers, Paradise Papers, Pandora Papers; offshore ownership structures | Open | offshoreleaks.icij.org |
| **FactSet** | — | Ownership data, supply chain relationships, financial data, estimates | Commercial | factset.com |
| **Refinitiv (LSEG) Ownership Data** | — | Institutional and insider ownership data; detailed holder profiles | Commercial | refinitiv.com |

---

## I. Ontologies and Standards

### I.1 FIBO (Financial Industry Business Ontology)

The **Financial Industry Business Ontology (FIBO)** is the most comprehensive and widely adopted formal ontology for the financial industry:

- **Scope**: Legal entities, corporate structures, ownership, governance, financial instruments, business processes, market data, loans, derivatives, indices
- **Legal Entities Module**: Covers corporate structures (subsidiaries, branches, holding companies), ownership relationships (equity, debt, beneficial), governance structures (boards, committees, officers), and regulatory status
- **Standards Body**: Developed and maintained by the **EDM Council** (now a program of GLEIF) and formalized as an **OMG (Object Management Group)** standard
- **Technical Basis**: Built on **OWL (Web Ontology Language)** and **RDF (Resource Description Framework)** with formal semantics enabling automated reasoning and consistency checking
- **Extensibility**: Designed to be extended by institutions and regulators for domain-specific needs (e.g., adding keiretsu-specific relationship types, or modeling dual-class share structures)
- **Adoption**: Used by major banks (JPMorgan, Wells Fargo, Deutsche Bank), regulators (OFR, GLEIF, Bank of England), and data providers (Bloomberg, Refinitiv) for data harmonization and interoperability
- **Limitations for Governance Research**: While FIBO covers legal entities and basic ownership, it lacks deep modeling of governance-specific concepts like board committee structures, director independence criteria, voting mechanisms, shareholder engagement practices, and governance code compliance

### I.2 BODS (Beneficial Ownership Data Standard)

The **Beneficial Ownership Data Standard (BODS)**, developed by **Open Ownership**, provides a standardized schema for publishing beneficial ownership data:

- **Format**: JSON-based schema defining how to declare beneficial ownership relationships
- **Data Model**: Three statement types:
  1. **Entity statements**: Describing legal entities (companies, trusts, partnerships)
  2. **Person statements**: Describing natural persons who are beneficial owners
  3. **Ownership-or-control statements**: Describing the relationship between an entity and a person (or another entity), including ownership percentage, voting rights, and nature of control
- **Complex structures**: Supports multi-layered ownership, nominee arrangements, trust structures, and conditional interests
- **International adoption**: Adopted by the UK (Persons with Significant Control register), Ukraine, Armenia, Nigeria, and other countries as the basis for their beneficial ownership registers
- **Interoperability**: Designed to enable cross-border data sharing and analysis of international ownership structures
- **Graph compatibility**: BODS data naturally maps to a directed graph (or knowledge graph), making it directly usable for network analysis and KG construction

### I.3 FinRegOnt (Financial Regulation Ontology)

**FinRegOnt** aims to represent financial regulations as structured, machine-readable linked data:

- **Scope**: Regulatory requirements, compliance obligations, reporting standards, supervisory expectations
- **Cross-jurisdictional mapping**: Links equivalent regulatory requirements across jurisdictions (e.g., mapping SOX Section 404 to J-SOX, mapping UK Corporate Governance Code provisions to Japan's CG Code)
- **Machine-readable compliance rules**: Enables automated compliance checking — for example, encoding "a Prime Market-listed company must have at least one-third independent directors" as a machine-executable rule that can be checked against a governance KG
- **Rule-based reasoning**: Combined with OWL reasoning, FinRegOnt can derive compliance status from corporate governance facts: given a board composition and independence criteria, the system can determine compliance without manual assessment

### I.4 Other Relevant Standards

| Standard | Organization | Purpose |
|----------|-------------|---------|
| **LEI (Legal Entity Identifier)** | GLEIF / ISO 17442 | 20-character alphanumeric code uniquely identifying legal entities; enables entity resolution across datasets |
| **ISIN (International Securities Identification Number)** | ISO 6166 | 12-character code identifying securities; links shares to issuing entities |
| **XBRL (eXtensible Business Reporting Language)** | XBRL International | Standardized financial reporting; enables machine-readable extraction of financial data from filings |
| **EDGAR Full-Text Search Taxonomy** | SEC | Taxonomies for US financial reporting; governance-related tags in DEF 14A filings |
| **Inline XBRL for CG Reports** | FSA Japan | Japanese governance report tagging in XBRL; enables structured extraction of governance data from 有価証券報告書 |
| **GRI Standards** | Global Reporting Initiative | Sustainability reporting standards including governance disclosures (GRI 405: Diversity, GRI 2: Governance) |

---

## J. Research Gaps and Future Directions

### J.1 Absence of a Governance-Specific Ontology

**The Problem:**
Despite the maturity of FIBO for financial entities and the existence of BODS for beneficial ownership, there is **no comprehensive, standardized ontology for corporate governance**. Current ontologies cover the "what" (legal entities, ownership shares) but not the "how" (governance mechanisms, decision-making processes, stakeholder interactions).

**What is Missing:**
- **Board structure ontology**: Formal representation of board types (unitary, dual-tier), committee structures (audit, nomination, compensation, risk), roles (chair, lead independent director, committee chair), and independence criteria (which vary by jurisdiction)
- **Voting mechanism ontology**: Modeling different voting systems (straight voting, cumulative voting, proxy voting, majority-of-minority voting), quorum requirements, and shareholder proposal processes
- **Compensation structure ontology**: Base salary, annual bonus, long-term incentives (stock options, RSUs, performance shares), deferred compensation, clawback provisions, change-of-control provisions
- **Governance code compliance ontology**: Machine-readable representation of governance code provisions and their comply-or-explain status for each company
- **Stakeholder engagement ontology**: Shareholder activism, proxy contests, say-on-pay votes, ESG engagement, stewardship activities

**Opportunity:**
A governance ontology bridging legal, financial, and organizational concepts would enable automated governance analysis, cross-jurisdictional comparison, and integration of governance data with existing financial KGs.

### J.2 Temporal Knowledge Graphs for Governance

**The Problem:**
Governance structures are inherently temporal — boards change, directors rotate, ownership transfers, governance policies evolve, regulations are amended. Current knowledge graphs for governance are **mostly static snapshots**, capturing the state of governance at a single point in time.

**What is Needed:**
- **Temporal KG frameworks** that capture governance dynamics: entity validity periods (director X served on board Y from date A to date B), event-driven updates (CEO resignation, ownership disclosure, governance code amendment), and temporal queries ("what was the board composition as of date D?")
- **Event-driven governance KG updates**: Triggering KG updates from real-time data feeds — EDINET filings, TDnet disclosures, SEC EDGAR filings, news articles
- **Temporal link prediction**: Predicting future governance changes (e.g., which directors will be appointed/departed, which cross-holdings will be unwound) based on historical temporal patterns
- **Temporal embedding methods**: Extending static KG embedding models (TransE, RotatE, ComplEx) with temporal dimensions to capture governance dynamics (e.g., TTransE, DE-SimplE, TNTComplEx)

### J.3 Japan Governance Reform × Latest KG/GNN Methods (Almost Unexplored)

**The Opportunity:**
Japan's rapid governance reform since 2015 creates a **unique natural experiment** for studying the interaction between governance regulation and corporate network structure. This is arguably the most significant governance transformation in any major economy in the 21st century, yet it remains **virtually unexplored** with modern KG/GNN methods.

**Why Japan is Uniquely Interesting:**
1. **Cross-shareholding unwinding** can be tracked through network dynamics — measuring changes in edge weights, network density, community structure, and centrality over time as companies divest cross-holdings
2. **Board independence increase** is measurable through director network evolution — new independent directors enter the interlock network, changing its structure, diversity, and information flow properties
3. **TSE market restructuring (2022)** as a structural break — the reorganization into Prime/Standard/Growth created a natural experiment where Prime Market firms face stricter governance requirements than Standard Market firms, enabling difference-in-differences analysis
4. **Rich, structured data**: Japan's disclosure requirements (有価証券報告書, CG報告書, 株主総会招集通知) provide detailed, machine-readable governance data amenable to KG construction
5. **Temporal dimension**: The reform is ongoing, creating a multi-year time series of governance network changes

**★ Virtually no research combines these reforms with modern KG/GNN methods:**
- No temporal knowledge graph tracking Japanese governance reform
- No GNN-based analysis of how governance improvements propagate through keiretsu networks
- No causal inference study using KG/GNN methods to assess the impact of the Corporate Governance Code on network structure and firm outcomes
- No LLM-based extraction pipeline for Japanese governance documents populating a temporal KG

**Proposed Research Direction:**
Temporal KG of Japanese governance reform (2015–present) with GNN-based impact analysis:
1. Construct a temporal KG from EDINET filings, governance reports, and ownership disclosures
2. Model governance reform events as temporal edges in the KG
3. Apply temporal GNNs to study how governance changes propagate through the corporate network
4. Use causal inference methods (difference-in-differences, regression discontinuity around TSE restructuring) to identify the causal effect of governance reforms on network structure and firm outcomes

### J.4 LLM × Governance KG Construction

**The Opportunity:**
Large Language Models can potentially automate the construction and maintenance of governance knowledge graphs from unstructured Japanese-language documents:

- **Source Documents**:
  - 有価証券報告書 (Annual Securities Reports): Contain detailed governance information — board composition, major shareholders, cross-shareholdings, officer compensation, corporate governance structure
  - 招集通知 (Convocation Notices / Proxy Statements): Shareholder meeting agenda, director election proposals, compensation proposals, articles of incorporation amendments
  - CG報告書 (Corporate Governance Reports): Filed with TSE; contain governance structure, comply-or-explain disclosures for CG Code principles, cross-shareholding policies
  - Press releases and news articles: Management changes, M&A announcements, governance events

- **Challenges**:
  - **Japanese language**: Domain-specific financial Japanese with specialized terminology (株式持ち合い, 独立社外取締役, 指名委員会等設置会社), formal legal language, and dense tabular formats
  - **Domain specificity**: Governance concepts require financial and legal domain knowledge; general-purpose LLMs may miss nuances
  - **Accuracy requirements**: Governance data feeds into investment decisions and regulatory compliance — errors have real consequences
  - **Structured extraction**: Extracting structured relationships (director-company-role-date) from semi-structured and unstructured text

- **Potential**:
  - Fully automated governance KG construction and updating pipeline
  - Near-real-time governance monitoring from continuous document processing
  - Multi-language governance analysis (Japanese ↔ English ↔ Chinese) enabling cross-border comparison
  - Integration with GraphRAG for governance Q&A and compliance checking

### J.5 International Comparative Governance Network Framework

**The Opportunity:**
Different countries exhibit fundamentally different corporate governance regimes, each with characteristic network structures. A comparative network framework would enable systematic cross-country analysis:

| Governance Regime | Country | Key Network Characteristics |
|---|---|---|
| **Anglo-Saxon dispersed ownership** | US, UK | Sparse ownership networks; institutional investors dominate; active market for corporate control; dense interlock networks among large firms |
| **Bank-centered / coordinated** | Germany | Dense ownership networks centered on banks and insurance companies; codetermination (worker representatives on supervisory boards); *Deutschland AG* interlock model (now weakening) |
| **Keiretsu / cross-shareholding** | Japan | Horizontal and vertical keiretsu; cross-shareholding networks; main bank system (now unwinding); see Section D |
| **Chaebol / family conglomerate** | South Korea | Family-controlled conglomerates with circular cross-shareholding; pyramid structures; concentrated control |
| **State ownership / Party governance** | China | State-owned enterprises (SOEs) controlled through SASAC; Communist Party committees embedded in corporate governance; dual governance structure (party + corporate) |
| **Family business groups** | India, SE Asia, Latin America | Promoter families control diversified groups through pyramids and dual-class shares; limited minority shareholder protection |

**Proposed Framework:**
1. **Standardized network construction**: Uniform methodology for constructing ownership and interlock networks from country-specific data sources, enabling apples-to-apples comparison
2. **Network metrics for regime classification**: Using network statistics (density, clustering, degree distribution, community structure, bow-tie decomposition, power-law exponents) to quantitatively characterize and classify governance regimes
3. **Convergence/divergence analysis**: Tracking how governance networks evolve over time and whether they converge toward a common structure (the "convergence hypothesis") or maintain persistent differences
4. **Shock propagation analysis**: Comparing how economic shocks (financial crises, pandemics, regulatory changes) propagate differently through networks with different governance structures
5. **Governance reform impact measurement**: Using network analysis to quantify the impact of governance reforms (Japan's CG Code, South Korea's chaebol reform, China's mixed-ownership reform) on corporate network structure

---

## References

### Foundational
- Vitali, S., Glattfelder, J.B. & Battiston, S. (2011). The network of global corporate control. *PLoS ONE*, 6(10), e25995.
- Garcia-Bernardo, J., Fichtner, J., Takes, F.W. & Heemskerk, E.M. (2017). Uncovering offshore financial centers: Conduits and sinks in the global corporate ownership network. *Scientific Reports*, 7, 6246.
- Fichtner, J., Heemskerk, E.M. & Garcia-Bernardo, J. (2017). Hidden power of the Big Three? Passive index funds, re-concentration of corporate ownership, and new financial risk. *Business and Politics*, 19(2), 298–326.

### Board Interlocks
- Mizruchi, M.S. (1996). What do interlocks do? An analysis, critique, and assessment of research on interlocking directorates. *Annual Review of Sociology*, 22, 271–298.
- Davis, G.F. (1991). Agents without principles? The spread of the poison pill through the intercorporate network. *Administrative Science Quarterly*, 36(4), 583–613.
- Davis, G.F., Yoo, M. & Baker, W.E. (2003). The small world of the American corporate elite, 1982–2001. *Strategic Organization*, 1(3), 301–326.
- Larcker, D.F., So, E.C. & Wang, C.C.Y. (2013). Boardroom centrality and firm performance. *Journal of Accounting and Economics*, 55(2–3), 225–250.
- Hallock, K.F. (1997). Reciprocally interlocking boards of directors and executive compensation. *Journal of Financial and Quantitative Analysis*, 32(3), 331–344.
- Haunschild, P.R. (1993). Interorganizational imitation: The impact of interlocks on corporate acquisition activity. *Administrative Science Quarterly*, 38(4), 564–592.
- Cai, Y. & Sevilir, M. (2012). Board connections and M&A transactions. *Journal of Financial Economics*, 103(2), 327–349.
- Bizjak, J.M., Lemmon, M.L. & Whitby, R.J. (2009). Option backdating and board interlocks. *Review of Financial Studies*, 22(11), 4821–4847.
- Conyon, M.J. & Muldoon, M.R. (2006). The small world of corporate boards. *Journal of Business Finance & Accounting*, 33(9–10), 1321–1343.
- Fracassi, C. & Tate, G. (2012). External networking and internal firm governance. *Journal of Finance*, 67(1), 153–194.
- Kramarz, F. & Thesmar, D. (2013). Social networks in the boardroom. *Journal of the European Economic Association*, 11(4), 780–807.
- Adams, R.B. & Ferreira, D. (2009). Women in the boardroom and their impact on governance and performance. *Journal of Financial Economics*, 94(2), 291–309.

### Ownership Networks
- Pfeffer, J. & Salancik, G.R. (1978). *The External Control of Organizations: A Resource Dependence Perspective*. Harper & Row.
- Domhoff, G.W. (1967). *Who Rules America?* Prentice-Hall.
- Useem, M. (1984). *The Inner Circle: Large Corporations and the Rise of Business Political Activity in the U.S. and U.K.* Oxford University Press.

### Japan / Keiretsu
- Lincoln, J.R. & Gerlach, M.L. (2004). *Japan's Network Economy: Structure, Persistence, and Change*. Cambridge University Press.
- Miyajima, H. & Kuroki, F. (2007). The unwinding of cross-shareholding in Japan: Causes, effects, and implications. In Aoki, M., Jackson, G. & Miyajima, H. (Eds.), *Corporate Governance in Japan*, Oxford University Press.
- Aoki, M. (1994). The Japanese firm as a system of attributes: A survey and research agenda. In Aoki, M. & Dore, R. (Eds.), *The Japanese Firm: Sources of Competitive Strength*, Oxford University Press.

### GNN × Governance
- Company-as-Tribe: TH-GNN. KDD 2022.
- Corporate Fraud Detection in Rich-yet-Noisy Financial Graphs. Various venues.

### Knowledge Graph × Governance
- Bank of Italy. Enterprise KG for company ownership (EDBT 2020).
- Firmographica (2025). KG-based framework for short-selling risk assessment.

### Standards and Ontologies
- EDM Council. Financial Industry Business Ontology (FIBO). https://spec.edmcouncil.org/fibo/
- Open Ownership. Beneficial Ownership Data Standard (BODS). https://standard.openownership.org/
- GLEIF. Global Legal Entity Identifier Foundation. https://www.gleif.org/
