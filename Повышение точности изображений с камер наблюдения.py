import cv2
from cv2 import dnn_superres
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# Script to perform super resolution on png images.
# The methods (i.e. the neural networks), should be saved in the same folder are this script.
# Define the available methods alongside with the corresponding scaling factor. EDSR_x4=("EDSR_x4.pb", 4, "edsr"),, LapSRN_x8=("LapSRN_x8.pb", 8, "lapsrn")
methods = dict(EDSR_x4=("EDSR_x2.pb", 42, "edsr"),FSRCNN_x4=("FSRCNN_x4.pb", 4, "fsrcnn"),
               LapSRN_x4=("LapSRN_x4.pb", 4, "lapsrn"))


# Define the upscaling function in OpenCV (i.e. loads the model, runs the model and saves the image.
def upscale(path, model, scale, image, file_path):
    # Read the desired model
    sr.readModel(path)
    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel(model, scale)
    # Upscale the image
    result = sr.upsample(image)
    # Save the image
    cv2.imwrite(file_path + "-" + path + "-" + "HLS_FULL.png", result)


# Open an user interface to look for the image or images to be upscaled.
root = tk.Tk()
root.withdraw()
files_path = filedialog.askopenfilenames()

# Iterates through all the images selected.
for m in range(len(files_path)):
    name = Path(files_path[m]).stem
    # Read image
    image = cv2.imread(files_path[m])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS_FULL)
    # Create an SuperResolution object
    sr = dnn_superres.DnnSuperResImpl_create()
    # This is a reminder in case you wonder how to operate with dictionaries
    # x=[(k, v) for k, v in methods.items()] This is how to extract the keys and values of a dictionary.
    # Iterates through all the networks in methods (for a 2048 by 2048 px takes about two minutes to run)
    # Prints the image name and then applies the upscale (which also saves the output once up scaled)
    print('Image ' + name)
    for k in methods:
        print('Currently doing ' + methods[k][0])
        upscale(methods[k][0], methods[k][2], methods[k][1], image, files_path[m])

# Indicates that the script has finished.
print('++++++++++++++++ All done ++++++++++++++++')
