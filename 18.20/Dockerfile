FROM ubuntu
MAINTAINER Parham Alvani <parham.alvani@gmail.com>

# Install packages
RUN apt update
RUN apt install -y git nginx wget \
	sudo dbus curl \
	php-fpm php-curl php-mysql php-mcrypt php-json php-cli php-curl php-mongodb

# Cleanup
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/packages/* && apt autoremove -y

# Install composer
RUN wget https://getcomposer.org/composer.phar -O /usr/local/bin/composer && \
	chmod +x /usr/local/bin/composer

# Git
RUN mkdir -p /var/www && \
    chown www-data:www-data -R /var/www && \
    sudo -u www-data git config --global credential.helper store

# PHP
COPY conf/php.ini /etc/php5/fpm/php.ini
COPY conf/www.conf /etc/php5/fpm/pool.d/www.conf

# Nginx
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/nginx-default /etc/nginx/sites-enabled/default

# Home dir
RUN mkdir -p /var/www && chown -R www-data:www-data /var/www

# Dist
COPY dist /opt/dist

# Lasser
COPY laaser /usr/share/laaser

# Bin
COPY bin /usr/local/bin

#Entrypoint Script
ENTRYPOINT ["/usr/local/bin/entrypoint"]
