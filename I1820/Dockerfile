FROM ubuntu
MAINTAINER Parham Alvani <parham.alvani@gmail.com>

EXPOSE 8080

# Install packages
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3 python3-venv python3-pip python3-dev
RUN apt-get install -y libyaml-dev

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/packages/* && apt autoremove -y

#
RUN useradd -ms /bin/bash aolab
USER aolab
WORKDIR /home/aolab

# I1820
RUN git clone https://github.com/aolab/I1820
RUN cd I1820; pyvenv .; pip3 install -r requirements.txt

# Entrypoint Script
ENTRYPOINT ["/home/aolab/I1820/18.20-serve.py"]
