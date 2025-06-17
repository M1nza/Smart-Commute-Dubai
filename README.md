# Smart-Commute-Dubai
An innovative Python + SQLite project designed to help Dubai residents and expats make smart housing and commute decisions.  

## Features
- Input **any office location** in Dubai by latitude & longitude  
- Analyze over 20+ popular residential areas for:  
  - Average monthly rent (AED)  
  - Distance (km) from office  
  - Public transport modes (Metro, Bus) available  
  - Estimated commute time (minutes)  
  - Monthly transport cost (AED)  
- Results sorted by increasing distance and rent for easy comparison  
- Output as a clean Excel table (`SmartCommute_Affordability_Analyzer.xlsx`)  

## How to Use
1. Clone the repo  
2. Create the SQLite DB by running the SQL file:  
   ```bash sqlite3
   smart_commute.db < smart_commute.sql
3. Install Python dependencies:
   pip install -r requirements.txt
4. Run the Python analyzer:
   python analyzer.py
5. Open SmartCommute_Affordability_Analyzer.xlsx for results.
