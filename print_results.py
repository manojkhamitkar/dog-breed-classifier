# PROGRAMMER: Your Name
# DATE CREATED: Today's Date
# REVISED DATE:
# PURPOSE: Print summary results and misclassifications if requested

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results and optionally misclassifications.
    Parameters:
      results_dic - Dictionary with key=filename and value=list of results
      results_stats_dic - Dictionary of statistics (counts & percentages)
      model - CNN model architecture used (string)
      print_incorrect_dogs - True prints incorrectly classified dogs (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds (bool)
    Returns:
      None - prints to console
    """

    # Print model architecture
    print("\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")

    # Print overall counts
    print("Number of Images:", results_stats_dic['n_images'])
    print("Number of Dog Images:", results_stats_dic['n_dogs_img'])
    print("Number of 'Not-a' Dog Images:", results_stats_dic['n_notdogs_img'])

    # Print percentages
    for key in results_stats_dic:
        if key.startswith('pct_'):
            print(f"{key}: {results_stats_dic[key]:.2f}%")

    # Print incorrectly classified dogs
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] +
                                 results_stats_dic['n_correct_notdogs']
                                 != results_stats_dic['n_images']):
        print("\nIncorrect Dog Classifications:")
        for key in results_dic:
            # sum of indices 3 & 4 = 1 means disagreement on dog/not-dog
            if sum(results_dic[key][3:]) == 1:
                print("Filename:", key,
                      "Pet Label:", results_dic[key][0],
                      "Classifier Label:", results_dic[key][1])

    # Print incorrectly classified breeds
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs']
                                  != results_stats_dic['n_correct_breed']):
        print("\nIncorrect Breed Classifications:")
        for key in results_dic:
            # Both labels are dogs (sum indices 3 & 4 = 2) but breed mismatch (index 2 = 0)
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Filename:", key,
                      "Pet Label:", results_dic[key][0],
                      "Classifier Label:", results_dic[key][1])
