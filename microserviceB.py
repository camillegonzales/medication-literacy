import zmq
import requests


def fetch_medication_data(med):
    """
    Fetches medication data from the FDA API based on the medication name.

    Args:
        med (str): The name of the medication.

    Returns:
        str: A formatted string containing the brand and generic names of the medication, 
             or None if the medication is not found.
    """
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
    """
    The main server function that listens for medication requests and sends responses.

    Sets up a ZeroMQ REP socket, binds it to a specified port, and continuously
    listens for incoming medication requests. For each request, it fetches the medication data
    using the fetch_medication_data function and sends the result back to the client.
    """
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
