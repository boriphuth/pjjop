# Apache vs Nginx
```
docker run --name webserver1 -p 800:80 httpd:2.4.41-alpine
http://cpsudevops.com:800
It works!

docker ps -a
mkdir httpd_dock
docker network create web_network
docker network ls
docker-compose ps
Hello Apache Web Server
docker volume ls
จะเห็นว่า Docker ไม่ได้สร้าง Volume ขึ้นมาใหม่ เนื่องจากเราใช้วิธี Mount Folder "html" ที่มีอยู่แล้วกับ Folder "/usr/local/apache2/htdocs/" ใน Apache Container
docker exec -it httpd /bin/bash
cd htdocs
vi index.html 
docker-compose down --rmi all
```
## Nginx Web Server
```
docker-compose up -d
http://cpsudevops.com:800
docker-compose down --rmi all

```

## Nginx + php
```
mkdir lemp_dock
cd lemp_dock
docker-compose up -d
docker-compose ps
http://cpsudevops.com:800
```

## Nginx + php + MariaDB
```
docker-compose build
docker-compose up -d
http://cpsudevops.com:800
```