-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: hpdb1
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `dep` varchar(45) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `sem` varchar(45) DEFAULT NULL,
  `std_id` varchar(45) NOT NULL,
  `std_name` varchar(45) DEFAULT NULL,
  `un_roll_no` varchar(45) DEFAULT NULL,
  `class_roll_no` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone_no` varchar(45) DEFAULT NULL,
  `father` varchar(45) DEFAULT NULL,
  `teacher` varchar(45) DEFAULT NULL,
  `photo_sample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Computer science','B.tech','2021-2022','5th','1','Himanshu','1918381','38','Male','18/05/2021','himanshu@gmail.com','1234567890','mukesh','lisa','Yes'),('Machanical','B.tech','2021-2022','5th','2','vishal','1918382','40','Male','18/04/2021','vishal@gmail.com','1234667890','bijendra','preem','Yes'),('Machanical','B.tech','2021-2022','5th','3','kshitj','1918385','42','Male','18/04/2021','vishal@gmail.com','1234667890','bijendra','preem','Yes'),('Machanical','B.tech','2021-2022','5th','4','kshitj','1918385','42','Male','18/04/2021','vishal@gmail.com','1234667890','bijendra','preem','Yes'),('Machanical','B.tech','2021-2022','5th','8','kshitj','1918385','42','Male','18/04/2021','vishal@gmail.com','1234667890','bijendra','preem','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-25 10:28:58
