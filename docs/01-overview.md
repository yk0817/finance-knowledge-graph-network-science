# 概要: 金融ネットワーク科学とナレッジグラフ

## 1. 金融ネットワーク科学の歴史

### 1.1 基礎の確立 (1990年代後半)

金融へのネットワーク科学の応用は、**Mantegna (1999)** に起源を遡る。彼はNYSEにおける株式リターンの相関関係から**最小全域木 (Minimum Spanning Tree, MST)** を構築した。この研究は、金融資産の階層的クラスタリングが経済的に意味のある分類体系を明らかにすることを示した。すなわち、価格の共変動からセクター構造が自然に浮かび上がったのである。Mantegnaのアプローチは統計物理学から直接手法を借用し、相関行列にグラフ理論的手法を適用したものであり、金融ネットワーク科学の創始的貢献として広く認められている。

同時期に、**Vandewalle, Brisbois & Trevisan (1998)** および **Bonanno, Lillo & Mantegna (2001)** が相関ベースのネットワーク分析を外国為替市場やより広範な資産クラスに拡張し、今日でも影響力を持つランダム行列理論 (Random Matrix Theory, RMT) とネットワークフィルタリングのパイプラインを確立した。

### 1.2 2000年代初頭: 伝染と複雑ネットワーク

2000年代初頭には、二つの並行した発展が見られた:

**金融伝染理論:**
- **Allen & Gale (2000)** は *Journal of Political Economy* に「Financial Contagion」を発表し、銀行間ネットワーク構造を通じて伝染が広がる最初の形式モデルを提供した。彼らは、ネットワークトポロジー -- 完全型か不完全型か -- がシステムの頑健性を決定することを示した。
- **Freixas, Parigi & Rochet (2000)** は銀行間決済システムにおけるシステミックリスクをモデル化した。
- **Eisenberg & Noe (2001)** は銀行間債務に対するクリアリング支払ベクトルフレームワークを導入し、ネットワーク化された金融システムにおける損失の計算を可能にした。

**経済学に適用された複雑ネットワーク理論:**
- **Caldarelli (2007)** およびその共同研究者は、スケールフリーネットワークモデルを金融システムに適用した。
- **Boss, Elsinger, Summer & Thurner (2004)** は、国家レベルの銀行間ネットワーク (オーストリア) の最初の実証的マッピングの一つを作成し、次数分布の裾の重さを明らかにした。
- **Iori, De Masi, Precup, Gabbi & Caldarelli (2008)** は、イタリアのオーバーナイト金融市場を複雑ネットワークとして分析した。

### 1.3 2008年金融危機: 転換点

2007年から2009年の世界金融危機 (Global Financial Crisis, GFC) は、金融ネットワーク科学にとって画期的な出来事であった。この危機は、デリバティブ、レポ市場、クロスホールディングスを通じた相互接続が、従来のリスクモデルでは全く捉えられなかった方法でショックを増幅・伝播しうることを白日の下に晒した。

**主要な知的対応:**

- **Andrew Haldaneの「Rethinking the Financial Network」講演 (2009)** は、Bank of England (イングランド銀行) において行われ、金融ネットワークと生態学的・疫学的ネットワークとの間に明示的な類似性を描いた。Haldaneは、規制当局がシステムの脆弱性を決定するネットワークトポロジーを無視しながら、個別金融機関のリスクに焦点を当ててきたと主張した。この講演は、ネットワークに基づく金融規制の結集点となった。

- **Haldane & May (2011)** は *Nature* に発表され、May (1972) の生態学的安定性の結果を銀行エコシステムに適用することでこの議論を形式化し、複雑性と接続性の増大が臨界閾値を超えると金融ネットワークを不安定化させうることを示した。

- **Basel III (バーゼルIII) とマクロプルーデンス規制** は、部分的にこのネットワーク認識的な思考から生まれた。**グローバルなシステム上重要な銀行 (Global Systemically Important Banks, G-SIBs)** の指定には、規模、複雑性、代替可能性に加えて、相互接続性の指標が明示的に組み込まれた。

