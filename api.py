from flask import Flask, redirect, request
import views


app = Flask(__name__)


@app.route('/imoveis', methods=['GET'])
def index():
    print(request)
    imoveis = views.index()
    return imoveis


@app.route('/imoveis/<imovel_id>', methods=['GET'])
def get_imovel(imovel_id):
    print(request)
    imovel = views.get_imovel(imovel_id) 
    return imovel



    



if __name__ == "__main__":
    app.run(debug=True)
    