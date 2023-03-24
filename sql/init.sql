CREATE DATABASE development;
\connect development;
CREATE TABLE IF NOT EXISTS tc (
id SERIAL NOT NULL PRIMARY KEY,
time timestamp NOT NULL DEFAULT now(),
tc1 FLOAT,  -- LNG TC
tc2 FLOAT,  -- LOX TC
tc3 FLOAT,  -- COPV TC
tc4 FLOAT   -- MVAS TC
);

CREATE TABLE IF NOT EXISTS pt (
id SERIAL NOT NULL PRIMARY KEY,
time timestamp NOT NULL DEFAULT now(),
pt1 FLOAT, -- LNG PT
pt2 FLOAT, -- LOX PT
pt3 FLOAT, -- COPV PT
pt4 FLOAT  -- LNG INJ
);

CREATE TABLE IF NOT EXISTS solenoids (
	id SERIAL NOT NULL PRIMARY KEY,
	time timestamp NOT NULL DEFAULT now(),
	he smallint,
	lng smallint,
	lox smallint,
	pv1 smallint,
	pv2 smallint,
	mvas smallint
);

CREATE TABLE IF NOT EXISTS location (
	time timestamp NOT NULL DEFAULT now(),
	lat numeric,
	lon numeric
);

CREATE TABLE IF NOT EXISTS gyro (
	time timestamp NOT NULL DEFAULT now(),
	x numeric,
	y numeric,
	z numeric
);

CREATE TABLE IF NOT EXISTS acc (
	time timestamp NOT NULL DEFAULT now(),
	x numeric,
	y numeric,
	z numeric
);

CREATE TABLE IF NOT EXISTS bmp (
	time timestamp NOT NULL DEFAULT now(),
	temp numeric,
	altitude numeric,
	pressure numeric
);

