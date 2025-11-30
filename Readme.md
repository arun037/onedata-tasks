RCA:

The sample python application uses mysql db and records the api request inside the table

Whenever more no.of concurrent request raises it shows internal server error and pool has exhausted due to small pool size.

In order to handle more concurent request we need raise the pool size and increase the db connection in the mysql container also.
In case if we are using aws RDS as a database for querying we can use read replicas and primary db is configured only for writ operations.