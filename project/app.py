from flask import Flask, render_template, request
from cat_detection import perform_cat_detection

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # Получаем загруженный файл из формы.
    uploaded_file = request.files['file']

    # Сохраняем загруженный файл на сервере.
    file_path = 'static/images/input_image.jpg'
    uploaded_file.save(file_path)

    # Выполняем распознавание котов
    output_image_path = perform_cat_detection(file_path)

    # Передаем пути к изображениям в шаблон result.html.
    return render_template('result.html', input_image_path=file_path, output_image_path=output_image_path)


if __name__ == '__main__':
    app.run()
