# 0x0F. Load balancer

## Tasks

## Mandatory

* 0 - In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

* 1 - Install and configure HAproxy on your lb-01 server.


## Advanced

* 2 - Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
