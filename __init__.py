# Call vendor to add the dependencies to the classpath
import vendor
vendor.add('lib')


# Import the Flask Framework
from flask import Flask, render_template, request
app = Flask(__name__)


from ocr import get_text_from_img, get_image


@app.route('/')
def index():
	return render_template("index.html")


@app.route("/extract")
def extract_route():
	url = request.args.get("url")
	if not url:
		return ""
	else:
		img = get_image(url)
		text = get_text_from_img(img)
		return text


if __name__ == '__main__':
    app.run()