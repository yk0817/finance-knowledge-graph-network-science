# Ontologies and Standards for Financial Knowledge Graphs

This document catalogs ontologies, data standards, and representation frameworks relevant to constructing and querying financial knowledge graphs.

---

## Financial Industry Business Ontology (FIBO)

### Overview

| Property | Detail |
|----------|--------|
| **Full Name** | Financial Industry Business Ontology |
| **Maintained By** | EDM Council / Object Management Group (OMG) |
| **Format** | OWL 2 / RDF |
| **License** | MIT License (open source) |
| **URL** | https://spec.edmcouncil.org/fibo/ |
| **GitHub** | https://github.com/edmcouncil/fibo |

### Description

FIBO is the most comprehensive formal ontology for the financial industry. It provides machine-readable definitions of financial concepts, instruments, entities, and relationships. Developed collaboratively by financial institutions, regulators, and technology firms under EDM Council and OMG governance.

### FIBO Module Structure

| Module | Scope | Key Classes |
|--------|-------|-------------|
| **Foundations (FND)** | Base concepts: parties, dates, relations, quantities, contracts | Party, Agent, LegalEntity, Date, Agreement |
| **Business Entities (BE)** | Legal entities, corporations, partnerships, trusts, government entities | CorporateBody, LegalPerson, Partnership, GovernmentBody |
| **Financial Business and Commerce (FBC)** | Financial services, products, regulatory bodies | FinancialServiceProvider, RegulatoryAgency, FinancialProduct |
| **Securities (SEC)** | Equities, debt, funds, derivatives | Security, Equity, Bond, DerivativeInstrument, Fund |
| **Derivatives (DER)** | OTC and exchange-traded derivatives, swaps, options, futures | Swap, Option, Future, CreditDefaultSwap |
| **Loans (LOAN)** | Loan types, mortgage products, student loans | Loan, Mortgage, RevolvingCredit |
| **Indices and Indicators (IND)** | Market indices, economic indicators, interest rates | MarketIndex, EconomicIndicator, InterestRateBenchmark |
| **Market Data (MD)** | Prices, quotes, trade data | Price, Quote, Trade |
| **Corporate Actions (CAE)** | Dividends, mergers, stock splits | CorporateAction, Dividend, Merger |

### Legal Entities Module (Detail)

Particularly relevant for ownership knowledge graphs:

| Concept | Description | Relationships |
|---------|-------------|---------------|
| LegalEntity | Any entity recognized by law | hasRegistrationDate, isRegisteredIn |
| CorporateBody | Incorporated entity | hasDirector, hasShareholder |
| OwnershipInterest | Stake in an entity | hasPercentage, isHeldBy |
| ControllingInterest | Ownership exceeding control threshold | controlsEntity |
| BeneficialOwner | Person who ultimately owns/controls | ultimatelyOwns, beneficiallyControls |
| RegisteredAgent | Agent authorized to act for entity | actsFor, isRegisteredIn |

### Adoption and Integration

- Used by major banks, regulators, and data vendors for semantic interoperability
- Aligned with ISO standards (ISO 20022, LEI)
- Available as OWL ontology files, SKOS vocabularies, and JSON-LD contexts
- Integration with GLEIF LEI data and regulatory reporting frameworks

---

## Beneficial Ownership Data Standard (BODS)

### Overview

| Property | Detail |
|----------|--------|
| **Full Name** | Beneficial Ownership Data Standard |
| **Maintained By** | Open Ownership |
| **Format** | JSON Schema |
| **Version** | 0.4 (latest) |
| **License** | Apache 2.0 |
| **URL** | https://standard.openownership.org/ |

### Description

BODS provides a structured format for publishing beneficial ownership information. It enables interoperability between national beneficial ownership registers and supports the creation of ownership knowledge graphs.

### Statement Types

| Statement Type | Purpose | Key Fields |
|----------------|---------|------------|
| **Entity Statement** | Describes a legal entity | entityType, name, jurisdiction, identifiers, foundingDate |
| **Person Statement** | Describes a natural person | personType, names, nationalities, birthDate, addresses |
| **Ownership-or-Control Statement** | Links persons/entities in ownership chain | subject, interestedParty, interests (shareholding, voting rights, control) |

### Interest Types

| Interest Type | Description |
|---------------|-------------|
| shareholding | Direct or indirect shareholding percentage |
| votingRights | Voting rights percentage |
| appointmentOfBoard | Right to appoint/remove board members |
| otherInfluenceOrControl | Other forms of significant control |
| seniorManagingOfficial | Senior management position |
| settlor | Settlor of a trust |
| trustee | Trustee of a trust |
| beneficiaryOfLegalArrangement | Beneficiary of trust or similar |

### Adoption

