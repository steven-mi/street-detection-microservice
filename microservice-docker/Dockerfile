FROM tensorflow/serving
LABEL maintainer="stevenmi - Steven Mi <s0558366@htw-berlin.de>"

# Python
ARG PYTHON_VERSION=3.6

# Install python and pip
RUN apt-get update \
    && apt-get install -y \
            git \
            python${PYTHON_VERSION} \
            python3-pip \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests \
    && pip3 install pytest \
    && pip3 install tensorflow

RUN mkdir /entrypoint
COPY entrypoint.sh /entrypoint
RUN chmod u+x /entrypoint/entrypoint.sh
ENTRYPOINT /entrypoint/entrypoint.sh