import zmq
import requests


def fetch_medication_side_effects(med):
    api_url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{med}"
    
    response = requests.get(api_url)
    if response.status_code == 200 and 'results' in response.json():
        data = response.json()['results'][0]

        potential_fields = ['warnings', 'precautions', 'side_effects', 'adverse_reactions']
        side_effects = 'N/A'
        
        for field in potential_fields:
            if field in data:
                side_effects_list = data[field]
                if isinstance(side_effects_list, list):
                    side_effects = '\n'.join(side_effects_list)
                else:
                    side_effects = side_effects_list
                break
        
        return f"Possible Side Effects for {med}: \n{side_effects}"
    else:
        return None


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5553")

    while True:
        med = socket.recv_string()
        result = fetch_medication_side_effects(med)
        print(f"Request: {med}\nResponse: {result}")
        if result:
            socket.send_string(result)
        else:
            socket.send_string("Error: Medication side effects not found. Please check your spelling or try a different medication.")


if __name__ == "__main__":
    main()
