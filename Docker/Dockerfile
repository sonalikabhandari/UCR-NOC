
FROM alpine/git  as base

COPY id_rsa /tmp/id_rsa

RUN apk add --update git openssh-client && \
    chmod 600 /tmp/id_rsa && \
    eval $(ssh-agent) && \
    echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
    ssh-add /tmp/id_rsa && \
    git clone --depth=1 -b port_request_manage git@git.netops.charter.com:P2818726/ucr-noc.git /dbAudited && \
    rm -rf /tmp/id_rsa

FROM node:carbon-alpine as frontend

COPY --from=base /dbAudited /dbAudited

RUN cd /dbAudited/frontend && \
    npm install && \
    npm run build


FROM python:3.6.9-slim-buster

COPY --from=base /dbAudited /dbAudited
COPY --from=frontend /dbAudited/frontend/dist /dbAudited/frontend/dist
COPY --from=frontend /dbAudited/frontend/webpack-stats.json /dbAudited/frontend/webpack-stats.json
COPY web-entrypoint.sh /usr/local/bin/
COPY db_audit.sh /usr/local/bin/

RUN  apt-get update && apt-get upgrade -y                                    && \
    pip install --upgrade pip setuptools                                    && \
    pip install -r /dbAudited/requirements.txt                              && \

    chmod a+rx /usr/local/bin/web-entrypoint.sh                             && \
    chmod a+rx /usr/local/bin/db_audit.sh                                   && \
    cd /dbAudited                                                           && \
    mkdir log                                                               && \
    python manage.py collectstatic --no-input                               && \
    cd public                                                               && \
    tar czf static.tgz *                                                    && \
    mv static.tgz /

EXPOSE 8000
WORKDIR /dbAudited
