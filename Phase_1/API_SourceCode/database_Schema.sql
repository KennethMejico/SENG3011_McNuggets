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
    -- LocationID INTEGER NOT NULL CHECK (LocationID > 0),                            /*  */
    MainText TEXT NOT NULL,                                             /*  */
    LinkToArticle TEXT NOT NULL                                        /* URL */
    -- FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

-- CREATE TABLE IF NOT EXISTS Article_Locations (
-- 	ArticleID INTEGER NOT NULL CHECK (ArticleID > 0),
-- 	LocationID INTEGER NOT NULL CHECK (LocationID > 0),
-- 	CONSTRAINT PK_Article_Locations PRIMARY KEY (ArticleID, LocationID),
-- 	FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID),
--     FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
-- );

CREATE TABLE IF NOT EXISTS Reports (
    ReportID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,                                        /* Primary Key */
    ArticleID INTEGER NOT Null,                                         /*  */
    -- LocationID INTEGER NOT NULL,                                                 /* IF NULL get location from article location*/
    -- Disease varchar(100) NOT NULL,                                      /*  */
    -- Syndrome varchar(100) NOT NULL,                                     /*  */
    EventDate DATE,                                                     /* IF NULL get date from article */
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) 
    -- FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

CREATE TABLE IF NOT EXISTS Report_Locations (
	ReportID INTEGER NOT NULL,
	LocationID INTEGER NOT NULL,
	CONSTRAINT PK_Report_Locations PRIMARY KEY (ReportID, LocationID),
	FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);

CREATE TABLE IF NOT EXISTS Diseases (
	DiseaseID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	DiseaseName varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Syndromes (
	SyndromeID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
	SyndromeName varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Keywords (
    KeywordID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Keyword varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Report_Diseases (
	ReportID INTEGER NOT NULL,
	DiseaseID INTEGER NOT NULL,
	CONSTRAINT PK_Report_Diseases PRIMARY KEY (ReportID, DiseaseID),
	FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
	FOREIGN KEY (DiseaseID) REFERENCES Diseases(DiseaseID)
);

CREATE TABLE IF NOT EXISTS Report_Syndromes (
	ReportID INTEGER NOT NULL,
	SyndromeID INTEGER NOT NULL,
	CONSTRAINT PK_Report_Syndromes PRIMARY KEY (ReportID, SyndromeID),
	FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
	FOREIGN KEY (SyndromeID) REFERENCES Syndromes(SyndromeID)
);

CREATE TABLE IF NOT EXISTS Report_Keywords (
	ReportID INTEGER NOT NULL,
	KeywordID INTEGER NOT NULL,
	CONSTRAINT PK_Report_Keywords PRIMARY KEY (ReportID, KeywordID),
	FOREIGN KEY (ReportID) REFERENCES Reports(ReportID),
	FOREIGN KEY (KeywordID) REFERENCES Keywords(KeywordID)
);

CREATE TABLE IF NOT EXISTS metaData (
	lastUpdated TIMESTAMP NOT NULL,
	lastUserToUpdate TEXT NOT NULL
);


-- /* UPDATE FUNCTIONS */

-- /*

-- CREATE FUNCTION check_reports_insert() 
-- 	RETURNS TRIGGER 
-- 	LANGUAGE PLPGSQL
-- 	AS $$
-- 	BEGIN
-- 		NEW.LOCATIONID =  COALESCE ( ( OLD.LOCATIONID ), ( SELECT  LOCATIONID  from  articles  where  articles.articleID == old.articleID ) );
-- 		NEW.EVENTDATE  =  COALESCE ( ( OLD.EVENTDATE  ), ( SELECT  PUBDATE     from  articles  where  articles.articleID == old.articleID ) );
-- 		RETURN NEW;
-- 	END;
-- 	$$

-- CREATE TRIGGER IF NOT EXISTS reports_Insert
-- 	BEFORE INSERT ON "REPORTS"
-- 	FOR EACH ROW WHEN reports.locationID IS NULL OR reports.eventDate IS NULL
-- 	EXECUTE PROCEDURE check_reports_insert();

-- */

-- /* 
-- CREATE FUNCTION update_metaData()
-- 	RETURNS TRIGGER
-- 	LANGUAGE PLPGSQL
-- 	AS $$
-- 	BEGIN
-- 		UPDATE metaData SET
-- 		lastUpdated = ( SELECT NOW() ),
-- 		lastUserToUpdate = ( SELECT CURRENT_USER );
-- 	END;
-- 	$$ 
-- */

delimiter $$
create procedure select_or_insert_disease(IN diseaseSearch varchar(100), OUT diseaseID INTEGER)
begin
    IF EXISTS(SELECT DiseaseID FROM Diseases WHERE DiseaseName = diseaseSearch) THEN 
        SELECT DiseaseID into diseaseID FROM Diseases WHERE DiseaseName = diseaseSearch;
    ELSE
        INSERT INTO Diseases (DiseaseName) VALUES (diseaseSearch);
        SELECT LAST_INSERT_ID() into diseaseID;
END IF;
end $$


create procedure select_or_insert_syndrome(IN syndromeSearch varchar(100), OUT syndromeID INTEGER)
begin
    IF EXISTS(SELECT SyndromeID FROM Syndromes WHERE SyndromeName = syndromeSearch) THEN 
        SELECT SyndromeID into syndromeID FROM Syndromes WHERE SyndromeName = syndromeSearch;
    ELSE
        INSERT INTO Syndromes (SyndromeName) VALUES (syndromeSearch);
        SELECT LAST_INSERT_ID() into syndromeID;
END IF;
end $$

delimiter ;