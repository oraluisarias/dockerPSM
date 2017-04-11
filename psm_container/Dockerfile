FROM gse-admin.oraclecloud.com/gse_psm:latest
ENV HTTP_PROXY=http://www-proxy.us.oracle.com:80
ENV HTTPS_PROXY=http://www-proxy.us.oracle.com:80
COPY configure_psm.sh /app/

ARG USERNAME
ARG PASSWORD
ARG IDENTITY_DOMAIN
ARG DATACENTERPSM
ARG DATACENTER

RUN sh /app/configure_psm.sh $USERNAME $PASSWORD $IDENTITY_DOMAIN $DATACENTERPSM 
