from flask import Flask, request, jsonify,render_template_string
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'itsriteshmahale2002@gmail.com'
app.config['MAIL_PASSWORD'] = 'jduq xhqz tizb xviq'
app.config['MAIL_PORT'] = 465  # Use port 465 for SMTP over SSL
app.config['MAIL_USE_SSL'] = True  # Use SSL encryption

mail = Mail(app)

email_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drowsiness Detection Alert</title>
    <style>
        /* Reset styles */
        body, h1, p {
            margin: 0;
            padding: 0;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }
        /* Container */
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        /* Header */
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .header h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 10px;
        }
        /* Content */
        .content {
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        .content p {
            color: #666;
            font-size: 16px;
            line-height: 1.5;
        }
        /* Button */
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
        }
        /* Alert */
        .alert {
            background-color: #ff9999;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .alert p {
            color: #cc0000;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Drowsiness Detection Alert</h1>
            <p>Attention Required!</p>
        </div>
        <div class="content">
            <div class="alert">
                <p>A drowsiness detection system has detected signs of driver fatigue. Please take necessary precautions and avoid driving if feeling drowsy.</p>
            </div>
            <p>{{ message }}</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    if not recipient or not subject or not body:
        return jsonify({'message': 'Missing recipient, subject, or body in request'}), 400

    try:
        html_content = render_template_string(email_template, message=body)
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.html = html_content
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
