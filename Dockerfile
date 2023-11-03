FROM python:3.8.17-bookworm
RUN apt update
RUN apt install -y apache2 apache2-dev nginx vim
