# app.py

from flask import Flask, render_template, request

from prompt_enhancer import PromptEnhancer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_prompt = request.form.get('input_prompt')
        model = request.form.get('model', 'gpt-4o-mini')
        temperature = float(request.form.get('temperature', 0.0))

        if not input_prompt:
            error_message = "Please provide an input prompt."
            return render_template('index.html', error_message=error_message)

        enhancer = PromptEnhancer(model=model, temperature=temperature)

        try:
            # Since enhance_prompt is now synchronous
            advanced_prompt_data = enhancer.enhance_prompt(input_prompt, perform_eval=False)
            advanced_prompt = advanced_prompt_data["advanced_prompt"]
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('index.html', error_message=error_message)

        return render_template(
            'index.html',
            advanced_prompt=advanced_prompt,
            input_prompt=input_prompt,
            model=model,
            temperature=temperature
        )
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
