# Example Dockerfile
FROM python:3.7.2-alpine3.8

LABEL maintainer="nuttachot@hotmail.com"

RUN apk add --update git

WORKDIR /myapp

COPY . .

ARG my_var=my_default_value

ENTRYPOINT ["python", "./app/hello.py", "my_var"]

EXPOSE 8000

VOLUME /my_volume