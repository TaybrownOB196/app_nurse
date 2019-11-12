FROM mysql:8.0.17

ENV MYSQL_DATABASE temp

ADD ["create_tables.sql", "/docker-entrypoint-initdb.d/005_create_tables.sql"]
ADD ["insert_data.sql", "/docker-entrypoint-initdb.d/010_insert_data.sql"]
ADD ["create_procedures.sql", "/docker-entrypoint-initdb.d/015_create_procedures.sql"]
ADD ["setup_users.sql", "/docker-entrypoint-initdb.d/020_setup_users.sql"]
