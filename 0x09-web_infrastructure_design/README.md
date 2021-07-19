# Web infrastructure design 📝

The object of this project is to understand how the internet works, and how different servers communicate
 over the internet.

## Files 📁

- 0-simple_web_stack
- 1-distributed_web_infrastructure
- 2-secured_and_monitored_web_infrastructure

### 0-simple_web_stack 🌐
This is a simple web server design that contains:


- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to IP 8.8.8.8

### 1-distributed_web_infrastructure 🌐
This is a web server design based off of *0-simple_web_stack* that contains:

- 2 more servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

### 2-secured_and_monitored_web_infrastructure 🌐
This is a web server design based off of *1-distributed_web_infrastructure* that contains:

- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)
