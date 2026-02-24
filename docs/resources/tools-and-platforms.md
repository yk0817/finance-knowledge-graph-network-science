# 金融ネットワーク分析とナレッジグラフのためのツールとプラットフォーム

本文書は、金融ネットワークおよびナレッジグラフの構築・分析のためのソフトウェアツール、ライブラリ、プラットフォーム、サービスをまとめたものである。

---

## グラフデータベース

| ツール | 種類 | 説明 | ライセンス | URL |
|--------|------|------|-----------|-----|
| Neo4j | ネイティブグラフデータベース（ラベル付きプロパティグラフ） | 最も普及しているグラフデータベース; Cypherクエリ言語; ACID準拠; 充実したエコシステム（APOC、GDSライブラリ） | Community (GPLv3) / Enterprise (商用) | https://neo4j.com/ |
| TigerGraph | ネイティブ並列グラフデータベース | 高性能分散グラフ分析; GSQLクエリ言語; リアルタイム深層リンク分析 | 商用（無料枠あり） | https://www.tigergraph.com/ |
| Amazon Neptune | マネージドグラフデータベース (AWS) | プロパティグラフ（Gremlin/openCypher）とRDF（SPARQL）の両方をサポート; サーバーレスオプション | 商用 (AWS) | https://aws.amazon.com/neptune/ |
| ArangoDB | マルチモデル（ドキュメント、グラフ、キーバリュー） | ネイティブグラフ＋ドキュメントストア; AQLクエリ言語; Pregelベースのグラフ分析 | Apache 2.0 / 商用 | https://www.arangodb.com/ |
| JanusGraph | 分散グラフデータベース | 複数バックエンドに対応（Cassandra、HBase、BerkeleyDB）; Gremlin/TinkerPop互換 | Apache 2.0 | https://janusgraph.org/ |
| Dgraph | ネイティブ分散グラフデータベース | GraphQLネイティブ; 水平スケーリング; ACIDトランザクション | Apache 2.0 / 商用 | https://dgraph.io/ |
| Stardog | エンタープライズナレッジグラフプラットフォーム | 推論機能付きRDF/OWLトリプルストア; SPARQL + GraphQL; 仮想グラフフェデレーション | 商用 | https://www.stardog.com/ |
| Ontotext GraphDB | 推論機能付きRDFトリプルストア | OWL 2推論; SPARQL 1.1; セマンティック推論; SHACLバリデーション | 商用（無料版あり） | https://www.ontotext.com/products/graphdb/ |
| Ultipa | リアルタイムグラフデータベース | 高性能並列グラフ走査; HDFSライクな分散アーキテクチャ | 商用 | https://www.ultipa.com/ |
| Memgraph | インメモリグラフデータベース | Cypher互換; ストリーミンググラフ分析; Kafka統合 | BSL / Community（無料） | https://memgraph.com/ |
| NebulaGraph | 分散グラフデータベース | 水平スケーリング; nGQLクエリ言語; 超大規模グラフ向け設計 | Apache 2.0 | https://www.nebula-graph.io/ |

---

## グラフ分析ライブラリ

| ツール | 言語 | 説明 | ライセンス | URL |
|--------|------|------|-----------|-----|
| NetworkX | Python | Pythonにおけるネットワーク分析のデファクトスタンダード; 豊富なアルゴリズムライブラリ; 使いやすい | BSD | https://networkx.org/ |
| igraph | R / Python / C | 高性能ネットワーク分析; 高速なコミュニティ検出、中心性計算、可視化 | GPL-2.0 | https://igraph.org/ |
| graph-tool | Python (C++コア) | ベイズ推論を備えた高性能ネットワーク分析; 確率的ブロックモデル | LGPL-3.0 | https://graph-tool.skewed.de/ |
| SNAP | C++ / Python | Stanford大規模ネットワーク分析; 数十億エッジ対応; PageRank、モチーフ、コミュニティ | BSD | https://snap.stanford.edu/snap/ |
| DGL (Deep Graph Library) | Python (PyTorch/TensorFlow) | GNNのための柔軟なフレームワーク; メッセージパッシング; 異種グラフ | Apache 2.0 | https://www.dgl.ai/ |
| PyG (PyTorch Geometric) | Python (PyTorch) | GNNライブラリ; 豊富なモデルリポジトリ; ミニバッチ学習; 異種グラフ | MIT | https://pyg.org/ |
| StellarGraph | Python (TensorFlow/Keras) | ノード/エッジ/グラフタスク用GNN; GraphSAGE、GAT、GCN実装 | Apache 2.0 | https://stellargraph.readthedocs.io/ |
| cuGraph (NVIDIA RAPIDS) | Python (CUDA) | GPU加速グラフ分析; GPU上でのPageRank、BFS、Louvain | Apache 2.0 | https://github.com/rapidsai/cugraph |
| Networkit | Python (C++コア) | 大規模ネットワーク分析; 並列アルゴリズム; コミュニティ検出 | MIT | https://networkit.github.io/ |
| GraphFrames | Python/Scala (Apache Spark) | Spark上の分散グラフ処理; モチーフ検索; 連結成分 | Apache 2.0 | https://graphframes.github.io/graphframes/ |
| Tulip | C++ / Python | 大規模グラフ可視化・分析フレームワーク | LGPL | https://tulip.labri.fr/ |
| PowerGraph (GraphLab) | C++ | 分散グラフ計算; 頂点カット分割 | Apache 2.0 | https://github.com/jegonzal/PowerGraph |

