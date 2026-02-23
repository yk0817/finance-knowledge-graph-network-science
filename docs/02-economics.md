# Economics Perspective on Financial Networks

## 1. Systemic Risk and Financial Networks

Systemic risk — the risk that the failure of one or several financial institutions triggers a cascade of failures threatening the entire financial system — is fundamentally a network phenomenon. Understanding it requires mapping the web of exposures, obligations, and interdependencies that link financial institutions.

### 1.1 Research Groups

#### FINEXUS Center for Financial Networks and Sustainability (University of Zurich)

**Lead: Stefano Battiston**

The FINEXUS Center is arguably the most influential research group in financial network science. Battiston, trained in statistical physics, has pioneered the application of complex network theory to systemic risk measurement and climate-finance stress testing.

**Key contributions:**
- **DebtRank** (Battiston et al., 2012): A recursive distress propagation algorithm that measures the systemic importance of financial institutions. Unlike simple centrality measures, DebtRank captures feedback loops and non-linear amplification through the network. Published in *Scientific Reports*, it has become a standard tool in macroprudential analysis.
- **Climate financial risk** (Battiston et al., 2017): "A climate stress-test of the financial system" in *Nature Climate Change* — first systematic assessment of how climate policy shocks propagate through financial networks, showing that European banks' exposures to fossil fuel sectors create systemic climate-financial risk.
- **Network valuation of financial assets** (Barucca et al., 2020): Framework unifying various network models of distress propagation under a common valuation approach.
- Ongoing work on ESG risk transmission, biodiversity-finance networks, and green finance taxonomies.

#### LSE Systemic Risk Centre (SRC)

**Key researchers: Jon Danielsson, Jean-Pierre Zigrand, Hyun Song Shin (formerly)**

The SRC focuses on **endogenous risk** — the idea that risk is not simply an external input but is created and amplified by the collective behavior of market participants within the financial network.

**Key contributions:**
- **Endogenous risk theory** (Danielsson, Shin & Zigrand, 2004, 2012): Models showing how Value-at-Risk constraints and mark-to-market accounting create procyclical feedback loops that amplify shocks.
- **Amplification mechanisms**: Fire-sale externalities, margin spirals, and liquidity black holes emerge from network interactions, not individual bank failures.
- Risk measurement critique: Danielsson's "The Illusion of Control" — arguing that standard risk models systematically underestimate tail risk because they ignore network feedback.
- Policy contributions to post-crisis regulatory design (Basel III, MiFID II).

#### Princeton Bendheim Center for Finance

**Key researchers: Markus Brunnermeier, Yuliy Sannikov**

**Key contributions:**
- **Brunnermeier & Sannikov (2014)**: "A Macroeconomic Model with a Financial Sector" — *AER* — continuous-time macro-finance model with amplification through balance sheet networks. Shows how small shocks can cause large crises through leverage-driven amplification.
- **Brunnermeier & Oehmke (2013)**: "The Maturity Rat Race" — explains how short-term debt creates fragility in financial networks.
- **CoVaR** (Adrian & Brunnermeier, 2016): Conditional Value-at-Risk — measures the systemic risk contribution of individual institutions, adopted by regulators.
- **Liquidity spirals** (Brunnermeier & Pedersen, 2009): Feedback between market liquidity and funding liquidity creates network-wide liquidity crises.

#### Complexity Science Hub Vienna

**Lead: Stefan Thurner**

**Key contributions:**
- **DebtRank extensions** (Thurner & Poledna, 2013; Poledna et al., 2015): Multi-layer financial network models capturing simultaneous credit, derivatives, FX, and securities exposures between banks. Showed that single-layer analysis dramatically underestimates systemic risk.
- **Agent-based models of financial markets** (Thurner, Farmer & Geanakoplos, 2012): Leverage cycle model where heterogeneous agents with margin constraints generate endogenous crashes.
- **Empirical financial network analysis** using comprehensive Austrian banking data.
- **Network-based taxation** (Poledna & Thurner, 2016): Proposing Pigouvian taxes on systemic risk based on network contributions.

