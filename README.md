# Extracting text from memes
Since most memes use the same font, all you do is train Google's [Tesseract OCR](https://github.com/tesseract-ocr) with this font and use it on these memes.


![Sample text](http://cf.chucklesnetwork.com/items/7/7/4/7/6/original/meme-text-impact-font-with-outline.jpg)
```sh
$ python ocr.py http://cf.chucklesnetwork.com/items/7/7/4/7/6/original/meme-text-impact-font-with-outline.jpg
MEME TEXT

IMPACT FONT WITH
OUTLINE
```


## Setup
```sh
$ source setup.sh # This may take a very long time
$ source app.sh
```

## Usage
You can pass an image or URL to an image as the first argiment to `ocr.py` and run it on the command line. The resulting image is saved into `result.png`.
```sh
$ python ocr.py https://i.imgur.com/YzMXGdQ.jpg
WALKER TOLD US

 

WE HAVE AIDS
```

You can also run a Flask server on localhost.
```sh
$ python __init__.py
```


## Resources
- [Setting up a simple OCR server](https://realpython.com/blog/python/setting-up-a-simple-ocr-server/)
  - Much of the instructions are here
- [https://github.com/johnlinp/meme-ocr](Meme-ocr)
  - This guy already had the trained data that I just took from him
- [Minimal Theme](https://github.com/orderedlist/minimal)