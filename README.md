# Chris Hoang — Portfolio API

FastAPI + SQLAlchemy + PostgreSQL backend for [chrishoang.dev](https://chrishoang.dev) (frontend repo: `chris-hoang-portfolio-frontend`).

## Endpoints

- `GET /api/health`
- `GET /api/projects` — list all projects
- `GET /api/projects/{slug}` — single project
- `POST /api/contact` — submit a contact message `{name, email, message}`

## Local development

```bash
docker compose up --build
```

API available at `http://localhost:8000`, interactive docs at `http://localhost:8000/docs`.

To seed/update the project list (edit `app/seed.py`, then re-run — it's an idempotent upsert):

```bash
docker compose exec api python -m app.seed
```

## Environment variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string (Railway injects this automatically when a Postgres plugin is attached) |
| `CORS_ORIGINS` | Comma-separated list of allowed frontend origins |

## Deployment

Deployed on [Railway](https://railway.app) from a `Dockerfile`. Railway sets `PORT` automatically; the container reads it via `${PORT:-8000}`.
