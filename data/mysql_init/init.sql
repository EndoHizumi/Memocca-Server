create database sticky_boards;
use sticky_boards;
create table stickies
(
    sticky_id varchar(32) NOT NULL,
    user_id int,
    board_id varchar(6),
    color_code VARCHAR(20),
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
    salt VARCHAR(29),
    private int
);

create table users
(
    user_id varchar(8),
    user_name VARCHAR(256),
    password varchar(255),
    email VARCHAR(256),
    salt VARCHAR(29)
);

INSERT INTO boards VALUES("foobar","board1","owner1","password","salt",0);
-- 付箋テストデータ
INSERT INTO stickies VALUES(0,0,"foobar","#f8f8f8","test",0,0,300,300);
INSERT INTO stickies VALUES(0,0,"foobar","whitesmoke","test2",0,0,100,100);