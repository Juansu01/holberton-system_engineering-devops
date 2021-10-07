# Double the amount of worker processes for nginx
exec { "change workers":
        command => "sed -i 's/worker_processes 8;/worker_processes 100;/g' /etc/nginx/nginx.conf",
        provider=> 'shell',
}
# Restart the nginx service
exec { "restart service":
        command => "sudo service nginx restart",
        provider => 'shell',
}
