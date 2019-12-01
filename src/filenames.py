import os

directory = "data/training"
print("hello")
for f in os.walk(directory):
    print(f)