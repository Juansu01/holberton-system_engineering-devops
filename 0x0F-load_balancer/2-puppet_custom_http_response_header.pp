# This file configures a custom header
exec {'Installing nginx and configuring header':
    command  => 'sudo apt-get update -y && sudo apt-get install nginx -y && sudo sed -i "15i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx restart'
    provider => shell
}
