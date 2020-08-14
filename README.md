# pjjop

How to Install and Use Docker on Ubuntu 18.04
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce
sudo apt install docker-ce=5:18.09.6~3-0~ubuntu-bionic
sudo apt-mark hold docker-ce
sudo systemctl status docker
sudo usermod -aG docker $USER
docker container run hello-world

```