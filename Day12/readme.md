# Folder structure for a Python ETL/ELT project using CSV, pandas, and MongoDB:

````plaintext
mtd2507/
│
├── data/                # Raw and processed data files (CSVs, exports)
│   ├── raw/             # Raw data (as extracted)
│   └── processed/       # Transformed data (ready for warehouse)
│
├── etl/                 # ETL scripts and modules
│   ├── extract.py       # Extraction logic (CSV, APIs, etc.)
│   ├── transform.py     # Data cleaning, transformation logic (pandas)
│   └── load.py          # Loading logic (MongoDB, warehouse)
│
├── config/              # Configuration files (DB credentials, settings)
│   └── config.yaml
│
├── warehouse/           # Scripts for loading transformed data into warehouse
│   └── warehouse_loader.py
│
├── lake/                # Scripts for loading raw data into data lake
│   └── lake_loader.py
│
├── notebooks/           # Jupyter notebooks for exploration and prototyping
│
├── tests/               # Unit and integration tests
│   └── test_etl.py
│
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── main.py              # Entry point to run ETL/ELT pipeline
````

**Explanation of each item:**

- **data/**: Stores all data files. `raw/` for unprocessed (lake), `processed/` for transformed (warehouse).
- **etl/**: Contains modular scripts for each ETL step.
- **config/**: Holds configuration files for easy management of settings.
- **warehouse/**: Scripts for loading processed data into the warehouse.
- **lake/**: Scripts for loading raw data into the lake.
- **notebooks/**: For data exploration and prototyping.
- **tests/**: Automated tests for your ETL logic.
- **requirements.txt**: Lists Python packages needed.
- **README.md**: Project overview and instructions.
- **main.py**: Main script to orchestrate the pipeline.
