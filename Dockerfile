FROM python:slim-bullseye

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "sql_app.main:app"]
