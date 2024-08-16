import pandas as pd

#  dummy drone data
drone_data = {
    "Lake Name": ["Lake Alpha", "Lake Beta", "Lake Gamma", "Lake Delta", "Lake Epsilon"],
    "Area (sq km)": [10.5, 8.2, 15.3, 12.7, 9.4],
    "Elevation (m)": [1500, 1450, 1550, 1480, 1520]
}

# Convert  to a DataFrame
df = pd.DataFrame(drone_data)

# Display the DataFrame
print(df)



# Dummy drone data
drone_data = {
    "Lake Name": ["Lake Alpha", "Lake Beta", "Lake Gamma", "Lake Delta", "Lake Epsilon"],
    "Area (sq km)": [10.5, 8.2, 15.3, 12.7, 9.4],
    "Elevation (m)": [1500, 1450, 1550, 1480, 1520]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(drone_data)

# Assume depth-to-elevation ratio (for example, 1/10th of the elevation is the depth)
depth_to_elevation_ratio = 0.1

# Calculate the approximate depth of each lake
df['Depth (m)'] = df['Elevation (m)'] * depth_to_elevation_ratio

# Calculate the volume of each lake assuming a simple conical shape
# Volume (km^3) = 1/3 * Depth (m) * Area (sq km)
df['Volume (km^3)'] = (1/3) * df['Depth (m)'] * df['Area (sq km)']

# Display the DataFrame with the new features
print(df)
