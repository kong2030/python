/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : sky

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-01-03 16:01:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add user info', '7', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('20', 'Can change user info', '7', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete user info', '7', 'delete_userinfo');
INSERT INTO `auth_permission` VALUES ('22', 'Can add module', '8', 'add_module');
INSERT INTO `auth_permission` VALUES ('23', 'Can change module', '8', 'change_module');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete module', '8', 'delete_module');
INSERT INTO `auth_permission` VALUES ('25', 'Can add app system', '9', 'add_appsystem');
INSERT INTO `auth_permission` VALUES ('26', 'Can change app system', '9', 'change_appsystem');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete app system', '9', 'delete_appsystem');
INSERT INTO `auth_permission` VALUES ('28', 'Can add environment', '10', 'add_environment');
INSERT INTO `auth_permission` VALUES ('29', 'Can change environment', '10', 'change_environment');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete environment', '10', 'delete_environment');
INSERT INTO `auth_permission` VALUES ('31', 'Can add host', '11', 'add_host');
INSERT INTO `auth_permission` VALUES ('32', 'Can change host', '11', 'change_host');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete host', '11', 'delete_host');
INSERT INTO `auth_permission` VALUES ('34', 'Can add order', '12', 'add_order');
INSERT INTO `auth_permission` VALUES ('35', 'Can change order', '12', 'change_order');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete order', '12', 'delete_order');
INSERT INTO `auth_permission` VALUES ('37', 'Can add order host', '13', 'add_orderhost');
INSERT INTO `auth_permission` VALUES ('38', 'Can change order host', '13', 'change_orderhost');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete order host', '13', 'delete_orderhost');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$QgVAri4gnKKe$BdejV6ZAevS3HAk/UtVJEN9Qoc90iSwXRDXkWL90gsw=', '2019-01-02 13:36:13.916000', '1', 'admin', '', '', 'yangwenren@message.guosen.com.cn', '1', '1', '2018-12-29 03:18:05.734761');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for cmdb_appsystem
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_appsystem`;
CREATE TABLE `cmdb_appsystem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `chinese_name` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_appsystem_app_name_a1425c8a_uniq` (`app_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of cmdb_appsystem
-- ----------------------------
INSERT INTO `cmdb_appsystem` VALUES ('1', 'QQ', '个股期权系统');
INSERT INTO `cmdb_appsystem` VALUES ('2', 'SMEN', '内存交易系统');
INSERT INTO `cmdb_appsystem` VALUES ('3', 'OTC', '场外柜台系统');

