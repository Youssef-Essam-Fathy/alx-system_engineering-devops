#  set up your client SSH configuration file so that you can connect to a server without typing a password
file { 'config':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => 'IdentityFile ~/.ssh/school
              PasswordAuthentication no'
}
