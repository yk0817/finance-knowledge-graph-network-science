# 金融ナレッジグラフのためのオントロジーと標準規格

本文書は、金融ナレッジグラフの構築とクエリに関連するオントロジー、データ標準、表現フレームワークをまとめたものである。

---

## Financial Industry Business Ontology (FIBO)（金融業界ビジネスオントロジー）

### 概要

| 項目 | 詳細 |
|------|------|
| **正式名称** | Financial Industry Business Ontology |
| **管理主体** | EDM Council / Object Management Group (OMG) |
| **形式** | OWL 2 / RDF |
| **ライセンス** | MIT License（オープンソース） |
| **URL** | https://spec.edmcouncil.org/fibo/ |
| **GitHub** | https://github.com/edmcouncil/fibo |

### 説明

FIBOは金融業界のための最も包括的な形式オントロジーである。金融概念、商品、エンティティ、および関係の機械可読な定義を提供する。金融機関、規制当局、テクノロジー企業がEDM CouncilおよびOMGのガバナンスの下で共同開発している。

### FIBOモジュール構造

| モジュール | 対象範囲 | 主要クラス |
|-----------|---------|-----------|
| **Foundations (FND)** | 基本概念: 当事者、日付、関係、数量、契約 | Party, Agent, LegalEntity, Date, Agreement |
| **Business Entities (BE)** | 法人、会社、パートナーシップ、信託、政府機関 | CorporateBody, LegalPerson, Partnership, GovernmentBody |
| **Financial Business and Commerce (FBC)** | 金融サービス、商品、規制機関 | FinancialServiceProvider, RegulatoryAgency, FinancialProduct |
| **Securities (SEC)** | 株式、債券、ファンド、デリバティブ | Security, Equity, Bond, DerivativeInstrument, Fund |
| **Derivatives (DER)** | OTCおよび取引所取引デリバティブ、スワップ、オプション、先物 | Swap, Option, Future, CreditDefaultSwap |
| **Loans (LOAN)** | ローン種類、住宅ローン商品、学資ローン | Loan, Mortgage, RevolvingCredit |
| **Indices and Indicators (IND)** | 市場指数、経済指標、金利 | MarketIndex, EconomicIndicator, InterestRateBenchmark |
| **Market Data (MD)** | 価格、気配値、取引データ | Price, Quote, Trade |
| **Corporate Actions (CAE)** | 配当、合併、株式分割 | CorporateAction, Dividend, Merger |

### 法人モジュール（詳細）

所有ナレッジグラフに特に関連する部分:

| 概念 | 説明 | 関係 |
|------|------|------|
| LegalEntity | 法律で認められた全てのエンティティ | hasRegistrationDate, isRegisteredIn |
| CorporateBody | 法人化された組織 | hasDirector, hasShareholder |
| OwnershipInterest | エンティティへの持分 | hasPercentage, isHeldBy |
| ControllingInterest | 支配閾値を超える所有 | controlsEntity |
| BeneficialOwner | 最終的に所有/支配する人物 | ultimatelyOwns, beneficiallyControls |
| RegisteredAgent | エンティティのために行動する権限を持つ代理人 | actsFor, isRegisteredIn |

### 採用と統合

- 主要な銀行、規制当局、データベンダーがセマンティックインターオペラビリティのために使用
- ISO標準（ISO 20022、LEI）との整合
- OWLオントロジーファイル、SKOS語彙、JSON-LDコンテキストとして利用可能
- GLEIF LEIデータおよび規制報告フレームワークとの統合

---

## Beneficial Ownership Data Standard (BODS)（実質的所有者データ標準）

### 概要

| 項目 | 詳細 |
|------|------|
| **正式名称** | Beneficial Ownership Data Standard |
| **管理主体** | Open Ownership |
| **形式** | JSON Schema |
| **バージョン** | 0.4（最新） |
| **ライセンス** | Apache 2.0 |
| **URL** | https://standard.openownership.org/ |

### 説明

