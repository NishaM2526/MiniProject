# LuxuryHousingSales

## Overview
This project analyzes luxury housing sales data in Bangalore, India. It includes data extraction, cleaning, and analysis scripts to provide insights into the luxury real estate market.

## Project Structure
```
LuxuryHousingSales/
├── Code/
│   ├── DataCleaning.py          # Python script for data cleaning operations
│   ├── DataCleaningNotebook.ipynb  # Jupyter notebook for interactive data cleaning
│   └── LoadData.py              # Script to load and process housing data
├── Data/
│   ├── Cleaned_Luxury_Housing_Bangalore.csv  # Processed and cleaned dataset
│   └── Luxury_Housing_Bangalore.csv          # Raw housing sales data
└── README.md                    # This file
```

## Data Description
- **Raw Data**: `Luxury_Housing_Bangalore.csv` contains the original luxury housing sales data for Bangalore
- **Cleaned Data**: `Cleaned_Luxury_Housing_Bangalore.csv` is the processed version with data cleaning applied

## Prerequisites
- Python 3.7+
- Required packages: pandas, numpy, matplotlib, seaborn (install via pip)

## Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

## Usage
### Data Loading
Run the data loading script:
```bash
python Code/LoadData.py
```

### Data Cleaning
- **Script**: Execute `DataCleaning.py` for automated cleaning
- **Notebook**: Open `DataCleaningNotebook.ipynb` in Jupyter for interactive cleaning

### Analysis
Use the cleaned data for further analysis, visualization, or modeling.

## Scripts Description
- `LoadData.py`: Handles data ingestion and initial processing
- `DataCleaning.py`: Applies data cleaning transformations
- `DataCleaningNotebook.ipynb`: Interactive notebook version of cleaning process

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
This project is open-source. Please check the license file for details.

## Contact
For questions or issues, please open an issue in the repository.