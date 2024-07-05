import zmq


def print_intro():
    """
    Prints the introductory banner and welcome message for the Medication Literacy App.
    """
    banner = '''
    __  ___         ___            __  _                __    _ __                            
   /  |/  /__  ____/ (_)________ _/ /_(_)___  ____     / /   (_) /____  _________ ________  __
  / /|_/ / _ \/ __  / / ___/ __ `/ __/ / __ \/ __ \   / /   / / __/ _ \/ ___/ __ `/ ___/ / / /
 / /  / /  __/ /_/ / / /__/ /_/ / /_/ / /_/ / / / /  / /___/ / /_/  __/ /  / /_/ / /__/ /_/ / 
/_/  /_/\___/\__,_/_/\___/\__,_/\__/_/\____/_/ /_/  /_____/_/\__/\___/_/   \__,_/\___/\__, /  
                                                                                     /____/                                                                                         
'''
    intro = ("Welcome to the Medication Literacy App!" 
             "\n\nLearn about medication's different names, uses, side effects, and potential interactions to improve your medication understanding.")
    print(banner)
    print(intro)


def get_med():
    """
    Prompts the user to enter a medication name or type 'help' for more information.
    
    Returns:
        str: The name of the medication entered by the user.
    """
    while True:
        medication = input("\nEnter a medication name or type 'help' for more information: ")
        if medication.lower() == 'help':
            print("\nHELP - Entering medications: \n"
                  "- Type the name of the medication you wish to learn about and press Enter. \n"
                  "- Ensure correct spelling of medications to get accurate information.")
        else:
            return medication


def get_info_type():
    """
    Prompts the user to choose the type of information they wish to receive about the medication.
    
    Returns:
        str: The number corresponding to the chosen information type.
    """
    while True:
        print("\nChoose the type of information you wish to receive: \n"
              "1) Brand and Generic Names \n"
              "2) Uses of the Medication \n"
              "3) Possible Side effects \n"
              "4) Drug Interactions \n")

        info_type = input("Type the number of your choice or type 'help' for more information: ")

        if info_type.lower() == 'help':
            print("\nHELP - Choosing A Feature/Information Type: \n"
                  "1. Brand and Generic Names - Lists the official name and common brand names. \n"
                  "2. Uses of the Medication - Describes what the medication is typically used for. \n"
                  "3. Possible Side effects - Details common and rare side effects associated with the medication. \n"
                  "4. Drug Interactions - Provides information on how the drug interacts with other medications, foods, or health conditions. \n"
                  "- To select an option, type the number of your choice then press Enter.")
        elif info_type in ['1', '2', '3', '4']:
            return info_type
        else:
            print("\nInvalid input, please enter a valid number or 'help'.")


def display_results(med, info_type):
    """
    Displays the fetched information about the medication based on the selected type.

    Args:
        med (str): The name of the medication.
        info_type (str): The type of information to fetch and display.
    """
    result = fetch_med_data(med, info_type)
    print(f"\n{result}\n")


def display_options():
    """
    Displays the options for the next action the user can take.
    
    Returns:
        str: The chosen option by the user ('back', 'new', or 'exit').
    """
    print("Options:\n"
          "- 'back' to explore previous options \n"
          "- 'new' to learn about a different medication \n"
          "- 'exit' to close the app \n")

    option = input("Choose an option: ")
    return option.lower()


def fetch_med_data(med, info_type):
    """
    Fetches information about the medication from the server.

    Sets up a ZeroMQ REQ socket, connects to the server, sends the medication
    name and information type, and waits for a response from the server. The server listens
    on the appropriate port based on the information type.

    Args:
        med (str): The name of the medication.
        info_type (str): The type of information to fetch.

    Returns:
        str: The fetched information about the medication.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:555{info_type}")

    socket.send_string(med)
    result = socket.recv_string()
    return result


def main():
    """
    The main function to run the Medication Literacy App.
    """
    print_intro()
    med = get_med()
    while True:
        info_type = get_info_type()
        display_results(med, info_type)
        option = display_options()
        if option == 'back':
            continue
        elif option == 'new':
            med = get_med()
        elif option == 'exit':
            print("\nThank you for using the Medication Literacy App. Have a great day!")
            break


if __name__ == "__main__":
    main()
