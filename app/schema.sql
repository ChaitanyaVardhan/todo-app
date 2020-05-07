import sqlite3


CREATE TABLE User (
  id,
  username,
  password,
);

CREATE TABLE Task (
  id,
  owner_id,
  title,
  description,
  done,
  FOREIGN KEY owner_id REFERS User(id)
);
