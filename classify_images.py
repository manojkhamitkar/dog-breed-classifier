# PROGRAMMER: Your Name
# DATE CREATED: Today's Date
# REVISED DATE:
# PURPOSE: Use classifier function to classify pet images and compare labels

from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images using the classifier function and compares labels.
    Parameters:
      images_dir - The path to the folder of pet images (string)
      results_dic - Dictionary with key=filename and value=[pet label] (dict)
      model - CNN model architecture to use (string: resnet, alexnet, vgg)
    Returns:
      None - results_dic is mutable, so it is updated in place
    """

    # Iterate through all filenames in results_dic
    for key in results_dic:
        # Full path to image
        full_path = images_dir + key

        # Get classifier label
        classifier_label = classifier(full_path, model)

        # Format classifier label: lowercase, strip whitespace
        classifier_label = classifier_label.lower().strip()

        # Add classifier label to results_dic
        results_dic[key].append(classifier_label)

        # Compare pet label (index 0) with classifier label
        pet_label = results_dic[key][0]

        if pet_label in classifier_label:
            # Match found
            results_dic[key].append(1)
        else:
            # No match
            results_dic[key].append(0)
