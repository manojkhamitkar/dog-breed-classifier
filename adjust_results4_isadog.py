# PROGRAMMER: Your Name
# DATE CREATED: Today's Date
# REVISED DATE:
# PURPOSE: Adjust results dictionary to determine if labels are dogs or not

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly
    classified images as 'a dog' or 'not a dog'.
    Parameters:
      results_dic - Dictionary with key=filename and value=list:
                    index 0 = pet image label
                    index 1 = classifier label
                    index 2 = match flag (1/0)
      dogfile - Text file with dog names (string)
    Returns:
      None - results_dic is mutable, so updated in place
    """

    # Read dog names into a dictionary for fast lookup
    dognames_dic = dict()
    with open(dogfile, "r") as f:
        for line in f:
            name = line.strip()
            if name not in dognames_dic:
                dognames_dic[name] = 1
            else:
                print("** Warning: Duplicate dog name found:", name)

    # Iterate through results_dic and update with dog/not-dog flags
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Check if pet label is a dog
        if pet_label in dognames_dic:
            pet_isdog = 1
        else:
            pet_isdog = 0

        # Check if classifier label is a dog
        if classifier_label in dognames_dic:
            classifier_isdog = 1
        else:
            classifier_isdog = 0

        # Extend results list with these flags
        results_dic[key].extend([pet_isdog, classifier_isdog])
