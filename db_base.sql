
-- Removing everything
DROP SCHEMA IF EXISTS aok;
DROP DATABASE IF EXISTS aok;
DROP ROLE IF EXISTS svc_aok;
DROP ROLE IF EXISTS svc_django;

-- Creating roles and grants for admin
CREATE ROLE svc_aok WITH LOGIN PASSWORD 'aokpwd';
CREATE ROLE svc_django WITH LOGIN PASSWORD 'djangopwd';
GRANT svc_aok TO current_user;
GRANT svc_django TO current_user;

-- Create database and connect to it
CREATE DATABASE aok OWNER svc_aok;
\connect aok;

-- Creating App schema and permissions for App roles
CREATE SCHEMA IF NOT EXISTS aok AUTHORIZATION svc_aok;
GRANT ALL ON SCHEMA aok TO svc_aok;
GRANT ALL ON SCHEMA aok TO svc_django;
