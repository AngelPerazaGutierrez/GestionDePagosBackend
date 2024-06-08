-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: database_cp
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `cp`
--

DROP TABLE IF EXISTS `cp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adjuntos` varchar(100) DEFAULT NULL,
  `fecha` date NOT NULL,
  `ciudad` varchar(100) NOT NULL,
  `nit` int(11) NOT NULL,
  `tercero` varchar(100) NOT NULL,
  `concepto` varchar(100) NOT NULL,
  `banco` varchar(100) NOT NULL,
  `tipo_cuenta` varchar(100) NOT NULL,
  `numero_cuenta` int(11) NOT NULL,
  `valor` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_cp_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cp`
--

LOCK TABLES `cp` WRITE;
/*!40000 ALTER TABLE `cp` DISABLE KEYS */;
INSERT INTO `cp` VALUES (1,'text.txt','2024-06-04','Bogota',808080800,'testEmpresa','TestConcepto','TestBanco','Ahorros',123456789,1234567890),(3,'text.txt','2024-06-04','Bogota',808080800,'testEmpresa','TestConcepto','TestBanco','Ahorros',123456789,1234567890),(12,'C:\\fakepath\\to do.txt','2024-06-05','Bogotá',545455965,'torcoroma Arias','pago','Banco de Bogota','Ahorros',455588,13055893),(13,'','2024-06-06','Bogotá',789456123,'Alianz','Creado desde el front','Banco de Bogota','Corriente',123366538,103669876),(14,'C:\\fakepath\\tareasFront.txt','2024-06-06','Bogotá',545454545,'Testprimero','454545454','Banco de Bogota','Ahorros',2147483647,2147483647),(15,'C:\\fakepath\\tareasFront.txt','2024-06-06','Bogotá',545454545,'Testprimero','454545454','Banco de Bogota','Ahorros',2147483647,2147483647),(16,'C:\\fakepath\\tareasFront.txt','2024-06-06','Bogotá',545454545,'Testprimero','454545454','Banco de Bogota','Ahorros',2147483647,2147483647),(17,'C:\\fakepath\\Captura.PNG','2024-06-04','Bogotá',456123789,'ultimo','last','Banco de Bogota','Ahorros',12336547,1033767374),(18,'','2024-05-20','Bogotá',456698785,'gsdjhfaskfgsdjhf','dfalsdhfgasdjhfg','Banco de Bogota','Ahorros',456123,1589667),(21,'text.txt','2024-06-07','Bogota',808080800,'testEmpresa','TestConcepto','TestBanco','Ahorros',123456789,1234567890);
/*!40000 ALTER TABLE `cp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-07 16:18:34
