"""
Program for getting text from meme.
"""

import vendor
vendor.add("lib")

import sys
import requests
import pytesseract
from PIL import Image
from StringIO import StringIO


"""
Convert the image to black and white to
make the white text stand out more.

This usually helps with extracting the text
since the text is usually white.
"""
def darken_background(img, limit=255):
	img = img.convert('L') # Create lookup table of rgb values
	img = img.point(lambda x: 0 if x<limit else 255, '1') # Change each point
	return img


"""
Get the image from the url
"""
def get_image(url, darken=True):
	try:
		if "http" in url:
			img = Image.open(StringIO(requests.get(url).content))
		else:
			img = Image.open(url)
	except IOError:
		return None

	if darken:
		img = darken_background(img)

	# Prevent IOError: cannot write mode RGBA as BMP
	# Fix by ignoring the alpha value
	if len(img.split()) == 4:
	    r,g,b,a = img.split()
	    img = Image.merge("RGB", (r,g,b))
	return img


"""
Extract the text from the image object
"""
def get_text_from_img(img):
	return pytesseract.image_to_string(img)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        image = get_image(sys.argv[1])
        if not image:
        	print "URL is invalid"
        else:
        	image.save("result.png")
        	print get_text_from_img(image)