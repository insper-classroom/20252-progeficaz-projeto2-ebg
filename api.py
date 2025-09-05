from flask import Flask, redirect, request, render_template_string
import views


app = Flask(__name__)


@app.route('/imoveis', methods=['GET'])
def index():
    print(request)
    imoveis = views.index()
    return {"imoveis": imoveis}
    



if __name__ == '__main__':
    app.run(debug=True)