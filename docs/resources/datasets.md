# 金融ネットワーク科学とナレッジグラフのためのデータセット

本文書は、金融ネットワーク分析、ナレッジグラフ構築、および関連研究に関連するデータセットをまとめたものである。ドメインごとに整理している。

---

## 所有構造と企業構造

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| Orbis | Bureau van Dijk (Moody's) | グローバルな企業レベルの所有構造、財務、企業構造データベース | 全世界4億以上のエンティティ | 商用 | https://www.bvdinfo.com/en-gb/our-products/data/international/orbis |
| OpenOwnership Register | Open Ownership | 各国の登録簿から集約されたグローバルな実質的所有者データ | 2,700万以上の所有記録 | オープン | https://register.openownership.org/ |
| GLEIF LEI Database | Global Legal Entity Identifier Foundation（グローバルLEI財団） | 関係データ（直接親会社／最終親会社）を含む法人識別子 | 250万以上の法人 | オープン | https://www.gleif.org/en/lei-data/gleif-concatenated-file |
| OpenCorporates | OpenCorporates | 法域別登録情報を含む最大のオープン企業データベース | 2億2,000万以上の企業、170以上の法域 | フリーミアム | https://opencorporates.com/ |
| SEC EDGAR | U.S. Securities and Exchange Commission（米国証券取引委員会） | 企業開示書類（10-K、10-Q、13-F、DEF 14A委任状）、所有開示 | 全米上場企業 | オープン | https://www.sec.gov/edgar/ |
| Companies House UK | UK Government（英国政府） | 英国企業登録、取締役、重要支配者 | 500万以上の企業 | オープン | https://www.gov.uk/government/organisations/companies-house |
| ICIJ Offshore Leaks | International Consortium of Investigative Journalists（国際調査報道ジャーナリスト連合） | Panama Papers、Paradise Papers、Pandora Papers — オフショア法人ネットワーク | 80万以上のオフショア法人 | オープン | https://offshoreleaks.icij.org/ |
| Wikidata Corporate Entities | Wikidata / Wikimedia | 企業、所有構造、取締役会メンバーの構造化データ | 1,000万以上の組織エンティティ | オープン | https://www.wikidata.org/ |
| EDGAR Company Ownership (13F/13D) | SEC | 機関投資家所有開示、アクティビスト投資家ポジション | 全米機関投資家 | オープン | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=13F |
| Refinitiv Ownership Data | LSEG (Refinitiv) | グローバルな機関投資家およびインサイダー所有データ | 全世界8万以上の企業 | 商用 | https://www.refinitiv.com/ |
| Bureau van Dijk Zephyr | Bureau van Dijk (Moody's) | M&A、IPO、プライベートエクイティ取引情報（ネットワークデータ付き） | 200万以上の取引 | 商用 | https://www.bvdinfo.com/en-gb/our-products/data/international/zephyr |

---

## 金融ネットワークとインターバンクデータ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| BIS International Banking Statistics | Bank for International Settlements（国際決済銀行） | 国別・セクター別のクロスボーダー銀行債権・負債 | 30カ国以上の報告国 | オープン（集計値） | https://www.bis.org/statistics/bankstats.htm |
| ECB Securities Holdings Statistics | European Central Bank（欧州中央銀行） | ユーロ圏のセクター別・商品別証券保有データ | ユーロ圏 | 制限付き | https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/securities/html/index.en.html |
| Federal Reserve Flow of Funds (Z.1) | Federal Reserve Board（連邦準備制度理事会） | 米国の資金循環勘定 — セクター間フロー | 米国経済 | オープン | https://www.federalreserve.gov/releases/z1/ |
| DTCC Trade Repository Data | DTCC | OTCデリバティブ取引データ（金利、クレジット、株式、外国為替） | 想定元本で数兆ドル規模 | 制限付き／規制当局向け | https://www.dtcc.com/repository-otc-data |
| Fedwire Funds Transfer Data | Federal Reserve Bank of New York（ニューヨーク連邦準備銀行） | 大口インターバンク決済フロー | 日次約3兆ドルの送金 | 制限付き（研究アクセス） | https://www.newyorkfed.org/fedwire |
| TARGET2 Payment Data | European Central Bank（欧州中央銀行） | ユーロ圏大口決済システムデータ | 日次2兆ユーロ以上 | 制限付き（中央銀行研究向け） | — |
| e-MID Interbank Market | e-MID SIM S.p.A. | 欧州電子インターバンク預金市場 — 二者間取引 | 欧州の銀行 | 学術アクセス可能 | https://www.e-mid.it/ |
| CDS Data (DTCC TIW) | DTCC | クレジットデフォルトスワップ取引レベルデータ | グローバルCDS市場 | 制限付き | https://www.dtcc.com/ |

---

## 相関ネットワークのための市場データ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| CRSP | Center for Research in Security Prices (Wharton) | 1925年以降の米国株式価格、リターン、出来高（ヒストリカル） | 全米株式 | 学術（商用） | https://www.crsp.org/ |
| TAQ (Trade and Quote) | NYSE | 米国株式のティックバイティック取引・気配データ | ミリ秒精度 | 学術（商用） | https://www.nyse.com/market-data/historical |
| Yahoo Finance | Yahoo | 無料の日次/日中株価、ファンダメンタルズ | グローバル株式 | オープン | https://finance.yahoo.com/ |
| WRDS (Wharton Research Data Services) | Wharton / U Penn | 統合プラットフォーム: CRSP、Compustat、IBES、TAQ等 | マルチデータベース | 学術（サブスクリプション） | https://wrds-www.wharton.upenn.edu/ |
| Compustat | S&P Global (WRDS経由) | 米国/グローバル企業の財務諸表、貸借対照表、損益計算書 | 8万以上の企業 | 学術（商用） | https://www.spglobal.com/marketintelligence/ |
| Bloomberg Terminal Data | Bloomberg L.P. | 包括的な市場データ、ニュース、分析、企業データ | グローバル | 商用 | https://www.bloomberg.com/professional/ |
| Quandl / Nasdaq Data Link | Nasdaq | オルタナティブデータ、金融・経済データセット | 各種 | フリーミアム | https://data.nasdaq.com/ |
| Kenneth French Data Library | Dartmouth / Kenneth French | ファクターリターン（Fama-French）、業種別ポートフォリオ、ベンチマークデータ | 米国/グローバル株式 | オープン | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html |

---

## NLPおよびテキストデータ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| EDGAR Full-Text Filings | SEC | 全SEC開示書類の全文テキスト（10-K、10-Q、8-K等） | 数百万の書類 | オープン | https://www.sec.gov/edgar/searchedgar/efulltext.htm |
| EDGAR-CORPUS | Lancaster University / EMNLP | NLP研究用に前処理・クリーニング済みのEDGAR年次報告書 | 1万以上の年次報告書 | オープン | https://github.com/nlpaueb/edgar-corpus |
| FinancialPhraseBank | Malo et al. (Aalto University) | 金融ニュースからの文レベルセンチメントアノテーション | 4,846文 | オープン | https://huggingface.co/datasets/financial_phrasebank |
| FiQA (Financial Question Answering) | WWW 2018 Challenge | マイクロブログとヘッドラインからの金融オピニオンマイニング、質問応答、センチメント | 17,000以上の文 | オープン | https://sites.google.com/view/fiqa/ |
| TweetFinSent | — | Twitter/Xの投稿からの金融センチメント | 数千のツイート | オープン | https://huggingface.co/datasets/ |
| Reuters Financial News | Thomson Reuters | メタデータとカテゴリ付きの金融ニュース記事 | 1万以上の記事 | 学術 | — |
| SEntFiN | — | エンティティレベルの金融センチメントデータセット | 1万以上のアノテーション | オープン | https://github.com/ |
| FinSim | FinNLP Workshop | 金融用語の類似性と上位語検出の共有タスク | 数千の用語ペア | オープン | https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp/ |
| Financial Times Archive | Financial Times | 金融テキストマイニング用の過去のニュース記事 | 数十年分のカバレッジ | 商用 | https://www.ft.com/ |
| Loughran-McDonald Sentiment Word Lists | Notre Dame | 金融特化型センチメント辞書（ポジティブ、ネガティブ、不確実性等） | 約4,000語 | オープン | https://sraf.nd.edu/loughranmcdonald-master-dictionary/ |

---

## ブロックチェーンと暗号資産データ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| Elliptic Bitcoin Dataset | Elliptic / Kaggle | 不正取引検出のためのラベル付きビットコイントランザクショングラフ | 20万3千トランザクション、23万4千エッジ | オープン | https://www.kaggle.com/datasets/ellipticco/elliptic-data-set |
| Ethereum Blockchain (BigQuery) | Google Cloud | Ethereumブロックチェーン全体 — トランザクション、コントラクト、トークン転送 | ブロックチェーン全体 | オープン | https://cloud.google.com/blog/products/data-analytics/ethereum-bigquery-public-dataset |
| Bitcoin Blockchain | 各種 (Blockchair等) | ビットコイントランザクショングラフ全体およびUTXOセット | ブロックチェーン全体 | オープン | https://blockchair.com/ |
| Chainalysis Reactor Data | Chainalysis | コンプライアンス用のラベル付き暗号資産トランザクションデータ | マルチチェーン | 商用 | https://www.chainalysis.com/ |
| Token Terminal | Token Terminal | DeFiプロトコルの財務データ（TVL、収益、PER等） | 200以上のDeFiプロトコル | フリーミアム | https://tokenterminal.com/ |
| DeFi Llama | DeFi Llama | DeFi TVL、プロトコルデータ、クロスチェーン分析 | 2,000以上のプロトコル | オープン | https://defillama.com/ |

---

## 日本およびアジアの金融データ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| TSR（東京商工リサーチ）企業間取引データ | Tokyo Shoko Research（東京商工リサーチ） | 日本の企業間取引（売り手・買い手）ネットワーク | 約100万社、約400万取引リンク | 商用（学術アクセス可） | https://www.tsr-net.co.jp/ |
| TDB（帝国データバンク） | Teikoku Databank（帝国データバンク） | サプライチェーンおよび所有関係を含む日本の企業データ | 約150万社 | 商用（学術アクセス可） | https://www.tdb.co.jp/ |
| Nikkei NEEDS | Nikkei（日経） | 日本の財務諸表、株価、企業データ | 日本の全上場企業 | 学術（商用） | https://www.nikkei.co.jp/needs/ |
| EDINET | Financial Services Agency（金融庁） | XBRL形式の日本の企業開示書類（SEC EDGARに相当） | 日本の全上場企業 | オープン | https://disclosure.edinet-fsa.go.jp/ |
| JPX Market Data | Japan Exchange Group（日本取引所グループ） | 日本の株式取引データ、注文板、コーポレートアクション | 東証上場企業 | 商用 | https://www.jpx.co.jp/english/markets/statistics-equities/ |
| BOJ Flow of Funds | Bank of Japan（日本銀行） | 日本のセクター別資金循環勘定 — セクター間フロー | 日本経済 | オープン | https://www.boj.or.jp/en/statistics/sj/ |
| CSMAR | GTA（中国） | 中国の金融市場および企業データ | 中国の全上場企業 | 学術（商用） | https://www.gtarsc.com/ |
| WIND Information | Wind Info（中国） | 中国の金融端末データ、企業データ | 中国市場 | 商用 | https://www.wind.com.cn/ |

---

## 日本のコーポレート・ガバナンスデータ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| EDINET API（大量保有報告書） | 金融庁 | 5%以上保有の大量保有報告書（投資家→企業の保有関係）、XBRL形式 | 日本の全上場企業 | オープン（要登録） | https://disclosure.edinet-fsa.go.jp/ |
| EDINET API（臨時報告書） | 金融庁 | 株主総会議決結果（議案別賛否票数）、XBRL形式 | 日本の全上場企業 | オープン（要登録） | https://disclosure.edinet-fsa.go.jp/ |
| FSA スチュワードシップ・コード受入れ機関リスト | 金融庁 | SC受入れを表明した機関投資家一覧（投資信託、信託銀行、保険、年金等を分類） | 約350機関（2025年12月時点） | オープン | https://www.fsa.go.jp/en/refer/councils/stewardship/ |
| 議決権行使結果の個別開示 | 各機関投資家 | 各投資家が自社サイトで公表する議案別賛否データ | 各社ごとに異なる | オープン（分散、要スクレイピング） | — |
| JPX コーポレートガバナンス報告書 | 日本取引所グループ | 独立取締役比率、委員会設置状況等のガバナンス指標 | 東証上場企業 | ウェブ検索無料、CSV一括有料 | https://www.jpx.co.jp/equities/listing/cg/ |
| Nikkei NEEDS-Cges | 日経 | コーポレートガバナンス評価システム（取締役構成、報酬、株式保有等約150指標） | 約3,600社 | 商用（学術サブスクリプション） | https://www.nikkei.co.jp/needs/ |
| SakanaAI EDINET-Bench | SakanaAI | EDINET有価証券報告書からの質問応答ベンチマーク | オープンソース | オープン | https://huggingface.co/datasets/SakanaAI/EDINET-Bench |

---

## グラフおよびナレッジグラフのベンチマークデータセット

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| FinDKG | Cheng et al. (2024) | 時間的関係を持つニュースからの動的金融ナレッジグラフ | 14,000以上のエンティティ、時間的 | オープン | https://github.com/ |
| FNKG (Financial News Knowledge Graph) | 各種 | 金融ニュース記事から抽出されたナレッジグラフ | 数千のトリプル | オープン | — |
| Freebase (FB15k / FB15k-237) | Google / Meta | リンク予測のための一般的なナレッジグラフベンチマーク | 15,000エンティティ、592,000トリプル | オープン | https://www.microsoft.com/en-us/download/details.aspx?id=52312 |
| OGB (Open Graph Benchmark) | Stanford SNAP | ogbn-products、ogbn-arxivを含む標準化されたグラフ機械学習ベンチマーク | 各種規模 | オープン | https://ogb.stanford.edu/ |
| WikiKG90Mv2 | OGB / Wikidata | Wikidataからの大規模KGベンチマーク | 9,000万以上のエンティティ | オープン | https://ogb.stanford.edu/docs/lsc/wikikg90mv2/ |
| YAGO | Max Planck Institute | Wikipedia、WordNet、GeoNamesを統合した大規模ナレッジグラフ | 5,000万以上のファクト | オープン | https://yago-knowledge.org/ |
| DBpedia | DBpedia Association | Wikipediaから抽出された構造化データ | 数十億のトリプル | オープン | https://www.dbpedia.org/ |
| ConceptNet | MIT Media Lab | 常識知識グラフ | 2,100万以上のエッジ | オープン | https://conceptnet.io/ |
| FinKG | Ren et al. | 投資分析のための金融ナレッジグラフ | 数千のエンティティ | オープン | — |
| Temporal KG Benchmarks (ICEWS, GDELT) | 各種 | タイムスタンプ付きのイベントベース時間的ナレッジグラフ | 数百万のイベント | オープン | https://www.gdeltproject.org/ |

---

## その他およびオルタナティブデータ

| データセット | 提供元 | 説明 | 規模 | アクセス | URL |
|-------------|--------|------|------|----------|-----|
| World Input-Output Database (WIOD) | Groningen / EU | 各国間の産業を連結する国際産業連関表 | 43カ国、56セクター | オープン | https://www.rug.nl/ggdc/valuechain/wiod/ |
| OECD Inter-Country Input-Output (ICIO) | OECD | 二国間産業連関表 | 76経済圏、45産業 | オープン | https://www.oecd.org/sti/ind/inter-country-input-output-tables.htm |
| UN Comtrade | United Nations（国際連合） | 商品別・国別の国際貿易データ | 200カ国以上 | オープン | https://comtrade.un.org/ |
| Global Financial Development Database | World Bank（世界銀行） | 国別の金融システム特性 | 200カ国以上 | オープン | https://www.worldbank.org/en/publication/gfdr/data |
| EORA Global Supply Chain Database | University of Sydney | 多地域産業連関表 | 190カ国、26セクター | オープン | https://worldmrio.com/ |
| BoardEx | WRDS / Management Diagnostics | 経営幹部・取締役会メンバーの経歴データ、取締役兼任 | 100万以上の個人 | 学術（商用） | https://www.boardex.com/ |
| ISS (Institutional Shareholder Services) | ISS | コーポレートガバナンス格付け、議決権行使、取締役データ | グローバル企業 | 商用 | https://www.issgovernance.com/ |

---

*最終更新: 2026-03-01*
