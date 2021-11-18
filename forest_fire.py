from tkinter import *                                       #importing files
from tkinter import filedialog
from PIL import Image, ImageTk
from simpleimage import SimpleImage

BRIGHT_THRESHOLD = 195
DEFAULT_FILE = r'C:\Users\HERMEHAR BEDI\OneDrive\Desktop\Hermehar\Programming\Python\Fire\FF5.jfif'

root = Tk()                                                 #giving title and heading
root.title("Forest Fire Detector")
label = Label(root, text = "Forest Fire Detector", fg = "purple").grid(row = 0,column = 2)

def get_file():                                             #input file function
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def compute_luminosity(red, green, blue):                   #calculate the luminosity 
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def get_avg(pixel):                                         #calculate average pixels
    return (pixel.red + pixel.green + pixel.blue) // 3

def grayscale(filename):                                    #transform the image into grayscale
    for pixel in filename:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return filename

def fire(filename):                                        #identify the fire in the image 
    for pixel in filename:
        pixel_avg = get_avg(pixel)
        if pixel.red >= BRIGHT_THRESHOLD:
            pixel.red = pixel_avg * 2
            pixel.green = 0
            pixel.blue = 0
    return filename

def open_file():                                        #opening a file
    root.filename = filedialog.askopenfilename(initialdir = r"C:\Users\Lenovo\Desktop\Hermehar", title = "Select File to open", filetypes = (("Jpeg images","*.jpg"),("Png images","*.png"),("All files","*.*")))

def layout():                                           #entry fields
    
    l1 = Label(root, text = "Please select a jpeg or png file").grid(row = 1, column = 1)

    open_filename_button = Button(root, text = "Select File", command = open_file, fg = "#33FFCA", bg = "black").grid(row = 1, column = 2)
  

def cancel_button():                                        #cancel nutton to quit the program
    quit()


def submit_button():                                    #defining submit button
    open_layout = layout()                              #calling the layout function to give layout of the program
    filename = root.filename                            #opening directory for selecting a file
    filename = SimpleImage(filename)                    #selecting a file
    filename.show()                                     #display original image
    grayscale_filename = grayscale(filename)            #convert image into grayscale
    grayscale_filename.show()                           #show the grayscaled image
    final_output = fire(filename)                       #find the fire in an image
    final_output.show()                                 #show the image with fire marked in it 


submit_button = Button(root, text = "Open", command = submit_button, fg = "#33FFCA", bg = "black").grid(row = 15, column = 1)
cancel_button = Button(root, text =  "Close", command = cancel_button, fg = "#33FFCA", bg = "black").grid(row = 15, column = 2)

root.mainloop()                                              #ending the document
