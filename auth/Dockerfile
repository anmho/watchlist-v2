FROM watchlist-base:latest

WORKDIR /app
COPY . /app

EXPOSE 5002
RUN pip install -r requirements.txt

# RUN python -m app.models.utils.create_tables

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]