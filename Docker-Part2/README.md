## Dockerfile
FROM กำหนด Base image
LABEL ใช้กำหนด Metadata เช่น ชื่อ Version หรือเจ้าของ Image
ENV กำหนด Environment variable ภายใน Container
RUN ใช้สำหรับติดตั้ง Packagesให้ Container
COPY สำหรับ Copy file และ Folder ไปยัง Container
ADD สำหรับ Copy file และ Folder ไปยัง Container โดยสามารถแตกไฟล์ .tar รวมทั้ง Copy file จาก Host ภายนอกได้
CMD สำหรับรันคำสั่งที่ต้องการขณะรัน Container
WORKDIR กำหนด Working directory ของ Container
ARG กำหนด Variable ขณะสร้าง Image
ENTRYPOINT สำหรับรันคำสั่งที่ต้องการขณะรัน Container
EXPOSE กำหนด Port ที่เปิดให้ Container อื่นติดต่อเข้ามา
VOLUME สร้าง Folder เก็บข้อมูลแบบถาวรให้ Container

```
RUN apt-get update && apt-get install my_package
```
## Build a smaller image
```
cd small_image
docker build -t debiandock .
docker history debiandock
docker images
จะเห็นว่า debiandock image มีขนาด 150MB
docker build -t small_debiandock -f Dockerfile.small .
docker history small_debiandock
docker images
ซึ่งจะเห็นว่าขนาดของ Image ลดลงจาก 150MB เป็น 116MB
```

## Docker Compose
```
mkdir web_dock
docker-compose build 
docker images
docker history web_dock_server
docker network prune
docker network ls
docker network create web_network
docker-compose up -d
docker-compose ps
docker volume ls
docker volume inspect web_dock_server_volume
sudo ls ~/var/lib/docker/volumes/web_dock_server_volume/_data
docker exec -it web_dock_server_1 sh
docker-compose down --rmi all
docker volume ls
docker volume rm web_dock_server_volume
docker volume prune
docker network rm web_network

```
### Add /etc/hosts 
```
127.0.0.1	cpsudevops.com
```

http://cpsudevops.com/


## Web Based Container Management 
portainer.io
```
docker network create webproxy
docker-compose up -d
```
http://cpsudevops.com/