#### IMT School for Advanced Studies Lucca

**Key researchers: Guido Caldarelli, Tiziano Squartini**

**Key contributions:**
- **Network topology of financial systems** (Caldarelli & Catanzaro, 2012): Applying statistical physics methods to characterize degree distributions, clustering, and community structure in financial networks.
- **Maximum-entropy network reconstruction** (Squartini, Mastrandrea & Garlaschelli, 2011; Cimini et al., 2015): Methods for reconstructing bilateral exposures from aggregate balance sheet data using the principle of maximum entropy. Critical for regulators who observe only partial network data.
- **Enhanced capital requirements** using network-based methods (Squartini et al., 2013).
- **Bipartite network analysis** of banks and assets (Caccioli et al., 2014): Overlapping portfolio contagion.

### 1.2 Key Papers

| Authors | Year | Title | Venue | Key Contribution |
|---|---|---|---|---|
| Allen & Gale | 2000 | Financial Contagion | *J. Political Economy* | Seminal model of interbank contagion; complete vs. incomplete networks |
| Eisenberg & Noe | 2001 | Systemic Risk in Financial Systems | *Management Science* | Clearing vector framework for interbank obligations |
| Boss, Elsinger, Summer & Thurner | 2004 | Network Topology of the Interbank Market | *Quantitative Finance* | First comprehensive empirical mapping of a national interbank network |
| Nier, Yang, Yorulmazer & Alentorn | 2007 | Network Models and Financial Stability | *J. Economic Dynamics & Control* | Simulation study of contagion in random interbank networks |
| Upper | 2011 | Simulation Methods to Assess Systemic Risk | *J. Financial Stability* | Survey of network contagion simulation approaches |
| Haldane & May | 2011 | Systemic Risk in Banking Ecosystems | *Nature* | Ecology-finance parallel; network complexity destabilizes beyond threshold |
| Battiston et al. | 2012 | DebtRank: Too Central to Fail? | *Scientific Reports* | Recursive network centrality for systemic importance |
| Cont, Moussa & Santos | 2013 | Network Structure and Systemic Risk in Banking | *Handbook on Systemic Risk* | Credit vs. funding contagion channels; Brazilian banking system |
| Elliott, Golub & Jackson | 2014 | Financial Networks and Contagion | *AER* | Cross-holdings model; integration vs. diversification trade-off |
| Acemoglu, Ozdaglar & Tahbaz-Salehi | 2015 | Systemic Risk and Stability in Financial Networks | *AER* | Phase transition: dense networks absorb small shocks but amplify large ones |
| Glasserman & Young | 2016 | Contagion in Financial Networks | *J. Economic Literature* | Comprehensive survey; bounds on cascade sizes |
| Battiston et al. | 2016 | Complexity Theory and Financial Regulation | *Science* | Policy manifesto for network-based financial regulation |
| Barucca et al. | 2020 | Network Valuation in Financial Systems | *Mathematical Finance* | Unified framework for distress propagation models |

---

## 2. Financial Network Theory

### 2.1 Matthew O. Jackson (Stanford University)

Jackson is one of the leading theorists of social and economic networks. His textbook *Social and Economic Networks* (2008, Princeton University Press) is the standard graduate reference.

**Key contributions to financial networks:**
- **Elliott, Golub & Jackson (2014)**: Financial networks and contagion model — analyzed how cross-holdings create interdependencies and how diversification and integration have opposing effects on systemic stability.
- **Jackson & Pernoud (2021)**: "Systemic Risk in Financial Networks: A Survey" — comprehensive survey connecting network theory to financial stability.
- **Game theory on networks**: Strategic network formation, diffusion of innovations and behaviors, Bayesian learning on networks.
- **Network centrality and power**: Formal analysis of how network position translates to economic influence.

### 2.2 Daron Acemoglu (MIT)

While primarily known for institutional economics and political economy, Acemoglu has made foundational contributions to production network theory.

