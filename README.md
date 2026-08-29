markdown
# Dog Breed Classifier 🐶

## 📌 Project Overview
This project uses pre-trained Convolutional Neural Networks (CNNs) to classify pet images.  
The goal is to:
1. Identify whether an image is of a dog or not.
2. Correctly classify the breed of dog (if the image is of a dog).
3. Compare three CNN architectures (ResNet, AlexNet, VGG) for accuracy and runtime.
4. Evaluate trade-offs between accuracy and computational cost.

The project was built as part of a Python learning exercise, focusing on **data structures, command-line arguments, and program organization**.

---

## 📂 Repository Structure
dog-breed-classifier/
│── check_images.py              # Main program
│── get_input_args.py            # Handles command-line arguments
│── get_pet_labels.py            # Extracts labels from filenames
│── classify_images.py           # Runs classifier and compares labels
│── adjust_results4_isadog.py    # Determines dog vs. not-dog
│── calculates_results_stats.py  # Computes statistics
│── print_results.py             # Prints summary and misclassifications
│── classifier.py                # Provided classifier function
│── dognames.txt                 # List of valid dog breeds
│── run_models_batch.sh          # Batch script for all models
│── pet_images/                  # Dataset of 40 test images
│── uploaded_images/             # Folder for user-uploaded test images

Code

---

## ⚙️ Setup & Usage
### Requirements
- Python 3.x
- Libraries: `argparse`, `os`, `time`

### Run the Program
```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
Arguments:

--dir → path to images folder (default: pet_images/)

--arch → CNN model architecture (resnet, alexnet, vgg; default: vgg)

--dogfile → text file with dog names (default: dognames.txt)

Batch Processing
Run all three models at once:

bash
sh run_models_batch.sh
Outputs:

resnet_pet-images.txt

alexnet_pet-images.txt

vgg_pet-images.txt

📊 Results
Model	% Correct Dogs	% Correct Not-a-Dog	% Correct Breed	Notes
ResNet	~93%	~90%	~85%	Strong breed accuracy, slower runtime
AlexNet	100%	100%	~75%	Fastest runtime, weaker breed accuracy
VGG	100%	100%	~93.3%	Best balance of accuracy and runtime


Best Model: VGG

Perfect dog/not-dog classification

Highest breed accuracy (~93.3%)

Reasonable runtime compared to ResNet

🧪 Testing with Uploaded Images
You can test with your own images by placing them in uploaded_images/ and running:

bash
sh run_models_batch_uploaded.sh
This will generate:
resnet_uploaded-images.txt

alexnet_uploaded-images.txt

vgg_uploaded-images.txt

🎯 Learning Objectives Achieved
Correctly identified dogs vs. not dogs.

Correctly classified dog breeds.

Compared CNN architectures for accuracy and runtime.

Practiced Python programming with command-line arguments, dictionaries, and file handling.

📖 References
ImageNet Dataset

Argparse Documentation (docs.python.org in Bing)

Python os module (docs.python.org in Bing)

Code

---

This README gives you a professional, portfolio-ready presentation.  

Would you like me to also add a **“Getting Started” section with installation instructions** (like cloning the repo and setting up a virtual environment), so it’s beginner-friendly for anyone who tries your project?

resnet_uploaded-images.txt

alexnet_uploaded-images.txt

vgg_uploaded-images.txt
