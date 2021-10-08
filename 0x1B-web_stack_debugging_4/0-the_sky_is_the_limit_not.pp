# Increment amount of open files
exec { 'change workers':
        command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf",
        provider => 'shell',
}
exec { 'increment open files':
        command  => 'sed -i s/15/2000/ /etc/default/nginx',
        provider => 'shell',
}
exec { 'restart service':
        command  => 'sudo service nginx restart',
        provider => 'shell',
}
