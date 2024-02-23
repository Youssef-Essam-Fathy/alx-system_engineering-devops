# Ensure Python 3 is installed
package { 'python3': ensure => installed }

#Using Puppet, install flask from pip3

package { 'flask':
ensure   => '2.1.0',
provider => 'pip3'
}