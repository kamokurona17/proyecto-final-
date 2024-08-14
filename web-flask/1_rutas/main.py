#llamar la libreria de flask 
from flask import Flask

# indicar variable principal 

app=Flask(__name__)

#rutas
#raiz
@app.route('/')
def principal ():
    return "esta es la hoja principal"

#otra paginas 
@app.route('/pagina_2')
def pagina2():
    return "esta es la mision de la pagina 2"

@app.route('/pagina_3')
def pagina3():
    return "esta es la mision de la pagina 3"

#@app.route(/)
#ejecutar servidores 

if __name__ == '__main__':
    app.run()


