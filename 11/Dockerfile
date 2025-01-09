FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000/tcp
CMD ["python", "app.py"]