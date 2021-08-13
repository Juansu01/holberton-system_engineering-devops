# This file creates a file
file { 'create file':
path    => '/tmp/holberton',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
