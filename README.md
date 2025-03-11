# Ethiopian Medical Data Warehouse

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue)](https://www.python.org/) [![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-green)](https://www.postgresql.org/)

This project builds a **data warehouse** to centralize and analyze Ethiopian medical business data scraped from Telegram channels and web sources. The system integrates **Telegram scraping**, **object detection using YOLO**, **ETL/ELT workflows**, and **FastAPI** for API development. It also includes an **interactive Streamlit dashboard** for real-time monitoring and reporting.

---

## Table of Contents

1.  [Overview](#overview)
2.  [Features](#features)
3.  [Technologies Used](#technologies-used)
4.  [Project Structure](#project-structure)
5.  [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
6.  [Usage](#usage)
    * [Running the Telegram Scraper](#running-the-telegram-scraper)
    * [Data Cleaning and Transformation](#data-cleaning-and-transformation)
    * [Object Detection with YOLO](#object-detection-with-yolo)
    * [Launching the Streamlit Dashboard](#launching-the-streamlit-dashboard)
    * [Using the FastAPI Endpoint](#using-the-fastapi-endpoint)
7.  [Contributing](#contributing)
8.  [License](#license)
9.  [Acknowledgments](#acknowledgments)

---

## Overview

The **Ethiopian Medical Data Warehouse** is designed to streamline the collection, storage, and analysis of data related to Ethiopian medical businesses. By leveraging modern data engineering tools and techniques, this project enables:

* Centralized storage of structured data in a PostgreSQL database.
* Automated scraping of Telegram channels and web sources.
* Object detection in images using YOLO for enriched data.
* Real-time insights via an interactive Streamlit dashboard.
* Seamless integration with downstream applications through a FastAPI endpoint.

This solution is particularly valuable for stakeholders in the healthcare and finance sectors, as it helps identify trends, optimize inventory management, and improve decision-making.

---

## Features

* **Telegram Scraping**: Extracts data from public Telegram channels relevant to Ethiopian medical businesses.
* **Data Cleaning and Transformation**: Uses DBT (Data Build Tool) for ETL/ELT workflows to clean and transform data.
* **Object Detection**: Integrates YOLOv5 for detecting objects in images collected from Telegram channels.
* **Data Warehouse**: Stores structured data in a scalable PostgreSQL database.
* **Interactive Dashboard**: Provides real-time insights using Streamlit.
* **API Development**: Exposes the collected data via a FastAPI-based RESTful API.

---

## Technologies Used

* **Programming Languages**: Python
* **Data Collection**: Telethon, Beautiful Soup, Scrapy
* **Data Storage**: PostgreSQL
* **Data Transformation**: DBT (Data Build Tool)
* **Object Detection**: YOLOv5 (PyTorch-based)
* **API Development**: FastAPI
* **Dashboard**: Streamlit
* **Version Control**: Git, GitHub
* **CI/CD**: GitHub Actions

---
## Project Structure

ethiopian_medical_data_warehouse/
├── Data/                 # Telegram scraping scripts
├── Yolo5/                # YOLO-based object detection
├── scripts/              # python scripts used in the project 
├── my_project/           # FastAPI application
├── dashboard/            # Streamlit dashboard
│   ├── app.py            # Main Streamlit app
│   ├── utils.py          # Helper functions for database queries
├── test/                 # Unit and integration tests
├── notebooks/            # jupitor notebook files used in data anlysis 
├── logs/                 # Logs for monitoring
├── README.md             # Documentation
└── requirements.txt      # Python dependencies

---

## Getting Started

### Prerequisites

* Python 3.9 or higher
* PostgreSQL installed and running locally or on a server
* Git for version control
* Basic knowledge of SQL, Python, and APIs

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/your-username/ethiopian-medical-data-warehouse.git](https://github.com/your-username/ethiopian-medical-data-warehouse.git)
    cd ethiopian-medical-data-warehouse
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Set up environment variables:

    * Create a `.env` file in the root directory and add the following:

        ```
        DATABASE_URL=postgresql://user:password@localhost/dbname
        TELEGRAM_API_ID=your_api_id
        TELEGRAM_API_HASH=your_api_hash
        ```

4.  Initialize the database:

    ```bash
    python database/setup_db.py
    ```

---

## Usage

### Running the Telegram Scraper

To scrape data from Telegram channels:

```bash
python scraping/scrape_telegram.py

Data Cleaning and Transformation
Run DBT transformations:

Bash

dbt run
dbt test
Object Detection with YOLO
Detect objects in images:

Bash

python object_detection/detect_objects.py --input_path path/to/images
Launching the Streamlit Dashboard
Start the Streamlit dashboard:

Bash

streamlit run dashboard/app.py
Using the FastAPI Endpoint
Run the FastAPI server:

Bash

uvicorn api.main:app --reload
Access the API documentation at http://127.0.0.1:8000/docs.

Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.
Please ensure your code adheres to PEP 8 standards and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
10 Academy: For providing the challenge and learning resources.
Tutors: Mahlet, Elias, Rediet, Kerod, Emitinan, and Rehmet for their guidance.
Open-Source Libraries: Special thanks to the contributors of Telethon, DBT, YOLOv5, FastAPI, and Streamlit.