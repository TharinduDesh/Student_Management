-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 21, 2022 at 12:19 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `stNo` int(5) NOT NULL,
  `fName` varchar(15) DEFAULT NULL,
  `lName` varchar(15) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `telephoneNo` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`stNo`, `fName`, `lName`, `dob`, `telephoneNo`) VALUES
(12345, 'Tharindu', 'Deshanjana', '2002/07/17', 788149472),
(13425, 'Ravindu', 'Sahan', '2003/02/20', 707892461),
(13902, 'Oshada', 'Induruwan', '2000/09/12', 774507392),
(15432, 'Devindu', 'Vimukthi', '2000/06/20', 703798330),
(20000, 'Omitha', 'Weerasinghe', '2000/03/21', 772003000);

-- --------------------------------------------------------

--
-- Table structure for table `student_attend`
--

CREATE TABLE `student_attend` (
  `stNo` int(5) DEFAULT NULL,
  `attendDate` varchar(15) DEFAULT NULL,
  `attendance` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_attend`
--

INSERT INTO `student_attend` (`stNo`, `attendDate`, `attendance`) VALUES
(12345, '2022/08/18', 'Yes'),
(13425, '2022/08/19', 'No'),
(13902, '2022/08/20', 'Yes'),
(15432, '2022/08/21', 'Yes'),
(20000, '2022/08/22', 'No'),
(12345, '2022/09/12', 'Yes'),
(13425, '2022/09/13', 'No'),
(13902, '2022/09/13', 'Yes'),
(15432, '2022/09/15', 'Yes'),
(20000, '2022/09/16', 'No'),
(12345, '2022/08/22', 'Yes'),
(13425, '2022/08/22', 'No'),
(13902, '2022/08/22', 'Yes'),
(15432, '2022/08/23', 'Yes'),
(20000, '2022/08/24', 'No');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stNo`);

--
-- Indexes for table `student_attend`
--
ALTER TABLE `student_attend`
  ADD KEY `student` (`stNo`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student_attend`
--
ALTER TABLE `student_attend`
  ADD CONSTRAINT `student` FOREIGN KEY (`stNo`) REFERENCES `student` (`stNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_attend_ibfk_1` FOREIGN KEY (`stNo`) REFERENCES `student` (`stNo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
