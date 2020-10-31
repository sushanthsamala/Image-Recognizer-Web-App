FROM ubuntu:latest

# Metadata
LABEL maintainer="Sushanth Samala (ss12852@nyu.edu)"

RUN mkdir /app

WORKDIR /app
ADD . /app
COPY . .

# Install just the Python runtime (no dev)
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y \
    python3 \
    python3-pip \
    ca-certificates

# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev

RUN pip3 install -r requirements.txt
RUN pip3 install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

EXPOSE 5000

CMD python3 api.py
