from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mail import Mail, Message
import os
import secrets
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')

mail = Mail(app)

# In-memory storage for demo (use database in production)
users = {}
email_verification_tokens = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_newsletter', methods=['POST'])
def send_newsletter():
    if request.method == 'POST':
        email = request.form['newsletter_email']
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return jsonify({'success': False, 'message': 'Invalid email address'})
        
        try:
            msg = Message(
                'Welcome to AFRI-CONNECT MEDIA Newsletter',
                sender=app.config['MAIL_USERNAME'],
                recipients=[email]
            )
            msg.body = f'''
            Hello,
            
            Thank you for subscribing to AFRI-CONNECT MEDIA newsletter!
            
            You will now receive updates about our latest projects, services, and industry insights.
            
            Best regards,
            AFRI-CONNECT MEDIA Team
            '''
            
            mail.send(msg)
            return jsonify({'success': True, 'message': 'Newsletter subscription successful!'})
            
        except Exception as e:
            return jsonify({'success': False, 'message': 'Error sending newsletter. Please try again.'})

@app.route('/contact_form', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        try:
            # Send email to company
            msg = Message(
                f'Contact Form: {subject}',
                sender=app.config['MAIL_USERNAME'],
                recipients=[app.config['MAIL_USERNAME']]
            )
            msg.body = f'''
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            '''
            
            mail.send(msg)
            
            # Send confirmation to user
            confirmation_msg = Message(
                'Thank you for contacting AFRI-CONNECT MEDIA',
                sender=app.config['MAIL_USERNAME'],
                recipients=[email]
            )
            confirmation_msg.body = f'''
            Hello {name},
            
            Thank you for contacting AFRI-CONNECT MEDIA!
            
            We have received your message and will get back to you within 24 hours.
            
            Your message:
            {message}
            
            Best regards,
            AFRI-CONNECT MEDIA Team
            '''
            
            mail.send(confirmation_msg)
            
            return jsonify({'success': True, 'message': 'Message sent successfully!'})
            
        except Exception as e:
            return jsonify({'success': False, 'message': 'Error sending message. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True)
