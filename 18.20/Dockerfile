FROM ubuntu
MAINTAINER Parham Alvani <parham.alvani@gmail.com>

# Install packages
RUN apt-get update
RUN apt-get install -y git nginx wget \
	gnutls-bin curl \
	php-curl php-mysql php-mcrypt php-json php-cli php-curl php-mongodb php-mbstring

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/packages/* && apt autoremove -y

# Install composer
RUN wget https://getcomposer.org/composer.phar -O /usr/local/bin/composer && \
	chmod +x /usr/local/bin/composer

# Apache
COPY conf/18.20.conf /etc/apache2/sites-available/000-default.conf

# Home dir
RUN mkdir -p /var/www
RUN git clone https://github.com/aolab/18.20 /var/www/18.20

# Bin
COPY bin /usr/local/bin

# Entrypoint Script
ENTRYPOINT ["/usr/local/bin/entrypoint"]
