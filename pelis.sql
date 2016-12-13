create database pelis;
use pelis;

create table renta(
cliente varchar (200) not null,
    pelicula varchar(200) not null,
    formato varchar(200) not null,
    tiempo varchar(200) not null,
    total varchar(200) not null
);