import zmq
import requests


def fetch_medication_uses(med):
    """
    Fetches the uses of a medication from the FDA API based on the medication name.

    Args:
        med (str): The name of the medication.

    Returns:
        str: A formatted string containing the uses of the medication, or None if the medication is not found.
    """
    api_url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{med}"
    
    response = requests.get(api_url)
    if response.status_code == 200 and 'results' in response.json():
        data = response.json()['results'][0]
        uses_list = data.get('indications_and_usage', ['N/A'])
        if isinstance(uses_list, list):
            uses = '\n'.join(uses_list)
        else:
            uses = 'N/A'
        return f"Uses for {med}: \n{uses}"
    else:
        return None


def main():
    """
    The main server function that listens for medication use requests and sends responses.

    Sets up a ZeroMQ REP socket, binds it to a specified port, and continuously
    listens for incoming medication use requests. For each request, it fetches the medication uses
    using the fetch_medication_uses function and sends the result back to the client.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5552")

    while True:
        med = socket.recv_string()
        result = fetch_medication_uses(med)
        print(f"Request: {med}\nResponse: {result}")
        if result:
            socket.send_string(result)
        else:
            socket.send_string("Error: Medication uses not found. Please check your spelling or try a different medication.")


if __name__ == "__main__":
    main()