**Key contributions:**
- **Acemoglu, Carvalho, Ozdaglar & Tahbaz-Salehi (2012)**: "The Network Origins of Aggregate Fluctuations" in *Econometrica* — demonstrated that if the input-output network has heavy-tailed degree distribution, idiosyncratic shocks to individual sectors do not average out and instead generate aggregate volatility. Overturned the conventional wisdom (Lucas, 1977) that micro shocks wash out.
- **Acemoglu, Ozdaglar & Tahbaz-Salehi (2015)**: Financial network stability — the "robust-yet-fragile" result showing a phase transition in how network density affects contagion.
- **Acemoglu, Ozdaglar & Tahbaz-Salehi (2017)**: Microeconomic origins of macroeconomic tail risks.

### 2.3 Rama Cont (University of Oxford)

Cont bridges mathematical finance, probability theory, and network science.

**Key contributions:**
- **Cont, Moussa & Santos (2013)**: Network structure and systemic risk — detailed simulation of the Brazilian banking system identifying the relative importance of credit vs. funding contagion.
- **Cont & Schaanning (2017)**: Fire sales, indirect contagion, and systemic stress testing — modeled how asset fire sales by distressed banks propagate losses to others with overlapping portfolios, even without direct bilateral exposures.
- **CCP networks**: Analysis of central counterparty clearing networks, stress testing of CCPs, and design of default fund allocation mechanisms.
- **Systemic risk measurement**: Developing stress testing frameworks that integrate network effects.

### 2.4 Vasco Carvalho (University of Cambridge → UCL)

**Key contributions:**
- **Acemoglu, Carvalho, Ozdaglar & Tahbaz-Salehi (2012)**: Co-authored the foundational network origins paper.
- **Carvalho (2014)**: "From Micro to Macro via Production Networks" — *Journal of Economic Perspectives* — accessible survey of how micro shocks propagate through production networks to generate aggregate fluctuations.
- **Carvalho, Nirei, Saito & Tahbaz-Salehi (2021)**: Supply chain disruptions and aggregate output — studied the 2011 Great East Japan Earthquake as a natural experiment for production network propagation.
- **Granular origins of fluctuations**: Extending the Gabaix (2011) granular hypothesis through production networks.

---

## 3. Economic Complexity

### 3.1 Harvard Growth Lab

**Key researchers: Ricardo Hausmann, Cesar Hidalgo (formerly)**

The Growth Lab pioneered the **economic complexity** framework, which uses bipartite network analysis (countries × products) to predict economic growth and development.

**Key contributions:**
- **Economic Complexity Index (ECI)** (Hidalgo & Hausmann, 2009): A measure of the productive knowledge embedded in a country's export basket, derived from the spectral properties of the country-product bipartite network. Countries that export diverse, non-ubiquitous products score high.
- **Product Space** (Hidalgo, Klinger, Barabási & Hausmann, 2007): A network where products are connected if countries that export one tend to also export the other. Shows that economic development is constrained by proximity in product space — countries diversify into "nearby" products.
- **Atlas of Economic Complexity** (Hausmann et al., 2013): Book and interactive visualization tool mapping the product space of countries worldwide.
- **The Building Blocks of Economic Complexity** (Hidalgo & Hausmann, 2009, *PNAS*): Formal development of the "method of reflections" algorithm for computing complexity indices.
- **Growth predictions**: ECI predicts future GDP growth better than standard institutional and human capital measures (Hidalgo & Hausmann, 2009).

### 3.2 Observatory of Economic Complexity (OEC)

Originally developed at the MIT Media Lab by Hidalgo and colleagues, the OEC is an interactive data visualization platform for international trade data:

- Visualizes the product space, trade flows, and economic complexity indices
- Covers 200+ countries and 5000+ products
- Uses HS (Harmonized System) and SITC classification
- Enables exploration of comparative advantage (RCA), trade partners, and structural transformation trajectories
- Now maintained independently; widely used in development economics research and policy

### 3.3 Fitness-Complexity Method

**Key researchers: Andrea Tacchella, Luciano Pietronero (Sapienza University of Rome / Enrico Fermi Research Center)**

