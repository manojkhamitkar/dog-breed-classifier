# PROGRAMMER: Your Name
# DATE CREATED: Today's Date
# REVISED DATE:
# PURPOSE: Create pet image labels from filenames

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on the filenames in the given directory.
    Parameters:
     image_dir - The path to the folder of pet images (string)
    Returns:
     results_dic - Dictionary with key=filename and value=[pet label]
    """
    # Retrieve list of files in directory
    filename_list = listdir(image_dir)

    # Create empty dictionary
    results_dic = dict()

    # Process each filename
    for filename in filename_list:
        # Skip hidden/system files
        if filename[0] == ".":
            continue

        # Convert filename to lowercase
        low_filename = filename.lower()

        # Split by underscores
        word_list = low_filename.split("_")

        # Build pet label from alphabetic words only
        pet_label = ""
        for word in word_list:
            if word.isalpha():
                pet_label += word + " "

        # Strip leading/trailing whitespace
        pet_label = pet_label.strip()

        # Add to dictionary if not already present
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Duplicate key:", filename,
                  "already exists with value:", results_dic[filename])

    return results_dic
