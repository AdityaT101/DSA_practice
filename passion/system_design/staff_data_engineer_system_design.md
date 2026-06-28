# System Design Questions for Staff Data Engineer (FAANG/MAANG)

## Overview
Staff-level interviews focus on **end-to-end data platform design**, **scalability**, **trade-offs**, and **cross-functional leadership**. Expect deep dives into data modeling, pipeline architecture, and real-time vs batch processing.

---

## Category 1: Data Pipeline & ETL Systems

### 1. Design a Real-Time Data Ingestion Pipeline
**Companies:** Meta, Uber, LinkedIn, Netflix

**Requirements:**
- Ingest 1M+ events/second from multiple sources
- Sub-second latency for real-time analytics
- Handle schema evolution
- Exactly-once semantics

**Key Components:**
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Sources   │───▶│   Kafka     │───▶│ Spark/Flink │───▶│  Data Lake  │
│ (Apps, IoT) │    │  (Buffer)   │    │ (Process)   │    │ (S3/HDFS)   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                              │
                                              ▼
                                      ┌─────────────┐
                                      │  Real-time  │
                                      │   (Druid)   │
                                      └─────────────┘
```

**Discussion Points:**
- Kafka partitioning strategy
- Backpressure handling
- Dead letter queues
- Idempotency & deduplication
- Schema registry (Avro/Protobuf)

---

### 2. Design a Data Lake Architecture
**Companies:** Amazon, Netflix, Airbnb, Uber

**Requirements:**
- Store petabytes of structured/unstructured data
- Support batch and streaming workloads
- Enable self-service analytics
- Cost-effective storage tiers

**Key Components:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAKE ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐         │
│  │  Bronze  │──▶│  Silver  │──▶│   Gold   │──▶│  Serving │         │
│  │  (Raw)   │   │ (Cleaned)│   │(Curated) │   │  (Views) │         │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘         │
│                                                                      │
│  Storage: S3/ADLS/GCS with Delta Lake/Iceberg/Hudi                  │
│  Compute: Spark/Databricks/EMR                                       │
│  Catalog: Hive Metastore/AWS Glue/Unity Catalog                     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Discussion Points:**
- Medallion architecture (Bronze/Silver/Gold)
- Delta Lake vs Iceberg vs Hudi
- Partitioning strategies
- Data compaction & vacuum
- Access control & governance

---

### 3. Design a Change Data Capture (CDC) System
**Companies:** Uber, LinkedIn, Stripe, Square

**Requirements:**
- Capture changes from 1000+ database tables
- Near real-time replication
- Handle schema changes gracefully
- Support multiple downstream consumers

**Key Components:**
```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────────────┐
│  MySQL   │───▶│ Debezium │───▶│  Kafka   │───▶│ Data Warehouse   │
│ Postgres │    │ (CDC)    │    │          │    │ Data Lake        │
│ MongoDB  │    │          │    │          │    │ Search (ES)      │
└──────────┘    └──────────┘    └──────────┘    └──────────────────────┘
```

**Discussion Points:**
- Log-based vs query-based CDC
- Handling deletes (soft delete, tombstones)
- Initial snapshot + incremental
- Ordering guarantees
- Exactly-once delivery

---

### 4. Design an Event-Driven Data Platform
**Companies:** Netflix, Uber, DoorDash

**Requirements:**
- Decouple producers and consumers
- Support event replay
- Handle 10M+ events/second
- Multi-region deployment

**Discussion Points:**
- Event schema design
- Event sourcing vs event streaming
- Kafka vs Pulsar vs Kinesis
- Consumer group management
- Cross-region replication

---

## Category 2: Data Warehouse & Analytics

### 5. Design a Data Warehouse for E-commerce
**Companies:** Amazon, Walmart, Shopify

**Requirements:**
- Support 100+ analysts running queries
- Sub-minute query latency for dashboards
- Handle 10TB+ daily data ingestion
- Support slowly changing dimensions

**Key Components:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                      DATA WAREHOUSE DESIGN                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Fact Tables:                    Dimension Tables:                  │
│  ┌─────────────────┐             ┌─────────────────┐                │
│  │ fact_orders     │             │ dim_customer    │                │
│  │ fact_page_views │             │ dim_product     │                │
│  │ fact_inventory  │             │ dim_date        │                │
│  └─────────────────┘             │ dim_geography   │                │
│                                  └─────────────────┘                │
│                                                                      │
│  Modeling: Star Schema / Snowflake / Data Vault                     │
│  Platform: Snowflake / BigQuery / Redshift / Databricks             │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Discussion Points:**
- Star vs Snowflake schema
- SCD Type 1, 2, 3
- Incremental vs full refresh
- Materialized views
- Query optimization (clustering, partitioning)

---

### 6. Design a Metrics Platform
**Companies:** Meta, Airbnb, LinkedIn, Pinterest

**Requirements:**
- Define and compute 10,000+ business metrics
- Consistent metric definitions across company
- Support real-time and historical metrics
- Self-service metric creation

**Key Components:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                        METRICS PLATFORM                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   Metric     │───▶│   Compute    │───▶│   Serving    │          │
│  │  Definition  │    │   Engine     │    │    Layer     │          │
│  │   (YAML)     │    │  (Spark)     │    │  (Cache/DB)  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                                       │                   │
│         ▼                                       ▼                   │
│  ┌──────────────┐                      ┌──────────────┐            │
│  │   Semantic   │                      │  Dashboards  │            │
│  │    Layer     │                      │   & APIs     │            │
│  └──────────────┘                      └──────────────┘            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Discussion Points:**
- Semantic layer (dbt metrics, Cube.js, Minerva)
- Metric versioning
- Backfilling strategies
- Anomaly detection
- Metric lineage

---

### 7. Design a Real-Time Analytics Dashboard
**Companies:** Uber, DoorDash, Instacart

**Requirements:**
- 1-second refresh rate
- Support 1000+ concurrent users
- Aggregate millions of events
- Drill-down capabilities

**Discussion Points:**
- Pre-aggregation vs on-the-fly
- OLAP cubes (Druid, Pinot, ClickHouse)
- Caching strategies
- Approximate algorithms (HyperLogLog)
- WebSocket vs polling

---

## Category 3: ML & Feature Engineering

### 8. Design a Feature Store
**Companies:** Uber, Airbnb, Netflix, Spotify

**Requirements:**
- Serve features for 100+ ML models
- Support batch and real-time features
- Feature versioning and lineage
- Low-latency serving (<10ms p99)

**Key Components:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                         FEATURE STORE                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   Feature    │───▶│   Offline    │───▶│   Training   │          │
│  │  Pipelines   │    │    Store     │    │    Jobs      │          │
│  │  (Spark)     │    │  (S3/Hive)   │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                                                           │
│         ▼                                                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   Stream     │───▶│   Online     │───▶│   Model      │          │
│  │  Processing  │    │    Store     │    │   Serving    │          │
│  │  (Flink)     │    │ (Redis/DDB)  │    │              │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                      │
│  Tools: Feast, Tecton, Databricks Feature Store                     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Discussion Points:**
- Online vs offline store
- Point-in-time correctness
- Feature freshness SLAs
- Feature sharing & discovery
- Training-serving skew

---

### 9. Design an ML Training Pipeline
**Companies:** Google, Meta, Amazon

**Requirements:**
- Train models on petabytes of data
- Distributed training support
- Experiment tracking
- Model versioning and registry

**Discussion Points:**
- Data versioning (DVC, Delta Lake)
- Distributed training (Horovod, Ray)
- Hyperparameter tuning
- Model registry (MLflow, SageMaker)
- CI/CD for ML

---

### 10. Design a Recommendation System Data Pipeline
**Companies:** Netflix, Spotify, YouTube, TikTok

**Requirements:**
- Process user interactions in real-time
- Generate embeddings for 100M+ items
- Support A/B testing
- Handle cold start problem

**Discussion Points:**
- Collaborative filtering data needs
- Real-time feature updates
- Embedding storage and retrieval
- Feedback loops
- Offline evaluation data

---

## Category 4: Search & Indexing

### 11. Design a Search Indexing Pipeline
**Companies:** Google, Amazon, LinkedIn, Airbnb

**Requirements:**
- Index 1B+ documents
- Near real-time index updates
- Support full-text and structured search
- Handle schema changes

**Key Components:**
```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  Source  │───▶│  Kafka   │───▶│ Indexer  │───▶│  Elastic │
│   DBs    │    │          │    │ (Spark)  │    │  Search  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                                      │
                                      ▼
                               ┌──────────┐
                               │  Search  │
                               │   API    │
                               └──────────┘