BODSは実質的所有者情報を公開するための構造化フォーマットを提供する。各国の実質的所有者登録簿間の相互運用性を実現し、所有ナレッジグラフの構築を支援する。

### ステートメントタイプ

| ステートメントタイプ | 目的 | 主要フィールド |
|---------------------|------|---------------|
| **Entity Statement** | 法人の記述 | entityType, name, jurisdiction, identifiers, foundingDate |
| **Person Statement** | 自然人の記述 | personType, names, nationalities, birthDate, addresses |
| **Ownership-or-Control Statement** | 所有チェーンにおける人物/法人の連結 | subject, interestedParty, interests (shareholding, voting rights, control) |

### 利益タイプ

| 利益タイプ | 説明 |
|-----------|------|
| shareholding | 直接または間接的な持株比率 |
| votingRights | 議決権比率 |
| appointmentOfBoard | 取締役の任命/解任権 |
| otherInfluenceOrControl | その他の重要な支配形態 |
| seniorManagingOfficial | 上級管理職の地位 |
| settlor | 信託の委託者 |
| trustee | 信託の受託者 |
| beneficiaryOfLegalArrangement | 信託またはそれに類する制度の受益者 |

### 採用状況

- 英国（PSC Register）、スロバキア、アルメニア、ラトビア等で使用
- OpenOwnership Registerが複数国のデータを集約
- 実質的所有者の透明性イニシアチブ（EITI、FATF）を支援

---

## FinRegOnt（金融規制オントロジー）

### 概要

| 項目 | 詳細 |
|------|------|
| **正式名称** | Financial Regulation Ontology |
| **目的** | 金融規制の機械可読な表現 |
| **形式** | OWL 2 |
| **対象範囲** | 規制要件、コンプライアンス規則、規制機関 |

### 説明

FinRegOntは金融規制要件を機械可読な形式で表現することを目的とし、自動コンプライアンスチェックと規制分析を可能にする。複数の法域と規制機関の規制をカバーしている。

### 主要概念

| 概念 | 説明 |
|------|------|
| Regulation | 規制文書または規則 |
| RegulatoryBody | 規制を発行するエンティティ（SEC、FCA、ECB等） |
| Requirement | 特定の義務または禁止 |
| RegulatedEntity | 規制対象のエンティティ |
| ComplianceObligation | 特定のコンプライアンス要件 |
| ReportingRequirement | 法定報告義務 |
| Threshold | 定量的な規制閾値 |

---

## 金融業界標準

| 標準 | 正式名称 | 対象範囲 | 管理主体 | 形式 | URL |
|------|----------|---------|----------|------|-----|
| LEI | Legal Entity Identifier | 金融取引における法人の一意識別 | GLEIF (Global LEI Foundation) | ISO 17442; 20文字英数字 | https://www.gleif.org/ |
| XBRL | eXtensible Business Reporting Language | 構造化された財務報告; 財務諸表のタクソノミー | XBRL International | XMLベース | https://www.xbrl.org/ |
| FpML | Financial products Markup Language | OTCデリバティブ取引の記述 | ISDA | XML Schema | https://www.fpml.org/ |
| FIX Protocol | Financial Information eXchange | 電子取引メッセージ; 注文フロー | FIX Trading Community | Tag-value / FIXML | https://www.fixtrading.org/ |
| ISO 20022 | Universal financial industry message scheme | 決済、証券、貿易金融、FXメッセージング | ISO TC68 | XML / ASN.1 | https://www.iso20022.org/ |
| ISDA CDM | Common Domain Model | デリバティブと証券の標準化されたライフサイクルイベント | ISDA | JSON / Java / Rosetta DSL | https://www.isda.org/2019/10/14/isda-common-domain-model/ |
| ISO 10962 (CFI) | Classification of Financial Instruments | 金融商品分類コード | ISO | 6文字コード | https://www.iso.org/ |
| ISO 6166 (ISIN) | International Securities Identification Number | 証券の一意識別 | ANNA (Association of National Numbering Agencies) | 12文字英数字 | https://www.anna-web.org/ |
| ISO 4217 | Currency Codes | 標準化された通貨識別子 | ISO | 3文字アルファ / 3桁数字 | https://www.iso.org/ |
| FIGI | Financial Instrument Global Identifier | 金融商品識別のためのオープン標準 | OMG / Bloomberg | 12文字英数字 | https://www.openfigi.com/ |
| MiFID II RTS 25 | Regulatory Technical Standards | 金融商品リファレンスデータ | ESMA | XML | https://www.esma.europa.eu/ |
| GLEIF Relationship Records | LEI-to-LEI relationship data | 直接/最終親会社、ファンド関係 | GLEIF | XML / CSV | https://www.gleif.org/en/lei-data/lei-mapping |

