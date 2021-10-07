# Double the amount of worker processes for nginx
exec { "change workers":
        command => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf",
        provider => 'shell',
}
exec { "increment open files":
        command => "sed -i 's/ULIMIT="-n 15"/ULIMIT="-n 2100"/g' /etc/default/nginx",
        provider => 'shell',
}
# Restart the nginx service
exec { "restart service":
        command => "sudo service nginx restart",
        provider => 'shell',
}
