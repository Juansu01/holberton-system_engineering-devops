# Fix typo! there's an extra p                             
exec { 'remove extra p':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php"
}
