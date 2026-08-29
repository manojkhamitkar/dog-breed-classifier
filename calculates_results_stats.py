# PROGRAMMER: Your Name
# DATE CREATED: Today's Date
# REVISED DATE:
# PURPOSE: Calculate results statistics from results dictionary

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results dictionary and returns a results statistics dictionary.
    Parameters:
      results_dic - Dictionary with key=filename and value=list:
                    index 0 = Pet Image Label
                    index 1 = Classifier Label
                    index 2 = Match flag (1/0)
                    index 3 = Pet Label is dog (1/0)
                    index 4 = Classifier Label is dog (1/0)
    Returns:
      results_stats_dic - Dictionary containing counts and percentages
    """

    # Initialize counters
    n_images = len(results_dic)
    n_dogs_img = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
    n_label_matches = 0

    # Iterate through results_dic
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        match = results_dic[key][2]
        pet_isdog = results_dic[key][3]
        classifier_isdog = results_dic[key][4]

        # Count label matches
        if match == 1:
            n_label_matches += 1

        # Count dog images
        if pet_isdog == 1:
            n_dogs_img += 1

            # Correctly classified as dog
            if classifier_isdog == 1:
                n_correct_dogs += 1

            # Correct breed match
            if match == 1:
                n_correct_breed += 1
        else:
            # Not-a-dog image
            if classifier_isdog == 0:
                n_correct_notdogs += 1

    # Number of not-dog images
    n_notdogs_img = n_images - n_dogs_img

    # Calculate percentages
    pct_correct_dogs = (n_correct_dogs / n_dogs_img * 100.0) if n_dogs_img > 0 else 0.0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img * 100.0) if n_notdogs_img > 0 else 0.0
    pct_correct_breed = (n_correct_breed / n_dogs_img * 100.0) if n_dogs_img > 0 else 0.0
    pct_label_matches = (n_label_matches / n_images * 100.0) if n_images > 0 else 0.0

    # Create results statistics dictionary
    results_stats_dic = {
        'n_images': n_images,
        'n_dogs_img': n_dogs_img,
        'n_notdogs_img': n_notdogs_img,
        'n_correct_dogs': n_correct_dogs,
        'n_correct_notdogs': n_correct_notdogs,
        'n_correct_breed': n_correct_breed,
        'n_label_matches': n_label_matches,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_notdogs': pct_correct_notdogs,
        'pct_correct_breed': pct_correct_breed,
        'pct_label_matches': pct_label_matches
    }

    return results_stats_dic
