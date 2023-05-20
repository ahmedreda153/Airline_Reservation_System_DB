/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2017                    */
/* Created on:     5/20/2023 2:20:01 PM                         */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('FLIGHT') and o.name = 'FK_FLIGHT_BELONGS_T_AIRCRAFT')
alter table FLIGHT
   drop constraint FK_FLIGHT_BELONGS_T_AIRCRAFT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('FLYING') and o.name = 'FK_FLYING_FLYING_AIRCRAFT')
alter table FLYING
   drop constraint FK_FLYING_FLYING_AIRCRAFT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('FLYING') and o.name = 'FK_FLYING_FLYING2_PILOT')
alter table FLYING
   drop constraint FK_FLYING_FLYING2_PILOT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('PASSENGER') and o.name = 'FK_PASSENGE_ASSIGN_FLIGHT')
alter table PASSENGER
   drop constraint FK_PASSENGE_ASSIGN_FLIGHT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('TICKET') and o.name = 'FK_TICKET_BOOK_PERSON')
alter table TICKET
   drop constraint FK_TICKET_BOOK_PERSON
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('TICKET') and o.name = 'FK_TICKET_HAS_FLIGHT')
alter table TICKET
   drop constraint FK_TICKET_HAS_FLIGHT
go

if exists (select 1
            from  sysobjects
           where  id = object_id('AIRCRAFT')
            and   type = 'U')
   drop table AIRCRAFT
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('FLIGHT')
            and   name  = 'BELONGS_TO_FK'
            and   indid > 0
            and   indid < 255)
   drop index FLIGHT.BELONGS_TO_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('FLIGHT')
            and   type = 'U')
   drop table FLIGHT
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('FLYING')
            and   name  = 'FLYING2_FK'
            and   indid > 0
            and   indid < 255)
   drop index FLYING.FLYING2_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('FLYING')
            and   name  = 'FLYING_FK'
            and   indid > 0
            and   indid < 255)
   drop index FLYING.FLYING_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('FLYING')
            and   type = 'U')
   drop table FLYING
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('PASSENGER')
            and   name  = 'ASSIGN_FK'
            and   indid > 0
            and   indid < 255)
   drop index PASSENGER.ASSIGN_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PASSENGER')
            and   type = 'U')
   drop table PASSENGER
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PERSON')
            and   type = 'U')
   drop table PERSON
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PILOT')
            and   type = 'U')
   drop table PILOT
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('TICKET')
            and   name  = 'HAS_FK'
            and   indid > 0
            and   indid < 255)
   drop index TICKET.HAS_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('TICKET')
            and   name  = 'BOOK_FK'
            and   indid > 0
            and   indid < 255)
   drop index TICKET.BOOK_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('TICKET')
            and   type = 'U')
   drop table TICKET
go

/*==============================================================*/
/* Table: AIRCRAFT                                              */
/*==============================================================*/
create table AIRCRAFT (
   SERIAL_NUM           int                  not null,
   CAPACITY             int                  null,
   MODEL                varchar(15)          null,
   AIRCRAFT_TYPE        varchar(15)          null,
   MANUFACTURER         varchar(15)          null,
   constraint PK_AIRCRAFT primary key (SERIAL_NUM)
)
go

/*==============================================================*/
/* Table: FLIGHT                                                */
/*==============================================================*/
create table FLIGHT (
   FLIGHT_NUM           int                  not null,
   SERIAL_NUM           int                  not null,
   ARRIVAL_TIME         datetime             null,
   DEPARTURE_TIME       datetime             null,
   SOURCE_LOCATION      varchar(20)          null,
   DESTINATION_LOCATION varchar(20)          null,
   DURATION             datetime             null,
   AIRLINE              varchar(20)          null,
   constraint PK_FLIGHT primary key (FLIGHT_NUM)
)
go

/*==============================================================*/
/* Index: BELONGS_TO_FK                                         */
/*==============================================================*/




create nonclustered index BELONGS_TO_FK on FLIGHT (SERIAL_NUM ASC)
go

