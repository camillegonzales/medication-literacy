import zmq
import requests


def fetch_medication_uses(med):
    api_url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{med}"
    
    response = requests.get(api_url)
    if response.status_code == 200 and 'results' in response.json():
        data = response.json()['results'][0]
        uses_list = data.get('indications_and_usage', ['N/A'])
        if isinstance(uses_list, list):
            uses = '\n'.join(uses_list)
        else:
            uses = 'N/A'
        return f"Uses: \n{uses}"
    else:
        return None


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")

    while True:
        med = socket.recv_string()
        result = fetch_medication_uses(med)
        if result:
            socket.send_string(result)
        else:
            socket.send_string("Error: Medication uses not found. Please check your spelling or try a different medication.")


if __name__ == "__main__":
    main()
