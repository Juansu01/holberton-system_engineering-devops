exec { 'killmenow':
  command => 'pkill -15 killmenow',
  path    => '/usr/bin',
}
