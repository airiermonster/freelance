# Group 8 Freelance Platform

<div align="center">
  <img src="media/atcLogo.png" alt="ATC Logo" width="200"/>
  <h2>Python Programming Module Assignment</h2>
  <h3>NTA Level 7-1 Semester 2, 2025</h3>
  <p>Arusha Technical College (ATC), Tanzania</p>
</div>

## Logo Usage Disclaimer

The Arusha Technical College (ATC) logo used in this project is the intellectual property of Arusha Technical College. Its use in this project is strictly for academic purposes as part of our coursework submission. All rights, trademarks, and intellectual property associated with the logo remain the exclusive property of Arusha Technical College. Any unauthorized use, reproduction, or distribution of this logo outside the context of this academic project is strictly prohibited.

## Project Overview

A comprehensive freelance platform developed as a group assignment by Group Number 8 at Arusha Technical College (ATC). This platform aims to connect freelancers with clients in a user-friendly and efficient manner.

## Team Members

### Group Number 8
1. Maximilian Urio
2. Majaliwa Raymond
3. Minhajj Minhajj
4. Daniel Mbwambo
5. Samweli James
6. Irene Mwembe
7. Irene Denis
8. Miriam Msigwa

## Project Setup

### Prerequisites
- Python 3.8 or higher
- MySQL 5.7 or higher
- pip (Python package manager)
- common sense 😁

### Detailed Installation Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/airiermonster/freelance.git
   cd freelance
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**
   
   a. Start MySQL server if not already running
   
   b. Create the database:
   ```sql
   mysql -u root -e "CREATE DATABASE IF NOT EXISTS group8;"
   ```
   
   Note: If your MySQL installation has a password, use:
   ```sql
   mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS group8;"
   ```

4. **Environment Configuration:**
   
   a. Copy the example environment file:
   ```bash
   copy .env.example .env  # On Windows
   # OR
   cp .env.example .env    # On Linux/Mac
   ```
   
   b. Update the `.env` file with your database credentials:
   ```plaintext
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DB_NAME=group8
   DB_USER=root
   DB_PASSWORD=your-password  # Leave empty if no password
   DB_HOST=localhost
   DB_PORT=3306
   ```

5. **Initialize the Database:**
   ```bash
   # Create database tables
   python manage.py migrate
   
   # Create an admin user
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

   The site will be available at:
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

### Troubleshooting

If you encounter any issues:

1. **Database Connection:**
   - Ensure MySQL is running
   - Verify database credentials in `.env`
   - Check if the database exists

2. **Server Not Starting:**
   - Check if port 8000 is available
   - Ensure all requirements are installed
   - Verify Python version compatibility

3. **Static Files Not Loading:**
   ```bash
   python manage.py collectstatic
   ```

## Project Structure

```
freelance/
├── freelance_platform/    # Main project directory
│   ├── settings.py       # Project settings
│   ├── urls.py          # URL configurations
│   └── wsgi.py          # WSGI configurations
├── static/              # Static files
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
├── templates/          # HTML templates
├── media/              # User-uploaded files
├── requirements.txt    # Project dependencies
├── manage.py          # Django management script
└── .env              # Environment variables
```

## Features

- Modern and responsive design
- MySQL database integration
- Customized admin interface
- Static file handling
- Environment-based configuration
- Timezone set to Africa/Dar_es_Salaam

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request
5. Wait for review and approval

## Academic Integrity

This project is submitted as part of the Python Programming Module assessment at Arusha Technical College. All work presented is the original work of Group Number 8 members.

## Contact

For any inquiries about this project, please contact:
- Any Group Number 8 Member listed above
- Python Programming Module
- NTA Level 7-1, Semester 2, 2025
- Arusha Technical College (ATC)
- Arusha, Tanzania

## License

© 2025 Group Number 8, Arusha Technical College. All rights reserved.

The project codebase is the work of Group Number 8, while institutional branding elements including but not limited to the ATC logo, name, and associated trademarks are the property of Arusha Technical College. 