---

## ナレッジグラフ構築・管理ツール

| ツール | 種類 | 説明 | ライセンス | URL |
|--------|------|------|-----------|-----|
| Protégé | オントロジーエディタ | StanfordのOWL/RDFオントロジーエディタ; 視覚的クラス階層; プラグインエコシステム | BSD-2-Clause | https://protege.stanford.edu/ |
| Apache Jena | RDFフレームワーク (Java) | RDF/SPARQLフレームワーク; TDBトリプルストア; Fuseki SPARQLサーバー; OWL推論 | Apache 2.0 | https://jena.apache.org/ |
| RDFLib | RDFライブラリ (Python) | PythonでのRDF操作; SPARQLクエリ; シリアライゼーション（Turtle、JSON-LD、N-Triples） | BSD | https://rdflib.readthedocs.io/ |
| Owlready2 | オントロジーライブラリ (Python) | PythonでOWLオントロジーのロード/修正; HermiT推論; SPARQLクエリ | LGPL-3.0 | https://owlready2.readthedocs.io/ |
| PyKEEN | KG埋め込みライブラリ (Python) | ナレッジグラフ埋め込みモデル（TransE、RotatE、ConvE等）; ハイパーパラメータ探索 | MIT | https://pykeen.readthedocs.io/ |
| AmpliGraph | KG埋め込みライブラリ (Python) | ナレッジグラフ埋め込み; リンク予測; モデル評価 | Apache 2.0 | https://docs.ampligraph.org/ |
| OpenKE | KG埋め込みフレームワーク | オープンソースKG埋め込みツールキット; 効率的なC++バックエンドとPythonインターフェース | MIT | https://github.com/thunlp/OpenKE |
| spaCy + REL | 固有表現認識 + エンティティリンキング | ナレッジベースへのエンティティリンキング機能付き固有表現認識 | MIT | https://spacy.io/ |
| DeepKE | 知識抽出 (Python) | 少リソースでのナレッジグラフ構築; NER、関係抽出、属性抽出 | MIT | https://github.com/zjunlp/DeepKE |
| OpenIE / Stanford KG | 情報抽出 | テキストからのトリプル生成のためのオープン情報抽出 | Apache 2.0 | https://stanfordnlp.github.io/CoreNLP/ |

---

## 金融NLPツール