- **Battiston, Puliga, Kaushik, Tasca & Caldarelli (2012)** は **DebtRank** を導入した。これはフィードバック中心性に着想を得た再帰的アルゴリズムであり、ネットワークを通じてディストレスを伝播させることで金融機関のシステム的重要性を測定する。DebtRankは、マクロプルーデンスネットワーク分析において最も広く採用されたツールの一つとなった。

- **Cont, Moussa & Santos (2013)** は、ブラジルの銀行システムにおける伝染についてシミュレーションに基づく詳細な研究を行い、信用伝染と資金調達伝染のチャネルを区別した。

### 1.4 2010年代: 拡張と成熟

危機後の10年間には、複数の次元にわたる研究の爆発的増加が見られた:

**銀行間ネットワークと決済ネットワーク:**
- TARGET2 (ECB)、Fedwire (Fed) およびその他の大口決済システムのネットワークトポロジー
- **Craig & von Peter (2014)**: 銀行間ネットワークの階層構造
- **in 't Veld & van Lelyveld (2014)**: 不完全なデータからの銀行間ネットワークの再構築

**生産ネットワークと貿易ネットワーク:**
- **Acemoglu, Carvalho, Ozdaglar & Tahbaz-Salehi (2012)**: マクロ経済変動のネットワーク的起源 -- 裾の重い産業連関ネットワークが固有ショックの分散化を妨げることを示した
- **Carvalho (2014)**: 生産ネットワークを通じたマクロ経済変動のミクロ的起源に関するサーベイ
- **Barrot & Sauvagnat (2016)**: サプライチェーンを通じた自然災害ショックの伝播

**理論的進展:**
- **Acemoglu, Ozdaglar & Tahbaz-Salehi (2015)**: *AER* 掲載の「Systemic Risk and Stability in Financial Networks」 -- 分散化 (密なネットワークが小さなショックを吸収) と伝染 (密なネットワークが大きなショックを増幅) の間の相転移を示した
- **Elliott, Golub & Jackson (2014)**: *AER* 掲載の「Financial Networks and Contagion」 -- クロスホールディングスと統合対分散化
- **Glasserman & Young (2016)**: 金融ネットワークにおける伝染とデフォルトカスケードの上界

**規制への導入:**
- 世界中の中央銀行がネットワークベースのストレステストツールを開発
- ECBのNATkit、OFR (Office of Financial Research) の金融安定モニター
- 監督枠組みへのネットワーク指標の統合

### 1.5 2020年代: ナレッジグラフ、GNN、LLM

現在の最前線では、現代のAIと金融ネットワーク分析が統合されている:

- **グラフニューラルネットワーク (Graph Neural Networks, GNNs)** の金融ネットワークへの適用: 信用リスク予測、不正検知、関係データを用いた株価変動予測 (Wang et al., 2021; Cheng et al., 2022)
- **ナレッジグラフ (Knowledge Graphs, KGs)** による金融規制、コンプライアンス、リスク分析
- **大規模言語モデル (Large Language Models, LLMs)** とKGsの組み合わせによる金融テキスト分析、イベント抽出、推論 (GraphRAGアプローチ)
- **FinDKG (Cheng, Xu & Farmer, 2024)**: マクロ金融予測のための金融ニュースからの動的ナレッジグラフ構築
- **時間的金融ネットワーク**: 動的コミュニティ検出を伴う時変トポロジー分析
- **気候-金融ネットワーク**: 金融ネットワークの伝達経路を通じた気候ストレステストに関するBattistonらの研究

---

## 2. 金融におけるナレッジグラフ

### 2.1 セマンティックウェブの起源

ナレッジグラフは、知識表現における数十年の研究の上に構築されている:

- **RDF (Resource Description Framework)**: 情報を主語-述語-目的語のトリプルとして表現するためのW3C標準。ナレッジグラフの基盤となるデータモデルを提供する。
- **OWL (Web Ontology Language)**: 形式的なオントロジー推論を可能にする。クラス階層、プロパティ制約、論理的推論を含む。
- **SPARQL**: RDFデータのためのクエリ言語であり、複雑なグラフパターンマッチングを可能にする。
- **元祖「ナレッジグラフ」**: Google (2012) がこの用語を普及させたが、基盤となる技術はセマンティックウェブ、記述論理、および初期のAI知識表現研究 (Cyc、WordNetなど) に由来する。