/*==============================================================*/
/* Table: FLYING                                                */
/*==============================================================*/
create table FLYING (
   SERIAL_NUM           int                  not null,
   SSN                  int                  not null,
   constraint PK_FLYING primary key (SERIAL_NUM, SSN)
)
go

/*==============================================================*/
/* Index: FLYING_FK                                             */
/*==============================================================*/




create nonclustered index FLYING_FK on FLYING (SERIAL_NUM ASC)
go

/*==============================================================*/
/* Index: FLYING2_FK                                            */
/*==============================================================*/




create nonclustered index FLYING2_FK on FLYING (SSN ASC)
go

/*==============================================================*/
/* Table: PASSENGER                                             */
/*==============================================================*/
create table PASSENGER (
   FLIGHT_NUM           int                  not null,
   P_ID                 int                  not null,
   FNAME                varchar(20)          null,
   LNAME                varchar(20)          null,
   constraint PK_PASSENGER primary key (FLIGHT_NUM, P_ID)
)
go

/*==============================================================*/
/* Index: ASSIGN_FK                                             */
/*==============================================================*/




create nonclustered index ASSIGN_FK on PASSENGER (FLIGHT_NUM ASC)
go

/*==============================================================*/
/* Table: PERSON                                                */
/*==============================================================*/
create table PERSON (
   ID                   int                  not null,
   FNAME                varchar(20)          null,
   LNAME                varchar(20)          null,
   EMAIL                varchar(50)          null,
   PERSON_PASSWORD      varchar(20)          null,
   PHONENUM             varchar(20)          null,
   DOB                  datetime             null,
   AGE                  int                  null,
   CITY                 varchar(20)          null,
   PERSON_STATE         varchar(20)          null,
   STREET               varchar(20)          null,
   ZIPCODE              int                  null,
   PERSON_ROLE          varchar(15)          null,
   constraint PK_PERSON primary key (ID)
)
go

/*==============================================================*/
/* Table: PILOT                                                 */
/*==============================================================*/
create table PILOT (
   SSN                  int                  not null,
   PNAME                varchar(20)          null,
   AGE                  int                  null,
   DOB                  datetime             null,
   constraint PK_PILOT primary key (SSN)
)
go

/*==============================================================*/
/* Table: TICKET                                                */
/*==============================================================*/
create table TICKET (
   TICKETID             int                  not null,
   FLIGHT_NUM           int                  not null,
   ID                   int                  not null,
   SOURCE_LOCATION      varchar(20)          null,
   DESTINATION_LOCATION varchar(20)          null,
   PNAME                varchar(20)          null,
   PRICE                decimal(5,2)         null,
   SEAT                 varchar(5)           null,
   CLASS                varchar(15)          null,
   ARRIVAL_TIME         datetime             null,
   DEPARTURE_TIME       datetime             null,
   constraint PK_TICKET primary key (TICKETID)
)
go

/*==============================================================*/
/* Index: BOOK_FK                                               */
/*==============================================================*/




create nonclustered index BOOK_FK on TICKET (ID ASC)
go

/*==============================================================*/
/* Index: HAS_FK                                                */
/*==============================================================*/




create nonclustered index HAS_FK on TICKET (FLIGHT_NUM ASC)
go

alter table FLIGHT
   add constraint FK_FLIGHT_BELONGS_T_AIRCRAFT foreign key (SERIAL_NUM)
      references AIRCRAFT (SERIAL_NUM)
go

alter table FLYING
   add constraint FK_FLYING_FLYING_AIRCRAFT foreign key (SERIAL_NUM)
      references AIRCRAFT (SERIAL_NUM)
go

alter table FLYING
   add constraint FK_FLYING_FLYING2_PILOT foreign key (SSN)
      references PILOT (SSN)
go

alter table PASSENGER
   add constraint FK_PASSENGE_ASSIGN_FLIGHT foreign key (FLIGHT_NUM)
      references FLIGHT (FLIGHT_NUM)
go

alter table TICKET
   add constraint FK_TICKET_BOOK_PERSON foreign key (ID)
      references PERSON (ID)
go

alter table TICKET
   add constraint FK_TICKET_HAS_FLIGHT foreign key (FLIGHT_NUM)
      references FLIGHT (FLIGHT_NUM)
go

