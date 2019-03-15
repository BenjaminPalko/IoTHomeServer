FROM python:3.7.2
COPY . /code
WORKDIR /code
RUN pip install -r dependencies.txt
RUN mkdir -pv /code/logs
ENTRYPOINT ["python","script.py"]