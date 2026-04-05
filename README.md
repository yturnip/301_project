## Student Performance Analysis

A multi-part data analysis project investigating the academic, behavioral, and socioeconomic factors that predict student exam performance and identify at-risk students.

## Questions Explored
- **Q1:** Do study hours, attendance, and parental involvement actually drive exam scores?
- **Q2:** Which combination of factors best predicts exam performance?
- **Q3:** Can we classify students as at-risk?

## Project Structure
├── data/              # raw and clean data 
├── database/          # SQLite database (students.db)
├── notebooks/         # Jupyter notebooks for each question
├── report/figures/    # Generated charts and diagnostic plots
├── visualization/     # Tableau dashboard
├── .gitignore
├── README.md
└── requirements.txt   # the complete list of packages installed

## Setup Instructions

1. Clone this repository to your local machine.
2. It is recommended to use a virtual environment (venv or conda).
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Reproducing the Results

1. **Data Cleaning:** Run `notebooks/csv_cleaning.py` first, this will clean the data so that it does not have a null value. Then run `notebooks/01_etl_cleaning.ipynb`, this will generate the `student.db` SQLite database in the `/database/` folder.
2. **Modeling:** To reproduce the analysis and extract the final CSV outputs for Tableau, run the respective notebooks for each research question:
   - **Q1 Baseline Prediction:** Run `notebooks/q1_prediction_given.ipynb` to execute the unscaled Multiple Linear Regression model and export the raw coefficients. _(Note: The `random_state` is fixed at `98396096` to ensure exact reproducibility)._
   - **Q2 Feature Importance:** Run `notebooks/q2_prediction_linear.ipynb` to apply the Standard Scaler and Backward Selection. _(Note: The `random_state` is fixed at `91666719` to ensure exact reproducibility)._
   - **Q3 Classification:** Run `notebooks/q3_classification.ipynb` to execute the Random Forest Classifier pipeline. _(Note: The `random_state` is fixed at `301` to ensure exact reproducibility)._
3. **Dashboards:** Open the `.twbx` (Tableau Packaged Workbook) file located in the `visualizations/` folder. This workbook is pre-linked to the generated CSVs to recreate the final charts.

## Team
- Edgar Sipayung
- Eleonora Ansella Kartono
- Yohanes Amelio Turnip
