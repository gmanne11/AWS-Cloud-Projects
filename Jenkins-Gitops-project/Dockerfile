FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

# Pin Werkzeug version and install dependencies
RUN pip3 install werkzeug==1.0.1 && pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
