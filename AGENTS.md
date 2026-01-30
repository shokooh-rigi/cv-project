# AGENTS.md

This repo is a **Django 4.2 + Django REST Framework** project (`djangoProject/`) with one main app: `cv_app/`.

## Quickstart (local/dev)

- **Create and activate a venv**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- **Install dependencies**

```bash
python3 -m pip install -r requirements.txt
```

- **Migrate DB (SQLite by default)**

```bash
python3 manage.py migrate
```

- **Run the server**

```bash
python3 manage.py runserver
```

## Common commands

- **Create migrations**

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

- **Run tests (Django test runner)**

```bash
python3 manage.py test
```

Notes:
- `cv_app/tests.py` exists but is currently empty.
- There is also a test file under `cv_app/test/` that is named with **leading spaces** (`"    tests.py"`). Django’s default test discovery will likely ignore it; prefer adding tests under a normal `tests.py` / `tests/` layout.

## Project layout and conventions

- **Project settings**: `djangoProject/settings.py`
- **Project URL routing**: `djangoProject/urls.py`
  - Currently only routes `/admin/`. If you want the app API exposed, include `cv_app.urls` here (typical Django pattern: `path("", include("cv_app.urls"))`).
- **App URL routing + API docs**: `cv_app/urls.py`
  - JWT endpoints: `/api/token/`, `/api/token/refresh/`
  - Swagger/Redoc (when included in root URLs): `/api/docs/`, `/api/redoc/`
  - ViewSets registered via DRF router (biography/educations/certificates/skills).
- **Models/serializers/views**:
  - `cv_app/models.py`, `cv_app/serializers.py`, `cv_app/views.py`
- **Auth**:
  - DRF auth is configured for **JWT** in `REST_FRAMEWORK` settings.
  - Custom user model is set via `AUTH_USER_MODEL = "cv_app.User"`.

## Making changes safely

- **Migrations**: any model change that affects DB schema should include a migration under `cv_app/migrations/`.
- **URLs**: if you add endpoints, update `cv_app/urls.py` (and ensure it is included from `djangoProject/urls.py` if needed).
- **API changes**: keep serializers and viewsets aligned (validation should live in serializers/validators; business logic in `utils.py` as appropriate).
- **Tests**: prefer `python3 manage.py test` compatible tests; avoid introducing non-standard test file names/paths.

