from PIL import Image
from simpleimage import SimpleImage
BRIGHT_THRESHOLD = 195
DEFAULT_FILE = r'C:\Users\HERMEHAR BEDI\OneDrive\Desktop\Hermehar\Programming\Python\Fire\FF6.jfif'

def get_file():
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def get_avg(pixel):
    return (pixel.red + pixel.green + pixel.blue) // 3

def grayscale(filename):
    for pixel in filename:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return filename

def fire(filename):
    for pixel in filename:
        pixel_avg = get_avg(pixel)
        if pixel.red >= BRIGHT_THRESHOLD:
            pixel.red = pixel_avg * 2
            pixel.green = 0
            pixel.blue = 0
    return filename

def main():
    filename = get_file()
    filename = SimpleImage(filename)
    filename.show()
    grayscale_filename = grayscale(filename)
    grayscale_filename.show()
    final_output = fire(filename)
    final_output.show()


if __name__ == '__main__':
    main()
