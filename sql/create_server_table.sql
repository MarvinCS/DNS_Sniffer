CREATE TABLE IF NOT EXISTS server
(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ip varchar(15) NOT NULL,
  created_at time,
  updated_at time
)