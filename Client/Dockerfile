FROM python:3.6

RUN pip install --upgrade pip
RUN pip install --no-cache-dir scikit-learn pandas pymongo flask requests boto3

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

EXPOSE 27017 5000

CMD ["python", "-u", "s.py"]
