FROM ubuntu:bionic
LABEL version="2.1.2"

ENV PYTHONUNBUFFERED 1
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    LC_TYPE=en_US.UTF-8 \
    PYTHONIOENCODING=utf-8

RUN echo "========== Iniciando la instalacion de dependencias========== "
RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl \
    ca-certificates \
    wget build-essential\
    # python basic libs
    python3.7 python3.7-dev python3.7-venv gettext \
    python3.7-pip  python-enchant \
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev

RUN echo " ========== moviendo los archivos  ========== "
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/
RUN  pip2 install --no-cache-dir -r requirements.txt



CMD ["/bin/bash"]