FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./fi /app/fi

WORKDIR /app/fi

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]