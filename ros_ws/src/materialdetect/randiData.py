import csv
import random
import string
from time import sleep

# Loop to generate and save random variables
while (1):
    # Save the random variables to a CSV file
    with open('/mnt/c/Users/TexSort/Desktop/MasterThesis/materialDetectionTextile/ros_ws/src/materialdetect/materialData.csv', 'w', newline='') as file:
        
        writer = csv.writer(file)

        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        age = random.randint(20, 60)
        job = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
        location = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=7))

        writer.writerow([repr(name), repr(age), repr(job), repr(location)])

    sleep(1)
