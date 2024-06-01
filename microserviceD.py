import zmq
import requests


def fetch_medication_side_effects(med):
    api_url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{med}"
    
    response = requests.get(api_url)
    if response.status_code == 200 and 'results' in response.json():
        data = response.json()['results'][0]
        side_effects_list = data.get('adverse_reactions', ['N/A'])
        if isinstance(side_effects_list, list):
            side_effects = '\n'.join(side_effects_list)
        else:
            side_effects = 'N/A'
        return f"Possible Side effects: \n{side_effects}"
    else:
        return None


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")

    while True:
        medication_name = socket.recv_string()
        result = fetch_medication_side_effects(medication_name)
        if result:
            socket.send_string(result)
        else:
            socket.send_string("Error: Medication side effects not found. Please check your spelling or try a different medication.")


if __name__ == "__main__":
    main()