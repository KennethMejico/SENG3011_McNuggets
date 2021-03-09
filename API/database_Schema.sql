/*  CONSTANTS   */

/*  CREATING TABLES */

CREATE TABLE IF NOT EXISTS locations (
   locationID INTEGER CHECK (markerID > 0) PRIMARY KEY,                 /*  */
   latitude NUMERIC(10, 6) NOT NULL,                                    /*  */
   longitude NUMERIC(10, 6) NOT NULL,                                   /*  */
   locationName VARCHAR(100) NOT NULL                                   /*  */
);

CREATE TABLE IF NOT EXISTS articles (
    articleID INTEGER NOT NULL CHECK (articleID > 0) PRIMARY KEY,       /* Primary Key */
    pubDate DATE NOT NULL,												/*  */
    articleName VARCHAR(100),                                           /* HEADLINE */
    locationID INTEGER CHECK (markerID > 0),                            /*  */
    mainText TEXT NOT NULL,                                             /*  */
    linkToArticle TEXT NOT NULL,                                        /* URL */
    FOREIGN KEY (markerID) REFERENCES markerLocations(markerID)
);

CREATE TABLE IF NOT EXISTS reports (
    reportID SERIAL PRIMARY KEY,                                        /* Primary Key */
    articleID INTEGER not null,                                         /*  */
    locationID INTEGER,                                                 /* IF NULL get location from article location*/
    disease varchar(100) not null,                                      /*  */
    syndrome varchar(100) not null,                                     /*  */
    eventDate DATE,                                                     /* IF NULL get date from article */
    FOREIGN KEY (articleID) REFERENCES articles(articleID)
    FOREIGN KEY (reportLocation) REFERENCES locations(locationID)
);

CREATE TABLE IF NOT EXISTS metaData (
	lastUpdated TIMESTAMP not null,

);

CREATE FUNCTION check_reports_insert() 
	RETURNS TRIGGER 
	LANGUAGE PLPGSQL
	AS $$
	BEGIN
		NEW.LOCATIONID =  COALESCE ( ( OLD.LOCATIONID ), ( SELECT  LOCATIONID  from  articles  where  articles.articleID == old.articleID ) );
		NEW.EVENTDATE  =  COALESCE ( ( OLD.EVENTDATE  ), ( SELECT  PUBDATE     from  articles  where  articles.articleID == old.articleID ) );
		RETURN NEW;
	END;
	$$

CREATE TRIGGER IF NOT EXISTS reports_Insert
	BEFORE INSERT ON REPORTS
	FOR EACH ROW WHEN reports.locationID IS NULL OR reports.eventDate IS NULL
	EXECUTE PROCEDURE check_reports_insert();
