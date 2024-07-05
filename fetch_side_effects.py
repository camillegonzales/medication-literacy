import zmq
import requests


def fetch_medication_side_effects(med):
    """
    Fetches the potential side effects of a medication from the FDA API based on the medication name.

    Args:
        med (str): The name of the medication.

    Returns:
        str: A formatted string containing the possible side effects of the medication, or None if the medication is not found.
    """
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
    """
    The main server function that listens for medication side effect requests and sends responses.

    Sets up a ZeroMQ REP socket, binds it to a specified port, and continuously
    listens for incoming medication side effect requests. For each request, it fetches the medication side effects
    using the fetch_medication_side_effects function and sends the result back to the client.
    """
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
