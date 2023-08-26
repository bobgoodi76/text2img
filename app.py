from flask import Flask, render_template, request
import text_to_image_generator  # Your text-to-image generation logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    image_url = text_to_image_generator.generate_image(prompt)  # Replace with your generator function

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
