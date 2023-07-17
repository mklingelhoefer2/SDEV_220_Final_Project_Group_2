create database if not exists dcrm;

create table if not exists Employees 
(ID int auto_increment primary key,
fName varchar(20),
lName varchar(20),
email varchar(28),
jobTitle varchar(20)
);

create table if not exists Contacts
(ID int auto_increment primary key,
fName varchar(20),
lName varchar(20),
email varchar(28),
jobTitle varchar(20),
phone varchar(18),
lifecycleStage varchar(20),
leadStatus varchar(18),
createDate timestamp,
lastActivityDate timestamp,
ownerID int,
foreign key (ownerID) references Employees(ID)
);

create table if not exists ContactNotes
(ID int auto_increment primary key,
note text(65535),
noteType varchar(20),
createDate timestamp,
updateDate timestamp,
contactID int, 
ownerID int,
foreign key (contactID) references Contacts(ID),
foreign key (ownerID) references Employees(ID)
);

create table if not exists Tickets
(ID int auto_increment primary key,
ticketDescription text(65535),
ticketStatus varchar(20),
priority varchar(18),
contactID int,
ownerID int,
foreign key (contactID) references Contacts(ID),
foreign key (ownerID) references Employees(ID)
);

create table if not exists Subscriptions
(ID int auto_increment primary key,
subName varchar(20),
subDescription varchar(500),
subType varchar(20),
fee decimal(15, 2),
duration int,
durationType varchar(10)
);

create table if not exists ContactSubscriptions
(ID int auto_increment primary key,
renewDate datetime,
subStatus bool,
subID int,
contactID int,
foreign key (subID) references Subscriptions(ID),
foreign key (contactID) references Contacts(ID)
);

create table if not exists Companies
(ID int auto_increment primary key,
companyName varchar(50),
companyDescription varchar(500)
);

create table if not exists ContactCompanies
(ID int auto_increment primary key,
companyStatus varchar(50),
contactID int,
companyID int,
foreign key (contactID) references Contacts(ID),
foreign key (companyID) references Companies(ID) 
);

create table if not exists Deals
(ID int auto_increment primary key,
dealName varchar(120),
pipeline varchar(50),
stage varchar(18),
amount decimal(30, 2),
estCloseDate date,
createDate timestamp,
dealType varchar(18),
priority varchar(18),
ownerID int,
mainContact int,
foreign key (ownerID) references Employees(ID),
foreign key (mainContact) references ContactCompanies(ID)
);

create table if not exists LineItems
(ID int auto_increment primary key,
itemDescription text(65535),
inProduction bool,
endDate date
);

create table if not exists LineItemsDeals
(ID int auto_increment primary key,
qty int,
lineItemID int,
dealID int,
foreign key (lineItemID) references LineItems(ID),
foreign key (dealID) references Deals(ID)
);