# Puppet manifest to configure SSH client

file_line { 'Refuse to authenticate using a password':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Use private key':
  ensure => present,
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school'
}
