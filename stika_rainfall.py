import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/skita_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    