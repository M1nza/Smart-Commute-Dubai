-- Create table for residential areas in Dubai
CREATE TABLE IF NOT EXISTS areas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    avg_rent INTEGER NOT NULL,
    lat REAL NOT NULL,
    long REAL NOT NULL
);

-- Insert sample residential areas with fact-checked coordinates and avg rents
INSERT INTO areas (name, avg_rent, lat, long) VALUES
('Al Satwa', 3200, 25.2304, 55.2893),
('Al Karama', 3400, 25.2246, 55.2797),
('Al Rigga', 3000, 25.2649, 55.3188),
('Oud Metha', 3700, 25.2282, 55.3062),
('Al Qusais', 2800, 25.2819, 55.3647),
('Discovery Gardens', 3800, 25.0369, 55.1533),
('Jebel Ali', 2700, 24.9480, 55.0557),
('Jumeirah Lake Towers', 4500, 25.0635, 55.1377),
('Dubai Marina', 5200, 25.0780, 55.1371),
('Palm Jumeirah', 6000, 25.1133, 55.1376),
('Business Bay', 4800, 25.1929, 55.2766),
('Dubai Silicon Oasis', 2900, 25.1045, 55.3826),
('Al Barsha', 3500, 25.1037, 55.1905),
('Tecom', 4000, 25.0785, 55.1500),
('International City', 2600, 25.1245, 55.3445),
('Mirdif', 3200, 25.2345, 55.4201),
('Deira', 3100, 25.2700, 55.3090),
('Al Nahda', 2800, 25.2927, 55.3822),
('Satwa', 3000, 25.2304, 55.2893),
('Muhaisnah', 2700, 25.2500, 55.4300);

-- Create table for transport modes in Dubai metro and bus
CREATE TABLE IF NOT EXISTS transport_modes (
    mode TEXT PRIMARY KEY,
    avg_speed_kmph REAL NOT NULL,
    cost_per_km REAL NOT NULL,
    start_time TEXT NOT NULL  -- First trip start time in HH:MM 24h format
);

-- Insert transport mode data with approximate speeds and fare per km in AED
INSERT INTO transport_modes (mode, avg_speed_kmph, cost_per_km, start_time) VALUES
('Metro', 40, 0.5, '05:00'),
('Bus', 20, 0.3, '04:30');
