FROM python:3.11 as build-base-python

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN python3 -m venv /app/venv && \
    ./venv/bin/pip3 install --upgrade pip && \
    ./venv/bin/pip3 install -r /app/requirements.txt

COPY ./ /app/

FROM python:3.11 as run
WORKDIR /app
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    groupadd --gid 2000 app && \
    useradd -rm -d /home/app -s /bin/bash -g app -u 2000 app

COPY --from=build-base-python --chown=app:app /app /app
RUN chown app:app /app

USER app
EXPOSE 8501
CMD ["./venv/bin/streamlit", "run", "main.py"]