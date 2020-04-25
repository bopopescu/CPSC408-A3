# Data Generator and Importer
## CPSC 408
## Matthew Parnham
Simple programs to generate fake data for matches in the videogame 'Valorant'.  I am building a system to store
and analyze my personal Valorant statistics, and this step allows me to test data in bulk
with minimal input effort.
### Usage
```
> python Generate_Match.py <export csv name>
```
This will generate a csv containing fake, formatted match data for a Valorant match.
```
> python ImportCsv.py <csv name>
```
This will import a previously generated CSV, parse it, and import it into the appropriate tables in the database.

### Comments
* This will not work on its own since the database credentials are not posted to this repo.
* To use, please create a file called 'creds' in the same directory as the project.
    * Format it as below
    ```
  <DB Address>
  <Username>
  <Password>
    ``` 
 * The database used can be generated with the following MySQL code
 ```mysql
CREATE TABLE MatchDetails (
    MatchID INT PRIMARY KEY AUTO_INCREMENT,
    Map INT,
    Win BOOLEAN,
    RoundsWon INT,
    RoundsLost INT,
    Date DATE
);

CREATE TABLE Scoreboard (
    MatchID INT,
    PlayerName VARCHAR(32),
    Hero INT,
    AVGCombatScore INT,
    Kills INT,
    Deaths INT,
    Assists INT,
    EconRating INT,
    FirstBloods INT,
    Plants INT,
    Defuses INT
);

CREATE TABLE Timeline (
    MatchID INT,
    RoundNum INT,
    Score INT,
    Kills INT,
    Assists INT,
    Died BOOLEAN,
    MoneySpent INT,
    Weapon INT,
    Won BOOLEAN
);

CREATE TABLE Performance (
  MatchID INT,
  PlayerName VARCHAR(32),
  Kills INT,
  Deaths INT,
  Assists INT
);

CREATE TABLE Practice (
  PracticeType VARCHAR(32),
  KillCount INT,
  MinutesPlayed INT,
  Date DATE
);


CREATE TABLE Heroes (
    HeroID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(16)
);

CREATE TABLE Weapons (
    WeaponID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(16)
);

CREATE TABLE Maps (
    MapID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(16)
);

INSERT INTO Maps(Name)
VALUES('Bind');
INSERT INTO Maps(Name)
VALUES('Haven');
INSERT INTO Maps(Name)
VALUES('Split');
INSERT INTO Heroes(Name)
VALUES('Phoenix');
INSERT INTO Heroes(Name)
VALUES('Jett');
INSERT INTO Heroes(Name)
VALUES('Viper');
INSERT INTO Heroes(Name)
VALUES('Sova');
INSERT INTO Heroes(Name)
VALUES('Cypher');
INSERT INTO Heroes(Name)
VALUES('Brimstone');
INSERT INTO Heroes(Name)
VALUES('Sage');
INSERT INTO Heroes(Name)
VALUES('Omen');
INSERT INTO Heroes(Name)
VALUES('Breach');
INSERT INTO Heroes(Name)
VALUES('Raze');
INSERT INTO Weapons(Name)
VALUES('Bulldog');
INSERT INTO Weapons(Name)
VALUES('Vandal');
INSERT INTO Weapons(Name)
VALUES('Phantom');
INSERT INTO Weapons(Name)
VALUES('Guardian');
INSERT INTO Weapons(Name)
VALUES('Marshall');
INSERT INTO Weapons(Name)
VALUES('Operator');
INSERT INTO Weapons(Name)
VALUES('Classic');
INSERT INTO Weapons(Name)
VALUES('Shorty');
INSERT INTO Weapons(Name)
VALUES('Frenzy');
INSERT INTO Weapons(Name)
VALUES('Ghost');
INSERT INTO Weapons(Name)
VALUES('Sheriff');
INSERT INTO Weapons(Name)
VALUES('Stinger');
INSERT INTO Weapons(Name)
VALUES('Spectre');
INSERT INTO Weapons(Name)
VALUES('Bucky');
INSERT INTO Weapons(Name)
VALUES('Judge');
INSERT INTO Weapons(Name)
VALUES('Ares');
INSERT INTO Weapons(Name)
VALUES('Odin');
```
