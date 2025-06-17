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

## Why This Project?

Dubai’s fast-growing urban landscape demands smart decisions for housing and daily commute. This project combines real-world transport data, geolocation, and cost analysis to empower users with data-driven choices.

## How to Use

1. Clone the repo  
2. Create the SQLite DB by running the SQL file:  
   ```bash
   sqlite3 smart_commute.db < smart_commute.sql
   pip install -r requirements.txt
   python analyzer.py
   Open SmartCommute_Affordability_Analyzer.xlsx for results.
