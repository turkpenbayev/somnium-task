# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/app

# install psycopg2
# RUN apt-get update \
#     && apt-get install -y build-essential \
#     && apt-get install -y python3-dev\
#     && apt-get install -y libpq-dev

# RUN pip install psycopg2

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
# CMD python manage.py runserver 0.0.0.0:$PORT 
