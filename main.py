
from flask_mail import *
from flask import *
import smtplib


app=Flask(__name__)

@app.route('/')
def Index():
    return  render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('index.html')

@app.route('/send_email/',  methods=['POST', 'GET'])
def send_email():
    message1=request.form['message']
    password1=request.form['pass']
    server= smtplib.SMTP('smtp.gmail.com')
    sender_email='cjs.sassy01@gmail.com'
    reciever_email=request.form["Email"]
    password='camsas01'
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message1)
    server.quit()
    return render_template('email.html')





if __name__=='__main__':
    app.run(debug=True)