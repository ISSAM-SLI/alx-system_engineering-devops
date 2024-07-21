# we need to make a Customized HTTP header

# first we need to update ubuntu server
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# then we install nginx web server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# we customize Nginx response header
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# starting the service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
