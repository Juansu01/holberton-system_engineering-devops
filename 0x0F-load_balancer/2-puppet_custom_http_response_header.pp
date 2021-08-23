# This file configures a custom header
exec {'install nginx':
    command  => 'sudo sed -i "23i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx restart'
    
}
