# Double the amount of worker processes for nginx
exec { "change workers":
        command => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf",
        provider => 'shell',
}
# Restart the nginx service
exec { "restart service":
        command => "sed -i 's/# multi_accept on;/multi_accept on;/g' /etc/nginx/nginx.conf",
        provider => 'shell',
}
# Restart the nginx service
exec { "restart service":
        command => "sudo service nginx restart",
        provider => 'shell',
}
