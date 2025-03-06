# llm_fe/Dockerfile

FROM python:3.12.2-slim

WORKDIR /app

RUN apt-get update  -y

COPY app/requirements.txt .

# requirements.txt 설치
RUN pip3 install --no-cache-dir -r requirements.txt

# 파일 복사
COPY app/ .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["streamlit", "run","app.py", "--server.port=8501", "--server.address=0.0.0.0"]