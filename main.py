def print_intro():
    banner = '''
    __  ___         ___            __  _                __    _ __                            
   /  |/  /__  ____/ (_)________ _/ /_(_)___  ____     / /   (_) /____  _________ ________  __
  / /|_/ / _ \/ __  / / ___/ __ `/ __/ / __ \/ __ \   / /   / / __/ _ \/ ___/ __ `/ ___/ / / /
 / /  / /  __/ /_/ / / /__/ /_/ / /_/ / /_/ / / / /  / /___/ / /_/  __/ /  / /_/ / /__/ /_/ / 
/_/  /_/\___/\__,_/_/\___/\__,_/\__/_/\____/_/ /_/  /_____/_/\__/\___/_/   \__,_/\___/\__, /  
                                                                                     /____/                                                                                         
'''
    intro = ("Welcome to the Medication Literacy App! \n\nLearn about medication's different names, uses, side effects, and potential interactions to improve your medication understanding.")
    print(banner)
    print(intro)


def get_med():
    while True:
        medication = input("\nEnter a medication name or type 'help' for more information: ")
        if medication.lower() == 'help':
            print("\nHELP - Entering medications: \n"
                  "- Type the name of the medication you wish to learn about and press Enter. \n"
                  "- Ensure correct spelling of medications to get accurate information.")
        elif medication in medication_data:
            return medication
        else:
            print("\nNo information available for this medication. Please check your spelling or try a different medication.")


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
    med_info = medication_data.get(med.lower())
    if isinstance(med_info, str):
        print(med_info)
        return

    info_mapping = {
        '1': f"{med_info['brand']}\n{med_info['generic']}",
        '2': med_info['uses'],
        '3': med_info['side_effects'],
        '4': med_info['interactions']
    }
    print(f"\nShowing results for {med}:\n{info_mapping[info_type]}\n")


def display_options():
    print("Options:\n"
          "- 'back' to explore previous options \n"
          "- 'new' to learn about a different medication \n"
          "- 'exit' to close the app \n")

    option = input("Choose an option: ")
    return option.lower()


medication_data = {
    'acetaminophen': {
        'brand': "Brand Names: Tylenol, Panadol",
        'generic': "Generic Name: Acetaminophen",
        'uses': ("Used to relieve pain and reduce fever. Often used to treat "
                 "conditions like headache, muscle aches, arthritis, "
                 "backache, toothaches, colds, and fevers."),
        'side_effects': ("Possible side effects include nausea, upper stomach "
                         "pain, itching, loss of appetite, dark urine, "
                         "clay-colored stools, and jaundice."),
        'interactions': ("Can interact with alcohol, causing liver damage, "
                         "and may affect the efficacy of various drugs "
                         "including blood thinners like warfarin.")
    },
    'ibuprofen': {
        'brand': "Brand Names: Advil, Motrin",
        'generic': "Generic Name: Ibuprofen",
        'uses': ("Used to reduce fever and treat pain or inflammation "
                 "caused by many conditions such as headache, toothache, back "
                 "pain, arthritis, menstrual cramps, or minor injury."),
        'side_effects': ("Side effects may include stomach pain, "
                         "constipation, diarrhea, gas, heartburn, nausea, and "
                         "vomiting. Serious side effects include heart attack "
                         "or stroke, especially with long-term use."),
        'interactions': ("Interacts with aspirin, anticoagulants like "
                         "warfarin, other NSAIDs, ACE inhibitors, and "
                         "diuretics. Mixing with alcohol can increase stomach "
                         "bleeding risk.")
    }
}


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
            print("\nThank you for using the Medication Literacy App. Have a "
                  "great day!")
            break


if __name__ == "__main__":
    main()
