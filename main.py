from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
     return render_template ("/contactos/index.html")
 
@app.get("/contacto/<contactoId>/edit") 
def editarContacto(contactoId):
    return render_template ("/contactos/editar.html",contactoId=contactoId
 )
    
@app.get("/contacto/<int:edad>/edit") 
def editarContacto(edad):
    return render_template ("/contactos/edad.html",edad=edad 
                            
                            
 )
    
    
    #/edad/27

# http://localhost:5000/contacto/6/edit





app.run(debug=True)

   