- Used by UK (PSC Register), Slovakia, Armenia, Latvia, and others
- OpenOwnership Register aggregates data from multiple countries
- Supports beneficial ownership transparency initiatives (EITI, FATF)

---

## FinRegOnt (Financial Regulation Ontology)

### Overview

| Property | Detail |
|----------|--------|
| **Full Name** | Financial Regulation Ontology |
| **Purpose** | Machine-readable representation of financial regulations |
| **Format** | OWL 2 |
| **Scope** | Regulatory requirements, compliance rules, regulatory entities |

### Description

FinRegOnt aims to represent financial regulatory requirements in a machine-readable format, enabling automated compliance checking and regulatory analysis. It covers regulations from multiple jurisdictions and regulatory bodies.

### Key Concepts

| Concept | Description |
|---------|-------------|
| Regulation | A regulatory document or rule |
| RegulatoryBody | Entity issuing regulations (SEC, FCA, ECB, etc.) |
| Requirement | Specific obligation or prohibition |
| RegulatedEntity | Entity subject to regulation |
| ComplianceObligation | Specific compliance requirement |
| ReportingRequirement | Mandatory reporting obligation |
| Threshold | Quantitative regulatory threshold |

---

## Financial Industry Standards

| Standard | Full Name | Scope | Maintained By | Format | URL |
|----------|-----------|-------|---------------|--------|-----|
| LEI | Legal Entity Identifier | Unique identification of legal entities in financial transactions | GLEIF (Global LEI Foundation) | ISO 17442; 20-character alphanumeric | https://www.gleif.org/ |
| XBRL | eXtensible Business Reporting Language | Structured financial reporting; taxonomies for financial statements | XBRL International | XML-based | https://www.xbrl.org/ |
| FpML | Financial products Markup Language | OTC derivative transaction descriptions | ISDA | XML Schema | https://www.fpml.org/ |
| FIX Protocol | Financial Information eXchange | Electronic trading messages; order flow | FIX Trading Community | Tag-value / FIXML | https://www.fixtrading.org/ |
| ISO 20022 | Universal financial industry message scheme | Payment, securities, trade finance, FX messaging | ISO TC68 | XML / ASN.1 | https://www.iso20022.org/ |
| ISDA CDM | Common Domain Model | Standardized lifecycle events for derivatives and securities | ISDA | JSON / Java / Rosetta DSL | https://www.isda.org/2019/10/14/isda-common-domain-model/ |
| ISO 10962 (CFI) | Classification of Financial Instruments | Instrument classification codes | ISO | 6-character code | https://www.iso.org/ |
| ISO 6166 (ISIN) | International Securities Identification Number | Unique identification of securities | ANNA (Association of National Numbering Agencies) | 12-character alphanumeric | https://www.anna-web.org/ |
| ISO 4217 | Currency Codes | Standardized currency identifiers | ISO | 3-letter alpha / 3-digit numeric | https://www.iso.org/ |
| FIGI | Financial Instrument Global Identifier | Open standard for instrument identification | OMG / Bloomberg | 12-character alphanumeric | https://www.openfigi.com/ |
| MiFID II RTS 25 | Regulatory Technical Standards | Financial instrument reference data | ESMA | XML | https://www.esma.europa.eu/ |
| GLEIF Relationship Records | LEI-to-LEI relationship data | Direct/ultimate parent, fund relationships | GLEIF | XML / CSV | https://www.gleif.org/en/lei-data/lei-mapping |

---

## Knowledge Representation Standards

### Core Semantic Web Standards

| Standard | Full Name | Purpose | W3C Status | Relevance to Financial KG |
|----------|-----------|---------|------------|---------------------------|
| RDF | Resource Description Framework | Foundation for representing knowledge as triples (subject-predicate-object) | W3C Recommendation | Core representation for financial entity relationships, ownership chains |
| OWL | Web Ontology Language | Rich ontology modeling with classes, properties, restrictions, reasoning | W3C Recommendation | FIBO is written in OWL 2; enables inference over financial data |
| RDFS | RDF Schema | Lightweight ontology language; class/property hierarchies | W3C Recommendation | Simple schema for financial entity type hierarchies |
| SPARQL | SPARQL Protocol and RDF Query Language | Query language for RDF graphs | W3C Recommendation | Querying financial KGs; federated queries across data sources |
| SKOS | Simple Knowledge Organization System | Taxonomies, thesauri, controlled vocabularies | W3C Recommendation | Financial term taxonomies; industry classification schemes |
| SHACL | Shapes Constraint Language | Data validation for RDF graphs; shape constraints | W3C Recommendation | Validating financial KG data quality; enforcing ownership data constraints |
| JSON-LD | JSON for Linking Data | JSON-based serialization of linked data / RDF | W3C Recommendation | API-friendly financial KG access; embedding structured data in web pages |
| RDF-star | RDF-star (RDF 1.2 candidate) | Statement-level metadata (reification) | W3C Draft | Annotating financial relationships with confidence, temporal validity |

