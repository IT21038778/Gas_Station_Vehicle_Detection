import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
from tkinter import OptionMenu
from tkinter import simpledialog

# Create a function to open the file dialog and display the selected image
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    if file_path:
        global original_image
        original_image = Image.open(file_path)
        photo = ImageTk.PhotoImage(original_image)

        # Display the original image on the label
        original_image_label.config(image=photo)
        original_image_label.image = photo

# Create a function to convert the image to black and white without dithering
def convert_to_black_and_white():
    if 'original_image' in globals():
        bw_image = original_image.convert("1", dither=Image.NONE)
        bw_photo = ImageTk.PhotoImage(bw_image)

        # Display the black and white image on the label
        modified_image_label.config(image=bw_photo)
        modified_image_label.image = bw_photo

# Create a function to rotate the image by 90 degrees
def rotate_image90():
    if 'original_image' in globals():
        rotated_image = original_image.rotate(90)
        rotated_photo = ImageTk.PhotoImage(rotated_image)

        # Display the rotated image on the label
        modified_image_label.config(image=rotated_photo)
        modified_image_label.image = rotated_photo

def rotate_image180():
    if 'original_image' in globals():
        rotated_image = original_image.rotate(180)
        rotated_photo = ImageTk.PhotoImage(rotated_image)

        # Display the rotated image on the label
        modified_image_label.config(image=rotated_photo)
        modified_image_label.image = rotated_photo

def convert_to_GreyScale():
    if 'original_image' in globals():
        grayscale_image = original_image.convert("L")
        grayscale_photo = ImageTk.PhotoImage(grayscale_image)

        # Display the grayscale image on the label
        modified_image_label.config(image=grayscale_photo)
        modified_image_label.image = grayscale_photo

# Create a function to invert the colors of the image
def invert_image():
    if 'original_image' in globals():
        inverted_image = ImageOps.invert(original_image)
        inverted_photo = ImageTk.PhotoImage(inverted_image)

        # Display the inverted image on the label
        modified_image_label.config(image=inverted_photo)
        modified_image_label.image = inverted_photo

# Create a function for cropping the image based on user input
def crop_image_user_input():
    if 'original_image' in globals():
        crop_coords = simpledialog.askstring("Crop Image", "Enter crop coordinates (left, upper, right, lower):")
        try:
            left, upper, right, lower = map(int, crop_coords.split(','))
            cropped_image = original_image.crop((left, upper, right, lower))
            cropped_photo = ImageTk.PhotoImage(cropped_image)

            # Display the cropped image on the label
            modified_image_label.config(image=cropped_photo)
            modified_image_label.image = cropped_photo
        except ValueError:
            print("Invalid input. Please enter four integer values for the crop coordinates.")

# Create the main window
window = tk.Tk()
window.title("Image Uploader")

# Create a button to open the file dialog
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')

options_var = tk.StringVar()
options_var.set("Options")
options_menu = OptionMenu(window, options_var, "Convert to B&W", "Rotate 90°", "Rotate 180°", "GreyScale", "Invert Image")
options_menu.grid(row=0, column=1, padx=10, pady=10, sticky='w')

crop_button = tk.Button(window, text="Crop Image (User Input)", command=crop_image_user_input)
crop_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')

def handle_option(option):
    if option == "Convert to B&W":
        convert_to_black_and_white()
    if option == "Rotate 90°":
        rotate_image90()
    if option == "Rotate 180°":
        rotate_image180()
    if option == "GreyScale":
        convert_to_GreyScale()
    if option == "Invert Image":
        invert_image()

# Bind the option change event to the handler function
options_var.trace("w", lambda *args: handle_option(options_var.get()))

# Create a label to display the original image
original_image_label = tk.Label(window, text="Original Image")
original_image_label.grid(row=1, column=0, padx=10, pady=10)

# Create a label to display the modified image
modified_image_label = tk.Label(window, text="Modified Image")
modified_image_label.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

# Start the main event loop
window.mainloop()
