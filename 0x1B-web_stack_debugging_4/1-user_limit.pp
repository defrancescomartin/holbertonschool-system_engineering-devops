# Scritp to fix permision of holberton user
exec { '/usr/bin/env sed -i "s/holberton/#holberton/" /etc/security/limits.conf': }
