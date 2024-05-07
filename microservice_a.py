import time
import requests
import json


while True:
    time.sleep(3)

    with open("input.txt", "r") as file:
        medication = file.read().strip()

    if medication:
        encoded_medication = requests.utils.quote(medication)
        url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{encoded_medication}&limit=1"
        response = requests.get(url)
        data = response.json()

        output = json.dumps(data, indent=4)

        with open("output_a.txt", "w") as file:
            file.write(str(output))
