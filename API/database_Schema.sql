/*  CONSTANTS   */

/*  CREATING TABLES */

CREATE TABLE [IF NOT EXISTS] locations (
   locationID INTEGER CHECK (markerID > 0) PRIMARY KEY,                 /*  */
   latitude NUMERIC(10, 6) NOT NULL,                                    /*  */
   longitude NUMERIC(10, 6) NOT NULL,                                   /*  */
   locationName VARCHAR(100) NOT NULL                                   /*  */
);

CREATE TABLE [IF NOT EXISTS] articles (
    articleID INTEGER NOT NULL CHECK (articleID > 0) PRIMARY KEY,       /* Primary Key */
    pub_Date DATE NOT NULL,                                             /*  */
    articleName VARCHAR(100),                                           /* HEADLINE */
    locationID INTEGER CHECK (markerID > 0),                            /*  */
    mainText TEXT NOT NULL,                                             /*  */
    linkToArticle TEXT NOT NULL,                                        /* URL */
    FOREIGN KEY (markerID) REFERENCES markerLocations(markerID)         
);

CREATE TABLE [IF NOT EXISTS] reports (
    reportID SERIAL PRIMARY KEY,                                        /* Primary Key */
    articleID INTEGER not null,                                         /*  */
    disease varchar(100) not null,                                      /*  */
    syndrome varchar(100) not null,                                     /*  */
    eventDate DATE,                                                     /* IF NULL get date from article */
    locationID INTEGER,                                                 /* IF NULL get location from article location*/
    FOREIGN KEY (articleID) REFERENCES articles(articleID)              /*  */
    FOREIGN KEY (reportLocation) REFERENCES locations(locationID)       /*  */
);