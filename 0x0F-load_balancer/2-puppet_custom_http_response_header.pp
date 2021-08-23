# This file configures a custom header
exec {'install nginx':
    command  => 'sudo apt-get update -y && sudo apt-get install nginx -y && sudo sed -i "23i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx restart'
    
}