---

## 知識表現標準

### コアセマンティックウェブ標準

| 標準 | 正式名称 | 目的 | W3Cステータス | 金融KGへの関連性 |
|------|----------|------|-------------|-----------------|
| RDF | Resource Description Framework | トリプル（主語-述語-目的語）として知識を表現するための基盤 | W3C勧告 | 金融エンティティの関係、所有チェーンのコア表現 |
| OWL | Web Ontology Language | クラス、プロパティ、制約、推論を備えた豊富なオントロジーモデリング | W3C勧告 | FIBOはOWL 2で記述; 金融データ上の推論を可能にする |
| RDFS | RDF Schema | 軽量オントロジー言語; クラス/プロパティ階層 | W3C勧告 | 金融エンティティ型階層のためのシンプルなスキーマ |
| SPARQL | SPARQL Protocol and RDF Query Language | RDFグラフのためのクエリ言語 | W3C勧告 | 金融KGへのクエリ; データソース間のフェデレーテッドクエリ |
| SKOS | Simple Knowledge Organization System | 分類体系、シソーラス、統制語彙 | W3C勧告 | 金融用語分類体系; 産業分類スキーム |
| SHACL | Shapes Constraint Language | RDFグラフのデータ検証; シェイプ制約 | W3C勧告 | 金融KGデータ品質の検証; 所有データ制約の強制 |
| JSON-LD | JSON for Linking Data | リンクトデータ/RDFのJSONベースシリアライゼーション | W3C勧告 | APIフレンドリーな金融KGアクセス; ウェブページへの構造化データ埋め込み |
| RDF-star | RDF-star (RDF 1.2候補) | ステートメントレベルのメタデータ（レイフィケーション） | W3Cドラフト | 金融関係への信頼度、時間的有効性の注釈付け |

### シリアライゼーション形式

| 形式 | 説明 | 用途 |
|------|------|------|
| Turtle (.ttl) | 人間可読なRDFシリアライゼーション | 金融オントロジーの作成とレビュー |
| N-Triples (.nt) | 行ベースのRDFシリアライゼーション | 金融KGデータの一括ロード |
| JSON-LD (.jsonld) | JSONベースのRDFシリアライゼーション | 金融KGアクセスのためのWeb API |
| RDF/XML (.rdf) | XMLベースのRDFシリアライゼーション | レガシーシステム統合 |
| N-Quads (.nq) | 名前付きグラフ付きN-Triples | マルチソース金融KGデータセット |
| HDT | Header-Dictionary-Triples | 大規模金融KGのための圧縮RDF |

---

## ドメイン固有のオントロジーと語彙

### 金融ドメイン

