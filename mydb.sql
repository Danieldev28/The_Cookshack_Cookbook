-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: Cookshack
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Allergens`
--

DROP TABLE IF EXISTS `Allergens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Allergens` (
  `Allergen_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Allergen_name` varchar(30) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Allergen_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Allergens`
--

LOCK TABLES `Allergens` WRITE;
/*!40000 ALTER TABLE `Allergens` DISABLE KEYS */;
INSERT INTO `Allergens` VALUES (1,'Dairy','Any milk product'),(2,'Wheat','Any Wheat product'),(3,'Shellfish','Any Shellfish product'),(4,'Bread','Any Bread product'),(5,'Peanuts','Any Peanut product'),(6,'Eggs','Any Egg product'),(7,'Fish','Any Fish product'),(8,'Soy','Any Soy product');
/*!40000 ALTER TABLE `Allergens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Categories`
--

DROP TABLE IF EXISTS `Categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Categories` (
  `Category_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Category_name` varchar(30) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Category_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categories`
--

LOCK TABLES `Categories` WRITE;
/*!40000 ALTER TABLE `Categories` DISABLE KEYS */;
INSERT INTO `Categories` VALUES (1,'Breakfast','Any Breakfast item'),(2,'Lunch','Any Lunch item'),(3,'Dinner','Any Dinner item'),(4,'Drink','Any Drink item'),(5,'Dessert','Any Dessert item');
/*!40000 ALTER TABLE `Categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recipes`
--

DROP TABLE IF EXISTS `Recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Recipes` (
  `Recipe_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Recipe_name` varchar(30) DEFAULT NULL,
  `Ingredients` varchar(300) DEFAULT NULL,
  `Category_ID` int(11) DEFAULT NULL,
  `User_ID` int(11) DEFAULT NULL,
  `Allergen_ID` int(11) DEFAULT NULL,
  `Instructions` varchar(300) DEFAULT NULL,
  `WorldCuisine_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`Recipe_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipes`
--

LOCK TABLES `Recipes` WRITE;
/*!40000 ALTER TABLE `Recipes` DISABLE KEYS */;
INSERT INTO `Recipes` VALUES (1,'soup','       these are ingredients',1,2,3,'      these are instrucitons',2),(2,'soup','some ingredients',2,13,3,'      some instruction',3),(3,'soup','       these are ingredients ',1,15,2,'      these are instructions',4),(4,'salad','       ingredients',2,17,2,'      instructions',1);
/*!40000 ALTER TABLE `Recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `User_ID` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(30) DEFAULT NULL,
  `Dateofbirth` varchar(20) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=19  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Daniel','2020-12-16','danielsmittyd@hotmail.com','Canada'),(2,'Daniel','2019-09-24','danielsmittyd@hotmail.com','Canada'),(3,'Daniel1','2019-09-20','danielsmittyd@hotmail.com','Canada'),(4,'Daniel2','2019-09-03','danielsmittyd@hotmail.com','Canada'),(5,'daniel3','2019-09-19','splinter683@hotmail.com','Canada'),(6,'daniel','2019-09-17','splinter683@hotmail.com','Canada'),(7,'daniel','2019-09-21','danielsmittyd@hotmail.com','Canada'),(8,'Daniel','2019-09-20','isa@kynnecme.com','Canada'),(9,'daniel','2019-09-18','danielsmittyd@hotmail.com','Canada'),(10,'daniel','2019-09-18','splinter683@hotmail.com','Canada'),(11,'daniel','2019-09-18','danielsmittyd@hotmail.com','Canada'),(12,'fdsa','2019-09-20','splinter683@hotmail.com','Canada'),(13,'daniel','2019-09-18','splinter683@hotmail.com','Canada'),(14,'dfds','2019-09-17','isa@kynnecme.com','Canada'),(15,'Daniel','2019-01-01','danielsmittyd@hotmail.com','Canada'),(16,'daniel','2019-01-02','splinter683@hotmail.com','Canada'),(17,'','2020-01-01','danielsmittyd@hotmail.com','Canada'),(18,'Brian','1994-09-18','brian123@hotmail.com','Canada');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WorldCuisine`
--

DROP TABLE IF EXISTS `WorldCuisine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WorldCuisine` (
  `WorldCuisine_ID` int(11) NOT NULL AUTO_INCREMENT,
  `WorldCuisine_name` varchar(30) DEFAULT NULL,
  `Description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`WorldCuisine_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5  DEFAULT CHARACTER SET utf8
  DEFAULT COLLATE utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WorldCuisine`
--

LOCK TABLES `WorldCuisine` WRITE;
/*!40000 ALTER TABLE `WorldCuisine` DISABLE KEYS */;
INSERT INTO `WorldCuisine` VALUES (1,'Mexican','Any Mexcian dish'),(2,'Asian','Any Asian dish'),(3,'Indian','Any Indian dish'),(4,'Italian','Any Italian dish');
/*!40000 ALTER TABLE `WorldCuisine` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-17 16:08:50
