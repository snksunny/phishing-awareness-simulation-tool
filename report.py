import csv 

clicked_ids = set() 

with open("clicks_log.csv", "r") as file:
    for line in file:
        parts = line.strip().split(",") 
        tracking_id = parts[0]
        clicked_ids.add(tracking_id)


total_targets = 0
clicked_targets = 0

with open("targets.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_targets += 1 
        tracking_id = row['tracking_id']
        if tracking_id in clicked_ids: 
            clicked_targets += 1 
            print(f"{row['name']} clicked the link!") 
        else:
            print (f"{row['name']} did not click.") 


click_rate = (clicked_targets / total_targets) * 100

print(f"\n--- Summary ---")
print(f"Total targets: {total_targets}")
print(f"Clicked: {clicked_targets}")
print(f"Click rate: {click_rate:.1f}%")
