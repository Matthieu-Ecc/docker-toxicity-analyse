FROM python:3.7

COPY . /app

# set work directory
WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# install dependencies
COPY * .
RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["flask", "run"]