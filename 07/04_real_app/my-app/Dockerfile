FROM python:3.11
WORKDIR /app
RUN pip install "fastapi[standard]" 
COPY . /app
EXPOSE 8000/tcp
CMD ["python", "app.py"]