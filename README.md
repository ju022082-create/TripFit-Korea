
# TripFit Korea
### Data Literacy Foundations — Final Project Task 1

A data-driven domestic travel recommendation service using Korea Tourism Organization (KTO) open data.

## Team Members

| Student ID | Name |
|---|---|
| 20260870 | Ju Sieon |
| 20260303 | Kim Minchan |
| 20260501 | Park Minjun |
| 20260503 | Kim Jaewoo |

## 1. Project Overview

TripFit Korea aims to recommend domestic travel destinations based on user preferences, including travel distance, purpose, and accommodation accessibility.

This repository contains the preliminary data exploration and analysis conducted for Task 1.

## 2. Dataset

**Primary dataset:** Korea Tourism Organization (KTO) — Tourism Information API (KorService2)

Source:
https://www.data.go.kr/data/15101578/openapi.do

Dataset file: `tourism_all.csv`

- Records: 12,563 tourist attractions
- Columns: 25
- Key fields: `contentid`, `title`, `addr1`, `mapx`, `mapy`, `lclsSystm3`

**Supplementary dataset:** KTO accommodation data, containing 3,113 records.

The datasets were retrieved through the KTO public API.

## 3. Data Access

The original dataset is not included in this repository.

To obtain the data:

1. Visit the public data portal using the URL above.
2. Apply for access to the KTO KorService2 API.
3. Retrieve tourist attractions using the `areaBasedList2` endpoint with `contentTypeId=12`.
4. Save the resulting records as `tourism_all.csv` in the project root directory.

Do not publish your API authentication key.

## 4. Data Exploration

The analysis includes:

- Dataset dimensions and field names
- Missing-value analysis
- Duplicate `contentid` detection
- Top 10 tourism category codes
- Category distribution visualization

### Results

- Total records: 12,563
- Total columns: 25
- Duplicate content IDs: 0
- Missing longitude values: 5
- Missing latitude values: 5
- Missing legacy category codes (`cat1`): 11,799
- Missing new category codes (`lclsSystm3`): 0

## 5. How to Run

Requirements:

- Python 3
- pandas
- matplotlib

Install dependencies:

```bash
pip install pandas matplotlib
```

Place the dataset in the following structure:

```text
TripFit_Korea/
├── tourism_all.csv
└── github_submission/
    └── data_exploration.py
```

From the `TripFit_Korea` directory, run:

```bash
python github_submission/data_exploration.py
```

Generated outputs:

- `eda_results/data_quality.csv`
- `eda_results/category_summary.csv`
- `eda_results/category_distribution.png`

The outputs are saved inside the `github_submission` directory.

## 6. Service Concept

The proposed service uses geographic distance, tourism category information, and nearby accommodation data to identify suitable destinations.

Future development will include improved classification, transport-aware accessibility, and a web-based recommendation interface.
