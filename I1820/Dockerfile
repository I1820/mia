FROM ubuntu
MAINTAINER Parham Alvani <parham.alvani@gmail.com>

# Install packages
RUN apt-get update
RUN apt-get install -y python3 python3-venv python3-pip

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/packages/* && apt autoremove -y

# Home dir
RUN mkdir -p $HOME/I1820
RUN git clone https://github.com/aolab/I1820 $HOME/I1820
RUN cd $HOME/I1820; pyvenv .; pip3 install -r requirements.txt

# Entrypoint Script
ENTRYPOINT ["~/I1820/18.20-serve.py"]
