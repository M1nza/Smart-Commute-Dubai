import pandas as pd
import sqlite3
import math
from datetime import datetime, timedelta

# Haversine formula to calculate distance in km
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)

    a = math.sin(d_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Main function to generate commute analysis
def generate_commute_analysis(office_lat, office_long, shift_start_time):
    conn = sqlite3.connect("smart_commute.db")
    cursor = conn.cursor()

    # Load residential areas
    areas = cursor.execute("SELECT name, avg_rent, lat, long FROM areas").fetchall()

    # Load transport modes
    transport_modes = cursor.execute("SELECT mode, avg_speed_kmph, cost_per_km, start_time FROM transport_modes").fetchall()

    output = []

    for area in areas:
        area_name, avg_rent, lat, lon = area
        distance = haversine(lat, lon, office_lat, office_long)

        for mode in transport_modes:
            mode_name, speed, cost_per_km, mode_start_time = mode
            commute_time_hr = distance / speed
            commute_time_min = commute_time_hr * 60
            commute_cost = distance * cost_per_km * 2 * 22  # round trip x 22 workdays

            # Earliest departure time
            departure_time = datetime.strptime(mode_start_time, "%H:%M")
            arrival_time = departure_time + timedelta(minutes=commute_time_min)
            shift_start = datetime.strptime(shift_start_time, "%H:%M")

            if arrival_time.time() <= shift_start.time():
                output.append({
                    "Area": area_name,
                    "Avg Rent (AED)": int(avg_rent),
                    "Mode": mode_name,
                    "Distance (km)": round(distance, 2),
                    "Commute Time (min)": round(commute_time_min, 1),
                    "Transport Cost (AED/mo)": round(commute_cost),
                    "Must Leave At": departure_time.strftime("%H:%M")
                })
                break  # Only take the best compatible transport

    df = pd.DataFrame(output)
    # Sort by Distance then Avg Rent (both ascending)
    df = df.sort_values(by=["Distance (km)", "Avg Rent (AED)"]).reset_index(drop=True)
    df.to_excel("SmartCommute_Affordability_Analyzer.xlsx", index=False)
    conn.close()

# Example run with Burj Khalifa office, 9 AM shift start
generate_commute_analysis(25.1972, 55.2744, "09:00")
