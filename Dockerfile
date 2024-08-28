FROM ubuntu:18.04
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true
RUN apt-get update && \
    apt-get install -y python3 python3-pip
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

RUN apt-get update && \
    apt-get install -y apt-utils locales && \
    locale-gen en_US.UTF-8




WORKDIR /data
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python3-dev python3-pip postgresql-client postgresql-server-dev-10
RUN apt-get update && apt-get install -y python3-pip
RUN apt-get -y install curl zip unzip
RUN pip3 install --upgrade pip

# Preperation
COPY . /data/
# Run the application
CMD ["bash", "-c", "python3 ./pysitee/manage.py makemigrations && python3 ./pysitee/manage.py migrate && python3 ./pysitee/manage.py runserver 0.0.0.0:8000"]




