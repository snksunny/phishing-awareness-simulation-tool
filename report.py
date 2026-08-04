import csv #imports the csv module for reading and writing CSV files

clicked_ids = set() #creates an empty set to store the tracking IDs of clicked links

with open("clicks_log.csv", "r") as file:
    for line in file:
        parts = line.strip().split(",") #splits each line of the CSV file into parts using a comma as the delimiter, uses strip() to remove any leading or trailing whitespace from the line
        tracking_id = parts[0]
        clicked_ids.add(tracking_id)


total_targets = 0
clicked_targets = 0

with open("targets.csv", "r") as file:
    reader = csv.DictReader(file) #creates a CSV reader object to read the contents of the targets.csv file
    for row in reader:
        total_targets += 1 #increments the total_targets counter for each row in the targets.csv file
        tracking_id = row['tracking_id'] #assumes that the tracking ID is in the 'tracking_id' column of the CSV file
        if tracking_id in clicked_ids: #checks if the tracking ID is present in the clicked_ids set
            clicked_targets += 1 #increments the clicked_targets counter if the tracking ID was clicked
            print(f"{row['name']} clicked the link!") #prints the name of the target that clicked the link
        else:
            print (f"{row['name']} did not click.") #prints the name and of the target that was not clicked


click_rate = (clicked_targets / total_targets) * 100

print(f"\n--- Summary ---")
print(f"Total targets: {total_targets}")
print(f"Clicked: {clicked_targets}")
print(f"Click rate: {click_rate:.1f}%")
