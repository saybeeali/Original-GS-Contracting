# Original-GS-Contracting

https://original-gs-contracting.fly.dev/

That sounds like a great project! Here's a template you can use for your README file to effectively showcase the website you built for Original GS Contracting using Python and Django:

# Original GS Contracting Website

Welcome to the Original GS Contracting website repository. This website was built to showcase the services provided by Original GS Contracting and provide an easy way for users to get in touch. Additionally, it includes a SQL database to manage customer information and track the company's daily work.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Original GS Contracting is a construction company specializing in a wide range of services, and this website serves as a digital showcase of their work. The primary goals of this website are:

- Display the company's portfolio and showcase completed projects.
- Provide a contact page for users to reach out for inquiries or estimates.
- Manage customer information and track daily work through an SQL database.

## Features

- **Home Page**: A welcoming landing page that highlights the company's services and a slideshow of their completed projects.
- **Portfolio**: A gallery of completed projects, complete with descriptions and images.
- **Contact Page**: A contact form for users to get in touch with the company.
- **Admin Panel**: Secure access for administrators to manage customer information and daily work records.
- **SQL Database**: A database to store customer details and track work history.

## Technologies Used

- Python: The programming language used for the backend logic.
- Django: The web framework used to develop the website.
- SQL Database: Used to store customer information and work records.
- HTML/CSS: Frontend development for website structure and styling.
- JavaScript: Used for interactive elements and client-side functionality.

## Getting Started

To run this website locally or on a server, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/original-gs-contracting.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your database configurations in `settings.py`.

4. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account for accessing the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the website locally at [http://localhost:8000](http://localhost:8000) and the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin).

## Usage

1. Visit the website's home page to explore the company's portfolio.
2. Navigate to the Contact Page to submit inquiries or requests for estimates.
3. For administrators, access the Admin Panel to manage customer information and daily work records.

## Database

The SQL database attached to this website is used to store customer information and daily work records. You can access and manage the database through the Django admin panel.

## Contributing

Contributions to improve this project are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for using and contributing to the Original GS Contracting website project! If you have any questions or need further assistance, please don't hesitate to reach out.
