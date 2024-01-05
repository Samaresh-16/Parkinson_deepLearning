import psutil
import time
import csv

# # Initialize a list to store CPU utilization
# cpu_utilizations = []

# try:
#     while True:
#         # Get the current CPU utilization
#         cpu_utilization = psutil.cpu_percent()
        
#         # Append the CPU utilization to the list
#         cpu_utilizations.append(cpu_utilization)
        
#         # Print the current CPU utilization
#         print(f'Current CPU utilization: {cpu_utilization}%')
        
#         # Wait for 6 seconds
#         time.sleep(6)
# except KeyboardInterrupt:
#     print('Recording stopped by user. Writing data to CSV file...')
    
#     # Write the CPU utilization values to a CSV file
#     with open('cpu_utilizations.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['CPU Utilization'])
#         for utilization in cpu_utilizations:
#             writer.writerow([utilization])
    
#     print('Data written to cpu_utilizations.csv')

import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv('D:/PublicationWork/Alok-Mastor/Codes/cpu_utilizations.csv')

# Plot the CPU utilization
plt.figure(figsize=(10, 5))
plt.plot(data['CPU Utilization'], color='skyblue')

# Fill the area under the plot
plt.fill_between(range(len(data['CPU Utilization'])), data['CPU Utilization'], color='skyblue', alpha=0.4)

plt.title('CPU Utilization Over Time', fontsize=16)
plt.xlabel('Time (in 6 second intervals)', fontsize=14)
plt.ylabel('CPU Utilization (%)', fontsize=14)
plt.grid(True)

# Save the plot as an image
plt.savefig('D:/PublicationWork/Alok-Mastor/Codes/cpu_utilization.png', dpi=300, bbox_inches='tight')