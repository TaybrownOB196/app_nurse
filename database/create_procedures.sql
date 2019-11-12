delimiter //

create procedure getAppServices ()
begin
    select id, appName, description, createDate from 
    AppService limit 10;
end //

create procedure getAppServicesByName (in applicationName varchar(50))
begin
    select id, appName, description, createDate from
    AppService where appName = applicationName limit 1;
end //

create procedure getAppServicesById (in appId int)
begin
    select id, appName, description, createDate from
    AppService where id = appId limit 1;
end //

create procedure saveAppService (in applicationName varchar(50), in dsc varchar(100))
begin
    insert into AppService (appName, description, createDate)
    values (applicationName, dsc, CURRENT_TIMESTAMP());
    select last_insert_id() as id;
end //

create procedure saveMetric (in applicationId int, in metricValue varchar(50), in metricDataType varchar(50), in tgs TEXT)
begin
    insert into Metric (appId, metricValue, metricDataType, tags, createDate)
    values (applicationId, metricValue, metricDataType, tgs, CURRENT_TIMESTAMP());
    select last_insert_id() as id;
end //

create procedure getMetricsByAppId (in applicationId int)
begin
    select id, appId, metricValue, metricDataType, tags, createDate from
    Metric where appId = applicationId order by id desc limit 20;
end //

create procedure getMetricsByAppIdPastMetricId (in applicationId int, in metricId int)
begin
    select id, appId, metricValue, metricDataType, tags, createDate from
    Metric where appId = applicationId and
    id > metricId
    order by id desc limit 20;
end //

delimiter ;