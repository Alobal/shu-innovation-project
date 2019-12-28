# 创新项目

## 后端

``` shell
python run './api.py'
```

## 前端

``` shell
npm install
npm run serve
```

## 部署过程

### flask+gunicorn+nginx部署

1. 买服务器

2. ubuntu系统

3. 开启80 8080端口 [教程](https://www.cnblogs.com/codeman-hf/p/10535923.html)

4. 安装nginx

   ```shell
   apt update
   apt upgrade
   sudo apt install nginx
   ```

5. 测试nginx

   ```shell
   sudo service nginx restart
   ```

   然后访问ip地址 [如何查看公网ip](https://blog.csdn.net/ssssSFN/article/details/89501469)

6. 安装docker [docker安装教程](https://www.runoob.com/docker/ubuntu-docker-install.html)

7. 编写dockerfile文件

   ```dockerfile
   FROM python:3.8
   RUN mkdir /home/web && cd /home/web
   WORKDIR /home/web
   COPY ./backend/* /home/web/
   RUN pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/  \
       && pip install gunicorn
   
   EXPOSE 8080
   CMD [ "gunicorn", "-w", "5",  "api:app"]
   
   ```

8. 

   ```shell
   docker build . flask:0.1
   docker save [image_id] > docker.tar
   ```

9. 在服务器

   ```
   docker load -i docker.tar
   ```

10. `npm run build && scp dist/* root@ip:path/`

11. 编写nginx配置

    ```
    worker_processes  1;
    
    events {
    	worker_connections  1024;
    }
    
    http {
        include       mime.types;
        default_type  application/octet-stream;
        keepalive_timeout  65;
    
        server {
    		listen       80;
    		server_name  ipAddr;
    
    		location / {
    			root /root/app;
    			index index.html;
    		}
    	}
    
        server {
    		listen       8080;
    		server_name  ipAddr;
    
    		location / {
    			proxy_pass  http://127.0.0.1:8080
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    		}
    	}    
    }
    ```

12. `gunicorn -w 4 api:app`

    报错说明端口占用

    `ps aux | grep 8080`



