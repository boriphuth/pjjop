## https://blog.pjjop.org/how-to-config-vps-and-letsencrypt-with-docker-container/

## Nginx-Proxy
```
cd nginx_proxy_dock
docker network create webproxy
docker-compose up -d
docker images
docker-compose ps
http://cpsudevops.com
```

## LEMP Stack Container
```
cd website1
docker network create webproxy
docker network create web_network
docker-compose build
docker-compose up -d
docker-compose ps
http://cpsudevops.com
docker-compose down --rmi all
```

## Multiple Websites on Docker Container
```
cd website2
docker network create web_network2
docker network ls
docker-compose build
docker-compose up -d
docker-compose ps
http://service.cpsudevops.com
docker-compose down --rmi all
```

## Let’s Encrypt
```
cd ..
cd nginx_proxy_dock
docker-compose down --rmi all
docker-compose up -d
docker-compose ps
cd ..
cd website1
docker-compose stop
docker-compose up -d
docker-compose ps
http://cpsudevops.com
https://cpsudevops.com
```

```
cd website2
docker-compose up -d
docker-compose ps
```

### Bonus!
```
cd website1
docker-compose stop
docker-compose up -d
docker-compose ps
http://mydb.cpsudevops.com
https://mydb.cpsudevops.com
```