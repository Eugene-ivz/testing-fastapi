docker run --name postgres_test -p 5556:5432 -e POSTGRES_USER=test -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test_db -d postgres:16.2

# for asynchronous support
alembic init -t async migrations 

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload