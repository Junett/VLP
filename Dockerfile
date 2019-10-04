FROM balenalib/rpi-debian-python:latest

RUN apt-get update
RUN apt-get install python3-pymongo

# Copy my application files
RUN mkdir -p apps
COPY . .

# runs a sample app on container start
CMD ["python3", "mainscript.py"]