```

**Discussion Points:**
- Incremental vs full reindex
- Index sharding strategy
- Relevance tuning data
- Query analytics pipeline
- A/B testing infrastructure

---

### 12. Design a Log Analytics System
**Companies:** All FAANG, Datadog, Splunk

**Requirements:**
- Ingest 100TB+ logs/day
- Sub-second search latency
- 30-day retention with archival
- Alerting on patterns

**Discussion Points:**
- Log parsing and enrichment
- Hot/warm/cold storage tiers
- Sampling strategies
- Aggregation pipelines
- Cost optimization

---

## Category 5: Data Quality & Governance

### 13. Design a Data Quality Framework
**Companies:** Airbnb, Uber, Netflix

**Requirements:**
- Monitor 10,000+ tables
- Detect anomalies automatically
- Block bad data from propagating
- Self-service rule creation

**Key Components:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA QUALITY FRAMEWORK                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │    Rules     │───▶│   Execution  │───▶│   Alerting   │          │
│  │  Definition  │    │   Engine     │    │  & Blocking  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                      │
│  Checks:                                                            │
│  • Schema validation      • Freshness                               │
│  • Null/duplicate rates   • Volume anomalies                        │
│  • Referential integrity  • Statistical drift                       │
│                                                                      │
│  Tools: Great Expectations, dbt tests, Monte Carlo, Soda            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Discussion Points:**
- Proactive vs reactive checks
- Circuit breaker pattern
- Data SLAs and SLIs
- Root cause analysis
- Data contracts

---

### 14. Design a Data Lineage System
**Companies:** Airbnb, LinkedIn, Lyft

**Requirements:**
- Track lineage across all data assets
- Column-level lineage
- Impact analysis for changes
- Integration with existing tools

**Discussion Points:**
- Lineage extraction (parsing, runtime)
- Graph storage (Neo4j, Neptune)
- UI for exploration
- Integration with catalog
- Automated documentation

---

### 15. Design a Data Catalog & Discovery Platform
**Companies:** Airbnb (Dataportal), LinkedIn (DataHub), Lyft (Amundsen)

**Requirements:**
- Catalog 100,000+ datasets
- Search and discovery
- Ownership and documentation
- Usage analytics

**Discussion Points:**
- Metadata extraction
- Search ranking
- Social features (ratings, comments)
- Integration with BI tools
- Automated tagging

---

## Category 6: Streaming & Real-Time

### 16. Design a Real-Time Fraud Detection Pipeline
**Companies:** Stripe, Square, PayPal, Amazon

**Requirements:**
- Process transactions in <100ms
- Low false positive rate
- Handle 100K+ transactions/second
- Model updates without downtime

**Discussion Points:**
- Stream processing (Flink, Kafka Streams)
- Feature computation in real-time
- Model serving architecture
- Feedback loop for labels
- Rule engine vs ML

---

### 17. Design a Real-Time Notification System
**Companies:** Meta, Twitter, LinkedIn

**Requirements:**
- Deliver notifications in <1 second
- Support 1B+ users
- Personalized delivery preferences
- Multi-channel (push, email, SMS)

**Discussion Points:**
- Event-driven architecture
- User preference storage
- Rate limiting
- Delivery tracking
- A/B testing

---

### 18. Design a Stream Processing Platform
**Companies:** Uber, Netflix, LinkedIn

**Requirements:**
- Support 1000+ streaming jobs
- Self-service job deployment
- Exactly-once semantics
- Auto-scaling

**Discussion Points:**
- Flink vs Spark Streaming vs Kafka Streams
- State management
- Checkpointing
- Backpressure handling
- Monitoring and alerting

---

## Category 7: Infrastructure & Platform

### 19. Design a Data Platform for Multi-Tenancy
**Companies:** Snowflake, Databricks, cloud providers

**Requirements:**
- Isolate tenant data
- Fair resource allocation
- Per-tenant billing
- Self-service provisioning

**Discussion Points:**
- Namespace isolation
- Resource quotas
- Chargeback models
- Access control (RBAC)
- Noisy neighbor problem

---

### 20. Design a Workflow Orchestration System
**Companies:** Airbnb (Airflow), Netflix (Maestro), Uber (Cadence)

**Requirements:**
- Schedule 100,000+ daily jobs
- Handle dependencies
- Retry and alerting
- Self-service DAG creation

**Key Components:**
```
┌─────────────────────────────────────────────────────────────────────┐
│                    WORKFLOW ORCHESTRATION                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   Scheduler  │───▶│   Executor   │───▶│   Workers    │          │
│  │              │    │   Queue      │    │  (K8s/EC2)   │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                      │
│  Features:                                                          │
│  • DAG versioning        • Backfills                                │
│  • Dynamic tasks         • SLA monitoring                           │
│  • Cross-DAG deps        • Cost attribution                         │
│                                                                      │
│  Tools: Airflow, Dagster, Prefect, Temporal                         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Discussion Points:**
- Scheduler architecture
- Task isolation
- Backfill strategies
- Observability
- Cost optimization