### Serialization Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| Turtle (.ttl) | Human-readable RDF serialization | Authoring and reviewing financial ontologies |
| N-Triples (.nt) | Line-based RDF serialization | Bulk loading financial KG data |
| JSON-LD (.jsonld) | JSON-based RDF serialization | Web APIs for financial KG access |
| RDF/XML (.rdf) | XML-based RDF serialization | Legacy system integration |
| N-Quads (.nq) | N-Triples with named graphs | Multi-source financial KG datasets |
| HDT | Header-Dictionary-Triples | Compressed RDF for large financial KGs |

---

## Domain-Specific Ontologies and Vocabularies

### Financial Domain

| Ontology/Vocabulary | Scope | Format | URL |
|---------------------|-------|--------|-----|
| FIBO (see above) | Comprehensive financial industry | OWL 2 | https://spec.edmcouncil.org/fibo/ |
| Financial Report Ontology (FRO) | Financial statements and reporting | OWL | — |
| GoodRelations | E-commerce, business relationships | OWL | http://purl.org/goodrelations/ |
| Schema.org (Financial) | Structured data: FinancialProduct, BankAccount, etc. | RDFa / JSON-LD | https://schema.org/ |
| Dublin Core (adapted) | Metadata for financial documents and entities | RDF | https://www.dublincore.org/ |
| PROV-O | Provenance ontology; data lineage | OWL | https://www.w3.org/TR/prov-o/ |
| ORG (W3C Organization) | Organizational structures, roles, memberships | OWL | https://www.w3.org/TR/vocab-org/ |
| FOAF | Friend-of-a-Friend; persons and relationships | RDF | http://xmlns.com/foaf/spec/ |
| RegOnto | Regulatory compliance ontology | OWL | — |

### Cross-Domain Ontologies Relevant to Finance

| Ontology | Scope | Relevance |
|----------|-------|-----------|
| GeoNames | Geographic entities and relationships | Jurisdiction mapping for financial entities |
| NUTS (Eurostat) | European territorial classification | European financial entity geographic classification |
| NACE / NAICS / SIC | Industry classification systems | Sectoral classification of financial network nodes |
| DBpedia Ontology | General knowledge from Wikipedia | Entity linking for financial KG enrichment |
| Wikidata Ontology | Structured general knowledge | Corporate entity data; cross-referencing |
| Time Ontology (OWL-Time) | Temporal concepts and relations | Temporal validity of ownership and financial relationships |

---

## Emerging Standards and Initiatives

| Initiative | Description | Status | Relevance |
|------------|-------------|--------|-----------|
| Verifiable Credentials (W3C) | Cryptographic proof of claims; digital identity | W3C Recommendation | KYC/AML identity verification in financial KGs |
| DID (Decentralized Identifiers) | Self-sovereign identity standard | W3C Recommendation | Decentralized entity identification for DeFi KGs |
| ISO/IEC 21838 (Top-Level Ontology) | Standard for top-level ontology frameworks | Published | Foundation alignment for financial ontologies |
| Knowledge Graph standard (ISO/IEC) | Emerging ISO standardization of KG concepts | In development | Industry standardization of financial KG practices |
| EU Data Spaces (Financial Data Space) | European data space for financial services | In development | Cross-border financial data sharing and KG interoperability |
| Digital Regulatory Reporting (DRR) | Machine-executable regulatory rules | Pilot programs | Automated compliance via KG reasoning |
| Open Banking Standards (PSD2/Open Finance) | API standards for financial data sharing | Active (EU, UK, etc.) | Structured financial data access for KG construction |

---

## Mapping Between Standards

Understanding how standards interrelate is critical for financial KG construction:

| Source Standard | Target Standard | Mapping Type | Notes |
|-----------------|-----------------|--------------|-------|
| LEI → FIBO | Entity identification to ontology | Official alignment | GLEIF provides LEI-FIBO mapping |
| XBRL → FIBO | Reporting taxonomy to ontology | Community effort | Financial fact to ontological concept mapping |
| ISO 20022 → FIBO | Message schema to ontology | Official alignment | Payment and securities message semantics |
| BODS → FIBO BE | Ownership data to ontology | Community mapping | Beneficial ownership to FIBO Business Entities |
| Schema.org → FIBO | Web vocabulary to ontology | Approximate | Lightweight web data to formal ontology |
| ISDA CDM → FpML | Domain model to messaging | Official | Derivatives lifecycle standardization |
| GLEIF → OpenOwnership | LEI to beneficial ownership | Emerging | Linking legal entities to ultimate beneficial owners |
| NACE/NAICS → FIBO | Industry classification to ontology | Reference | Sectoral classification of financial entities |

---

*Last updated: 2026-02-23*
