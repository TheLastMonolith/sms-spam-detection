FROM python:3.10-bookworm

WORKDIR /code

ADD . /code

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]