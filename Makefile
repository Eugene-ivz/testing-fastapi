# Docker Compose Commands
up:
	docker-compose up -d

down:
	docker-compose down -v

build:
	docker-compose build

# Alembic Commands
migrate:
	alembic upgrade head

makemigrations:
	alembic revision --autogenerate -m "$(message)"

downgrade:
	alembic downgrade -1

# Run FastAPI App Locally
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run Tests
test:
	pytest -vv

.PHONY: up down build logs migrate makemigrations downgrade run test