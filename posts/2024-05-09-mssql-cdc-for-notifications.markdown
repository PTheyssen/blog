---
title: CDC for generating Notifications in SQL Server
author: Philipp Theyssen
---

At work we are implementing an use-case of  generating notifications
for a user in a web application. The original events are based on updates made to certain tables
in a sql server DB (Azure sql managed instance). 

Multiple possibilities exist to generate the notifications, but
for now we have  decided to use Change Data Capture (CDC) for generating the actual events.
Other options would included asnyc decoupled events / message passing.

Which has its benefits but is definitely overkill for our current setup (infrastructure).


I have already encountered Change Data Capture (CDC) during my university,
and there is of course extensive documentation from [microsoft](https://learn.microsoft.com/en-us/azure/azure-sql/database/change-data-capture-overview?view=azuresql), but I feel like there not many good end-2-end walk throughs for building
a prototype with this technology. 

I feel like the ms learn article on the topic is a starting point but really just that,
of course there is the t-sql reference but still no advanced.

There exists more advanced tutorial on using debezium but this again requires eventhub 
https://github.com/Azure-Samples/azure-sql-db-change-stream-debezium.



We will consider a product table which can receive insert, updates and deletes events, 
in the form of SQL queries. These changes to the product table will be captures with CDC
and which we will use to populate a notifications table which in turn can then be consumed
by another application.

TODO: link to github repo

## Content

- azure sql edge in docker (version workin on mac)
- azure data studio
- simulating changes to product table
- CDC configuration for generating notifications
- consuming notifications in a simple web-app



## Initial setup
We setup a local instance of mssql with docker, we opt for azure-sql-edge as this
version runs on all major operating systems including mac (apple silicon) (??? TODO CONFIRM)

We use azure data studio to connect to the DB, using sql projects allows us to sync a DB easily after setup.


We create a single table for products for an example database "cdc-example":

```sql
CREATE TABLE [dbo].[Products] (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Category NVARCHAR(50),
    Price DECIMAL(10, 2),
    StockQuantity INT
);
```

Next we enable cdc for the table in the sql post-deployment script

```sql
USE [cdc-example]
EXEC sys.sp_cdc_enable_db;
GO
EXEC sys.sp_cdc_enable_table
    @source_schema = N'dbo',
    @source_name = N'Products',
    @role_name = NULL;
GO
```


## TODO create DB role to access tables!
```sql
CREATE LOGIN ShopAdminApp WITH PASSWORD = 'ABCDEFG!1'
GO

IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = 'ShopAdmin')
BEGIN
    CREATE USER [ShopAdminApp] FOR LOGIN [ShopAdminApp]
END;

CREATE ROLE ShopAdmin;
GO

ALTER ROLE  ShopAdmin ADD MEMBER ShopAdminApp;
GO

GRANT SELECT, INSERT, UPDATE, DELETE ON dbo.Products TO ShopAdmin;
GO
```


## Azure function backend (C#)

- creating azure functions


- CRUD azure function app on products
- GET notifications
- PUT (mark as read)


## TODO built basic app / frontend to showcase




