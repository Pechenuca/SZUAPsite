FROM node:lts-alpine AS frontend

WORKDIR /frontend
COPY frontend/package.json .
COPY frontend/yarn.lock .
COPY frontend .

#RUN yarn global add serve
RUN yarn install
RUN yarn build

FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
COPY --from=frontend /frontend/dist/ /usr/share/nginx/html/