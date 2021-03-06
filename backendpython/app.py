from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_cors import CORS, cross_origin
from json import dumps
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from datetime import datetime

app = Flask(__name__)
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/',methods=['POST'])
def agregarInteresado():
    nombres = request.get_json()["nombres"]
    correo = request.get_json()["correo"]
    return validarDatos(nombres,correo)

def validarDatos(nombres, correo):
    if not len(nombres):
        return {"nombres": nombres, "correo": correo,
                "status": 400, "mensaje": "Ingrese su nombre"}

    if not len(correo):
        return {"nombres": nombres, "correo": correo,
                "status": 400, "mensaje": "Ingrese su correo"}

    #enviarCorreo(nombres,correo)
    return {"nombres": nombres, "correo": correo,
            "status": 200, "mensaje": "Gracias por registrarse"}

def enviarCorreo(nombres,correo):
    crearmensaje(nombres,correo)
    mensaje = MIMEMultipart("plain")
    mensaje["From"]="360aplicacion@gmail.com"
    mensaje["To"]= "joseguzman@upeu.edu.pe"
    mensaje["Subject"] ="Correo de interesado - Moon Team"
    adjunto = MIMEBase("application","octect-stream")
    adjunto.set_payload(open("interesado.txt","rb").read())
    adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
    mensaje.attach(adjunto)
    smtp = SMTP("smtp.gmail.com")
    #smtp.gmail.com for google accounts
    #smtp.yahoo.com for yahoo accounts
    smtp.starttls()
    smtp.login("360aplicacion@gmail.com","360aplicacion123")
    smtp.sendmail("360aplicacion@gmail.com","kevinsoras@upeu.edu.pe",mensaje.as_string())
    smtp.quit()

def crearmensaje(nombres,correo):
    now = datetime.now()
    with open("interesado.txt","w") as File:
        File.write("Nombre del interesado : "+nombres+"\n")
        File.write("Correo del interesado : "+correo+"\n")
        File.write("Hora de registro : "+str(now))

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)