An alternative to the Hidalgo-Hausmann method, the Fitness-Complexity approach uses a non-linear iterative algorithm:

**Key contributions:**
- **Tacchella, Cristelli, Caldarelli, Gabrielli & Pietronero (2012)**: "A New Metrics for Countries' Fitness and Products' Complexity" in *Scientific Reports* — introduced the non-linear fitness-complexity algorithm. Country fitness and product complexity are coupled via non-linear equations where complex products are those exported only by fit countries, and fit countries are those exporting complex products.
- **Cristelli, Gabrielli, Tacchella, Caldarelli & Pietronero (2013)**: Showed that the Fitness-Complexity method outperforms ECI in predicting GDP growth, particularly for low-income countries.
- **Zaccaria, Cristelli, Tacchella & Pietronero (2014)**: Extended to sub-national analysis and technological innovation.
- **Adopted by the World Bank** (Tacchella et al., 2018) for GDP nowcasting and forecasting in developing countries.

**Key difference from ECI:** The fitness-complexity method is non-linear and breaks the symmetry between countries and products, arguing that complexity of products should be dominated by the least fit country that exports them (a max-entropy-like constraint), while ECI uses a linear eigenvector approach.

---

## 4. Complex Systems Approaches to Economics

### 4.1 Santa Fe Institute (SFI)

**Key researchers: W. Brian Arthur, J. Doyne Farmer (formerly), Samuel Bowles**

The Santa Fe Institute has been the intellectual home of complexity economics since the late 1980s.

**Key contributions:**
- **W. Brian Arthur**: "Increasing Returns and Path Dependence in the Economy" (1994) — challenged the neoclassical assumption of diminishing returns. Arthur showed that positive feedback, increasing returns, and lock-in effects create multiple equilibria and path dependence in economic systems.
- **Arthur (2015)**: *Complexity and the Economy* — collection presenting the complexity economics paradigm: the economy as an evolving complex system rather than an equilibrium system.
- **SFI Economics Program workshops (1987–)**: Seminal early workshops brought physicists, biologists, and economists together, producing *The Economy as an Evolving Complex System* volumes (Anderson, Arrow & Pines, 1988; Arthur, Durlauf & Lane, 1997).
- **Farmer, Patelli & Zovko (2005)**: "The predictive power of zero intelligence in financial markets" — showed that much of market structure can be explained by the interaction rules (network/market microstructure) rather than agent intelligence.

### 4.2 Institute for New Economic Thinking (INET) at Oxford

**Lead: J. Doyne Farmer**

Farmer's group at the Oxford Martin School / INET Oxford is at the frontier of agent-based computational economics and complexity economics.

**Key contributions:**
- **Agent-based models (ABMs) of financial markets**: Farmer & Foley (2009), "The economy needs agent-based modelling" in *Nature* — argued that conventional DSGE models failed to predict the crisis and ABMs offer a more realistic alternative by modeling heterogeneous, interacting agents.
- **Market ecology** (Farmer, 2002; Farmer & Lo, 2002): Viewing market participants as species in an ecosystem, with strategies coexisting, competing, and going extinct based on their interaction within the market network.
- **Leverage and crashes** (Thurner, Farmer & Geanakoplos, 2012): ABM showing how leverage constraints generate endogenous boom-bust cycles through network amplification.
- **Housing market ABM** (Baptista et al., 2016): Agent-based model of the UK housing market for macroprudential policy analysis.
- **Supply chain networks** (Pichler et al., 2022): ABM of production networks applied to pandemic shock analysis and COVID-19 economic impact.
- **Technology progress and economic growth** (Farmer & Lafond, 2016): Predicting technological improvement using network models of technology interdependence.

### 4.3 Aix-Marseille School of Economics (AMSE)

**Key researcher: Alan Kirman**

