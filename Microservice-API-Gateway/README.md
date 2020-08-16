# https://blog.pjjop.org/build-api-gateway-and-monitoring-microservice-with-kong-prometheus-and-grafana/
```
โดยเราสามารถตั้งค่า Kong ใน 4 ส่วนหลักๆ ได้แก่
Service คือ Service ปลายทางที่ต้องการให้ Kong ส่งต่อ Request ไปหา
Route คือ Path ที่  Client เรียกมาหา Kong โดยที่ Route จะต้องผูกกับ Service
Consumer คือ ผู้ที่จะเรียกใช้ Kong
Plugin คือ ตัวที่ทำให้ Kong สามารถทำ Authentication, Rate Limiting หรือ Monitoring Service ฯลฯ ได้
ซึ่ง Kong กำหนด Default Port ในการรับ-ส่งข้อมูลไว้ดังนี้
8000 สำหรับ HTTP Request ที่จะถูกส่งต่อไปยัง Service ตามที่กำหนด
8443 สำหรับ HTTPS Request ที่จะถูกส่งต่อไปยัง Service ตามที่กำหนด
8001 สำหรับการตั้งค่า Kong ผ่าน HTTP Request
8444 สำหรับการตั้งค่า Kong ผ่าน HTTPS Request
```

## Kong API Gateway
```
cd kong_dock
docker network create kong_network
docker-compose down --rmi all
docker-compose up -d
docker-compose ps
https://konga.boriphuth.net
Name:Devops
Kong Admin URL:http://kong:8001

https://service.boriphuth.net/register/
```

