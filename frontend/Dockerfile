FROM node:lts-alpine AS frontend

WORKDIR /frontend
COPY frontend/package.json .
COPY frontend/yarn.lock .
COPY frontend .

EXPOSE 8080

RUN yarn install
