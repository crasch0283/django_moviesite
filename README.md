# Django Movie Site

This project is a small Django application for storing movies. It now follows a conventional Django layout:

```
root/
├── app/            # Django application
├── config/         # Django project configuration
├── manage.py       # Management script
├── requirements.txt
```

`.idea/` directories have been removed from version control and a project wide `.gitignore` was added.

## GitHub OAuth Callback

GitHub OAuth is provided using `social-auth-app-django`. When configuring the OAuth application on GitHub use the following callback URL:

```
http://<host>/oauth/complete/github/
```

The `/oauth/` prefix matches the URL configuration in `config/urls.py`.

## Local Environment Variables

Create a `.env` file based on `.env.example` and provide your GitHub OAuth
credentials:

```
cp .env.example .env
# then edit .env to add your values
```

The application will load these variables automatically when it starts.
