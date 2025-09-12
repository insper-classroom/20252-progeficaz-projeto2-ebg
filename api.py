from flask import Flask, redirect, request, render_template_string
import views


app = Flask(__name__)


@app.route('/imoveis', methods=['GET'])
def index():
    print(request)
    imoveis = views.index()
    imoveis = {"imoveis": imoveis}
    return render_template_string(views.index())

@app.route('/imoveis/<imovel_id>', methods=['GET'])
def get_imovel(imovel_id):
    print(request)
    imovel = views.get_imovel(imovel_id) 
    print(f'/'*50)
    print('API.PY - GET_IMOVEL')
    return imovel



if __name__ == "__main__":
    app.run(debug=True)
    