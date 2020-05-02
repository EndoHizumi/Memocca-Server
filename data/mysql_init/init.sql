create database sticky_boards;
use sticky_boards;
create table stickies
(
    sticky_id varchar(32) NOT NULL,
    user_id int,
    board_id varchar(6),
    color_code int(8),
    text VARCHAR(8000),
    point_x int,
    point_y int,
    width int,
    height int
);
create table boards
(
    board_id varchar(256),
    board_name VARCHAR(512),
    owner_id varchar(32),
    password varchar(255),
    private int
);


insert into boards values ('fugafuga','board1','owner1','','0');
insert into boards values ('hogehoge','board2','owner2','','0');
insert into boards values ('foobar','board3','owner3','','1');