FROM python:3.7
LABEL version="0.1.0"

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1

RUN echo "========== Iniciando la instalacion de dependencias========== "
RUN apt-get update -y -qq && apt-get install --auto-remove -y -qq \
    gdal-bin binutils libproj-dev libgdal-dev locales

RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && /usr/sbin/locale-gen
RUN echo " ========== moviendo los archivos  ========== "
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN echo " ========== Instalando dependencias  ========== "
RUN  pip install --no-cache-dir -r requirements.txt

CMD ["/bin/bash"]