
CREATE TABLE IF NOT EXISTS Locations (
   LocationID INTEGER NOT NULL PRIMARY KEY,
   CHECK (LocationID > 0), 
   Latitude NUMERIC(10, 6) NOT NULL, 
   Longitude NUMERIC(10, 6) NOT NULL,  
   LocationName VARCHAR(100) NOT NULL  
);

CREATE TABLE IF NOT EXISTS Articles (
    ArticleID INTEGER NOT NULL CHECK (ArticleID > 0) PRIMARY KEY,
    PubDate DATE NOT NULL,	
    ArticleName VARCHAR(100), 
    MainText TEXT NOT NULL, 
    LinkToArticle TEXT NOT NULL 
);

CREATE TABLE IF NOT EXISTS Reports (
    ReportID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    ArticleID INTEGER NOT Null, 
    EventDate DATE,
    FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID) 
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

delimiter $$

create procedure select_or_insert_disease(IN diseaseSearch varchar(100), OUT disease_ID INTEGER)
begin
    IF EXISTS(SELECT DiseaseID FROM Diseases WHERE DiseaseName = diseaseSearch) THEN 
        SELECT DiseaseID into disease_ID FROM Diseases WHERE DiseaseName = diseaseSearch;
    ELSE
        INSERT INTO Diseases (DiseaseName) VALUES (diseaseSearch);
        SELECT LAST_INSERT_ID() into disease_ID;
END IF;
end $$


create procedure select_or_insert_syndrome(IN syndromeSearch varchar(100), OUT syndrome_ID INTEGER)
begin
    IF EXISTS(SELECT SyndromeID FROM Syndromes WHERE SyndromeName = syndromeSearch) THEN 
        SELECT SyndromeID into syndrome_ID FROM Syndromes WHERE SyndromeName = syndromeSearch;
    ELSE
        INSERT INTO Syndromes (SyndromeName) VALUES (syndromeSearch);
        SELECT LAST_INSERT_ID() into syndrome_ID;
END IF;
end $$

delimiter ;