| オントロジー/語彙 | 対象範囲 | 形式 | URL |
|------------------|---------|------|-----|
| FIBO（上記参照） | 包括的な金融業界 | OWL 2 | https://spec.edmcouncil.org/fibo/ |
| Financial Report Ontology (FRO) | 財務諸表と報告 | OWL | — |
| GoodRelations | 電子商取引、ビジネス関係 | OWL | http://purl.org/goodrelations/ |
| Schema.org（金融） | 構造化データ: FinancialProduct、BankAccount等 | RDFa / JSON-LD | https://schema.org/ |
| Dublin Core（改良版） | 金融文書とエンティティのメタデータ | RDF | https://www.dublincore.org/ |
| PROV-O | 来歴オントロジー; データリネージ | OWL | https://www.w3.org/TR/prov-o/ |
| ORG (W3C Organization) | 組織構造、役割、メンバーシップ | OWL | https://www.w3.org/TR/vocab-org/ |
| FOAF | Friend-of-a-Friend; 人物と関係 | RDF | http://xmlns.com/foaf/spec/ |
| RegOnto | 規制コンプライアンスオントロジー | OWL | — |

### 金融に関連する分野横断オントロジー

| オントロジー | 対象範囲 | 関連性 |
|-------------|---------|--------|
| GeoNames | 地理的エンティティと関係 | 金融エンティティの法域マッピング |
| NUTS (Eurostat) | 欧州地域分類 | 欧州金融エンティティの地理的分類 |
| NACE / NAICS / SIC | 産業分類システム | 金融ネットワークノードのセクター分類 |
| DBpedia Ontology | Wikipediaからの一般知識 | 金融KG充実のためのエンティティリンキング |
| Wikidata Ontology | 構造化された一般知識 | 企業エンティティデータ; クロスリファレンス |
| Time Ontology (OWL-Time) | 時間的概念と関係 | 所有関係と金融関係の時間的有効性 |

---

## 新興標準とイニシアチブ

| イニシアチブ | 説明 | ステータス | 関連性 |
|-------------|------|----------|--------|
| Verifiable Credentials (W3C) | 主張の暗号的証明; デジタルID | W3C勧告 | 金融KGにおけるKYC/AML本人確認 |
| DID (Decentralized Identifiers) | 自己主権型IDの標準 | W3C勧告 | DeFi KGのための分散型エンティティ識別 |
| ISO/IEC 21838（上位オントロジー） | 上位オントロジーフレームワークの標準 | 公開済み | 金融オントロジーの基盤整合 |
| Knowledge Graph standard (ISO/IEC) | KG概念の新興ISO標準化 | 策定中 | 金融KG実務の業界標準化 |
| EU Data Spaces (Financial Data Space) | 金融サービスのための欧州データスペース | 策定中 | 越境金融データ共有とKG相互運用性 |
| Digital Regulatory Reporting (DRR) | 機械実行可能な規制ルール | パイロットプログラム | KG推論による自動コンプライアンス |
| Open Banking Standards (PSD2/Open Finance) | 金融データ共有のためのAPI標準 | 運用中（EU、UK等） | KG構築のための構造化された金融データアクセス |

---

## 標準間のマッピング

金融KG構築において標準間の相互関係を理解することは重要である:

| ソース標準 | ターゲット標準 | マッピングタイプ | 備考 |
|-----------|-------------|----------------|------|
| LEI → FIBO | エンティティ識別からオントロジーへ | 公式アライメント | GLEIFがLEI-FIBOマッピングを提供 |
| XBRL → FIBO | 報告タクソノミーからオントロジーへ | コミュニティ主導 | 財務ファクトからオントロジー概念へのマッピング |
| ISO 20022 → FIBO | メッセージスキーマからオントロジーへ | 公式アライメント | 決済・証券メッセージのセマンティクス |
| BODS → FIBO BE | 所有データからオントロジーへ | コミュニティマッピング | 実質的所有者からFIBO Business Entitiesへ |
| Schema.org → FIBO | ウェブ語彙からオントロジーへ | 近似的 | 軽量ウェブデータから形式オントロジーへ |
| ISDA CDM → FpML | ドメインモデルからメッセージングへ | 公式 | デリバティブライフサイクルの標準化 |
| GLEIF → OpenOwnership | LEIから実質的所有者へ | 新興 | 法人と最終実質的所有者の連結 |
| NACE/NAICS → FIBO | 産業分類からオントロジーへ | 参照 | 金融エンティティのセクター分類 |

---

*最終更新: 2026-02-23*