| ツール | 種類 | 説明 | ライセンス | URL |
|--------|------|------|-----------|-----|
| FinBERT | 事前学習済み言語モデル | 金融テキストでファインチューニングされたBERT; センチメント分析; 金融固有表現認識 | Apache 2.0 | https://github.com/ProsusAI/finBERT |
| BloombergGPT | 大規模言語モデル | Bloombergの金融データで学習された500億パラメータのLLM; 金融NLPタスク | 商用 (Bloomberg) | — |
| FinGPT | オープンソース金融LLM | 金融LLMのためのオープンフレームワーク; 金融データによるRLHF | MIT | https://github.com/AI4Finance-Foundation/FinGPT |
| spaCy（金融パイプライン） | NLPライブラリ (Python) | 産業グレードのNLP; カスタム金融NERモデル; 高速トークナイゼーション | MIT | https://spacy.io/ |
| Stanza | NLPライブラリ (Python) | Stanford NLPツールキット; 多言語対応; バイオメディカル/金融モデル | Apache 2.0 | https://stanfordnlp.github.io/stanza/ |
| AllenNLP | NLPフレームワーク (Python) | 深層学習NLPフレームワーク; 意味役割付与; 共参照解析 | Apache 2.0 | https://allennlp.org/ |
| FinRL | 金融のための深層強化学習 (Python) | 定量ファイナンスのための強化学習ライブラリ | MIT | https://github.com/AI4Finance-Foundation/FinRL |
| Hugging Face Transformers | モデルハブ/フレームワーク | FinBERT、金融GPTモデルへのアクセスとファインチューニングパイプライン | Apache 2.0 | https://huggingface.co/ |
| SEC-API | SEC開示書類パーサー | 全文検索機能付きSEC EDGAR開示書類へのプログラマティックアクセス | フリーミアム | https://sec-api.io/ |

---

## 可視化ツール

| ツール | 種類 | 説明 | ライセンス | URL |
|--------|------|------|-----------|-----|
| Gephi | デスクトップアプリケーション | オープンソースのネットワーク可視化・探索ツール; ForceAtlas2レイアウト; 大規模グラフ対応 | GPL-3.0 / CDDL | https://gephi.org/ |
| Cytoscape | デスクトップアプリケーション | 元々は生物学向けのネットワーク可視化; 豊富なプラグインエコシステム; 大規模グラフ対応 | LGPL-2.1 | https://cytoscape.org/ |
| D3.js | JavaScriptライブラリ | 低レベルデータ可視化; 力学的レイアウト; 高度にカスタマイズ可能 | ISC | https://d3js.org/ |
| vis.js (vis-network) | JavaScriptライブラリ | インタラクティブなネットワーク可視化; 物理ベースレイアウト; ブラウザベース | Apache 2.0 / MIT | https://visjs.org/ |
| Sigma.js | JavaScriptライブラリ | 大規模グラフ向けウェブベースグラフ可視化; WebGLレンダリング | MIT | https://www.sigmajs.org/ |
| Linkurious | 商用プラットフォーム | グラフ可視化・調査プラットフォーム; Neo4j/Cosmos統合 | 商用 | https://linkurious.com/ |
| Graphistry | 商用プラットフォーム | GPU加速ビジュアルグラフ分析; 大規模探索 | 商用（無料枠あり） | https://www.graphistry.com/ |
| yFiles | 商用ライブラリ | プロフェッショナルグラフ可視化SDK（Java、JS、.NET）; 自動レイアウト | 商用 | https://www.yworks.com/products/yfiles |
| Plotly/Dash + NetworkX | Pythonフレームワーク | Plotly + Pythonを使用したインタラクティブなウェブベースネットワーク可視化 | MIT | https://plotly.com/ |
| Pyvis | Pythonライブラリ | Jupyterでのインタラクティブなネットワーク可視化; vis.jsラッパー | BSD | https://pyvis.readthedocs.io/ |
| Cosmograph | JavaScriptライブラリ | GPU駆動の大規模グラフ可視化 (WebGL) | — | https://cosmograph.app/ |
| Flourish | ウェブプラットフォーム | ノーコードインタラクティブデータ可視化; ネットワーク図テンプレート | フリーミアム | https://flourish.studio/ |

---

## 商用金融プラットフォーム

