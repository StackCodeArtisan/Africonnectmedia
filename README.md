# AFRI-CONNECT MEDIA Website

A professional media production company website built with Flask, Bootstrap, and modern web technologies.

## Features

- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **Email Authentication**: User registration and login with email verification
- **Email Automation**: Newsletter subscription and contact form automation
- **Modern UI**: Clean, professional design with smooth animations
- **Multi-page Structure**: Home, About, Services, Team, Work, Clients, Partners, Contact
- **Interactive Elements**: Smooth scrolling, form validation, and dynamic content

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
- **Email**: Flask-Mail for email automation
- **Styling**: Custom CSS with modern design patterns
- **Icons**: Font Awesome 6

## Project Structure

```
AFRICONNECTMEDIA/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── services.html     # Services page
│   ├── team.html         # Team page
│   ├── work.html         # Work/Portfolio page
│   ├── clients.html      # Clients page
│   ├── partners.html     # Partners page
│   ├── contact.html      # Contact page
│   ├── login.html        # Login page
│   └── register.html     # Registration page
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Custom CSS
    ├── js/
    │   └── main.js       # JavaScript functionality
    └── images/           # Image assets
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone/Download the Project

```bash
cd C:\Users\idowu\Desktop\AFRICONNECTMEDIA
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Email Settings

1. Create a `.env` file in the project root:
```env
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

2. For Gmail, you'll need to:
   - Enable 2-factor authentication
   - Generate an App Password
   - Use the App Password in the `.env` file

### Step 4: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Configuration

### Email Configuration

Update the email settings in `app.py`:

```python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')
```

### Customization

1. **Company Information**: Update company details in templates
2. **Styling**: Modify `static/css/style.css` for custom styling
3. **Content**: Edit HTML templates to match your content
4. **Images**: Add your images to `static/images/`

## Features Overview

### Authentication System
- User registration with email verification
- Secure login/logout functionality
- Session management
- Password validation

### Email Automation
- Newsletter subscription
- Contact form automation
- Email verification system
- Automated responses

### Responsive Design
- Mobile-first approach
- Bootstrap 5 components
- Custom CSS animations
- Smooth scrolling effects

### Interactive Elements
- Form validation
- AJAX form submissions
- Dynamic content loading
- Smooth animations

## Pages Overview

1. **Home**: Hero section, services overview, about preview
2. **About**: Company information, mission, vision, values
3. **Services**: Detailed service descriptions and offerings
4. **Team**: Team member profiles and information
5. **Work**: Portfolio and project showcase
6. **Clients**: Client testimonials and success stories
7. **Partners**: Strategic partnerships and collaborations
8. **Contact**: Contact form and company information

## Development

### Adding New Pages

1. Create HTML template in `templates/`
2. Add route in `app.py`
3. Update navigation in `base.html`

### Styling Changes

- Modify `static/css/style.css` for custom styling
- Use CSS variables for consistent theming
- Follow Bootstrap 5 conventions

### JavaScript Features

- All JavaScript is in `static/js/main.js`
- Modular functions for different features
- Event listeners and AJAX requests

## Deployment

### Production Considerations

1. **Database**: Replace in-memory storage with a proper database
2. **Security**: Implement proper password hashing
3. **Environment**: Use environment variables for sensitive data
4. **SSL**: Enable HTTPS for production
5. **Email**: Configure production email service

### Recommended Hosting

- **Heroku**: Easy Flask deployment
- **DigitalOcean**: VPS hosting
- **AWS**: Scalable cloud hosting
- **PythonAnywhere**: Python-focused hosting

## Support

For questions or issues:
1. Check the code comments
2. Review Flask documentation
3. Check Bootstrap 5 documentation
4. Contact the development team

## License

This project is created for AFRI-CONNECT MEDIA. All rights reserved.

---

**Note**: This is a demo application. For production use, implement proper security measures, database integration, and error handling.
# Africonnectmedia
# Africonnectmedia
