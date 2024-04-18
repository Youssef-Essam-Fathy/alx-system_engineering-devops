#Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 4096',
  path   => '/usr/local/bin/:/bin/
}
