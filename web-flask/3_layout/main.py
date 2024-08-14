from flask import Flask,render_template

app=Flask(__name__)

#rutinas 
#pagnas principal 

@app.route('/')
def principal():
    return render_template('home.html')


# pagina de mision 
@app.route('/mision')
def mision ():
    return render_template('mision.html')



#ejecutar el servidor 
if __name__=='__main__':
    app.run(debug=True)
    
# debug=true
