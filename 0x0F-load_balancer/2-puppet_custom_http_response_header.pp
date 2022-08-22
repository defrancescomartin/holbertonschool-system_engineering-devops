# automate the task of creating a custom HTTP header response, but with Puppet

# excecute update
exec {'update':
    command  => 'sudo apt-get -y update',
    provider => shell,
    before   => Exec['nginx'],
}

# nginx installation
exec {'nginx':
    command  => 'sudo apt-get -y install nginx',
    provider => shell,
    before  => Exec['custom header'],
}

# customizate header
exec {'custom header':
    provider => shell,
    command  => "sudo sed -i '/listen 80 default_server/a add_header X-Served-By ${hostname};' /etc/nginx/sites-enabled/default",
    before   => Exec['restart'],
}

# nginx restart to save changes
exec {'restart':
    command  => 'sudo service nginx restart',
    provider => shell
}
