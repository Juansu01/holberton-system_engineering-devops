# Fix typo! there's an extra p                             
exec { 'remove extra p':                                   
command => 'sed -i 's/phpp/php/' /var/www/html/wp-settings.php'
}   
