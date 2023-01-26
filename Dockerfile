#Written by: Masha
FROM python:3.9.0
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY ../../Desktop /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]