# AWS Multisource Data Pipeline

Example data engineering pipeline demonstrating ingestion of multiple data sources and preparation of analytics-ready datasets.

## Data Sources

This project simulates ingesting data from different sources commonly used in real-world data platforms:

• CSV file – supplier order data  
• JSON event data – shipment tracking events  
• API source – external service data

## Project Structure

aws-multisource-data-pipeline

data/
supplier_orders.csv
shipment_events.json

ingestion/
ingest_api.py

README.md


## Pipeline Concept

Typical pipeline flow:

1. Ingest raw data from multiple sources
2. Normalize and validate datasets
3. Prepare analytics-ready tables
4. Deliver datasets for BI and reporting

## Technologies Used

Python  
SQL  
PostgreSQL  
AWS (conceptual architecture)

## Architecture

The pipeline ingests data from multiple sources and prepares it for analytics using AWS services.
Data flows through the pipeline as follows:

Data Sources
(CSV / JSON / API)
↓
Python Ingestion Scripts
↓
AWS S3 Data Lake (Raw Storage)
↓
AWS Athena (Serverless Query Engine)
↓
Analytics / Reporting

## Future Enhancements

• Load processed data into a warehouse (Redshift / PostgreSQL)  
• Add orchestration with Airflow  
• Add data quality validation checks  
• Deploy pipeline using AWS services
