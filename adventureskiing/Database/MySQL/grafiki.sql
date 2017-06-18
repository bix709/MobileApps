-- phpMyAdmin SQL Dump
-- version 4.0.10.18
-- https://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Jun 17, 2017 at 11:58 AM
-- Server version: 5.6.35
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bix709_adventureskiing`
--

-- --------------------------------------------------------

--
-- Table structure for table `dostepnosc`
--

CREATE TABLE IF NOT EXISTS `dostepnosc` (
  `ID_INSTRUKTORA` int(11) NOT NULL,
  `START_DATE` datetime DEFAULT NULL,
  `END_DATE` datetime DEFAULT NULL,
  UNIQUE KEY `ID_INS_UIDX` (`ID_INSTRUKTORA`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `instruktorzy`
--

CREATE TABLE IF NOT EXISTS `instruktorzy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `LOGIN` varchar(20) DEFAULT NULL,
  `PASSWORD` varchar(20) DEFAULT NULL,
  `IMIE` varchar(20) DEFAULT NULL,
  `NAZWISKO` varchar(20) DEFAULT NULL,
  `UPRAWNIENIA` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `INSTRUKTORZY_PK` (`id`),
  UNIQUE KEY `LOGIN` (`LOGIN`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `instruktorzy`
--

INSERT INTO `instruktorzy` (`id`, `LOGIN`, `PASSWORD`, `IMIE`, `NAZWISKO`, `UPRAWNIENIA`) VALUES
(3, 'bronia', '-1449064029', 'Bronia', 'Maczynska', 'Admin'),
(4, 'bix709', '1407690334', 'Tomek', 'Teter', 'User');

-- --------------------------------------------------------

--
-- Table structure for table `lekcja`
--

CREATE TABLE IF NOT EXISTS `lekcja` (
  `IMIE` varchar(20) DEFAULT NULL,
  `GODZINA` int(11) DEFAULT NULL,
  `DATA` datetime DEFAULT NULL,
  `ILOSC_OSOB` int(11) DEFAULT NULL,
  `KOSZT` decimal(38,0) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ID_INSTRUKTORA` int(11) NOT NULL,
  `WIEK` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_id_ins` (`ID_INSTRUKTORA`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=85 ;

--
-- Dumping data for table `lekcja`
--

INSERT INTO `lekcja` (`IMIE`, `GODZINA`, `DATA`, `ILOSC_OSOB`, `KOSZT`, `id`, `ID_INSTRUKTORA`, `WIEK`) VALUES
('h', 11, '2017-02-06 00:00:00', 4, '140', 53, 3, 12),
('m18', 19, '2016-12-29 00:00:00', 1, '60', 54, 3, 18),
('20', 20, '2016-12-29 00:00:00', 2, '90', 55, 4, 20),
('Ania', 9, '2016-12-18 00:00:00', 1, '60', 56, 4, 23),
('b', 9, '2017-03-03 00:00:00', 1, '60', 57, 3, 1),
('b8', 9, '2016-12-08 00:00:00', 1, '60', 58, 4, 8),
('b18', 18, '2016-12-29 00:00:00', 1, '60', 59, 3, 18),
('hihi	', 15, '2017-02-03 00:00:00', 2, '90', 60, 4, 12),
('t18', 18, '2016-12-29 00:00:00', 1, '60', 61, 4, 18),
('Ania', 9, '2017-02-07 00:00:00', 1, '60', 62, 3, 23),
('asd', 17, '2017-03-07 00:00:00', 5, '150', 63, 3, 123),
('mati', 12, '2016-12-28 00:00:00', 1, '60', 64, 4, 35),
('Ania', 12, '2016-12-28 00:00:00', 1, '60', 65, 3, 22),
('Mati', 11, '2016-12-29 00:00:00', 1, '60', 66, 4, 35),
('B2', 13, '2016-12-29 00:00:00', 4, '140', 67, 4, 21),
('M', 10, '2016-12-29 00:00:00', 4, '140', 68, 3, 21),
('tomek', 9, '2017-06-04 00:00:00', 5, '150', 69, 4, 15),
('aa', 15, '2017-06-11 00:00:00', 3, '120', 72, 3, 11),
('ania', 9, '2017-06-11 00:00:00', 1, '60', 73, 4, 23),
('anna', 9, '2017-06-15 00:00:00', 1, '60', 75, 3, 23),
('bb', 16, '2017-06-15 00:00:00', 2, '90', 76, 4, 12),
('tt', 16, '2017-06-15 00:00:00', 1, '60', 77, 3, 5),
('tt', 15, '2017-06-15 00:00:00', 1, '60', 78, 4, 5),
('tomk', 19, '2017-06-15 00:00:00', 3, '120', 83, 4, 21),
('aa', 9, '2017-06-17 00:00:00', 3, '120', 84, 3, 21);

-- --------------------------------------------------------

--
-- Table structure for table `powiadomienia`
--

CREATE TABLE IF NOT EXISTS `powiadomienia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session_id` int(11) NOT NULL,
  `data` date NOT NULL,
  `godzina` int(11) NOT NULL,
  `ilosc_osob` int(11) NOT NULL,
  `operacja` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `session_id_fk` (`session_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE IF NOT EXISTS `session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `expiration_date` date NOT NULL,
  `device_id` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `device_id` (`device_id`),
  KEY `user_id_fk` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`id`, `user_id`, `expiration_date`, `device_id`) VALUES
(3, 3, '2017-02-06', '3');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dostepnosc`
--
ALTER TABLE `dostepnosc`
  ADD CONSTRAINT `dostepnosc_ibfk_1` FOREIGN KEY (`ID_INSTRUKTORA`) REFERENCES `instruktorzy` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `lekcja`
--
ALTER TABLE `lekcja`
  ADD CONSTRAINT `lekcja_ibfk_1` FOREIGN KEY (`ID_INSTRUKTORA`) REFERENCES `instruktorzy` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `powiadomienia`
--
ALTER TABLE `powiadomienia`
  ADD CONSTRAINT `session_id_fk` FOREIGN KEY (`session_id`) REFERENCES `session` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `session`
--
ALTER TABLE `session`
  ADD CONSTRAINT `user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `instruktorzy` (`id`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