**Key contributions:**
- **Kirman (1992)**: "Whom or What Does the Representative Individual Represent?" — *Journal of Economic Perspectives* — influential critique arguing that representative agent models cannot capture emergent phenomena arising from interactions among heterogeneous agents.
- **Interaction-based approach to economics** (Kirman, 1997, 2006): Proposed treating the economy as a complex adaptive system where agent interactions (modeled as network connections) generate macro patterns not deducible from individual optimization.
- **Ants model** (Kirman, 1993): Simple model showing how agent interactions create herding behavior resembling financial market bubbles and crashes.
- Extensive work on Marseille fish market as an empirical laboratory for interaction economics.

### 4.4 Complexity Economics: Core Principles

The complexity economics paradigm, in contrast to neoclassical general equilibrium, emphasizes:

| Principle | Neoclassical | Complexity Economics |
|---|---|---|
| **Agents** | Representative, fully rational | Heterogeneous, boundedly rational |
| **Equilibrium** | System tends to unique equilibrium | Multiple attractors, out-of-equilibrium dynamics |
| **Interactions** | Via market clearing prices | Direct interactions on networks, local information |
| **Dynamics** | Comparative statics | Evolutionary, path-dependent, emergent |
| **Shocks** | Exogenous | Endogenously generated by system dynamics |
| **Policy analysis** | Optimization-based | Simulation-based, scenario analysis |
| **Mathematics** | Calculus, fixed-point theorems | Dynamical systems, agent-based simulation, network theory |

---

## 5. Central Banks and Network Analysis

Central banks have become major consumers and producers of financial network analysis, driven by their mandates for financial stability and prudential supervision.

### 5.1 Bank for International Settlements (BIS)

The BIS serves as the "central bank of central banks" and coordinates international financial stability research.

**Key contributions:**
- **BIS Consolidated Banking Statistics**: Data on international banking exposures used to construct the global banking network.
- **BIS Quarterly Review**: Regular publication of network-based analyses of global financial flows.
- **Craig & von Peter (2014)**: "Interbank tiering and money center banks" — published by BIS researchers, identifying the core-periphery structure of interbank networks.
- **Research on correspondent banking networks**: Mapping the decline and restructuring of cross-border banking relationships.
- **International data hub**: Coordinates data sharing among central banks for systemic risk monitoring (e.g., International Data Hub initiative).

### 5.2 European Central Bank (ECB)

The ECB has been at the forefront of operationalizing network analysis for central banking.

**Key tools and contributions:**
- **NATkit (Network Analysis Tool Kit)**: Internal software developed by ECB staff for analyzing financial networks — interbank exposures, payment flows, securities holdings. Used in supervisory analysis under the Single Supervisory Mechanism (SSM).
- **TARGET2 payment network analysis**: Extensive research on the topology and dynamics of the TARGET2 large-value payment system:
  - Iori et al. (2015): Network analysis of TARGET2 flows
  - Arciero et al. (2009): Tiered structure and systemic importance in payment systems
- **SSM supervisory data**: Under the SSM, the ECB collects granular exposure data from significant euro area banks, enabling network-based systemic risk assessment.
- **Securities Holdings Statistics (SHS)**: Granular data on who holds what securities, enabling portfolio overlap and indirect contagion analysis.
- **Financial Stability Review**: Regularly features network-based analyses of euro area banking system interconnectedness.

### 5.3 Office of Financial Research (OFR), U.S. Treasury

The OFR was created by the Dodd-Frank Act (2010) explicitly to monitor systemic risk.

**Key contributions:**
- **Financial Stability Monitor**: Dashboard of systemic risk indicators including network-based metrics (interconnectedness, contagion indices).
- **Network visualization tools**: Interactive tools for mapping financial system interconnections.
- **Reference data infrastructure**: Development of the Legal Entity Identifier (LEI) system through GLEIF — enabling network construction by uniquely identifying counterparties.
- **Research papers**: Numerous working papers on financial network analysis:
  - Flood et al. (2015): Network-based approaches to OTC derivatives regulation
  - Paddrik et al. (2016): Agent-based model of CDS market contagion
- **Financial Entity Identification and Data Standards**: Developing and promoting data standards for financial network construction.

### 5.4 Federal Reserve System

