FROM docker.io/python:3.11
LABEL authors="aiquen"

RUN groupadd -g 142 webgroup
RUN useradd -u 142 -m -d /app -r -s /sbin/nologin webuser

COPY --chown=142:142 main.py requirements.txt /app/

WORKDIR /app
USER webuser

RUN pip install -r requirements.txt

EXPOSE 8083

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]