import psutil
import time
import csv

# Initialize a list to store CPU utilization
cpu_utilizations = []

try:
    while True:
        # Get the current CPU utilization
        cpu_utilization = psutil.cpu_percent()
        
        # Append the CPU utilization to the list
        cpu_utilizations.append(cpu_utilization)
        
        # Print the current CPU utilization
        print(f'Current CPU utilization: {cpu_utilization}%')
        
        # Wait for 6 seconds
        time.sleep(6)
except KeyboardInterrupt:
    print('Recording stopped by user. Writing data to CSV file...')
    
    # Write the CPU utilization values to a CSV file
    with open('cpu_utilizations.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CPU Utilization'])
        for utilization in cpu_utilizations:
            writer.writerow([utilization])
    
    print('Data written to cpu_utilizations.csv')