**Key contributions:**
- **Fedwire payment network studies**:
  - Soramäki, Bech, Arnold, Glass & Beyeler (2007): "The topology of interbank payment flows" — foundational empirical analysis of the Fedwire payment network, revealing small-world properties, heavy-tailed degree distributions, and a tight core-periphery structure.
  - Bech & Atalay (2010): The topology of the federal funds market — network analysis of overnight lending.
- **Financial interconnectedness research**:
  - Federal Reserve Board staff use network models for stress testing (CCAR/DFAST framework integrating network effects).
  - Research on interconnectedness of bank holding companies, nonbank financial institutions, and money market funds.
- **Financial Accounts of the United States (Z.1)**: Flow of funds data providing the basis for who-to-whom financial network construction.
- **Federal Reserve Bank of New York**: Particularly active in network analysis — Liberty Street Economics blog regularly features network-based financial analysis.

### 5.5 Bank of England (BoE)

**Key contributions:**
- **Haldane (2009)**: "Rethinking the Financial Network" — landmark speech that catalyzed regulatory interest in network approaches.
- **Macroprudential network analysis**: BoE's Financial Policy Committee uses network models in its systemic risk assessment toolkit.
- **Insurance and reinsurance networks**: Analysis of interconnectedness in the insurance sector, mapping reinsurance chains that could propagate losses.
- **Supervisor network models**: Internal models mapping UK bank exposures for stress testing.
- **Staff working papers**: Extensive series on financial network analysis:
  - Langfield, Liu & Ota (2014): Mapping the UK interbank system
  - Coen, Coen & Hüser (2024): Network effects in stress testing
- **Collaboration with academia**: Strong links with LSE SRC, Cambridge, Oxford for financial network research.

### 5.6 Bank of Japan (BoJ)

**Key contributions:**
- **Payment and settlement system analysis**: Network analysis of the BOJ-NET large-value payment system.
- **Inaoka, Ninomiya, Taniguchi, Shimizu & Takayasu (2004)**: Early analysis of the Japanese interbank network.
- **Financial System Report**: Regularly includes network-based analysis of the Japanese financial system's stability.
- **Financial system stability assessment**: Uses network models to assess contagion risk among Japanese banks, securities firms, and insurance companies.
- **Research on cross-shareholdings**: Analysis of the complex cross-holding network structure unique to Japanese corporate groups (keiretsu).
- **Collaboration with complexity scientists**: BoJ researchers have published with Takayasu, Aoyama, and other Japanese complex systems researchers on financial network analysis.

---

## 6. Key Economics Papers on Financial Networks

