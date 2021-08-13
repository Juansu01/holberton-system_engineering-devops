# this script runs a script and kills it.
exec { 'kill killmenow':
  command => 'pkill -15 killmenow',
  path    => '/usr/bin',
}
