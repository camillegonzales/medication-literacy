import zmq
import requests


def fetch_medication_data(med):
    api_url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{med}"
    
    response = requests.get(api_url)
    if response.status_code == 200 and 'results' in response.json():
        data = response.json()['results'][0]
        brand_name = data['openfda'].get('brand_name', 'N/A')
        generic_name = data['openfda'].get('generic_name', 'N/A')
        return f"Brand Names: {', '.join(brand_name)}\nGeneric Name: {', '.join(generic_name)}"
    else:
        return None


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5551")

    while True:
        med = socket.recv_string()
        result = fetch_medication_data(med)
        print(f"Request: {med}\nResponse: {result}")
        if result:
            socket.send_string(result)
        else:
            socket.send_string("\nError: Medication not found. Please check your spelling or try a different medication.\n")


if __name__ == "__main__":
    main()
