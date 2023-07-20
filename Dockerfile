FROM python:slim

ARG ARG_POKEAPI_BERRY_BASE_URL

RUN useradd pokeapi

WORKDIR /home/pokeapi

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY . .
RUN chmod +x boot.sh

ENV FLASK_APP pokeapi.py
ENV POKEAPI_BERRY_BASE_URL=$ARG_POKEAPI_BERRY_BASE_URL

RUN chown -R pokeapi:pokeapi ./
USER pokeapi

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]