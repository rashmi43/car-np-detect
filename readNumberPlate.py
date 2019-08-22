import argparse
import detect

parser = argparse.ArgumentParser()
parser.add_argument("Image_File")  # Here we are reading the image path and name
args = parser.parse_args()
# print(args.Image_File)
print(detect.read_image(args.Image_File))
