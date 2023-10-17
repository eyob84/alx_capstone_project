from flask import Flask, render_template,url_for, request, redirect
from flask_mail import Mail,Message
app = Flask(__name__)


app.config['SECRET_KEY'] = "tsfyguaistyatuis589566875623568956"

app.config['MAIL_SERVER'] = "smtp.googlemail.com"

app.config['MAIL_PORT'] = 587

app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = "eyobabebe28@gmail.com"

app.config['MAIL_PASSWORD'] = "gymf mrus moxp mpxd"
    # server.login('eyobabebe28@email.com', 'gymf mrus moxp mpxd')  # Provide your email and password

mail = Mail(app)


n=1

prjs = [
    {"id":1,
    "description":"blah blah blah",
    "title":"title 1"
    },
     {"id":2,
    "description":"blah blah blah",
    "title":"title 2"
    }, {"id":3,
    "description":"blah blah blah",
    "title":"title 3"
    }
]
sks=['sa','sadas']
# number_template/<int:n>
@app.route('/', strict_slashes=False,methods=['GET'])
def home():
    return render_template('index.html', number=n)

@app.route('/about', strict_slashes=False,methods=['GET'])
def about():
    return render_template('about.html', number=n)
@app.route('/projects', strict_slashes=False,methods=['GET'])
def projects():
    return render_template('projects.html', projects=prjs)
@app.route('/projects/<int:x>', strict_slashes=False,methods=['GET'])
def project(x):
    return render_template('project.html', project = prjs[x-1])
@app.route('/skills', strict_slashes=False,methods=['GET'])
def skills():
    return render_template('skills.html', skills=sks)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate the form data
        if not name or not email or not message:
            return "All fields are required. Please go back and fill in all the fields."

        # Send an email notification
        try:
            send_email(name, email, message)
            return render_template('sent.html')

        except Exception as e:
            print("failed")
            render_template('failed.html')


        # return "Thank you for your message. We will get back to you soon."

    return render_template('contact.html')

def send_email(name, email, message):
	msg_title = "contact us submission from portfolio"
	sender = "noreply@app.com"
	msg = Message(msg_title,sender=sender,recipients=["eyobabebe28@gmail.com"])
	msg_body = f"This is the email {email}\n  name:{name}\n message:{message}"
	msg.body = "test body"
	data = {
		'app_name': "portfolio",
		'title': msg_title,
		'body': msg_body
	}

	msg.html = render_template("email.html",data=data)

	try:
		mail.send(msg)
		return "Email sent..."
	except Exception as e:
		print(e)
		return f"the email was not sent {e}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


__doc__ = """
this is documentation for my module
"""    
