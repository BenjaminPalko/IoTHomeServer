--devices table setup
create table devices
(
	id varchar(17) not null,
	type varchar(30) not null,
	timestamp timestamp not null
);

create unique index devices_id_uindex
	on devices (id);

alter table devices
	add constraint devices_pk
		primary key (id);

-- temp sensor table setup
create table temperature_sensor
(
	id varchar(17) not null,
	value float not null,
	timestamp timestamp not null
);

-- rgb table setup
create table rgb_led
(
	id varchar(17) not null
		constraint rgb_led_pk
			primary key,
	color varchar(7) not null,
	timestamp timestamp not null
);

-- weather table setup
create table weather
(
	id varchar(17) not null
		constraint weather_pk
			primary key,
	location int not null,
	timestamp timestamp not null
);

--doorlock table setup
create table doorlock
(
	id varchar(17) not null
		constraint doorlock_pk
			primary key,
	pin varchar(4) not null,
	timestamp timestamp not null
);