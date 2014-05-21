{% set app_name = 'project' %}
{% set app = pillar['project'] %}

{{ app_name }}.venv:
  virtualenv.managed:
    - name: {{ app['venv_dir'] }}
    # if you use mysql-python it must be True
    - system_site_packages: True
    - require:
      - pkg: python2


{{ app_name }}.pip:
  pip.installed:
    - bin_env: {{ app['venv_dir'] }}
    - names:
      - MySQL-python
      - Django
      - South
      - python-dateutil
      - django-filter
      - python-social-auth
      - djangorestframework
    - require:
      - virtualenv: {{ app_name }}.venv


{{ app_name }}.nginx.conf:
    file.managed:
        - name: /etc/nginx/sites-enabled/{{ app_name }}.conf
        - source: salt://{{ app_name }}/{{ app_name }}.nginx.conf
        - context: # помимо переменных вроде pillar, мы можем передать дополнительный контекст для тепмлейта
            django_addr: {{ app['django_addr'] }}
            dns_name: {{ app['dns_name'] }}
            path: {{ app['work_dir'] }}
        - template: jinja
        - makedirs: True
        - watch_in:
            - service: nginx