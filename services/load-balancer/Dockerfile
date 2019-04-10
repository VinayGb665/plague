FROM nginx:alpine
LABEL Hector bhai

COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
CMD ["nginx","-g","daemon off;"]