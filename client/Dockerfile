FROM node:latest

  WORKDIR "/opt/bullet"

RUN mkdir -p /opt/bullet/node_modules

RUN npm install -g angular-cli

  COPY package.json /opt/bullet 

 RUN npm install

 VOLUME /opt/bullet/node_modules 

VOLUME ["/var/www"]

