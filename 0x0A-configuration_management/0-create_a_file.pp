# This file creates a file
file { '/tmp':
path    => '/holberton',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
