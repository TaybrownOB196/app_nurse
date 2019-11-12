FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild

COPY deploy/httpd.conf /usr/local/apache/conf/

CMD [ "app_nurse/wsgi.py" ]