project:
  django_addr: http://127.0.0.1:8000
  dns_name: project.loc
  venv_dir: /home/vagrant/env/project_env
  work_dir: /project

python2:
  lookup:
    pkg: python2.7

mysql:
  # Manage databases
  database:
    - project_db

  # Manage users
  user:
    - name: user
      password: '123'
      host: localhost
      databases:
        - database: project_db
          grants: ['all privileges']