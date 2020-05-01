# Installation
## Adapted from Caroline Schmitt (DSI-ATL) and Boom Devahastin Na Ayudhya (DSI-NYC)

We will be installing two tools: PostgreSQL, which is the actual database system, and pgAdmin4, a powerful web-based GUI.

**Important**: You will likely be prompted to come up with a password at some point during installation. **Remember it!**

## Mac

1. Install [Postgres.app](https://postgresapp.com/). Make sure you move it to your `Applications` folder.
2. In your Terminal, run this line of code:
```Bash
sudo mkdir -p /etc/paths.d &&
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/
postgresapp
```
3. Install [pgAdmin4](https://www.pgadmin.org/download/pgadmin-4-macos/).

## Windows

Not being a Windows user myself, I'm not entirely certain if this will work. If you already have PostgreSQL & pgAdmin4 up and running, don't reinstall.

1. Download and run the [EnterpriseDB installer](https://www.postgresql.org/download/windows/). This should have both PostgreSQL and pgAdmin4.
2. If prompted to provide a password during installation, remember what you enter -- you'll need it for connecting.


## Running PostgreSQL

1. Open the PostgreSQL app and initialize a server. The default settings should be OK.

## Using pgAdmin4

1. Open pgAdmin4.
2. Create a server (right click on Servers -> create -> server). Name it something descriptive (ex. my_postgres_server) and set the connection Host name to be 'localhost'. Watch [this video](https://www.youtube.com/watch?v=lG2Nes-wi54) if you need more help with this step.
3. Create a Database (right click on the server you just created -> create -> Database). Name this something descriptive (ex. dsi_sql_practice) and hit save.
4. Under Servers > your-server-name > Databases, click on the name of the Database you just created. Click Tools -> Query Tool. Now we can start using SQL!

### Importing Data
The data used for this lesson was compiled by Boom Devahastin Na Ayudhya (DSI-NYC) which was from [Udemy's Master SQL for Data Science course](https://www.udemy.com/master-sql-for-data-science/learn/lecture/9790570#overview).

1. Copy and paste the database construction queries from the employees_table.txt script into your query. Run this.
2. Your table is saved and can be viewed under Schemas > Public > Tables.
3. You can now run queries accessing data from this table.
