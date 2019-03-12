FROM python:3.7.2
COPY . /code
WORKDIR /code
RUN pip install -r dependencies.txt
ENTRYPOINT ["flask","run","--host=0.0.0.0"]