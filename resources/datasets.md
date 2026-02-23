# Datasets for Financial Network Science and Knowledge Graphs

This document catalogs datasets relevant to financial network analysis, knowledge graph construction, and related research. Organized by domain.

---

## Ownership and Corporate Structure

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| Orbis | Bureau van Dijk (Moody's) | Global firm-level ownership, financials, and corporate structure database | 400M+ entities worldwide | Commercial | https://www.bvdinfo.com/en-gb/our-products/data/international/orbis |
| OpenOwnership Register | Open Ownership | Global beneficial ownership data aggregated from national registers | 27M+ ownership records | Open | https://register.openownership.org/ |
| GLEIF LEI Database | Global Legal Entity Identifier Foundation | Legal Entity Identifiers with relationship data (direct/ultimate parent) | 2.5M+ legal entities | Open | https://www.gleif.org/en/lei-data/gleif-concatenated-file |
| OpenCorporates | OpenCorporates | Largest open database of companies, with jurisdictional filings | 220M+ companies, 170+ jurisdictions | Freemium | https://opencorporates.com/ |
| SEC EDGAR | U.S. Securities and Exchange Commission | Corporate filings (10-K, 10-Q, 13-F, DEF 14A proxy), ownership disclosures | All US public companies | Open | https://www.sec.gov/edgar/ |
| Companies House UK | UK Government | UK company registrations, directors, persons with significant control | 5M+ companies | Open | https://www.gov.uk/government/organisations/companies-house |
| ICIJ Offshore Leaks | International Consortium of Investigative Journalists | Panama Papers, Paradise Papers, Pandora Papers — offshore entity networks | 800K+ offshore entities | Open | https://offshoreleaks.icij.org/ |
| Wikidata Corporate Entities | Wikidata / Wikimedia | Structured data on companies, ownership, board members | 10M+ organizational entities | Open | https://www.wikidata.org/ |
| EDGAR Company Ownership (13F/13D) | SEC | Institutional ownership filings, activist investor positions | All US institutional holders | Open | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=13F |
| Refinitiv Ownership Data | LSEG (Refinitiv) | Global institutional and insider ownership data | 80K+ companies globally | Commercial | https://www.refinitiv.com/ |
| Bureau van Dijk Zephyr | Bureau van Dijk (Moody's) | M&A, IPO, and private equity deal information with network data | 2M+ deals | Commercial | https://www.bvdinfo.com/en-gb/our-products/data/international/zephyr |

---

## Financial Networks and Interbank Data

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| BIS International Banking Statistics | Bank for International Settlements | Cross-border banking claims and liabilities by country and sector | 30+ reporting countries | Open (aggregated) | https://www.bis.org/statistics/bankstats.htm |
| ECB Securities Holdings Statistics | European Central Bank | Euro area securities holdings by sector and instrument | Euro area | Restricted | https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/securities/html/index.en.html |
| Federal Reserve Flow of Funds (Z.1) | Federal Reserve Board | Financial accounts of the United States — intersectoral flows | US economy | Open | https://www.federalreserve.gov/releases/z1/ |
| DTCC Trade Repository Data | DTCC | OTC derivatives trade data (interest rate, credit, equity, FX) | Trillions in notional | Restricted/Regulatory | https://www.dtcc.com/repository-otc-data |
| Fedwire Funds Transfer Data | Federal Reserve Bank of New York | Large-value interbank payment flows | ~$3T daily transfers | Restricted (research access) | https://www.newyorkfed.org/fedwire |
| TARGET2 Payment Data | European Central Bank | Euro area large-value payment system data | €2T+ daily | Restricted (central bank research) | — |
| e-MID Interbank Market | e-MID SIM S.p.A. | European electronic interbank deposit market — bilateral transactions | European banks | Academic access available | https://www.e-mid.it/ |
| CDS Data (DTCC TIW) | DTCC | Credit default swap trade-level data | Global CDS market | Restricted | https://www.dtcc.com/ |

---

## Market Data for Correlation Networks

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| CRSP | Center for Research in Security Prices (Wharton) | US stock prices, returns, volumes — historical since 1925 | All US equities | Academic (commercial) | https://www.crsp.org/ |
| TAQ (Trade and Quote) | NYSE | US equity tick-by-tick trade and quote data | Millisecond resolution | Academic (commercial) | https://www.nyse.com/market-data/historical |
| Yahoo Finance | Yahoo | Free daily/intraday stock prices, fundamentals | Global equities | Open | https://finance.yahoo.com/ |
| WRDS (Wharton Research Data Services) | Wharton / U Penn | Integrated platform: CRSP, Compustat, IBES, TAQ, and more | Multi-database | Academic (subscription) | https://wrds-www.wharton.upenn.edu/ |
| Compustat | S&P Global (via WRDS) | Financial statements, balance sheet, income statement for US/global firms | 80K+ companies | Academic (commercial) | https://www.spglobal.com/marketintelligence/ |
| Bloomberg Terminal Data | Bloomberg L.P. | Comprehensive market data, news, analytics, corporate data | Global | Commercial | https://www.bloomberg.com/professional/ |
| Quandl / Nasdaq Data Link | Nasdaq | Alternative data, financial and economic datasets | Various | Freemium | https://data.nasdaq.com/ |
| Kenneth French Data Library | Dartmouth / Kenneth French | Factor returns (Fama-French), industry portfolios, benchmark data | US/Global equities | Open | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html |

---

## NLP and Text Data

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| EDGAR Full-Text Filings | SEC | Raw text of all SEC filings (10-K, 10-Q, 8-K, etc.) | Millions of filings | Open | https://www.sec.gov/edgar/searchedgar/efulltext.htm |
| EDGAR-CORPUS | Lancaster University / EMNLP | Pre-processed, cleaned annual reports from EDGAR for NLP research | 10K+ annual reports | Open | https://github.com/nlpaueb/edgar-corpus |
| FinancialPhraseBank | Malo et al. (Aalto University) | Sentence-level sentiment annotations from financial news | 4,846 sentences | Open | https://huggingface.co/datasets/financial_phrasebank |
| FiQA (Financial Question Answering) | WWW 2018 Challenge | Financial opinion mining, QA, sentiment from microblogs and headlines | 17K+ sentences | Open | https://sites.google.com/view/fiqa/ |
| TweetFinSent | — | Financial sentiment from Twitter/X posts | Thousands of tweets | Open | https://huggingface.co/datasets/ |
| Reuters Financial News | Thomson Reuters | Financial news articles with metadata and categories | 10K+ articles | Academic | — |
| SEntFiN | — | Entity-level financial sentiment dataset | 10K+ annotations | Open | https://github.com/ |
| FinSim | FinNLP Workshop | Financial term similarity and hypernym detection shared task | Thousands of term pairs | Open | https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp/ |
| Financial Times Archive | Financial Times | Historical news articles for financial text mining | Decades of coverage | Commercial | https://www.ft.com/ |
| Loughran-McDonald Sentiment Word Lists | Notre Dame | Finance-specific sentiment dictionaries (positive, negative, uncertainty, etc.) | ~4,000 words | Open | https://sraf.nd.edu/loughranmcdonald-master-dictionary/ |

---

## Blockchain and Cryptocurrency Data

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| Elliptic Bitcoin Dataset | Elliptic / Kaggle | Labeled Bitcoin transaction graph for illicit transaction detection | 203K transactions, 234K edges | Open | https://www.kaggle.com/datasets/ellipticco/elliptic-data-set |
| Ethereum Blockchain (BigQuery) | Google Cloud | Full Ethereum blockchain — transactions, contracts, token transfers | Entire blockchain | Open | https://cloud.google.com/blog/products/data-analytics/ethereum-bigquery-public-dataset |
| Bitcoin Blockchain | Various (Blockchair, etc.) | Full Bitcoin transaction graph and UTXO set | Entire blockchain | Open | https://blockchair.com/ |
| Chainalysis Reactor Data | Chainalysis | Labeled cryptocurrency transaction data for compliance | Multi-chain | Commercial | https://www.chainalysis.com/ |
| Token Terminal | Token Terminal | DeFi protocol financial data (TVL, revenue, P/E ratios) | 200+ DeFi protocols | Freemium | https://tokenterminal.com/ |
| DeFi Llama | DeFi Llama | DeFi TVL, protocol data, cross-chain analytics | 2000+ protocols | Open | https://defillama.com/ |

---

## Japanese and Asian Financial Data

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| TSR (Tokyo Shoko Research) Firm Transaction Data | Tokyo Shoko Research | Japanese firm-to-firm transaction (buyer-seller) network | ~1M firms, ~4M transaction links | Commercial (academic access) | https://www.tsr-net.co.jp/ |
| TDB (Teikoku Databank) | Teikoku Databank | Japanese firm data with supply chain and ownership relationships | ~1.5M firms | Commercial (academic access) | https://www.tdb.co.jp/ |
| Nikkei NEEDS | Nikkei | Japanese financial statements, stock prices, corporate data | All listed Japanese firms | Academic (commercial) | https://www.nikkei.co.jp/needs/ |
| EDINET | Financial Services Agency (Japan) | Japanese corporate filings in XBRL (equivalent of SEC EDGAR) | All Japanese listed companies | Open | https://disclosure.edinet-fsa.go.jp/ |
| JPX Market Data | Japan Exchange Group | Japanese equity trading data, order book, corporate actions | TSE-listed companies | Commercial | https://www.jpx.co.jp/english/markets/statistics-equities/ |
| BOJ Flow of Funds | Bank of Japan | Japanese financial accounts by sector — intersectoral flows | Japanese economy | Open | https://www.boj.or.jp/en/statistics/sj/ |
| CSMAR | GTA (China) | Chinese financial market and corporate data | All Chinese listed firms | Academic (commercial) | https://www.gtarsc.com/ |
| WIND Information | Wind Info (China) | Chinese financial terminal data, corporate data | Chinese markets | Commercial | https://www.wind.com.cn/ |

---

## Graph and Knowledge Graph Benchmark Datasets

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| FinDKG | Cheng et al. (2024) | Dynamic financial knowledge graph from news with temporal relations | 14K+ entities, temporal | Open | https://github.com/ |
| FNKG (Financial News Knowledge Graph) | Various | Knowledge graph extracted from financial news articles | Thousands of triples | Open | — |
| Freebase (FB15k / FB15k-237) | Google / Meta | General knowledge graph benchmark for link prediction | 15K entities, 592K triples | Open | https://www.microsoft.com/en-us/download/details.aspx?id=52312 |
| OGB (Open Graph Benchmark) | Stanford SNAP | Standardized graph ML benchmarks including ogbn-products, ogbn-arxiv | Various scales | Open | https://ogb.stanford.edu/ |
| WikiKG90Mv2 | OGB / Wikidata | Large-scale KG benchmark from Wikidata | 90M+ entities | Open | https://ogb.stanford.edu/docs/lsc/wikikg90mv2/ |
| YAGO | Max Planck Institute | Large knowledge graph combining Wikipedia, WordNet, GeoNames | 50M+ facts | Open | https://yago-knowledge.org/ |
| DBpedia | DBpedia Association | Structured data extracted from Wikipedia | Billions of triples | Open | https://www.dbpedia.org/ |
| ConceptNet | MIT Media Lab | Common sense knowledge graph | 21M+ edges | Open | https://conceptnet.io/ |
| FinKG | Ren et al. | Financial knowledge graph for investment analysis | Thousands of entities | Open | — |
| Temporal KG Benchmarks (ICEWS, GDELT) | Various | Event-based temporal knowledge graphs with timestamps | Millions of events | Open | https://www.gdeltproject.org/ |

---

## Miscellaneous and Alternative Data

| Dataset | Provider | Description | Scale | Access | URL |
|---------|----------|-------------|-------|--------|-----|
| World Input-Output Database (WIOD) | Groningen / EU | International input-output tables linking industries across countries | 43 countries, 56 sectors | Open | https://www.rug.nl/ggdc/valuechain/wiod/ |
| OECD Inter-Country Input-Output (ICIO) | OECD | Bilateral inter-country input-output tables | 76 economies, 45 industries | Open | https://www.oecd.org/sti/ind/inter-country-input-output-tables.htm |
| UN Comtrade | United Nations | International trade data by commodity and country | 200+ countries | Open | https://comtrade.un.org/ |
| Global Financial Development Database | World Bank | Financial system characteristics by country | 200+ countries | Open | https://www.worldbank.org/en/publication/gfdr/data |
| EORA Global Supply Chain Database | University of Sydney | Multi-region input-output tables | 190 countries, 26 sectors | Open | https://worldmrio.com/ |
| BoardEx | WRDS / Management Diagnostics | Executive and board member biographical data, board interlocks | 1M+ individuals | Academic (commercial) | https://www.boardex.com/ |
| ISS (Institutional Shareholder Services) | ISS | Corporate governance ratings, proxy voting, director data | Global companies | Commercial | https://www.issgovernance.com/ |

---

*Last updated: 2026-02-23*
