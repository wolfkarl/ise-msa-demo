FROM python:3

WORKDIR /usr/src/app

RUN pip install pipenv
COPY Pipfile ./
RUN pipenv install

COPY . .

CMD [ "pipenv", "run", "python", "./main.py" ]