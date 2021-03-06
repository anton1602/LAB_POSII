FROM python:3.6

RUN pip install --upgrade pip
RUN pip install --no-cache-dir scikit-learn pandas pymongo

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

EXPOSE 27017

CMD ["python", "-u", "run.py"]