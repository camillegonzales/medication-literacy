import zmq


def print_intro():
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
    while True:
        medication = input("\nEnter a medication name or type 'help' for more information: ")
        if medication.lower() == 'help':
            print("\nHELP - Entering medications: \n"
                  "- Type the name of the medication you wish to learn about and press Enter. \n"
                  "- Ensure correct spelling of medications to get accurate information.")
        else:
            return medication


def get_info_type():
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
    if info_type == '1':
        result = fetch_brand_generic_names(med)
    elif info_type == '2':
        result = fetch_med_uses(med)
    elif info_type == '3':
        result = fetch_med_side_effects(med)
    elif info_type == '4':
        result = fetch_med_interactions(med)
    print(f"\n{result}\n")


def display_options():
    print("Options:\n"
          "- 'back' to explore previous options \n"
          "- 'new' to learn about a different medication \n"
          "- 'exit' to close the app \n")

    option = input("Choose an option: ")
    return option.lower()


def fetch_brand_generic_names(med):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5554")

    socket.send_string(med)
    result = socket.recv_string()
    return result


def fetch_med_uses(med):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")

    socket.send_string(med)
    result = socket.recv_string()
    return result


def fetch_med_side_effects(med):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    socket.send_string(med)
    result = socket.recv_string()
    return result

def fetch_med_interactions(med):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string(med)
    result = socket.recv_string()
    return result


def main():
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
