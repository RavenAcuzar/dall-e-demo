from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/generate-image', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    openai.organization = os.getenv("OPENAI_ORG_ID")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        # Call OpenAPI to generate image based on prompt
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256",
        )
        image_data = response["data"][0]["url"]
        return render_template('index.html', image_data=image_data, error=None)
    except:
        # Handle any errors that may occur when calling the OpenAPI endpoint
        return render_template('index.html', image_data=None, error=str(e))

if __name__ == '__main__':
    app.run()