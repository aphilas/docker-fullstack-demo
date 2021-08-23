```bash
# prod - nginx and gunicorn
docker-compose up -f docker-compose.prod.yml

#dev - inbuilt flask werkzeug server with docker volumes
docker-compose up
```
## Goal
Run an nginx reverse proxy to serve both frontend and backend (under `/api`)

## Backend
Flask and Postgres with SQLAlchemy

Requirements:
- Poetry

## Frontend
React with multistage build -> Nginx image with static files