| プラットフォーム | 提供元 | 説明 | 主な機能 | URL |
|-----------------|--------|------|----------|-----|
| Refinitiv Workspace | LSEG (London Stock Exchange Group) | 金融データ端末; 企業関係; 所有データ | 企業ツリー、サプライチェーン、所有ネットワーク | https://www.refinitiv.com/ |
| Bloomberg Terminal | Bloomberg L.P. | 包括的な金融データ; SPLC（サプライチェーン）; OWNS（所有構造） | サプライチェーンマップ、所有構造分析、企業構造 | https://www.bloomberg.com/professional/ |
| Sayari | Sayari | サプライチェーンおよびリスク分析のための貿易・企業記録 | 実質的所有者、貿易ネットワーク、エンティティ解決 | https://sayari.com/ |
| Palantir Foundry | Palantir Technologies | データ統合・分析プラットフォーム; グラフベースの調査 | エンティティ解決、リンク分析、金融犯罪検出 | https://www.palantir.com/ |
| Chainalysis | Chainalysis | ブロックチェーン分析・調査プラットフォーム | 暗号資産トランザクション追跡、コンプライアンス、ネットワーク可視化 | https://www.chainalysis.com/ |
| Elliptic | Elliptic | 暗号資産コンプライアンス・リスク管理 | トランザクションスコアリング、ウォレットスクリーニング、ネットワーク分析 | https://www.elliptic.co/ |
| GraphAware Hume | GraphAware (現Neo4j) | NLPとグラフ分析を備えたナレッジグラフプラットフォーム | エンティティ抽出、関係発見、知識管理 | https://graphaware.com/hume/ |
| Diffbot | Diffbot | AI駆動のウェブスクレイピングとナレッジグラフ構築 | 200億以上のエンティティナレッジグラフ; ウェブからの関係抽出 | https://www.diffbot.com/ |
| Moody's Analytics / RiskCalc | Moody's | 信用リスクおよび金融ネットワーク分析 | インターバンクエクスポージャー、カウンターパーティリスク、ネットワークストレステスト | https://www.moodysanalytics.com/ |
| FactSet | FactSet Research Systems | 金融データ、分析、サプライチェーン関係 | サプライチェーンマッピング、所有データ、エンティティ関係 | https://www.factset.com/ |
| S&P Capital IQ Pro | S&P Global | 企業関係データ付き金融データプラットフォーム | 企業階層、主要関係、サプライチェーンインテリジェンス | https://www.spglobal.com/marketintelligence/ |

---

## クラウドグラフサービス

| サービス | 提供元 | 説明 | グラフモデル | URL |
|----------|--------|------|-------------|-----|
| Amazon Neptune | AWS | マネージドグラフデータベースサービス; サーバーレスオプション | プロパティグラフ (Gremlin/openCypher) + RDF (SPARQL) | https://aws.amazon.com/neptune/ |
| Amazon Neptune Analytics | AWS | ベクトル検索を備えたグラフ分析; GNNベース予測のためのNeptune ML | プロパティグラフ + ML | https://aws.amazon.com/neptune/neptune-analytics/ |
| Google Cloud Knowledge Graph / Spanner | Google Cloud | エンタープライズナレッジグラフと分散グラフデータベース機能 | マルチモデル | https://cloud.google.com/spanner |
| Azure Cosmos DB (Gremlin API) | Microsoft Azure | グラフAPIを備えたグローバル分散マルチモデルデータベース | プロパティグラフ (Gremlin) | https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/ |
| Databricks (GraphFrames) | Databricks | Spark上の分散グラフ処理; Lakehouseアーキテクチャ | GraphFrames (Spark) | https://docs.databricks.com/ |
| Neo4j AuraDB | Neo4j | フルマネージドクラウドNeo4j; サービスとしてのグラフデータサイエンス | ラベル付きプロパティグラフ (Cypher) | https://neo4j.com/cloud/aura/ |
| TigerGraph Cloud | TigerGraph | MLワークベンチ付きマネージドTigerGraphインスタンス | プロパティグラフ (GSQL) | https://www.tigergraph.com/cloud/ |

---

## 開発・統合ツール

| ツール | 種類 | 説明 | ライセンス | URL |
|--------|------|------|-----------|-----|
| Apache Kafka + Graph Sink | ストリーム処理 | ストリーミング金融データからのリアルタイムグラフ構築 | Apache 2.0 | https://kafka.apache.org/ |
| Apache Airflow | ワークフローオーケストレーション | 金融データパイプラインDAGのスケジューリングと監視 | Apache 2.0 | https://airflow.apache.org/ |
| dbt | データ変換 | グラフ特徴量エンジニアリングのためのSQLベース変換 | Apache 2.0 | https://www.getdbt.com/ |
| LangChain（グラフモジュール） | LLMフレームワーク | LLM駆動のナレッジグラフ構築・クエリ | MIT | https://www.langchain.com/ |
| LlamaIndex (Knowledge Graph) | LLMフレームワーク | KG強化型検索; グラフストア; 構造化クエリ | MIT | https://www.llamaindex.ai/ |
| Jupyter + Graph Extensions | ノートブック環境 | yFiles、nxviz、pyvis統合によるインタラクティブなグラフ分析 | BSD | https://jupyter.org/ |

---

*最終更新: 2026-02-23*
