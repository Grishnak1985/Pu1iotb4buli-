from flask import Flask 


app = Flas(__name__) 


@app.route('/')
def index():
    return "Привет, мир!"
    
    
    app.run(port='8000')
   
