-- MySQL dump 10.13  Distrib 5.6.33, for Win64 (x86_64)
--
-- Host: 118.184.28.187    Database: ipodb
-- ------------------------------------------------------
-- Server version	5.1.73

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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_code` varchar(11) NOT NULL,
  `record_code` varchar(255) DEFAULT NULL,
  `product_name` varchar(255) NOT NULL,
  `shortname` varchar(255) DEFAULT NULL,
  `bank_account` varchar(255) NOT NULL,
  `ration_name` varchar(255) DEFAULT NULL COMMENT '配售对象名称',
  `sz_account` varchar(255) DEFAULT NULL,
  `sh_account` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'80088602','SH2834','华泰期货-江苏量化招盈3号资产管理计划','江苏招盈3号','','华泰期货有限公司-华泰期货-江苏量化招盈3号资产管理计划','0899104737','B880693632'),(2,'80088241','SJ1419','华泰期货-银华量化绝对收益资产管理计划','银华绝对收益','','华泰期货有限公司-华泰期货-银华量化绝对收益资产管理计划','0899106920','B880749548\r\nB880749548'),(3,'80080601','SE9008','华泰期货-江苏量化招盈2号资产管理计划','江苏量化招盈2号','',NULL,NULL,NULL),(4,'80088243','SH4433','华泰期货万成2号资产管理计划','万成2号','','华泰期货有限公司-华泰期货万成2号资产管理计划',NULL,NULL);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_code` varchar(255) NOT NULL,
  `stock_name` varchar(255) NOT NULL,
  `action` int(11) NOT NULL COMMENT '1：招股；2：材料提交；3：询价；4：网下申购；5：:缴款；',
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `operator` varchar(255) DEFAULT NULL COMMENT '操作者',
  `review` varchar(255) DEFAULT NULL COMMENT '复核者',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (1,'603225.SH','新凤鸣',1,'2017-03-27','2017-03-27','',''),(2,'603225.SH','新凤鸣',2,'2017-03-28','2017-03-28','杨文人',''),(3,'603225.SH','新凤鸣',3,'2017-03-29','2017-03-30','杨文人','杨雁南'),(4,'603225.SH','新凤鸣',4,'2017-04-07','2017-04-07','杨文人','杨雁南'),(5,'603225.SH','新凤鸣',5,'2017-04-11','2017-04-11','杨文人','杨雁南'),(6,'603926.SH','铁流股份',1,'2017-03-27','2017-03-27','',''),(7,'603926.SH','铁流股份',2,'2017-03-28','2017-03-28','杨雁南',''),(8,'603926.SH','铁流股份',3,'2017-03-29','2017-03-30','杨文人','杨雁南'),(9,'603926.SH','铁流股份',4,'2017-04-27','2017-04-27','杨文人',''),(10,'603926.SH','铁流股份',5,'2017-05-02','2017-05-02','杨文人','杨雁南'),(11,'300641.SZ','正丹股份',1,'2017-03-27','2017-03-27','',''),(12,'300641.SZ','正丹股份',2,'2017-03-28','2017-03-28','杨雁南',''),(13,'300641.SZ','正丹股份',3,'2017-03-30','2017-03-30','杨文人','杨雁南'),(14,'300641.SZ','正丹股份',4,'2017-04-06','2017-04-06','杨文人',''),(15,'300641.SZ','正丹股份',5,'2017-04-10','2017-04-10','杨文人','杨雁南'),(16,'603803.SH','瑞斯康达',1,'2017-03-28','2017-02-28','',''),(17,'603803.SH','瑞斯康达',2,'2017-03-29','2017-03-29','高干',''),(18,'603803.SH','瑞斯康达',3,'2017-03-31','2017-03-31','杨文人','杨雁南'),(19,'603803.SH','瑞斯康达',4,'2017-04-07','2017-04-07','杨文人','杨雁南'),(20,'603803.SH','瑞斯康达',5,'2017-04-11','2017-04-11','杨文人','杨雁南'),(21,'603139.SH','康惠制药',1,'2017-03-27','2017-03-27','',''),(22,'603139.SH','康惠制药',2,'2017-03-28','2017-03-28','杨雁南',''),(23,'603139.SH','康惠制药',3,'2017-03-31','2017-04-05','杨文人','杨雁南'),(24,'603139.SH','康惠制药',4,'2017-04-10','2017-04-10','','杨雁南材料无效'),(25,'603139.SH','康惠制药',5,'2017-04-12','2017-04-12','',''),(26,'603081.SH','大丰实业',1,'2017-03-28','2017-03-28','',''),(27,'603081.SH','大丰实业',2,'2017-03-29','2017-03-29','',''),(28,'603081.SH','大丰实业',3,'2017-03-31','2017-04-05','',''),(29,'603081.SH','大丰实业',4,'2017-04-10','2017-04-10','',''),(30,'603081.SH','大丰实业',5,'2017-04-12','2017-04-12','',''),(31,'002865.SZ','钧达股份',1,'2017-04-05','2017-04-05','',''),(32,'002865.SZ','钧达股份',2,'2017-04-06','2017-04-06','高干',''),(33,'002865.SZ','钧达股份',3,'2017-04-07','2017-04-10','杨文人','杨雁南'),(34,'002865.SZ','钧达股份',4,'2017-04-14','2017-04-14','杨文人','杨雁南'),(35,'002865.SZ','钧达股份',5,'2017-04-18','2017-04-18','杨雁南','杨文人'),(36,'603096.SH','新经典',1,'2017-04-06','2017-04-06','',''),(37,'603096.SH','新经典',2,'2017-04-07','2017-04-07','',''),(38,'603096.SH','新经典',3,'2017-04-10','2017-04-10','杨文人','杨雁南'),(39,'603096.SH','新经典',4,'2017-04-14','2017-04-14','杨文人','杨雁南'),(40,'603096.SH','新经典',5,'2017-04-18','2017-04-18','杨雁南','杨文人'),(41,'300514.SZ','友讯达',1,'2017-04-06','2017-04-06','',''),(42,'300514.SZ','友讯达',2,'2017-04-07','2017-04-10','','未盖章材料'),(43,'300514.SZ','友讯达',3,'2017-04-11','2017-04-11','杨文人','杨雁南'),(44,'300514.SZ','友讯达',4,'2017-04-17','2017-04-17','杨文人','杨雁南'),(45,'300514.SZ','友讯达',5,'2017-04-19','2017-04-19','','已到账'),(46,'002866.SZ','传艺科技',1,'2017-04-06','2017-04-06','',''),(47,'002866.SZ','传艺科技',2,'2017-04-07','2017-04-07','',''),(48,'002866.SZ','传艺科技',3,'2017-04-10','2017-04-11','关联方不通过',''),(49,'002866.SZ','传艺科技',4,'2017-04-17','2017-04-17','未参与询价',''),(50,'002866.SZ','传艺科技',5,'2017-04-19','2017-04-19','',''),(51,'603920.SH','世运电路',1,'2017-04-06','2017-04-06','',''),(52,'603920.SH','世运电路',2,'2017-04-07','2017-04-07','',''),(53,'603920.SH','世运电路',3,'2017-04-10','2017-04-10','杨文人','杨雁南'),(54,'603920.SH','世运电路',4,'2017-04-14','2017-04-14','杨文人','杨雁南'),(55,'603920.SH','世运电路',5,'2017-04-18','2017-04-18','杨雁南','杨文人'),(56,'603787.SH','新日股份',1,'2017-04-07','2017-04-07','',''),(57,'603787.SH','新日股份',2,'2017-04-07','2017-04-10','',''),(58,'603787.SH','新日股份',3,'2017-04-11','2017-04-12','杨文人','杨雁南'),(59,'603787.SH','新日股份',4,'2017-04-17','2017-04-17','杨文人','杨雁南'),(60,'603787.SH','新日股份',5,'2017-04-19','2017-04-19','','已到账'),(61,'300646.SZ','侨源气体',1,'2017-04-10','2017-04-10','',''),(62,'300646.SZ','侨源气体',2,'2017-04-10','2017-04-11','唐飘','高干'),(63,'300646.SZ','侨源气体',3,'2017-04-12','2017-04-13','杨文人','杨雁南'),(64,'300646.SZ','侨源气体',4,'2017-04-19','2017-04-19','推迟发行',''),(65,'300646.SZ','侨源气体',5,'2017-04-21','2017-04-21','',''),(66,'002868.SZ','绿康生化',1,'2017-04-10','2017-04-10','',''),(67,'002868.SZ','绿康生化',2,'2017-04-11','2017-04-13','',''),(68,'002868.SZ','绿康生化',3,'2017-04-14','2017-04-17','无效',''),(69,'002868.SZ','绿康生化',4,'2017-04-20','2017-04-20','',''),(70,'002868.SZ','绿康生化',5,'2017-04-22','2017-04-22','',''),(71,'002867.SZ','周大生',1,'2017-04-10','2017-04-10','',''),(72,'002867.SZ','周大生',2,'2017-04-11','2017-04-11','高干',''),(73,'002867.SZ','周大生',3,'2017-04-12','2017-04-13','杨文人','杨雁南'),(74,'002867.SZ','周大生',4,'2017-04-18','2017-04-18','杨文人',''),(75,'002867.SZ','周大生',5,'2017-04-20','2017-04-20','杨雁南',''),(76,'603320.SH','迪贝电气',1,'2017-04-11','2017-04-11','',''),(77,'603320.SH','迪贝电气',2,'2017-04-11','2017-04-12','高干','唐飘'),(78,'603320.SH','迪贝电气',3,'2017-04-13','2017-04-13','杨文人材料无效',''),(79,'603320.SH','迪贝电气',4,'2017-04-19','2017-04-19','',''),(80,'603320.SH','迪贝电气',5,'2017-04-21','2017-04-21','',''),(81,'300647.SZ','超频三',1,'2017-04-12','2017-04-12','',''),(82,'300647.SZ','超频三',2,'2017-04-12','2017-04-13','高干','唐飘'),(83,'300647.SZ','超频三',3,'2017-04-14','2017-04-17','杨文人','杨雁南'),(84,'300647.SZ','超频三',4,'2017-04-20','2017-04-20','杨雁南','杨文人'),(85,'300647.SZ','超频三',5,'2017-04-24','2017-04-24','杨雁南','杨文人'),(86,'603501.SH','韦尔股份',1,'2017-04-12','2017-04-12','',''),(87,'603501.SH','韦尔股份',2,'2017-04-13','2017-04-13','超时',''),(88,'603501.SH','韦尔股份',3,'2017-04-14','2017-04-17','未参与询价',''),(89,'603501.SH','韦尔股份',4,'2017-04-21','2017-04-21','',''),(90,'603501.SH','韦尔股份',5,'2017-04-25','2017-04-25','',''),(91,'603505.SH','金石资源',1,'2017-04-12','2017-04-12','',''),(92,'603505.SH','金石资源',2,'2017-04-13','2017-04-13','高干','唐飘'),(93,'603505.SH','金石资源',3,'2017-04-14','2017-04-17','杨文人','杨雁南'),(94,'603505.SH','金石资源',4,'2017-04-20','2017-04-20','杨雁南','杨文人'),(95,'603505.SH','金石资源',5,'2017-04-24','2017-04-24','杨雁南','杨文人'),(96,'300643.SZ','万通智控',1,'2017-04-13','2017-04-13','',''),(97,'300643.SZ','万通智控',2,'2017-04-14','2017-04-14','高干','唐飘'),(98,'300643.SZ','万通智控',3,'2017-04-17','2017-04-18','杨文人','杨雁南'),(99,'300643.SZ','万通智控',4,'2017-04-21','2017-04-21','杨雁南','杨文人'),(100,'300643.SZ','万通智控',5,'2017-04-25','2017-04-25','杨文人','杨雁南'),(101,'603229.SH','奥翔药业',1,'2017-04-17','2017-04-17','',''),(102,'603229.SH','奥翔药业',2,'2017-04-18','2017-04-19','高干','唐飘'),(103,'603229.SH','奥翔药业',3,'2017-04-20','2017-04-21','杨雁南','杨文人'),(104,'603229.SH','奥翔药业',4,'2017-04-26','2017-04-26','杨文人',''),(105,'603229.SH','奥翔药业',5,'2017-04-28','2017-04-28','杨文人',''),(106,'603728.SH','鸣志电器',1,'2017-04-18','2017-04-18','',''),(107,'603728.SH','鸣志电器',2,'2017-04-18','2017-04-19','未提交',''),(108,'603728.SH','鸣志电器',3,'2017-04-20','2017-04-21','',''),(109,'603728.SH','鸣志电器',4,'2017-04-26','2017-04-26','',''),(110,'603728.SH','鸣志电器',5,'2017-04-28','2017-04-28','',''),(111,'603896.SH','寿仙谷',1,'2017-04-18','2017-04-18','',''),(112,'603896.SH','寿仙谷',2,'2017-04-18','2017-04-19','高干','唐飘'),(113,'603896.SH','寿仙谷',3,'2017-04-20','2017-04-21','杨雁南','杨文人'),(114,'603896.SH','寿仙谷',4,'2017-04-27','2017-04-27','杨文人',''),(115,'603896.SH','寿仙谷',5,'2017-05-02','2017-05-02','杨文人','杨雁南'),(116,'603113.SH','金能科技',1,'2017-04-19','2017-04-19','',''),(117,'603113.SH','金能科技',2,'2017-04-19','2017-04-20','高干','唐飘'),(118,'603113.SH','金能科技',3,'2017-04-24','2017-04-25','杨雁南','杨文人'),(119,'603113.SH','金能科技',4,'2017-04-28','2017-04-28','杨文人',''),(120,'603113.SH','金能科技',5,'2017-05-03','2017-05-03','杨文人',''),(121,'002869.SZ','金溢科技',1,'2017-04-20','2017-04-20','高干','唐飘'),(122,'002869.SZ','金溢科技',2,'2017-04-20','2017-04-21','高干','唐飘'),(123,'002869.SZ','金溢科技',3,'2017-04-24','2017-04-25','杨雁南','杨文人'),(124,'002869.SZ','金溢科技',4,'2017-05-02','2017-05-02','杨文人','杨雁南'),(125,'002869.SZ','金溢科技',5,'2017-05-04','2017-05-04','杨文人',''),(126,'603488.SH','展鹏科技',1,'2017-04-24','2017-04-24','',''),(127,'603488.SH','展鹏科技',2,'2017-04-25','2017-04-26','高干','唐飘'),(128,'603488.SH','展鹏科技',3,'2017-04-27','2017-04-28','杨文人',''),(129,'603488.SH','展鹏科技',4,'2017-05-04','2017-05-04','杨文人',''),(130,'603488.SH','展鹏科技',5,'2017-05-08','2017-05-08','',''),(131,'601952.SH','苏垦农发',1,'2017-04-24','2017-04-24','',''),(132,'601952.SH','苏垦农发',2,'2017-04-25','2017-04-25','高干','唐飘'),(133,'601952.SH','苏垦农发',3,'2017-04-26','2017-04-26','杨文人',''),(134,'601952.SH','苏垦农发',4,'2017-05-03','2017-05-03','杨文人',''),(135,'601952.SH','苏垦农发',5,'2017-05-05','2017-05-05','杨文人',''),(136,'603758.SH','秦安机电',1,'2017-04-25','2017-04-25','',''),(137,'603758.SH','秦安机电',2,'2017-04-25','2017-04-26','唐飘','高干'),(138,'603758.SH','秦安机电',3,'2017-04-27','2017-04-28','杨文人',''),(139,'603758.SH','秦安机电',4,'2017-05-05','2017-05-05','',''),(140,'603758.SH','秦安机电',5,'2017-05-09','2017-05-09','',''),(141,'300652.SZ','雷迪克',1,'2017-04-25','2017-04-25','',''),(142,'300652.SZ','雷迪克',2,'2017-04-25','2017-04-27','高干','唐飘'),(143,'300652.SZ','雷迪克',3,'2017-04-28','2017-05-02','杨文人','材料审核不通过'),(144,'300652.SZ','雷迪克',4,'2017-05-05','2017-05-05','',''),(145,'300652.SZ','雷迪克',5,'2017-05-09','2017-05-09','',''),(146,'002870.SZ','香山股份',1,'2017-04-25','2017-04-25','',''),(147,'002870.SZ','香山股份',2,'2017-04-25','2017-04-26','高干','唐飘'),(148,'002870.SZ','香山股份',3,'2017-04-27','2017-04-28','杨文人',''),(149,'002870.SZ','香山股份',4,'2017-05-04','2017-05-04','杨文人',''),(150,'002870.SZ','香山股份',5,'2017-05-08','2017-05-08','',''),(151,'603269.SH','海鸥股份',1,'2017-04-25','2017-04-25','',''),(152,'603269.SH','海鸥股份',2,'2017-04-25','2017-04-26','高干','唐飘'),(153,'603269.SH','海鸥股份',3,'2017-04-28','2017-05-02','杨文人',''),(154,'603269.SH','海鸥股份',4,'2017-05-05','2017-05-05','杨文人',''),(155,'603269.SH','海鸥股份',5,'2017-05-09','2017-05-09','',''),(156,'603959.SH','永安行',1,'2017-04-27','2017-04-27','',''),(157,'603959.SH','永安行',2,'2017-04-27','2017-04-28','高干','唐飘'),(158,'603959.SH','永安行',3,'2017-05-03','2017-05-03','杨文人',''),(159,'603959.SH','永安行',4,'2017-05-08','2017-05-08','',''),(160,'603959.SH','永安行',5,'2017-05-10','2017-05-10','',''),(161,'300657.SZ','弘信电子',1,'2017-05-02','2017-05-02','',''),(162,'300657.SZ','弘信电子',2,'2017-05-03','2017-05-04','',''),(163,'300657.SZ','弘信电子',3,'2017-05-05','2017-05-08','杨文人',''),(164,'300657.SZ','弘信电子',4,'2017-05-12','2017-05-12','',''),(165,'300657.SZ','弘信电子',5,'2017-05-16','2017-05-16','',''),(166,'603197.SH','保隆科技',1,'2017-05-02','2017-05-02','',''),(167,'603197.SH','保隆科技',2,'2017-05-02','2017-05-03','杨雁南','杨雁南'),(168,'603197.SH','保隆科技',3,'2017-05-04','2017-05-04','杨文人',''),(169,'603197.SH','保隆科技',4,'2017-05-09','2017-05-09','',''),(170,'603197.SH','保隆科技',5,'2017-05-11','2017-05-11','',''),(171,'603383.SH','顶点软件',1,'2017-05-02','2017-05-02','',''),(172,'603383.SH','顶点软件',2,'2017-05-02','2017-05-03','高干','唐飘'),(173,'603383.SH','顶点软件',3,'2017-05-04','2017-05-04','杨文人',''),(174,'603383.SH','顶点软件',4,'2017-05-10','2017-05-10','',''),(175,'603383.SH','顶点软件',5,'2017-05-12','2017-05-12','',''),(176,'603767.SH','中马传动',1,'2017-05-02','2017-05-02','',''),(177,'603767.SH','中马传动',2,'2017-05-02','2017-05-03','高干','唐飘'),(178,'603767.SH','中马传动',3,'2017-05-04','2017-05-05','杨文人',''),(179,'603767.SH','中马传动',4,'2017-05-11','2017-05-11','',''),(180,'603767.SH','中马传动',5,'2017-05-15','2017-05-15','',''),(181,'002872.SZ','天圣制药',1,'2017-05-02','2017-05-02','',''),(182,'002872.SZ','天圣制药',2,'2017-05-02','2017-05-03','杨雁南','杨雁南'),(183,'002872.SZ','天圣制药',3,'2017-05-04','2017-05-04','杨文人',''),(184,'002872.SZ','天圣制药',4,'2017-05-10','2017-05-10','',''),(185,'002872.SZ','天圣制药',5,'2017-05-12','2017-05-12','',''),(186,'603680.SH','今创集团',1,'2017-05-02','2017-05-02','',''),(187,'603680.SH','今创集团',2,'2017-05-02','2017-05-02','',''),(188,'603680.SH','今创集团',3,'2017-05-04','2017-05-05','杨文人',''),(189,'603680.SH','今创集团',4,'2017-05-10','2017-05-10','',''),(190,'603680.SH','今创集团',5,'2017-05-12','2017-05-12','',''),(191,'603855.SH','华荣股份',1,'2017-05-03','2017-05-03','',''),(192,'603855.SH','华荣股份',2,'2017-05-03','2017-05-04','高干','唐飘'),(193,'603855.SH','华荣股份',3,'2017-05-05','2017-05-08','杨文人',''),(194,'603855.SH','华荣股份',4,'2017-05-12','2017-05-12','',''),(195,'603855.SH','华荣股份',5,'2017-05-16','2017-05-16','',''),(196,'300655.SZ','晶瑞股份',1,'2017-05-03','2017-05-03','',''),(197,'300655.SZ','晶瑞股份',2,'2017-05-03','2017-05-04','材料不通过',''),(198,'300655.SZ','晶瑞股份',3,'2017-05-05','2017-05-05','不参与询价',''),(199,'300655.SZ','晶瑞股份',4,'2017-05-11','2017-05-11','',''),(200,'300655.SZ','晶瑞股份',5,'2017-05-15','2017-05-15','','');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_code` varchar(255) NOT NULL,
  `stock_name` varchar(255) NOT NULL,
  `type` int(255) NOT NULL COMMENT '1:沪市，2:深市',
  `underwriter` varchar(255) NOT NULL COMMENT '承销商',
  `shortname` varchar(255) DEFAULT NULL,
  `telephone` varchar(255) DEFAULT NULL,
  `state` int(11) DEFAULT NULL COMMENT '0：已结束，包含未参与；1：正在进行',
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES (1,'603225.SH','新凤鸣',1,'申万宏源证券承销保荐有限责任公司','申万宏源','021-54034208',0,'已上市，并已确认份额'),(2,'603926.SH','铁流股份',1,'安信证券股份有限公司','安信证券','010-83321320，021-35082095',1,''),(3,'300641.SZ','正丹股份',2,'中国国际金融股份有限公司','中金公司','010-65353014',0,'已上市，并已确认份额'),(4,'603803.SH','瑞斯康达',1,'招商证券股份有限公司','招商证券','0755-25318606、0755-83168414',0,'已上市，并已确认份额'),(5,'603139.SH','康惠制药',1,'国金证券股份有限公司','国金证券','021-68826806、201-68826809',0,'材料无效'),(6,'603081.SH','大丰实业',1,'国泰君安证券股份有限公司','国泰君安证券','021-38676888',0,'没参与'),(7,'002865.SZ','钧达股份',2,'中国银河证券股份有限公司','银河证券','010-66568351、66568353',0,'已上市，并已确认份额'),(8,'603096.SH','新经典',1,'东方花旗证券有限公司','东方花旗证券','021-23153663、021-23153802',0,'已上市，并已确认份额'),(9,'300514.SZ','友讯达',2,'招商证券股份有限公司','招商证券','0755 -82943009 、0755 -82943078',0,'已上市，并已确认份额'),(10,'002866.SZ','传艺科技',2,'东吴证券股份有限公司','东吴证券','0512-62936311',0,'关联方不通过'),(11,'603920.SH','世运电路',1,'金元证券股份有限公司','金元证券','010-83958868',1,''),(12,'603787.SH','新日股份',1,'海通证券股份有限公司','海通证券','021-23219622、021-23219496',1,''),(13,'300646.SZ','侨源气体',2,'申万宏源证券承销保荐有限责任公司','申万宏源','010-88085885',1,''),(14,'002868.SZ','绿康生化',2,'兴业证券股份有限公司','兴业证券','021 -20370807 ',0,'材料无效'),(15,'002867.SZ','周大生',2,'广发证券股份有限公司','广发证券','020 －87555297 ',0,'已上市，并已确认份额'),(16,'603320.SH','迪贝电气',1,'东方花旗证券有限公司','东方花旗证券','021-23153863、021-23153791',0,'材料无效'),(17,'300647.SZ','超频三',2,'广发证券股份有限公司','广发证券','020－87555297、87557727',1,''),(18,'603501.SH','韦尔股份',1,'国信证券股份有限公司','国信证券','0755-22940052；0755-22940062',0,'材料无效'),(19,'603505.SH','金石资源',1,'中信证券股份有限公司','中信证券','010 -60837385',1,''),(20,'300643.SZ','万通智控',2,'海通证券股份有限公司','海通证券','021-23219622',1,''),(21,'603229.SH','奥翔药业',1,'国金证券股份有限公司','国金证券','021-68826099、 021-68826007',1,''),(22,'603728.SH','鸣志电器',1,'安信证券','安信证券','',0,'未参与'),(23,'603896.SH','寿仙谷',1,'国信证券股份有限公司','国信证券','',1,''),(24,'603113.SH','金能科技',1,'国泰君安','国泰君安','',1,''),(25,'002869.SZ','金溢科技',2,'国信证券','国信','',1,''),(26,'603488.SH','展鹏科技',1,'兴业证券股份有限公司','兴业证券','021-38565546',1,''),(27,'601952.SH','苏垦农发',1,'国信证券股份有限公司','国信证券','0755-22940052',1,''),(28,'603758.SH','秦安机电',1,'长城证券股份有限公司','长城证券','0755-83516151、0755-23934042',1,''),(29,'300652.SZ','雷迪克',1,'国金证券股份有限公司','国金证券','021-68826023、021-68826825',1,''),(30,'002870.SZ','香山股份',2,'安信证券股份有限公司','安信证券','010-83321320、010-83321321',1,''),(31,'603269.SH','海鸥股份',1,'民生证券股份有限公司','民生证券','010-85120190',1,''),(32,'603959.SH','永安行',1,'中国际金融股份有限公司','中金公司','010-65353014',1,''),(33,'300657.SZ','弘信电子',2,'兴业证券股份有限公司 ','兴业证券','021 -20370806',1,''),(34,'603197.SH','保隆科技',1,'第一创业摩根大通证券有限责任公司','摩根大通','010-63212503',1,''),(35,'603383.SH','顶点软件',1,'东方花旗证券有限公司','东方花旗','021-23153864、021-23153824',1,''),(36,'603767.SH','中马传动',1,'九州证券股份有限公司','九州证券','010-57672159',1,''),(37,'002872.SZ','天圣制药',1,'华西证券股份有限公司','华西证券','010-68566685、010-68566670',1,''),(38,'603680.SH','今创集团',1,'中信建投证券股份有限公司','中信建投','010-65608301、010-85159266',1,''),(39,'603855.SH','华荣股份',1,'国金证券股份有限公司','国金证券','021-68826809 ',1,''),(40,'300655.SZ','晶瑞股份',1,'招商证券股份有限公司','招商证券','0755 -25310420',1,'');
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_product`
--

