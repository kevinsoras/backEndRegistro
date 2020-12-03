FROM python:3.8.5-alpine

# nuevo
# instalando dependencias
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# estableciendo direcetorio de trabajo
WORKDIR /usr/src/app


# agregando app
COPY . /usr/src/app

# nuevo
# ejecutar server
CMD ["python app.py run -h 0.0.0.0"]