-- ----------------------------
-- Table structure for cmdb_environment
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_environment`;
CREATE TABLE `cmdb_environment` (
  `env_id` int(11) NOT NULL,
  `env_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `english_name` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `position` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `network` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`env_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of cmdb_environment
-- ----------------------------
INSERT INTO `cmdb_environment` VALUES ('1', '测试环境', null, null, null);
INSERT INTO `cmdb_environment` VALUES ('2', '预发环境', 'yfb', '东莞机房', '10.33.*.*,');
INSERT INTO `cmdb_environment` VALUES ('3', '生产环境', 'prd', '东莞机房', '10.33.*.*,');
INSERT INTO `cmdb_environment` VALUES ('4', '同城灾备', null, '深圳滨海', '192.168.*.*,');
INSERT INTO `cmdb_environment` VALUES ('5', '异地灾备', null, '上海宁桥', null);

-- ----------------------------
-- Table structure for cmdb_host
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_host`;
CREATE TABLE `cmdb_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host_name` varchar(20) COLLATE utf8_bin NOT NULL,
  `ip` varchar(20) COLLATE utf8_bin NOT NULL,
  `host_user` varchar(20) COLLATE utf8_bin NOT NULL,
  `password` varchar(50) COLLATE utf8_bin NOT NULL,
  `environment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_host_host_name_4ef18b66_uniq` (`host_name`),
  UNIQUE KEY `cmdb_host_ip_24107b95_uniq` (`ip`),
  KEY `cmdb_host_environment_id_4f8904ca_fk_cmdb_environment_env_id` (`environment_id`),
  CONSTRAINT `cmdb_host_environment_id_4f8904ca_fk_cmdb_environment_env_id` FOREIGN KEY (`environment_id`) REFERENCES `cmdb_environment` (`env_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of cmdb_host
-- ----------------------------
INSERT INTO `cmdb_host` VALUES ('1', 'DYQQ-DBPU152', '10.35.144.152', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2');
INSERT INTO `cmdb_host` VALUES ('2', 'DYQQ-DBPU142', '10.35.144.142', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2');
INSERT INTO `cmdb_host` VALUES ('3', 'DYQQ-WEB153', '10.35.144.153', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2');
INSERT INTO `cmdb_host` VALUES ('4', 'DYQQ-WEB154', '10.35.144.154', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2');
INSERT INTO `cmdb_host` VALUES ('5', 'ywr-kxbp01', '172.24.180.223', 'dgadmin', 'QDVyMjAxODEwMnd5', '1');

-- ----------------------------
-- Table structure for cmdb_host_module
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_host_module`;
CREATE TABLE `cmdb_host_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host_id` int(11) NOT NULL,
  `module_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_host_module_host_id_module_id_92caa760_uniq` (`host_id`,`module_id`),
  KEY `cmdb_host_module_module_id_7fc499fd_fk_cmdb_module_id` (`module_id`),
  CONSTRAINT `cmdb_host_module_host_id_dde09052_fk_cmdb_host_id` FOREIGN KEY (`host_id`) REFERENCES `cmdb_host` (`id`),
  CONSTRAINT `cmdb_host_module_module_id_7fc499fd_fk_cmdb_module_id` FOREIGN KEY (`module_id`) REFERENCES `cmdb_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of cmdb_host_module
-- ----------------------------
INSERT INTO `cmdb_host_module` VALUES ('1', '1', '1');
INSERT INTO `cmdb_host_module` VALUES ('2', '2', '1');
INSERT INTO `cmdb_host_module` VALUES ('3', '3', '2');
INSERT INTO `cmdb_host_module` VALUES ('4', '4', '2');
INSERT INTO `cmdb_host_module` VALUES ('5', '5', '3');

-- ----------------------------
-- Table structure for cmdb_module
-- ----------------------------
DROP TABLE IF EXISTS `cmdb_module`;
CREATE TABLE `cmdb_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `chinese_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `program_path` varchar(128) COLLATE utf8_bin NOT NULL,
  `script_path` varchar(128) COLLATE utf8_bin NOT NULL,
  `app_system_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cmdb_module_module_name_1a813686_uniq` (`module_name`),
  KEY `cmdb_module_app_system_id_9d7badb5_fk_cmdb_appsystem_id` (`app_system_id`),
  CONSTRAINT `cmdb_module_app_system_id_9d7badb5_fk_cmdb_appsystem_id` FOREIGN KEY (`app_system_id`) REFERENCES `cmdb_appsystem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of cmdb_module
-- ----------------------------
INSERT INTO `cmdb_module` VALUES ('1', 'QQ-DBPU', '个股期权-磁盘bpu', 'd$\\maServer', 'd$\\tools\\scripts\\deploy\\maServer', '1');
INSERT INTO `cmdb_module` VALUES ('2', 'QQ-WEB', '个股期权-web', 'd$\\kweb', 'd$\\tools\\scripts\\deploy\\kweb', '1');
INSERT INTO `cmdb_module` VALUES ('3', 'QQ-KCBP-JY', '个股期权-kcbp-jy', 'd$\\kcbp', 'd$\\tools\\scripts\\deploy\\kcbp', '1');

-- ----------------------------
-- Table structure for config_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `config_userinfo`;
CREATE TABLE `config_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_code` varchar(5) COLLATE utf8_bin DEFAULT NULL,
  `chinese_name` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `telephone` varchar(16) COLLATE utf8_bin DEFAULT NULL,
  `mobilephone` varchar(11) COLLATE utf8_bin DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `config_userinfo_user_id_345d9d4b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of config_userinfo
-- ----------------------------

-- ----------------------------
-- Table structure for deploy_order
-- ----------------------------
DROP TABLE IF EXISTS `deploy_order`;
CREATE TABLE `deploy_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_code` varchar(16) COLLATE utf8_bin NOT NULL,
  `type` int(11) NOT NULL,
  `deploy_args` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `env_1` int(11) NOT NULL,
  `env_2` int(11) NOT NULL,
  `env_3` int(11) NOT NULL,
  `env_4` int(11) NOT NULL,
  `env_5` int(11) NOT NULL,
  `app_system_id` int(11) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `module_id` int(11) NOT NULL,
  `current_env` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_code` (`order_code`),
  KEY `deploy_order_app_system_id_ccb8879c_fk_cmdb_appsystem_id` (`app_system_id`),
  KEY `deploy_order_creator_id_37094486_fk_auth_user_id` (`creator_id`),
  KEY `deploy_order_module_id_0d6e3b5b_fk_cmdb_module_id` (`module_id`),
  CONSTRAINT `deploy_order_app_system_id_ccb8879c_fk_cmdb_appsystem_id` FOREIGN KEY (`app_system_id`) REFERENCES `cmdb_appsystem` (`id`),
  CONSTRAINT `deploy_order_creator_id_37094486_fk_auth_user_id` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `deploy_order_module_id_0d6e3b5b_fk_cmdb_module_id` FOREIGN KEY (`module_id`) REFERENCES `cmdb_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of deploy_order
-- ----------------------------
INSERT INTO `deploy_order` VALUES ('1', '20181231132639KY', '1', '/Users/yangwenren/Desktop/install/upload/20181231132639KY.zip', '2018-12-31 13:26:39.000000', '2019-01-01 14:46:08.000000', '0', '0', '1', '0', '0', '1', '1', '1', '3');
INSERT INTO `deploy_order` VALUES ('2', '20181231132720RN', '1', '/Users/yangwenren/Desktop/install/upload/20181231132720RN.zip', '2018-12-31 13:27:20.000000', '2019-01-01 13:09:33.327699', '0', '0', '0', '1', '0', '1', '1', '2', '4');
INSERT INTO `deploy_order` VALUES ('3', '20190101131713KG', '1', '/Users/yangwenren/Desktop/install/upload/20190101131713KG.zip', '2019-01-01 13:17:13.399000', '2019-01-01 13:17:13.399000', '0', '0', '0', '0', '0', '1', '1', '3', '0');
INSERT INTO `deploy_order` VALUES ('4', '20190101132509ET', '1', '/Users/yangwenren/Desktop/install/upload/20190101132509ET.zip', '2019-01-01 13:25:09.140376', '2019-01-02 13:07:28.990000', '0', '2', '0', '0', '0', '1', '1', '1', '2');
INSERT INTO `deploy_order` VALUES ('5', '20190101132524BB', '1', '/Users/yangwenren/Desktop/install/upload/20190101132524BB.zip', '2019-01-01 13:25:24.507935', '2019-01-02 21:20:10.718000', '0', '1', '0', '0', '0', '1', '1', '1', '2');
INSERT INTO `deploy_order` VALUES ('6', '20190101132543KQ', '1', '/Users/yangwenren/Desktop/install/upload/20190101132543KQ.zip', '2019-01-01 13:25:43.745305', '2019-01-01 13:25:43.745305', '0', '0', '0', '0', '0', '1', '1', '3', '0');
INSERT INTO `deploy_order` VALUES ('7', '20190101132606BO', '1', '/Users/yangwenren/Desktop/install/upload/20190101132606BO.zip', '2019-01-01 13:26:06.323815', '2019-01-01 13:26:06.323815', '0', '0', '0', '0', '0', '1', '1', '2', '0');
INSERT INTO `deploy_order` VALUES ('8', '20190102144558ES', '1', 'D:\\backup\\deploy\\20190102144558ES.zip', '2019-01-02 14:46:01.738000', '2019-01-02 14:46:01.738000', '0', '0', '0', '0', '0', '1', '1', '3', '0');

-- ----------------------------
-- Table structure for deploy_order_host
-- ----------------------------
DROP TABLE IF EXISTS `deploy_order_host`;
CREATE TABLE `deploy_order_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_code` varchar(16) NOT NULL,
  `host_ip` varchar(20) NOT NULL,
  `deploy_status` int(11) NOT NULL,
  `deploy_time` datetime(6) NOT NULL,
  `module_name` varchar(50) NOT NULL,
  `deploy_log` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of deploy_order_host
-- ----------------------------
INSERT INTO `deploy_order_host` VALUES ('3', '20190101132509ET', '10.35.144.142', '1', '2019-01-03 15:12:18.395000', 'QQ-DBPU', 'deploy success');
INSERT INTO `deploy_order_host` VALUES ('4', '20190101132509ET', '10.35.144.152', '1', '2019-01-03 15:12:18.399000', 'QQ-DBPU', 'deploy success');
INSERT INTO `deploy_order_host` VALUES ('5', '20190101132509ET', '10.35.144.152', '0', '2019-01-03 15:55:08.866000', 'QQ-DBPU', 'deploy success');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-12-29 03:18:57.914139', 0x31, '个股期权系统', '1', 0x5B7B226164646564223A207B7D7D5D, '9', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-12-29 03:19:44.366399', 0x31, '测试环境', '1', 0x5B7B226164646564223A207B7D7D5D, '10', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-12-29 03:19:59.013150', 0x32, '预发布环境', '1', 0x5B7B226164646564223A207B7D7D5D, '10', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-12-29 03:20:16.869563', 0x33, '生产环境', '1', 0x5B7B226164646564223A207B7D7D5D, '10', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-12-29 03:20:30.918200', 0x34, '同城灾备', '1', 0x5B7B226164646564223A207B7D7D5D, '10', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2018-12-29 03:20:43.823001', 0x35, '异地灾备', '1', 0x5B7B226164646564223A207B7D7D5D, '10', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-12-29 03:21:03.591052', 0x31, 'QQ-DBPU', '1', 0x5B7B226164646564223A207B7D7D5D, '8', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-12-29 08:05:08.259402', 0x31, '10.35.144.152', '1', 0x5B7B226164646564223A207B7D7D5D, '11', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-12-29 10:45:37.321700', 0x32, '10.35.144.142', '1', 0x5B7B226164646564223A207B7D7D5D, '11', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-12-29 12:51:51.880965', 0x32, '内存交易系统', '1', 0x5B7B226164646564223A207B7D7D5D, '9', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-12-29 12:52:23.684337', 0x33, '场外柜台系统', '1', 0x5B7B226164646564223A207B7D7D5D, '9', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-12-29 12:52:46.296452', 0x31, '个股期权系统', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B226170705F6E616D65225D7D7D5D, '9', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-12-30 01:46:57.265800', 0x33, '10.35.144.153', '1', 0x5B7B226164646564223A207B7D7D5D, '11', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-12-30 01:47:19.543662', 0x34, '10.35.144.154', '1', 0x5B7B226164646564223A207B7D7D5D, '11', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-01-01 07:45:22.234924', 0x31, 'Order object', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B2263757272656E745F656E76225D7D7D5D, '12', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-01-01 07:48:22.095525', 0x31, 'Order object', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B2263757272656E745F656E76225D7D7D5D, '12', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2019-01-01 11:04:21.245557', 0x32, 'Order object', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B2263757272656E745F656E76225D7D7D5D, '12', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2019-01-01 14:46:49.125557', 0x31, 'Order object', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B22656E765F33225D7D7D5D, '12', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2019-01-02 05:14:44.930000', 0x32, '预发环境', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B22656E765F6E616D65225D7D7D5D, '10', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2019-01-02 05:40:45.203000', 0x35, '172.24.180.223', '1', 0x5B7B226164646564223A207B7D7D5D, '11', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2019-01-03 07:50:13.808000', 0x31, 'Order object', '2', 0x5B7B226368616E676564223A207B226669656C6473223A205B22656E765F33225D7D7D5D, '12', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('9', 'cmdb', 'appsystem');
INSERT INTO `django_content_type` VALUES ('10', 'cmdb', 'environment');
INSERT INTO `django_content_type` VALUES ('11', 'cmdb', 'host');
INSERT INTO `django_content_type` VALUES ('8', 'cmdb', 'module');
INSERT INTO `django_content_type` VALUES ('7', 'config', 'userinfo');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('12', 'deploy', 'order');
INSERT INTO `django_content_type` VALUES ('13', 'deploy', 'orderhost');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-29 03:17:09.473545');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-12-29 03:17:09.869761');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-12-29 03:17:09.946636');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-12-29 03:17:09.987823');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-12-29 03:17:10.057752');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-12-29 03:17:10.091466');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-12-29 03:17:10.129563');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-12-29 03:17:10.142528');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-12-29 03:17:10.183124');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-12-29 03:17:10.186325');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-12-29 03:17:10.201573');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2018-12-29 03:17:10.242435');
INSERT INTO `django_migrations` VALUES ('13', 'cmdb', '0001_initial', '2018-12-29 03:17:10.487648');
INSERT INTO `django_migrations` VALUES ('14', 'config', '0001_initial', '2018-12-29 03:17:10.568720');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2018-12-29 03:17:10.614370');
INSERT INTO `django_migrations` VALUES ('16', 'cmdb', '0002_auto_20181229_1324', '2018-12-29 13:24:35.282475');
INSERT INTO `django_migrations` VALUES ('17', 'deploy', '0001_initial', '2018-12-30 05:32:40.489246');
INSERT INTO `django_migrations` VALUES ('18', 'deploy', '0002_auto_20181230_0746', '2018-12-30 07:46:58.532421');
INSERT INTO `django_migrations` VALUES ('19', 'deploy', '0002_auto_20181231_1304', '2018-12-31 13:04:37.285384');
INSERT INTO `django_migrations` VALUES ('20', 'deploy', '0003_auto_20181231_1307', '2018-12-31 13:08:25.964902');
INSERT INTO `django_migrations` VALUES ('21', 'deploy', '0004_auto_20181231_1307', '2018-12-31 13:08:25.969065');
INSERT INTO `django_migrations` VALUES ('22', 'deploy', '0002_order', '2018-12-31 13:12:17.582715');
INSERT INTO `django_migrations` VALUES ('23', 'deploy', '0003_order_current_env', '2019-01-01 05:39:45.723375');
INSERT INTO `django_migrations` VALUES ('24', 'deploy', '0004_orderhost', '2019-01-03 02:57:02.069000');
INSERT INTO `django_migrations` VALUES ('25', 'deploy', '0005_auto_20190103_1105', '2019-01-03 03:06:23.896000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('2gryt2ike4t3zzoxv819sd5bistj07uc', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-12 04:01:11.333932');
INSERT INTO `django_session` VALUES ('4xgcnmvgv4qc57ew8m0wb9yjusnbfvco', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-13 13:23:44.194185');
INSERT INTO `django_session` VALUES ('7hvzh3ajcigwmuc9on3paowuigwrmoxi', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-13 13:12:42.668012');
INSERT INTO `django_session` VALUES ('8f1yvfccdbtzdw2nzfhg475yhrtwzztd', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-12 13:12:39.555317');
INSERT INTO `django_session` VALUES ('9b9bgihctm81u81qjxeyfdn7gahhzzvz', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-13 11:57:17.697524');
INSERT INTO `django_session` VALUES ('banjipovss0frcgxuur76xo8zhrhpwke', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-12 08:01:43.253075');
INSERT INTO `django_session` VALUES ('bmt6bvqmcfeqp4z1iavjut1bwmcuyou4', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-13 11:16:30.019345');
INSERT INTO `django_session` VALUES ('cwk5l38mk8kflcgqo4jzheq46x8fkyr3', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-16 13:36:13.921000');
INSERT INTO `django_session` VALUES ('hb1m8wxhew3wpk87ga2403bk8wxvuqt8', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-16 06:17:13.701000');
INSERT INTO `django_session` VALUES ('ic5vuqtym7hmbtj84psjh8y2r9ensykt', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-14 13:26:06.125746');
INSERT INTO `django_session` VALUES ('l8kyxoruf6sp4ezd6jga43hilub7cpsk', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-15 06:12:11.672931');
INSERT INTO `django_session` VALUES ('pzzjojqx0pi5bn1epi4warry0zezv8js', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-13 11:06:30.104409');
INSERT INTO `django_session` VALUES ('r4tgw7dbv4l0vz6vpjxl6njttavaykr0', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-15 06:12:53.072373');
INSERT INTO `django_session` VALUES ('tbfacbftt17zr98mjwaz1b9ofriq30rb', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-15 13:27:48.356028');
INSERT INTO `django_session` VALUES ('tebnl635c2gwzej31q9nwjcze5z5zoum', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-13 13:06:40.802065');
INSERT INTO `django_session` VALUES ('vehuputafs60wtyqrecj8h2rt0hs4p6x', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-12 04:02:55.447639');
INSERT INTO `django_session` VALUES ('z30s9t1si6esv91r236qx96rghsi6v9f', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-15 14:45:27.030498');
INSERT INTO `django_session` VALUES ('zjr5mrbwj3if1by9kq5ixgzorr8fk52r', 0x59324E6C4D57517A59324A6A4E444D3059324D314D574E69597A5A695A44566D4E475135596A4A694E544A694D6A51334F474E6C596A7037496C39686458526F5833567A5A584A666147467A61434936496A59315932466D596D5A695A54646C5A4449784F445578595459344E5441354D6D45324E54566C4E574D304E44466D4F4751355A5445694C434A6659585630614639316332567958324A685932746C626D51694F694A6B616D46755A3238755932397564484A70596935686458526F4C6D4A685932746C626D527A4C6B31765A475673516D466A613256755A434973496C39686458526F5833567A5A584A66615751694F694978496E303D, '2019-01-16 13:33:26.299000');
