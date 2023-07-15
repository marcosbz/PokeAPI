FROM python:slim

RUN useradd pokeapi

WORKDIR /home/pokeapi

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY pokeapi.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP pokeapi.py

RUN chown -R pokeapi:pokeapi ./
USER pokeapi

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]