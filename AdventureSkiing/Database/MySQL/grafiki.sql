-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2017 at 03:00 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 7.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grafiki`
--

-- --------------------------------------------------------

--
-- Table structure for table `dostepnosc`
--

CREATE TABLE `dostepnosc` (
  `ID_INSTRUKTORA` int(11) NOT NULL,
  `START_DATE` datetime DEFAULT NULL,
  `END_DATE` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `instruktorzy`
--

CREATE TABLE `instruktorzy` (
  `id` int(11) NOT NULL,
  `LOGIN` varchar(20) DEFAULT NULL,
  `PASSWORD` varchar(20) DEFAULT NULL,
  `IMIE` varchar(20) DEFAULT NULL,
  `NAZWISKO` varchar(20) DEFAULT NULL,
  `UPRAWNIENIA` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `instruktorzy`
--

INSERT INTO `instruktorzy` (`id`, `LOGIN`, `PASSWORD`, `IMIE`, `NAZWISKO`, `UPRAWNIENIA`) VALUES
(3, 'Bronia', '328194307', 'Bronia', 'Maczynska', 'Admin'),
(4, 'bix709', '-59130538', 'Tomek', 'Teter', 'User');

-- --------------------------------------------------------

--
-- Table structure for table `lekcja`
--

CREATE TABLE `lekcja` (
  `IMIE` varchar(20) DEFAULT NULL,
  `GODZINA` int(11) DEFAULT NULL,
  `DATA` datetime DEFAULT NULL,
  `ILOSC_OSOB` int(11) DEFAULT NULL,
  `KOSZT` decimal(38,0) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `ID_INSTRUKTORA` int(11) NOT NULL,
  `WIEK` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
('M', 10, '2016-12-29 00:00:00', 4, '140', 68, 3, 21);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dostepnosc`
--
ALTER TABLE `dostepnosc`
  ADD UNIQUE KEY `ID_INS_UIDX` (`ID_INSTRUKTORA`);

--
-- Indexes for table `instruktorzy`
--
ALTER TABLE `instruktorzy`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `INSTRUKTORZY_PK` (`id`),
  ADD UNIQUE KEY `LOGIN` (`LOGIN`);

--
-- Indexes for table `lekcja`
--
ALTER TABLE `lekcja`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_id_ins` (`ID_INSTRUKTORA`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `instruktorzy`
--
ALTER TABLE `instruktorzy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `lekcja`
--
ALTER TABLE `lekcja`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
