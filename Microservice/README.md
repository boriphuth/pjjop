# Microservice https://blog.pjjop.org/build-microservice-on-docker-container/
```
ดังนั้นในการออกแบบ Microservice ที่ดี เราจะยึดหลัก 2 ประการ คือ
Loosely Coupling แต่ละ Service มีหน้าที่ทำงานเพียงอย่างเดียว และควรขึ้นกับ Service อื่นให้น้อยที่สุด
High Cohesion ภายในแต่ละ Service จะมีงานที่ร่วมกันทำตามเป้าหมาย
```

```
docker-compose down --rmi all
```

## nginx
```
cd nginx-proxy-companion
docker network create webproxy
./start.sh
docker-compose ps
```

## portainer
```
cd port_dock
docker-compose down --rmi all
docker-compose up -d
docker-compose ps
http://portainer.boriphuth.net
https://portainer.boriphuth.net
```

## RabbitMQ
```
cd mq_dock
docker-compose down --rmi all
docker network create microservice_network
docker-compose up -d
docker-compose ps
https://rabbitmq.boriphuth.net
```

## Register Gateway
```
cd register_gateway_dock
docker-compose down --rmi all
docker-compose build --pull
docker-compose up -d
docker-compose ps
https://register.gateway.boriphuth.net/docs
```
## Student Service
```
cd student_dock
docker-compose down --rmi all
docker network create student_network
docker-compose build --pull
docker-compose up -d
docker-compose ps
https://student.boriphuth.net
```

## Enroll Service
```
cd enroll_dock
docker-compose down --rmi all
docker network create enroll_network
docker-compose build --pull
docker-compose up -d
docker-compose ps
https://enroll.boriphuth.net
```

## Email Service
```
cd email_dock
mv .env.sample .env and edit
docker-compose down --rmi all
docker network create email_network
docker-compose build --pull
docker-compose up -d
docker-compose ps
```
https://register.gateway.boriphuth.net/docs

http://boriphuth.net:7001/docs#
https://boriphuth.net:7001/docs#


docker run -d -e VIRTUAL_HOST=portainer.boriphuth.net \
              --network=webproxy \
              --name my_app \
              httpd:alpine

docker run -d -e VIRTUAL_HOST=portainer.boriphuth.net \
              -e LETSENCRYPT_HOST=portainer.boriphuth.net \
              -e LETSENCRYPT_EMAIL=boriphuth@boriphuth.net \
              --network=webproxy \
              --name my_app \
              httpd:alpine
```            
docker login
docker-compose build --pull
docker-compose push
  # and optionally:
$ docker logout
```