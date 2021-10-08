# change limitations
exec { 'increasing limits':
        command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 4000/g'  /etc/security/limits.conf",
        provider => 'shell',
}
exec { 'increasing limit':
        command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 2000/g'  /etc/security/limits.conf",
        provider => 'shell',
}