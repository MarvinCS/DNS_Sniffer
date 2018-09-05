CREATE TABLE IF NOT EXISTS domains
(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name varchar(255) NOT NULL ,
  created_at time,
  updated_at time
);