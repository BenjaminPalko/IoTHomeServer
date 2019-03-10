FROM python:3.7.2
ADD . /code
WORKDIR /code
RUN pip install -r dependencies.txt
ENTRYPOINT [ "python","script.py" ]