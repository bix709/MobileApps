-- ------------------------------------------------------
--  File created - Saturday-April-15-2017
-- ------------------------------------------------------
-- ------------------------------------------------------
--  DDL for Table DOSTEPNOSC
-- ------------------------------------------------------

  CREATE TABLE `DOSTEPNOSC`
   (	`ID_INSTRUKTORA` DECIMAL(38,0),
	`START_DATE` DATETIME,
	`END_DATE` DATETIME
   )
  ;
-- ------------------------------------------------------
--  DDL for Table GRAFIK
-- ------------------------------------------------------

  CREATE TABLE `GRAFIK`
   (	`ID` DECIMAL(38,0),
	`ID_INSTRUKTORA` DECIMAL(38,0),
	`START_DATE` DATETIME
   )
  ;
-- ------------------------------------------------------
--  DDL for Table INSTRUKTORZY
-- ------------------------------------------------------

  CREATE TABLE `INSTRUKTORZY`
   (	`ID` DECIMAL(38,0),
	`LOGIN` VARCHAR(20),
	`PASSWORD` VARCHAR(20),
	`IMIE` VARCHAR(20),
	`NAZWISKO` VARCHAR(20),
	`UPRAWNIENIA` VARCHAR(20)
   )
  ;
-- ------------------------------------------------------
--  DDL for Table LEKCJA
-- ------------------------------------------------------

  CREATE TABLE `LEKCJA`
   (	`IMIE` VARCHAR(20),
	`GODZINA` DOUBLE,
	`DATA` DATETIME,
	`ILOSC_OSOB` DOUBLE,
	`KOSZT` DECIMAL(38,0),
	`ID` DECIMAL(38,0),
	`ID_INSTRUKTORA` DECIMAL(38,0),
	`WIEK` DOUBLE
   )
  ;
-- ------------------------------------------------------
--  DDL for Sequence INSTRUKTORZY_ID_SEQ
-- ------------------------------------------------------

   CALL  CreateSequence('`INSTRUKTORZY_ID_SEQ`', 30, 1)    ;
-- ------------------------------------------------------
--  DDL for Sequence LESSON_ID_SEQ
-- ------------------------------------------------------

   CALL  CreateSequence('`LESSON_ID_SEQ`', 52, 1)    ;
-- INSERTING into DOSTEPNOSC
/* SET DEFINE OFF; */
-- INSERTING into GRAFIK
/* SET DEFINE OFF; */
-- INSERTING into INSTRUKTORZY
/* SET DEFINE OFF; */
Insert into INSTRUKTORZY (LOGIN,PASSWORD,IMIE,NAZWISKO,UPRAWNIENIA) values ('Bronia','328194307','Bronia','Maczynska','Admin');
Insert into INSTRUKTORZY (LOGIN,PASSWORD,IMIE,NAZWISKO,UPRAWNIENIA) values ('bix709','-59130538','Tomek','Teter','User');
-- INSERTING into LEKCJA
/* SET DEFINE OFF; */
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('h',11,str_to_date('06-FEB-17','%d-%b-%y'),4,140,3,12);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('m18',19,str_to_date('29-DEC-16','%d-%b-%y'),1,60,3,18);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('20',20,str_to_date('29-DEC-16','%d-%b-%y'),2,90,4,20);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('Ania',9,str_to_date('18-DEC-16','%d-%b-%y'),1,60,4,23);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('b',9,str_to_date('03-MAR-17','%d-%b-%y'),1,60,3,1);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('b8',9,str_to_date('08-DEC-16','%d-%b-%y'),1,60,4,8);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('b18',18,str_to_date('29-DEC-16','%d-%b-%y'),1,60,3,18);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('hihi	',15,str_to_date('03-FEB-17','%d-%b-%y'),2,90,4,12);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('t18',18,str_to_date('29-DEC-16','%d-%b-%y'),1,60,4,18);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('Ania',9,str_to_date('07-FEB-17','%d-%b-%y'),1,60,3,23);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('asd',17,str_to_date('07-MAR-17','%d-%b-%y'),5,150,3,123);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('mati',12,str_to_date('28-DEC-16','%d-%b-%y'),1,60,4,35);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('Ania',12,str_to_date('28-DEC-16','%d-%b-%y'),1,60,3,22);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('Mati',11,str_to_date('29-DEC-16','%d-%b-%y'),1,60,4,35);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('B2',13,str_to_date('29-DEC-16','%d-%b-%y'),4,140,4,21);
Insert into LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID_INSTRUKTORA,WIEK) values ('M',10,str_to_date('29-DEC-16','%d-%b-%y'),4,140,3,21);
-- ------------------------------------------------------
--  DDL for Index INSTRUKTORZY_PK
-- ------------------------------------------------------

  CREATE UNIQUE INDEX `INSTRUKTORZY_PK` ON `INSTRUKTORZY` (`ID`)
  ;
