import csv
import numpy as np

rows = []

with open("twice_cleaned_final.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)
        
headers = [rows[0]]
star_data_rows = [rows[1:]]

data = []

for i in star_data_rows:
  data.append(i)

m = 0
r = 0
n = 0

radiuses = []
masses = []
names = []

print("data: ",data)

for i_1 in data:
  s_mass = data[m][3]
  masses.append(s_mass)
  m = m + 1

for i_2 in data:
  s_radius = data[r][4]
  radiuses.append(s_radius)
  r = r + 1

for i_3 in data:
  s_name = data[n][1]
  names.append(s_name)
  n = n + 1

print("mass: ",masses)
print("radius: ",radiuses)
print("name :",names)

def convert_to_si(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i] * (6957 * (10 ^ 5))
        mass[i] = mass[i] * (1989 * (10 ^ 24))
        convert_to_si(radiuses, masses)
        
temp_star_data = [data]

def gravity():
    star_masses = []
    star_radiuses = []
    star_name = []
    
    for star_data in temp_star_data:
        star_masses.append(masses)
        star_radiuses.append(radiuses)
        star_name.append(names)
        
    star_gravity = []
    
    for index, name in enumerate(star_name):
        gravity = (float(star_masses[index]) * (5972 * (10 ^ 21))) / (float(star_radiuses[index]) * float(star_radiuses[index]) * (6371 * (10 ^ 3)) * 6371 * (10 ^ 3)) * (6.674 * (10 ^ -11))
        star_gravity.append(gravity)

gravity()