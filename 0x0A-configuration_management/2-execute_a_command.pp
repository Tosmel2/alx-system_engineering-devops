# runs pkill against the process killmenow
exec { 'pkill killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}

