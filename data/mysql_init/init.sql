create database sticky_boards;
use sticky_boards;
create table stickies
(
    sticky_id varchar(32),
    user_id int,
    tag varchar(255),
    board_id varchar(32),
    color_id int,
    text VARCHAR(1024),
    point_x int,
    point_y int,
    width int,
    height int
);
create table boards
(
    board_id varchar(32),
    owner_id varchar(32),
    user_id int,
    password varchar(255)
);
create table colors
(
    color_id int,
    color_namr VARCHAR(255)
);
