CREATE DATABASE MANAGEMENT;

CREATE TABLE ACCOUNT(
	UserName varchar(45) NOT NULL,
    PassWord varchar(45) NOT NULL,
    PRIMARY KEY(UserName)
);

CREATE TABLE CUSTOMER(
	Ref int NOT NULL,
    HoTenKH varchar(200),
    GioiTinh varchar(45),
    Mobile varchar(45),
    Email varchar(45),
    QuocTich varchar(100),
    LoaiThe varchar(45),
    SoThe varchar(45),
    DiaChi varchar(500),
    PRIMARY KEY(Ref)
);

CREATE TABLE DETAILS(
	floor varchar(45) NOT NULL,
    roomname varchar(45) NOT NULL,
    roomtype varchar(45),
    price int,
    max_customer varchar(45),
    subtotal int,
    coefficent decimal(5,2),
    status varchar(45),
    PRIMARY KEY(floor, roomname)
);

CREATE TABLE ROOM(
	Moblie varchar(45) NOT NULL,
    check_in varchar(45) NOT NULL,
    check_out varchar(45),
    roomtype varchar(45),
    Room varchar(45),
    totalcustomer varchar(45),
    foreigner varchar(45),
    noofdays varchar(45),
    totalcost varchar(45),
    PRIMARY KEY(Moblie, check_in)	
);

insert into Account values('admin','123456');

insert into Details values('1','100','C',200000,'3',25,'1.5','Ready');
insert into Details values('1','101','B',170000,'3',25,'1.5','Ready');
insert into Details values('1','102','A',150000,'3',25,'1.5','Not Ready');
insert into Details values('2','202','A',150000,'3',25,'1.5','Not Ready');
insert into Details values('2','203','B',170000,'3',25,'1.5','Ready');
insert into Details values('3','301','A',150000,'3',25,'1.5','Not Ready');
insert into Details values('3','302','C',200000,'3',25,'1.5','Ready');


insert into Customer values(1,'Jessie','Female','867245963','jessie@gmail.com','VietNam','CCCD','64745556','Ho Chi Minh');
insert into Customer values(2,'David','Male','9893285324','david@gmail.com','VietNam','CMND','6362858559','Ha Noi');