# Increment amount of open files
exec { "increment open files":
        command => "sed -i s/15/2000/ /etc/default/nginx",
        provider => 'shell',
}
exec { "restart service":
        command => "sudo service nginx restart",
        provider => 'shell',
}
