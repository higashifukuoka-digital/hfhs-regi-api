# hfhs-register-api

Backend of Register system for Higashi Fukuoka High School Festival 2023(東福岡高校 学園祭2023).

## Environment

* Python 3.11
* FastAPI
* Docker
* Nginx
* MySQL
For more: [docker](https://github.com/higashifukuoka-digital/hfhs-regi-api/tree/main/docker)

## Setup
### Development mode
```cmd
docker-compose -f docker-compose-prod.yml up
```

Your server will run without nginx.  You can check FastAPI on https://localhost:8000.

### Product mode
 1. Open your port 80.
 2. Install docker.
 3. Run the following command..
 ```cmd
 docker-compose up -d
 ```