### 2.2 FIBOオントロジー

**Financial Industry Business Ontology (FIBO、金融業界ビジネスオントロジー)** は、**EDM Council** (現在はGLEIFのプログラム) によって開発された、金融分野で最も重要なドメインオントロジーである:

- 対象範囲: 金融商品、事業体、コーポレートアクション、インデックス、市場データ、ローン、デリバティブ
- OWL/RDF標準に基づいて構築され、形式的意味論を持つ
- 金融機関間および規制機関間の相互運用性を実現
- 規制当局 (例: OFR、GLEIF) がエンティティ識別とデータ調和のために採用
- 業界ワーキンググループにより継続的に維持・拡張

### 2.3 業界での採用

| 組織 | KGの適用分野 | 規模・備考 |
|---|---|---|
| **Bloomberg** | 企業、人物、証券、イベントを結ぶエンタープライズKG | 数十億のトリプル。Bloomberg Terminal分析を支える |
| **Refinitiv (LSEG)** | Permidエンティティグラフ、ニュースからの関係抽出 | 金融エンティティ向けオープン識別子 |
| **JPMorgan** | 規制コンプライアンス、AML (マネーロンダリング対策) のための社内KG | 取引データとエンティティ関係を接続 |
| **Goldman Sachs** | 市場インテリジェンスと調査のためのKG | 金融データとオルタナティブデータソースを連携 |
| **Moody's Analytics** | Orbis企業ネットワーク、所有連鎖 | 約4億件の企業レコードと実質的所有者情報 |
| **IHS Markit (S&P Global)** | サプライチェーンと企業階層のマッピング | サプライチェーンリスク分析に使用 |
| **中央銀行** | GLEIF LEIグラフ、規制報告KG | エンティティ識別とシステミックリスクマッピング |

### 2.4 金融NLPからKG構築へのパイプライン

テキストから金融ナレッジグラフを構築する典型的なパイプライン:

1. **コーパス収集**: 金融ニュース (Reuters、Bloomberg)、SEC提出書類 (10-K、10-Q、8-K)、決算説明会のトランスクリプト、アナリストレポート、中央銀行のコミュニケーション
2. **固有表現認識 (Named Entity Recognition, NER)**: 金融エンティティの識別 -- 企業、人物、金融商品、金額、日付 (FinBERT、ドメイン適応NERモデル)
3. **関係抽出 (Relation Extraction, RE)**: 関係の抽出 -- 買収、パートナーシップ、供給関係、役員人事 (教師あり学習および遠距離教師あり学習アプローチ)
4. **エンティティリンキング / 解決**: 抽出されたエンティティを正規識別子 (LEI、ISIN、CUSIP、Permid) にマッピング
5. **ナレッジグラフ構築**: 抽出されたトリプルをRDF/プロパティグラフストアに格納
6. **時間的エンリッチメント**: タイムスタンプ、有効期間、来歴メタデータの付加
7. **推論と推論**: オントロジー規則を適用して暗黙的知識を導出

**主要な研究:**
- **Ding, Zhang, Liu & Duan (2019)**: 金融テキストからのナレッジグラフ構築
- **Chen, Wei & Huang (2018)**: FinKG -- SEC提出書類からの金融ナレッジグラフ
- **Cheng, Xu & Farmer (2024)**: FinDKG -- 時間的リンク予測を伴う金融ニュースからの動的KG

### 2.5 最近の進展: GraphRAGとLLMの統合

- **GraphRAG (Microsoft Research, 2024)**: 大規模文書コレクションに対する構造化推論のために、ナレッジグラフと検索拡張生成 (Retrieval-Augmented Generation) を組み合わせる
- **KGで強化された金融LLM**: ナレッジグラフを用いてLLMの出力を根拠づけ、ハルシネーションを低減し、構造化された金融推論を可能にする
- **LLMによる自動KG構築**: GPT-4、Claudeなどのモデルを用いたゼロショット関係抽出とオントロジー学習
- **マルチモーダル金融KG**: 構造化データ (財務諸表)、非構造化テキスト、時系列市場データを統合的なグラフ表現に統合