-- ------------------------------------------------------
--  Constraints for Table LEKCJA
-- ------------------------------------------------------

  ALTER TABLE `LEKCJA` MODIFY (`IMIE` NOT NULL ENABLE);

  ALTER TABLE `LEKCJA` MODIFY (`GODZINA` NOT NULL ENABLE);

  ALTER TABLE `LEKCJA` MODIFY (`DATA` NOT NULL ENABLE);

  ALTER TABLE `LEKCJA` MODIFY (`ILOSC_OSOB` NOT NULL ENABLE);

  ALTER TABLE `LEKCJA` MODIFY (`ID` NOT NULL ENABLE);

  ALTER TABLE `LEKCJA` MODIFY (`ID_INSTRUKTORA` NOT NULL ENABLE);

  ALTER TABLE `LEKCJA` MODIFY (`WIEK` NOT NULL ENABLE);
-- ------------------------------------------------------
--  Constraints for Table GRAFIK
-- ------------------------------------------------------

  ALTER TABLE `GRAFIK` MODIFY (`ID` NOT NULL ENABLE);

  ALTER TABLE `GRAFIK` MODIFY (`ID_INSTRUKTORA` NOT NULL ENABLE);

  ALTER TABLE `GRAFIK` MODIFY (`START_DATE` NOT NULL ENABLE);
-- ------------------------------------------------------
--  Constraints for Table INSTRUKTORZY
-- ------------------------------------------------------

  ALTER TABLE `INSTRUKTORZY` ADD CONSTRAINT `INSTRUKTORZY_PK` PRIMARY KEY (`ID`)
  10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE `USERS`  ENABLE;

  ALTER TABLE `INSTRUKTORZY` MODIFY (`ID` NOT NULL ENABLE);

  ALTER TABLE `INSTRUKTORZY` MODIFY (`LOGIN` NOT NULL ENABLE);

  ALTER TABLE `INSTRUKTORZY` MODIFY (`PASSWORD` NOT NULL ENABLE);

  ALTER TABLE `INSTRUKTORZY` MODIFY (`UPRAWNIENIA` NOT NULL ENABLE);
-- ------------------------------------------------------
--  Constraints for Table DOSTEPNOSC
-- ------------------------------------------------------

  ALTER TABLE `DOSTEPNOSC` MODIFY (`ID_INSTRUKTORA` NOT NULL ENABLE);

  ALTER TABLE `DOSTEPNOSC` MODIFY (`START_DATE` NOT NULL ENABLE);

  ALTER TABLE `DOSTEPNOSC` MODIFY (`END_DATE` NOT NULL ENABLE);
-- ------------------------------------------------------
--  Ref Constraints for Table DOSTEPNOSC
-- ------------------------------------------------------

  ALTER TABLE `DOSTEPNOSC` ADD CONSTRAINT `FK_DOSTEPNOSC_INSTRUKTOR` FOREIGN KEY (`ID_INSTRUKTORA`)
	  REFERENCES `INSTRUKTORZY` (`ID`) ON DELETE CASCADE;
-- ------------------------------------------------------
--  Ref Constraints for Table GRAFIK
-- ------------------------------------------------------

  ALTER TABLE `GRAFIK` ADD CONSTRAINT `FK_GRAFIK_INSTRUKTOR` FOREIGN KEY (`ID_INSTRUKTORA`)
	  REFERENCES `INSTRUKTORZY` (`ID`) ON DELETE CASCADE;
