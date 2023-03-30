from flask import Flask, jsonify , request
import smtplib, ssl

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"Status" : "App running"})

@app.route('/mail', methods=['POST'])
def process_form():
    try:
        name = request.args.get('name', None)
        textmsg = request.args.get('message', None)
        usermail = request.args.get('email' , None)
        sender = "pratikbhor@bhors.com"
        password = "Ionoschap@ssw0rd"
            
        where_to_email = "pratikbhor95@gmail.com"
        theme = "Recruiters Enquiry"
        message = "message from "+name+" is : "+textmsg+" and email is : "+usermail
        print(message)
        sender_password = password
        context = ssl.create_default_context()
        session = smtplib.SMTP_SSL('smtp.ionos.co.uk', 465,context=context)
        print(session)
        session.login(sender, sender_password)
        msg = f'From: {sender}\r\nTo: {where_to_email}\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: {theme}\r\n\r\n'
        msg += message
        session.sendmail(sender, where_to_email, msg.encode('utf8'))
        if usermail:
            theme = "Thank you for reaching out to me"
            message = """Dear {name} , \r\n Thank you so much for reaching out to me. Your message means a lot to me, and I appreciate the time you took to connect.\r\n
            \rIt's always great to hear from someone, and I'm grateful for your thoughtfulness.\r\n\r\n 
            \rThanks again for thinking of me, and I look forward to staying in touch.\r\n\r\n
            \rRegards\r\n \rPratik Bhor\r\n \r07768390279"""
            msg = f'From: {sender}\r\nTo: {usermail}\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: {theme}\r\n\r\n'
            msg += message
            session.sendmail(sender, usermail, msg.encode('utf8'))
            session.quit()
            return jsonify({'msg' : 'Thank you for reaching out to me'})
        session.quit()
        return jsonify({'msg' : 'Thank you for reaching out to me'})
    except Exception as e:
        return({'msg' : "error" , 'error' : str(e)})

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=443)