DROP TABLE IF EXISTS `stock_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_code` varchar(255) NOT NULL,
  `stock_name` varchar(255) DEFAULT NULL,
  `product_code` varchar(11) NOT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_product`
--

LOCK TABLES `stock_product` WRITE;
/*!40000 ALTER TABLE `stock_product` DISABLE KEYS */;
INSERT INTO `stock_product` VALUES (1,'603225.SH','新凤鸣','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(3,'603926.SH','铁流股份','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(4,'603926.SH','铁流股份','80088241','华泰期货-银华量化绝对收益资产管理计划'),(5,'603926.SH','铁流股份','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(6,'300641.SZ','正丹股份','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(7,'300641.SZ','正丹股份','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(8,'300641.SZ','正丹股份','80088241','华泰期货-银华量化绝对收益资产管理计划'),(9,'603803.SH','瑞斯康达','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(11,'603803.SH','瑞斯康达','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(12,'603139.SH','康惠制药','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(13,'603139.SH','康惠制药','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(14,'002865.SZ','钧达股份','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(15,'002865.SZ','钧达股份','80088241','华泰期货-银华量化绝对收益资产管理计划'),(16,'002865.SZ','钧达股份','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(17,'300646.SZ','侨源气体','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(18,'300646.SZ','侨源气体','80088241','华泰期货-银华量化绝对收益资产管理计划'),(19,'300646.SZ','侨源气体','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(20,'002867.SZ','周大生','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(21,'002867.SZ','周大生','80088241','华泰期货-银华量化绝对收益资产管理计划'),(22,'002867.SZ','周大生','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(23,'603320.SH','迪贝电气','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(24,'603320.SH','迪贝电气','80088241','华泰期货-银华量化绝对收益资产管理计划'),(25,'603320.SH','迪贝电气','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(26,'300647.SZ','超频三','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(27,'300647.SZ','超频三','80088241','华泰期货-银华量化绝对收益资产管理计划'),(28,'300647.SZ','超频三','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(29,'603505.SH','金石资源','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(30,'603505.SH','金石资源','80088241','华泰期货-银华量化绝对收益资产管理计划'),(31,'603505.SH','金石资源','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(32,'300643.SZ','万通智控','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(33,'300643.SZ','万通智控','80088241','华泰期货-银华量化绝对收益资产管理计划'),(34,'300643.SZ','万通智控','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(35,'603229.SH','奥翔药业','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(36,'603229.SH','奥翔药业','80088241','华泰期货-银华量化绝对收益资产管理计划'),(37,'603229.SH','奥翔药业','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(38,'603896.SH','寿仙谷','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(39,'603896.SH','寿仙谷','80088241','华泰期货-银华量化绝对收益资产管理计划'),(40,'603896.SH','寿仙谷','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(41,'603113.SH','金能科技','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(42,'603113.SH','金能科技','80088241','华泰期货-银华量化绝对收益资产管理计划'),(43,'603113.SH','金能科技','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(44,'002869.SZ','金溢科技','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(45,'002869.SZ','金溢科技','80088241','华泰期货-银华量化绝对收益资产管理计划'),(46,'002869.SZ','金溢科技','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(47,'601952.SH','苏垦农发','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(48,'601952.SH','苏垦农发','80088241','华泰期货-银华量化绝对收益资产管理计划'),(49,'601952.SH','苏垦农发','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(50,'300652.SZ','雷迪克','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(51,'300652.SZ','雷迪克','80088241','华泰期货-银华量化绝对收益资产管理计划'),(52,'300652.SZ','雷迪克','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(53,'603269.SH','海鸥股份','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(54,'603269.SH','海鸥股份','80088241','华泰期货-银华量化绝对收益资产管理计划'),(55,'603269.SH','海鸥股份','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(56,'603758.SH','秦安机电','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(57,'603758.SH','秦安机电','80088241','华泰期货-银华量化绝对收益资产管理计划'),(58,'603758.SH','秦安机电','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(59,'002870.SZ','香山股份','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(60,'002870.SZ','香山股份','80088241','华泰期货-银华量化绝对收益资产管理计划'),(61,'002870.SZ','香山股份','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(62,'603488.SH','展鹏科技','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(63,'603488.SH','展鹏科技','80088241','华泰期货-银华量化绝对收益资产管理计划'),(64,'603488.SH','展鹏科技','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(65,'603959.SH','永安行','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(66,'603959.SH','永安行','80088241','华泰期货-银华量化绝对收益资产管理计划'),(67,'603959.SH','永安行','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(68,'603767.SH','中马传动','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(69,'603767.SH','中马传动','80088241','华泰期货-银华量化绝对收益资产管理计划'),(70,'603767.SH','中马传动','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(71,'603383.SH','顶点软件','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(72,'603383.SH','顶点软件','80088241','华泰期货-银华量化绝对收益资产管理计划'),(73,'603383.SH','顶点软件','80088602','华泰期货-江苏量化招盈3号资产管理计划'),(74,'603855.SH','华荣股份','80080601','华泰期货-江苏量化招盈2号资产管理计划'),(75,'603855.SH','华荣股份','80088241','华泰期货-银华量化绝对收益资产管理计划'),(76,'603855.SH','华荣股份','80088602','华泰期货-江苏量化招盈3号资产管理计划');
/*!40000 ALTER TABLE `stock_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-07  0:58:03