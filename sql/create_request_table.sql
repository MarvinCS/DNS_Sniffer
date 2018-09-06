CREATE  TABLE  IF NOT EXISTS requests
(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ip varchar(55),
  mac varchar (55),
  domain_name INTEGER NOT NULL,
  server INTEGER,
  created_at time,
  updated_at time
)