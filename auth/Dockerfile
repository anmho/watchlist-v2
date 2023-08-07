FROM watchlist-base:latest

WORKDIR /usr/src/auth/

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt install -y protobuf-compiler

WORKDIR /usr/src/auth/src/proto
RUN ./generate.sh

WORKDIR /usr/src/auth

EXPOSE 5002

# RUN ["python", "-m", "src.models.create_tables"]

# CMD ["python", "main.py"]

RUN chmod +x ./start.sh

CMD ["./start.sh"]