---

## 3. 経済学とコンピュータサイエンスの交差点

### 3.1 方法論的伝統

| 次元 | 経済学 | コンピュータサイエンス |
|---|---|---|
| **認識論** | 理論駆動型、演繹的 | データ駆動型、帰納的 |
| **因果性** | 因果識別 (IV、RDD、DiD) | 予測重視、相関ベース |
| **モデル** | 均衡モデル、最適化 | 機械学習、スケーラブルなアルゴリズム |
| **エージェント** | 代表的個人 / ミクロ的基礎づけを持つ異質的エージェント | ネットワーク上のノード、MLの特徴量 |
| **検証** | 計量経済学的仮説検定 | 訓練/テスト分割、ベンチマーク |
| **データ** | パネルデータ、国民経済計算、調査 | ウェブスケールデータ、オルタナティブデータ |
| **出版** | トップ5ジャーナル、長い査読期間 | 学会論文 (NeurIPS、ICML、KDD)、短いサイクル |

### 3.2 収斂する領域

**経済予測のためのグラフニューラルネットワーク:**
- サプライチェーンネットワークへのGNN適用によるマクロ予測 (Brintrup et al., 2020)
- 企業関係グラフを用いた株価予測 (Feng et al., 2019)
- 借り手-貸し手ネットワーク特徴量による信用リスク評価 (Wang et al., 2021)

**金融規制のためのナレッジグラフ:**
- オントロジー推論による規制コンプライアンスチェック
- エンティティ解決とグラフ分析によるマネーロンダリング対策
- 税の透明性のための実質的所有者ネットワーク (例: OpenCorporates、GLEIF)

**経済テキストのためのNLP:**
- 中央銀行コミュニケーション分析 (Hansen & McMahon, 2016; Shapiro et al., 2022)
- 経済センチメントと不確実性の測定 (Baker, Bloom & Davis, 2016)
- 決算説明会からのサプライチェーン関係の抽出 (Barrot & Sauvagnat, 2016)

**エージェントベース計算経済学:**
- 金融市場のマルチエージェントシミュレーション (Farmer & Foley, 2009)
- ABMとネットワークトポロジーの組み合わせ (Thurner, Farmer & Geanakoplos, 2012)
- 経済環境における強化学習エージェント

### 3.3 相補性と緊張関係

**経済学がCSを強化する点:**
- 因果推論と識別戦略が、MLにおける見せかけの予測を防止する
- 均衡的思考がモデルに構造的制約を提供する
- 厚生分析とメカニズムデザインが規範的枠組みを提供する
- ドメイン知識が金融MLにおける「ゴミを入れればゴミが出る」問題を防止する

**CSが経済学を強化する点:**
- 大規模ネットワーク分析のためのスケーラブルな計算
- 複雑なパターンを捉える柔軟なノンパラメトリックモデル
- 膨大な制度的知識を整理するための知識表現
- 非構造化経済テキストからの大規模なNLPおよび情報抽出

**継続する緊張関係:**
- 解釈可能性 vs. 予測力
- 構造モデル vs. 誘導形ML
- 因果推論 vs. パターン認識
- 小標本の計量経済学的厳密性 vs. 大規模データマイニング
- 出版文化とインセンティブの違い

### 3.4 生まれつつある統合

いくつかの分野で生産的な統合が生まれつつある:

- **因果的ML**: MLの柔軟性と計量経済学的因果識別の組み合わせ (Athey & Imbens, 2019; Chernozhukov et al., 2018)
- **構造推定 + ML**: 構造的経済モデル内での推定にMLを活用
- **ネットワーク計量経済学**: ネットワークデータに対する厳密な統計的推論 (de Paula, 2017; Graham, 2017)
- **経済学に基づくGNN**: 経済理論 (均衡、無裁定) を帰納的バイアスとしてグラフニューラルネットワークに組み込む
- **経済エージェントとしてのLLM**: 言語モデルによる経済行動のシミュレーション (Horton, 2023)

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
