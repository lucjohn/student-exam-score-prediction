FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["python", "application.py"]
