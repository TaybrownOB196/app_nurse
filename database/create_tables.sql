create table AppService (
id int not null auto_increment,
appName varchar(50) not null,
description varchar(100) not null,
createDate datetime not null,
primary key(id));

create table Metric (
id int not null auto_increment,
appId int not null,
metricValue varchar(50) not null,
metricDataType varchar(25) not null,
tags TEXT,
createDate datetime not null,
primary key(id),
foreign key (appId) references AppService(id));