---

## Interview Tips for Staff Level

### What Interviewers Look For:

1. **End-to-End Thinking**
   - Don't just design one component
   - Consider data flow from source to consumption

2. **Trade-off Analysis**
   - Batch vs streaming
   - Consistency vs availability
   - Cost vs performance

3. **Scale Considerations**
   - Start with requirements (QPS, data volume)
   - Calculate storage, compute, network needs

4. **Operational Excellence**
   - Monitoring and alerting
   - Failure handling
   - On-call considerations

5. **Cross-Functional Impact**
   - How does this affect data scientists?
   - How do analysts use this?
   - What about data governance?

### Framework for Answering:

```
1. CLARIFY REQUIREMENTS (5 min)
   - Functional requirements
   - Non-functional (scale, latency, consistency)
   - Constraints (budget, timeline, team)

2. HIGH-LEVEL DESIGN (10 min)
   - Draw major components
   - Data flow diagram
   - API contracts

3. DEEP DIVE (15 min)
   - Pick 2-3 components to detail
   - Discuss trade-offs
   - Address scaling challenges

4. OPERATIONAL CONCERNS (5 min)
   - Monitoring
   - Failure scenarios
   - Evolution/migration
```

---

## Quick Reference: Technologies to Know

| Category | Technologies |
|----------|-------------|
| **Streaming** | Kafka, Flink, Spark Streaming, Kinesis |
| **Batch** | Spark, Hive, Presto/Trino |
| **Storage** | S3, HDFS, Delta Lake, Iceberg |
| **Warehouse** | Snowflake, BigQuery, Redshift, Databricks |
| **OLAP** | Druid, Pinot, ClickHouse |
| **Orchestration** | Airflow, Dagster, Prefect |
| **CDC** | Debezium, Fivetran, Airbyte |
| **Quality** | Great Expectations, dbt, Monte Carlo |
| **Catalog** | DataHub, Amundsen, Unity Catalog |
| **Feature Store** | Feast, Tecton, Databricks FS |

---

**Good luck with your Staff Data Engineer interviews!** 🚀
