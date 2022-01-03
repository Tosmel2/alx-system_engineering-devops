#Creates /tmp/school with the given attributes
file { '/tmp/school':
  owner   => www-data,
  group   => www-data,
  mode    => '0744',
  content => 'I love Puppet'
}