| # | Author(s) | Year | Title | Venue | Key Contribution |
|---|---|---|---|---|---|
| 1 | Allen & Gale | 2000 | Financial Contagion | *J. Political Economy* | First formal model of interbank network contagion |
| 2 | Eisenberg & Noe | 2001 | Systemic Risk in Financial Systems | *Management Science* | Clearing payment vector framework |
| 3 | Boss, Elsinger, Summer & Thurner | 2004 | Network Topology of the Interbank Market | *Quantitative Finance* | Empirical mapping of Austrian interbank network |
| 4 | Soramäki, Bech et al. | 2007 | Topology of Interbank Payment Flows | *Physica A* | Foundational study of Fedwire network topology |
| 5 | Hidalgo, Klinger, Barabási & Hausmann | 2007 | The Product Space Conditions the Development of Nations | *Science* | Product proximity network constraining structural transformation |
| 6 | Haldane | 2009 | Rethinking the Financial Network | *BoE Speech* | Catalyzed regulatory interest in network approaches |
| 7 | Hidalgo & Hausmann | 2009 | The Building Blocks of Economic Complexity | *PNAS* | Economic Complexity Index from bipartite trade network |
| 8 | Farmer & Foley | 2009 | The Economy Needs Agent-Based Modelling | *Nature* | Case for ABMs as alternative to DSGE |
| 9 | Brunnermeier & Pedersen | 2009 | Market Liquidity and Funding Liquidity | *Rev. Financial Studies* | Liquidity spiral feedback mechanism |
| 10 | Haldane & May | 2011 | Systemic Risk in Banking Ecosystems | *Nature* | Ecology-finance analogy; complexity-stability trade-off |
| 11 | Acemoglu, Carvalho, Ozdaglar & Tahbaz-Salehi | 2012 | Network Origins of Aggregate Fluctuations | *Econometrica* | Heavy-tailed production networks prevent shock diversification |
| 12 | Battiston et al. | 2012 | DebtRank: Too Central to Fail? | *Scientific Reports* | Network-based systemic importance measure |
| 13 | Tacchella, Cristelli, Caldarelli, Gabrielli & Pietronero | 2012 | A New Metrics for Countries' Fitness and Products' Complexity | *Scientific Reports* | Non-linear fitness-complexity method |
| 14 | Thurner, Farmer & Geanakoplos | 2012 | Leverage Causes Fat Tails and Clustered Volatility | *Quantitative Finance* | ABM of leverage-driven endogenous crashes |
| 15 | Cont, Moussa & Santos | 2013 | Network Structure and Systemic Risk in Banking | *Handbook on Systemic Risk* | Credit vs. funding contagion simulation |
| 16 | Carvalho | 2014 | From Micro to Macro via Production Networks | *J. Economic Perspectives* | Accessible survey of production network economics |
| 17 | Elliott, Golub & Jackson | 2014 | Financial Networks and Contagion | *AER* | Cross-holdings, integration-diversification trade-off |
| 18 | Acemoglu, Ozdaglar & Tahbaz-Salehi | 2015 | Systemic Risk and Stability in Financial Networks | *AER* | Phase transition in network contagion |
| 19 | Poledna, Molina-Borboa, Martínez-Jaramillo, van der Leij & Thurner | 2015 | The Multi-Layer Network Nature of Systemic Risk | *J. Financial Stability* | Multi-layer banking networks underestimate systemic risk in single layers |
| 20 | Battiston et al. | 2016 | Complexity Theory and Financial Regulation | *Science* | Policy framework for network-based regulation |
| 21 | Adrian & Brunnermeier | 2016 | CoVaR | *AER* | Conditional systemic risk measure |
| 22 | Glasserman & Young | 2016 | Contagion in Financial Networks | *J. Economic Literature* | Comprehensive survey with cascade bounds |
| 23 | Battiston et al. | 2017 | A Climate Stress-Test of the Financial System | *Nature Climate Change* | Climate risk transmission through financial networks |
| 24 | Jackson & Pernoud | 2021 | Systemic Risk in Financial Networks: A Survey | *Annual Rev. Economics* | Comprehensive theoretical survey |
| 25 | Pichler, Pangallo, del Rio-Chanona, Lafond & Farmer | 2022 | Forecasting the Propagation of Pandemic Shocks with a Dynamic Input-Output Model | *J. Economic Dynamics & Control* | ABM of production networks for pandemic impact |

---

## References

