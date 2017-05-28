--------------------------------------------------------
--  File created - Saturday-April-15-2017   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table DOSTEPNOSC
--------------------------------------------------------

  CREATE TABLE "TETER"."DOSTEPNOSC" 
   (	"ID_INSTRUKTORA" NUMBER(*,0), 
	"START_DATE" DATE, 
	"END_DATE" DATE
   ) SEGMENT CREATION DEFERRED 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table GRAFIK
--------------------------------------------------------

  CREATE TABLE "TETER"."GRAFIK" 
   (	"ID" NUMBER(*,0), 
	"ID_INSTRUKTORA" NUMBER(*,0), 
	"START_DATE" DATE
   ) SEGMENT CREATION DEFERRED 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table INSTRUKTORZY
--------------------------------------------------------

  CREATE TABLE "TETER"."INSTRUKTORZY" 
   (	"ID" NUMBER(*,0), 
	"LOGIN" VARCHAR2(20 BYTE), 
	"PASSWORD" VARCHAR2(20 BYTE), 
	"IMIE" VARCHAR2(20 BYTE), 
	"NAZWISKO" VARCHAR2(20 BYTE), 
	"UPRAWNIENIA" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table LEKCJA
--------------------------------------------------------

  CREATE TABLE "TETER"."LEKCJA" 
   (	"IMIE" VARCHAR2(20 BYTE), 
	"GODZINA" NUMBER, 
	"DATA" DATE, 
	"ILOSC_OSOB" NUMBER, 
	"KOSZT" NUMBER(*,0), 
	"ID" NUMBER(*,0), 
	"ID_INSTRUKTORA" NUMBER(*,0), 
	"WIEK" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Sequence INSTRUKTORZY_ID_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "TETER"."INSTRUKTORZY_ID_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 30 NOCACHE  NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence LESSON_ID_SEQ
--------------------------------------------------------

   CREATE SEQUENCE  "TETER"."LESSON_ID_SEQ"  MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 52 NOCACHE  NOORDER  NOCYCLE ;
REM INSERTING into TETER.DOSTEPNOSC
SET DEFINE OFF;
REM INSERTING into TETER.GRAFIK
SET DEFINE OFF;
REM INSERTING into TETER.INSTRUKTORZY
SET DEFINE OFF;
Insert into TETER.INSTRUKTORZY (ID,LOGIN,PASSWORD,IMIE,NAZWISKO,UPRAWNIENIA) values (2,'Bronia','328194307','Bronia','Maczynska','Admin');
Insert into TETER.INSTRUKTORZY (ID,LOGIN,PASSWORD,IMIE,NAZWISKO,UPRAWNIENIA) values (1,'bix709','-59130538','Tomek','Teter','User');
REM INSERTING into TETER.LEKCJA
SET DEFINE OFF;
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('h',11,to_date('06-FEB-17','DD-MON-RR'),4,140,27,1,12);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('m18',19,to_date('29-DEC-16','DD-MON-RR'),1,60,20,2,18);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('20',20,to_date('29-DEC-16','DD-MON-RR'),2,90,23,2,20);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('Ania',9,to_date('18-DEC-16','DD-MON-RR'),1,60,25,1,23);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('b',9,to_date('03-MAR-17','DD-MON-RR'),1,60,36,23,1);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('b8',9,to_date('08-DEC-16','DD-MON-RR'),1,60,11,2,8);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('b18',18,to_date('29-DEC-16','DD-MON-RR'),1,60,21,2,18);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('hihi	',15,to_date('03-FEB-17','DD-MON-RR'),2,90,26,2,12);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('t18',18,to_date('29-DEC-16','DD-MON-RR'),1,60,22,1,18);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('Ania',9,to_date('07-FEB-17','DD-MON-RR'),1,60,30,1,23);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('asd',17,to_date('07-MAR-17','DD-MON-RR'),5,150,38,1,123);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('mati',12,to_date('28-DEC-16','DD-MON-RR'),1,60,13,2,35);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('Ania',12,to_date('28-DEC-16','DD-MON-RR'),1,60,14,1,22);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('Mati',11,to_date('29-DEC-16','DD-MON-RR'),1,60,16,2,35);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('B2',13,to_date('29-DEC-16','DD-MON-RR'),4,140,17,2,21);
Insert into TETER.LEKCJA (IMIE,GODZINA,DATA,ILOSC_OSOB,KOSZT,ID,ID_INSTRUKTORA,WIEK) values ('M',10,to_date('29-DEC-16','DD-MON-RR'),4,140,19,1,21);
--------------------------------------------------------
--  DDL for Index INSTRUKTORZY_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "TETER"."INSTRUKTORZY_PK" ON "TETER"."INSTRUKTORZY" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  Constraints for Table LEKCJA
--------------------------------------------------------

  ALTER TABLE "TETER"."LEKCJA" MODIFY ("IMIE" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."LEKCJA" MODIFY ("GODZINA" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."LEKCJA" MODIFY ("DATA" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."LEKCJA" MODIFY ("ILOSC_OSOB" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."LEKCJA" MODIFY ("ID" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."LEKCJA" MODIFY ("ID_INSTRUKTORA" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."LEKCJA" MODIFY ("WIEK" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table GRAFIK
--------------------------------------------------------

  ALTER TABLE "TETER"."GRAFIK" MODIFY ("ID" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."GRAFIK" MODIFY ("ID_INSTRUKTORA" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."GRAFIK" MODIFY ("START_DATE" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table INSTRUKTORZY
--------------------------------------------------------

  ALTER TABLE "TETER"."INSTRUKTORZY" ADD CONSTRAINT "INSTRUKTORZY_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
 
  ALTER TABLE "TETER"."INSTRUKTORZY" MODIFY ("ID" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."INSTRUKTORZY" MODIFY ("LOGIN" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."INSTRUKTORZY" MODIFY ("PASSWORD" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."INSTRUKTORZY" MODIFY ("UPRAWNIENIA" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table DOSTEPNOSC
--------------------------------------------------------

  ALTER TABLE "TETER"."DOSTEPNOSC" MODIFY ("ID_INSTRUKTORA" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."DOSTEPNOSC" MODIFY ("START_DATE" NOT NULL ENABLE);
 
  ALTER TABLE "TETER"."DOSTEPNOSC" MODIFY ("END_DATE" NOT NULL ENABLE);
--------------------------------------------------------
--  Ref Constraints for Table DOSTEPNOSC
--------------------------------------------------------

  ALTER TABLE "TETER"."DOSTEPNOSC" ADD CONSTRAINT "FK_DOSTEPNOSC_INSTRUKTOR" FOREIGN KEY ("ID_INSTRUKTORA")
	  REFERENCES "TETER"."INSTRUKTORZY" ("ID") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table GRAFIK
--------------------------------------------------------

  ALTER TABLE "TETER"."GRAFIK" ADD CONSTRAINT "FK_GRAFIK_INSTRUKTOR" FOREIGN KEY ("ID_INSTRUKTORA")
	  REFERENCES "TETER"."INSTRUKTORZY" ("ID") ON DELETE CASCADE ENABLE;