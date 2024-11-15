FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install "fastapi[standard]" sqlalchemy
EXPOSE 8000/tcp
CMD ["python", "app.py"]