- Acemoglu, D., Carvalho, V.M., Ozdaglar, A. & Tahbaz-Salehi, A. (2012). The network origins of aggregate fluctuations. *Econometrica*, 80(5), 1977–2016.
- Acemoglu, D., Ozdaglar, A. & Tahbaz-Salehi, A. (2015). Systemic risk and stability in financial networks. *American Economic Review*, 105(2), 564–608.
- Adrian, T. & Brunnermeier, M.K. (2016). CoVaR. *American Economic Review*, 106(7), 1705–1741.
- Allen, F. & Gale, D. (2000). Financial contagion. *Journal of Political Economy*, 108(1), 1–33.
- Arthur, W.B. (1994). *Increasing Returns and Path Dependence in the Economy*. University of Michigan Press.
- Arthur, W.B. (2015). *Complexity and the Economy*. Oxford University Press.
- Barucca, P. et al. (2020). Network valuation in financial systems. *Mathematical Finance*, 30(4), 1181–1213.
- Battiston, S. et al. (2012). DebtRank: Too central to fail? *Scientific Reports*, 2, 541.
- Battiston, S. et al. (2016). Complexity theory and financial regulation. *Science*, 351(6275), 818–819.
- Battiston, S. et al. (2017). A climate stress-test of the financial system. *Nature Climate Change*, 7, 283–288.
- Boss, M., Elsinger, H., Summer, M. & Thurner, S. (2004). Network topology of the interbank market. *Quantitative Finance*, 4(6), 677–684.
- Brunnermeier, M.K. & Pedersen, L.H. (2009). Market liquidity and funding liquidity. *Review of Financial Studies*, 22(6), 2201–2238.
- Brunnermeier, M.K. & Sannikov, Y. (2014). A macroeconomic model with a financial sector. *American Economic Review*, 104(2), 379–421.
- Carvalho, V.M. (2014). From micro to macro via production networks. *Journal of Economic Perspectives*, 28(4), 23–48.
- Cont, R., Moussa, A. & Santos, E.B. (2013). Network structure and systemic risk in banking systems. In *Handbook on Systemic Risk*, Cambridge University Press.
- Craig, B. & von Peter, G. (2014). Interbank tiering and money center banks. *Journal of Financial Intermediation*, 23(3), 322–347.
- Cristelli, M., Gabrielli, A., Tacchella, A., Caldarelli, G. & Pietronero, L. (2013). Measuring the intangibles: A metrics for the economic complexity of countries and products. *PLoS ONE*, 8(8), e70726.
- Danielsson, J., Shin, H.S. & Zigrand, J.P. (2004). The impact of risk regulation on price dynamics. *Journal of Banking & Finance*, 28(5), 1069–1087.
- Eisenberg, L. & Noe, T.H. (2001). Systemic risk in financial systems. *Management Science*, 47(2), 236–249.
- Elliott, M., Golub, B. & Jackson, M.O. (2014). Financial networks and contagion. *American Economic Review*, 104(10), 3115–3153.
- Farmer, J.D. & Foley, D. (2009). The economy needs agent-based modelling. *Nature*, 460, 685–686.
- Glasserman, P. & Young, H.P. (2016). Contagion in financial networks. *Journal of Economic Literature*, 54(3), 779–831.
- Haldane, A.G. (2009). Rethinking the financial network. Speech at the Financial Student Association, Amsterdam.
- Haldane, A.G. & May, R.M. (2011). Systemic risk in banking ecosystems. *Nature*, 469, 351–355.
- Hidalgo, C.A. & Hausmann, R. (2009). The building blocks of economic complexity. *PNAS*, 106(26), 10570–10575.
- Hidalgo, C.A., Klinger, B., Barabási, A.L. & Hausmann, R. (2007). The product space conditions the development of nations. *Science*, 317(5837), 482–487.
- Jackson, M.O. (2008). *Social and Economic Networks*. Princeton University Press.
- Jackson, M.O. & Pernoud, A. (2021). Systemic risk in financial networks: A survey. *Annual Review of Economics*, 13, 171–202.
- Kirman, A. (1992). Whom or what does the representative individual represent? *Journal of Economic Perspectives*, 6(2), 117–136.
- Poledna, S., Molina-Borboa, J.L., Martínez-Jaramillo, S., van der Leij, M. & Thurner, S. (2015). The multi-layer network nature of systemic risk. *Journal of Financial Stability*, 20, 70–81.
- Soramäki, K., Bech, M.L., Arnold, J., Glass, R.J. & Beyeler, W.E. (2007). The topology of interbank payment flows. *Physica A*, 379(1), 317–333.
- Squartini, T., Mastrandrea, R. & Garlaschelli, D. (2011). Unbiased sampling of network ensembles. *New Journal of Physics*, 17(2), 023052.
- Tacchella, A., Cristelli, M., Caldarelli, G., Gabrielli, A. & Pietronero, L. (2012). A new metrics for countries' fitness and products' complexity. *Scientific Reports*, 2, 723.
- Thurner, S., Farmer, J.D. & Geanakoplos, J. (2012). Leverage causes fat tails and clustered volatility. *Quantitative Finance*, 12(5), 695–707.
