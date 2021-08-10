FROM python:3.6.14-alpine

RUN pip install archerysec-cli

CMD ["archerysec-cli"]