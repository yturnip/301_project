import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('student_performance_clean.db')
cursor = conn.cursor()

# Load the messy CSV into a table in SQLite
df = pd.read_csv('301_project/data/raw/StudentPerformanceFactors.csv')
df = df.dropna()
df.to_sql('raw_data', conn, if_exists='replace', index=False)

# Execute SQL to clean the data and store it in a new table
clean_query = """
    CREATE TABLE cleaned_data AS
    SELECT DISTINCT
        Hours_Studied,
        Attendance,
        Parental_Involvement,
        Access_to_Resources,
        Extracurricular_Activities,
        Sleep_Hours,
        Previous_Scores,
        Motivation_Level,
        Internet_Access,
        Tutoring_Sessions,
        Family_Income,
        Teacher_Quality,
        School_Type,
        Peer_Influence,
        Physical_Activity,
        Learning_Disabilities,
        Parental_Education_Level,
        Distance_from_Home,
        Gender,
        Exam_Score
    FROM raw_data
    -- This removes any row that has a missing value in these columns
    WHERE Teacher_Quality IS NOT NULL 
      AND Parental_Education_Level IS NOT NULL 
      AND Distance_from_Home IS NOT NULL;
"""
cursor.execute("DROP TABLE IF EXISTS cleaned_data;")
cursor.execute(clean_query)
conn.commit()

# Export the cleaned table back to a final CSV file
cleaned_df = pd.read_sql_query("SELECT * FROM cleaned_data", conn)
cleaned_df.to_csv('301_project/data/clean/cleaned_data.csv', index=False)

conn.close()