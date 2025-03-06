# backend.Dockerfile

FROM python:3.12.2-slim

WORKDIR /home

RUN apt-get update && apt install sqlite3 -y

COPY backend/requirements.txt .

# requirements.txt 설치
RUN pip3 install --no-cache-dir -r requirements.txt

# 파일 복사
COPY backend/ .

EXPOSE 8000




ENTRYPOINT ["python", "main.py"]