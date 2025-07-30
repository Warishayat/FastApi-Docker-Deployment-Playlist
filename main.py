import json
def load_data():
    with open("patient.json", "rb") as f:
        data = json.load(f)
    return data



data = load_data()
id = int(input("Enter the id that you want to check: "))
print(id)
for patient in data:
    if patient["id"] == id:
        print("Data is found")
        print(patient)
        break
    else:
        continue
    


