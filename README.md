# Video Platform

A bespoke video hosting platform built with Django and Django REST Framework.

## Features

- User authentication (signup, login, password reset)
- Video upload and management
- Video navigation (next/previous)
- Share links for videos
- Admin panel for content management

## Setup

1. Clone the repository:
git clone https://github.com/PM-Devs/videoplatform.git
cd videoplatform
2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install the requirements:
pip install -r requirements.txt
4. Run migrations:
python manage.py migrate
5. Create a superuser:
python manage.py createsuperuser
6. Run the development server:
## API Endpoints

- `/api/users/`: User management
- `/api/videos/`: Video management
- `/api/videopages/`: Video page management
- `/api/sharelinks/`: Share link management

## Testing

Run the tests using:
python manage.py test
## Deployment

For production deployment, make sure to:

1. Set `DEBUG = False` in settings.py
2. Use a production-grade database (e.g., PostgreSQL)
3. Set up proper static and media file serving
4. Use a production ASGI server like Daphne or Uvicorn
5. Set up proper security measures (HTTPS, secure cookies, etc.)

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

below must be added: permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]