/*  CONSTANTS   */

DECLARE textFileStoragePath CONSTANT VARCHAR DEFAULT "~/textFiles";

/*  CREATING TABLES */

CREATE TABLE [IF NOT EXISTS] markerLocations (
   markerID INTEGER NOT NULL CHECK (markerID > 0) PRIMARY KEY,
   latitude NUMERIC(10, 6) NOT NULL,
   longitude NUMERIC(10, 6) NOT NULL,
   locationName VARCHAR(100) NOT NULL,
   country VARCHAR(60) NOT NULL
);

CREATE TABLE [IF NOT EXISTS] articles (
    articleID INTEGER NOT NULL CHECK (articleID > 0) PRIMARY KEY,
    pub_Date DATE,
    articleName VARCHAR(100),
    markerID INTEGER CHECK (markerID > 0),
    FOREIGN KEY (markerID) REFERENCES markerLocations(markerID)
);