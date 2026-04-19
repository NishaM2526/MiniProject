# PhonePe Transaction Insights

A Streamlit-based analytics dashboard for PhonePe Pulse data, offering interactive insights into transactions, users, and insurance metrics across Indian states and districts.

## Project Overview

PhonePe Transaction Insights loads aggregated PhonePe Pulse JSON data into MySQL, then renders interactive charts and maps to support multi-dimensional business case studies.

The app covers:
- State-wise transaction trends
- Payment category analysis
- Device and user engagement analysis
- Insurance penetration analysis
- Geographic transaction mapping
- Top/bottom state and district rankings

## Project Structure

- `App/` - Streamlit dashboard and visualization modules
  - `PhonePeApp.py` - main app launcher
  - `Indiamap.py` - choropleth map view
  - `CaseStudy1.py` ... `CaseStudy4.py` - analysis pages
- `Code/` - data extraction and loading utilities
  - `DataExtract.py` - JSON extraction helpers
  - `LoadTransactionData.py` - MySQL table creation and data loading
- `Data/data/` - source PhonePe Pulse JSON dataset folders
- `env/` - local Python virtual environment files

## Prerequisites

- Python 3.8+ installed
- MySQL server installed and running
- Streamlit package
- Required Python libraries:
  - `streamlit`
  - `pandas`
  - `plotly`
  - `matplotlib`
  - `mysql-connector-python`

## Setup

1. Open a terminal in the project root:

   ```powershell
   cd "c:\Users\nisha\OneDrive\Desktop\Nisha\GUVI\MiniProject\PhonePeTransInsights"
   ```

2. Activate the Python virtual environment if needed:

   ```powershell
   .\env\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install streamlit pandas plotly matplotlib mysql-connector-python
   ```

4. Update database credentials in these files if your MySQL settings differ:
   - `App/PhonePeApp.py`
   - `App/Indiamap.py`
   - `App/CaseStudy1.py`
   - `Code/LoadTransactionData.py`

## Data Preparation

The project expects the PhonePe Pulse JSON dataset under `Data/data/` with folders like:
- `aggregated/transaction/`
- `aggregated/user/`
- `aggregated/insurance/`
- `map/transaction/`
- `map/user/`
- `map/insurance/`
- `top/transaction/`
- `top/user/`

The extraction script uses `Code/DataExtract.py` to parse JSON and `Code/LoadTransactionData.py` to create MySQL tables and load data.

### Load data into MySQL

Run the loader script after verifying the dataset path and credentials:

```powershell
python .\Code\LoadTransactionData.py
```

> If the `base_path` in `Code/DataExtract.py` is hard-coded, update it to match your local dataset path.

## Run the Streamlit App

Start the dashboard with:

```powershell
streamlit run .\App\PhonePeApp.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## Notes

- The app currently uses a MySQL database named `phone_pe_pulse`.
- If the dataset files or table structure change, update `Code/DataExtract.py` and `Code/LoadTransactionData.py` accordingly.
- The `env/` folder is a local Python environment and is not required for app logic.

## Contact

For issues or updates, edit the connection settings and dataset paths to match your local environment.
