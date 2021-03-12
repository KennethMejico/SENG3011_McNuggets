/*  CONSTANTS   */

/*  CREATING TABLES */

CREATE TABLE IF NOT EXISTS Locations (
   LocationID INTEGER NOT NULL PRIMARY KEY,
   CHECK (LocationID > 0),             									 /*  */
   Latitude NUMERIC(10, 6) NOT NULL,                                    /*  */
   Longitude NUMERIC(10, 6) NOT NULL,                                   /*  */
   LocationName VARCHAR(100) NOT NULL                                   /*  */
);

CREATE TABLE IF NOT EXISTS Articles (
    ArticleID INTEGER NOT NULL CHECK (ArticleID > 0) PRIMARY KEY,       /* Primary Key */
    PubDate DATE NOT NULL,												/*  */
    ArticleName VARCHAR(100),                                           /* HEADLINE */
    LocationID INTEGER NOT NULL CHECK (LocationID > 0),                            /*  */
    MainText TEXT NOT NULL,                                             /*  */
    LinkToArticle TEXT NOT NULL,                                        /* URL */
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

CREATE TABLE IF NOT EXISTS Reports (
    ReportID SERIAL NOT NULL PRIMARY KEY,                                        /* Primary Key */
    ArticleID INTEGER NOT Null,                                         /*  */
    LocationID INTEGER NOT NULL,                                                 /* IF NULL get location from article location*/
    Disease varchar(100) NOT NULL,                                      /*  */
    Syndrome varchar(100) NOT NULL,                                     /*  */
    EventDate DATE,                                                     /* IF NULL get date from article */
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID), 
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

CREATE TABLE IF NOT EXISTS metaData (
	lastUpdated TIMESTAMP NOT NULL,
	lastUserToUpdate TEXT NOT NULL
);


/* UPDATE FUNCTIONS */

/*

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
	BEFORE INSERT ON "REPORTS"
	FOR EACH ROW WHEN reports.locationID IS NULL OR reports.eventDate IS NULL
	EXECUTE PROCEDURE check_reports_insert();

*/

/* 
CREATE FUNCTION update_metaData()
	RETURNS TRIGGER
	LANGUAGE PLPGSQL
	AS $$
	BEGIN
		UPDATE metaData SET
		lastUpdated = ( SELECT NOW() ),
		lastUserToUpdate = ( SELECT CURRENT_USER );
	END;
	$$ 
*/
	