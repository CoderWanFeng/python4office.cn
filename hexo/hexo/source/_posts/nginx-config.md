---
title: NGINX 配置 同一域名端口下，根据URL 导向不同的项目目录
date: 2022-01-24 21:10:26
tags: [Linux,Nginx]
---



<p align="center" id='支付宝-banner'>
    <a target="_blank" href='http://www.python4office.cn/fuli/zhifubao-0923/'>
    <img src="https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/alipay/hong-3.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://kzurl19.cn/7CAHjq'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>

## 安装


1. 下载tar.gz：[下载链接](http://nginx.org/en/download.html)，上传到linux
2. 解压后运行：configure
3. 编译：make install
4. 修改：/usr/local/nginx/conf/nginx.conf

## 不同路径配置不同端口

<!-- more -->

配置文件：nginx.conf

```shell
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;

    keepalive_timeout  65;

    upstream hexo{
        server 115.159.63.27:18001;
    }

    server {
        listen       80;
        server_name  www.python4office.cn;

        location /hexo {
			proxy_pass http://hexo;

        }
      
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

    }

}

```

## 给同一项目的某个路径，配置账号和密码

a. 安装httpd-tools
```shell
yum -y install httpd-tools
```
b. 使用htpasswd生成指定用户名和密码的权限文件，示例如下，按照提示输入两次密码
```shell
# 在/etct/nginx目录下，生成passwd110文件
# 添加test110用户
htpasswd -c /etc/nginx/passwd110 test110
```

htpasswd还有其它参数，可以通过htpasswd -h来查看，例如可以指定一些密码加密方式

```shell

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;
    # upstream hexo{
    #     server 115.159.63.27:18001;
    # }   
    
     upstream api{
        server 115.159.63.27:18002;
    }    
     upstream swagger{
        server 115.159.63.27:18002;
    }
    # upstream api{
    #     server 127.0.0.1:8082;
    # }

    server {
        listen       18001;
        server_name  www.python4office.cn;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        # location / {
        #     root   html;
        #     index  index.html index.htm;
        # }

        # location /hexo {
		# 	proxy_pass http://hexo;

        # }

        location /api/ {
			proxy_pass http://api;

        }
        location /swagger {
			proxy_pass http://swagger;
            auth_basic "Please enter Password";
            auth_basic_user_file /opt/workplace/test/flasktest/password;

        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}

```

#### 参考链接

- [https://www.cnblogs.com/isylar/p/10402340.html](https://www.cnblogs.com/isylar/p/10402340.html)
- [https://www.cnblogs.com/fenqi/p/10879849.html](https://www.cnblogs.com/fenqi/p/10879849.html)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。