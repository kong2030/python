/*
 Navicat MySQL Data Transfer

 Source Server         : mysql
 Source Server Version : 50723
 Source Host           : localhost
 Source Database       : sky

 Target Server Version : 50723
 File Encoding         : utf-8

 Date: 01/02/2019 12:33:18 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `auth_group_permissions`
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
--  Table structure for `auth_permission`
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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add group', '2', 'add_group'), ('5', 'Can change group', '2', 'change_group'), ('6', 'Can delete group', '2', 'delete_group'), ('7', 'Can add permission', '3', 'add_permission'), ('8', 'Can change permission', '3', 'change_permission'), ('9', 'Can delete permission', '3', 'delete_permission'), ('10', 'Can add user', '4', 'add_user'), ('11', 'Can change user', '4', 'change_user'), ('12', 'Can delete user', '4', 'delete_user'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add user info', '7', 'add_userinfo'), ('20', 'Can change user info', '7', 'change_userinfo'), ('21', 'Can delete user info', '7', 'delete_userinfo'), ('22', 'Can add module', '8', 'add_module'), ('23', 'Can change module', '8', 'change_module'), ('24', 'Can delete module', '8', 'delete_module'), ('25', 'Can add app system', '9', 'add_appsystem'), ('26', 'Can change app system', '9', 'change_appsystem'), ('27', 'Can delete app system', '9', 'delete_appsystem'), ('28', 'Can add environment', '10', 'add_environment'), ('29', 'Can change environment', '10', 'change_environment'), ('30', 'Can delete environment', '10', 'delete_environment'), ('31', 'Can add host', '11', 'add_host'), ('32', 'Can change host', '11', 'change_host'), ('33', 'Can delete host', '11', 'delete_host'), ('34', 'Can add order', '12', 'add_order'), ('35', 'Can change order', '12', 'change_order'), ('36', 'Can delete order', '12', 'delete_order');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
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
--  Records of `auth_user`
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$QgVAri4gnKKe$BdejV6ZAevS3HAk/UtVJEN9Qoc90iSwXRDXkWL90gsw=', '2019-01-01 14:45:27.027874', '1', 'admin', '', '', 'yangwenren@message.guosen.com.cn', '1', '1', '2018-12-29 03:18:05.734761');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user_groups`
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
--  Table structure for `auth_user_user_permissions`
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
--  Table structure for `cmdb_appsystem`
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
--  Records of `cmdb_appsystem`
-- ----------------------------
BEGIN;
INSERT INTO `cmdb_appsystem` VALUES ('1', 'QQ', '个股期权系统'), ('2', 'SMEN', '内存交易系统'), ('3', 'OTC', '场外柜台系统');
COMMIT;

-- ----------------------------
--  Table structure for `cmdb_environment`
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
--  Records of `cmdb_environment`
-- ----------------------------
BEGIN;
INSERT INTO `cmdb_environment` VALUES ('1', '测试环境', null, null, null), ('2', '预发布环境', 'yfb', '东莞机房', '10.33.*.*,'), ('3', '生产环境', 'prd', '东莞机房', '10.33.*.*,'), ('4', '同城灾备', null, '深圳滨海', '192.168.*.*,'), ('5', '异地灾备', null, '上海宁桥', null);
COMMIT;

-- ----------------------------
--  Table structure for `cmdb_host`
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `cmdb_host`
-- ----------------------------
BEGIN;
INSERT INTO `cmdb_host` VALUES ('1', 'DYQQ-DBPU152', '10.35.144.152', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2'), ('2', 'DYQQ-DBPU142', '10.35.144.142', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2'), ('3', 'DYQQ-WEB153', '10.35.144.153', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2'), ('4', 'DYQQ-WEB154', '10.35.144.154', 'dgadmin', 'ITRiNTU4NTM1Znk=', '2');
COMMIT;

-- ----------------------------
--  Table structure for `cmdb_host_module`
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `cmdb_host_module`
-- ----------------------------
BEGIN;
INSERT INTO `cmdb_host_module` VALUES ('1', '1', '1'), ('2', '2', '1'), ('3', '3', '2'), ('4', '4', '2');
COMMIT;

-- ----------------------------
--  Table structure for `cmdb_module`
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
--  Records of `cmdb_module`
-- ----------------------------
BEGIN;
INSERT INTO `cmdb_module` VALUES ('1', 'QQ-DBPU', '个股期权-磁盘bpu', 'd$\\maServer', 'd$\\tools\\scripts\\deploy\\maServer', '1'), ('2', 'QQ-WEB', '个股期权-web', 'd$\\kweb', 'd$\\tools\\scripts\\deploy\\kweb', '1'), ('3', 'QQ-KCBP-JY', '个股期权-kcbp-jy', 'd$\\kcbp', 'd$\\tools\\scripts\\deploy\\kcbp', '1');
COMMIT;

-- ----------------------------
--  Table structure for `config_userinfo`
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
--  Table structure for `deploy_order`
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `deploy_order`
-- ----------------------------
BEGIN;
INSERT INTO `deploy_order` VALUES ('1', '20181231132639KY', '1', '/Users/yangwenren/Desktop/install/upload/20181231132639KY.zip', '2018-12-31 13:26:39.000000', '2019-01-01 14:46:08.000000', '0', '0', '2', '0', '0', '1', '1', '1', '3'), ('2', '20181231132720RN', '1', '/Users/yangwenren/Desktop/install/upload/20181231132720RN.zip', '2018-12-31 13:27:20.000000', '2019-01-01 13:09:33.327699', '0', '0', '0', '1', '0', '1', '1', '2', '4'), ('3', '20190101131713KG', '1', '/Users/yangwenren/Desktop/install/upload/20190101131713KG.zip', '2019-01-01 13:17:13.399000', '2019-01-01 13:17:13.399000', '0', '0', '0', '0', '0', '1', '1', '3', '0'), ('4', '20190101132509ET', '1', '/Users/yangwenren/Desktop/install/upload/20190101132509ET.zip', '2019-01-01 13:25:09.140376', '2019-01-01 13:25:09.140376', '0', '0', '0', '0', '0', '1', '1', '1', '0'), ('5', '20190101132524BB', '1', '/Users/yangwenren/Desktop/install/upload/20190101132524BB.zip', '2019-01-01 13:25:24.507935', '2019-01-01 13:25:24.507935', '0', '0', '0', '0', '0', '1', '1', '1', '0'), ('6', '20190101132543KQ', '1', '/Users/yangwenren/Desktop/install/upload/20190101132543KQ.zip', '2019-01-01 13:25:43.745305', '2019-01-01 13:25:43.745305', '0', '0', '0', '0', '0', '1', '1', '3', '0'), ('7', '20190101132606BO', '1', '/Users/yangwenren/Desktop/install/upload/20190101132606BO.zip', '2019-01-01 13:26:06.323815', '2019-01-01 13:26:06.323815', '0', '0', '0', '0', '0', '1', '1', '2', '0');
COMMIT;

-- ----------------------------
--  Table structure for `django_admin_log`
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
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `django_admin_log`
-- ----------------------------
BEGIN;
INSERT INTO `django_admin_log` VALUES ('1', '2018-12-29 03:18:57.914139', 0x31, '个股期权系统', '1', 0x5b7b226164646564223a207b7d7d5d, '9', '1'), ('2', '2018-12-29 03:19:44.366399', 0x31, '测试环境', '1', 0x5b7b226164646564223a207b7d7d5d, '10', '1'), ('3', '2018-12-29 03:19:59.013150', 0x32, '预发布环境', '1', 0x5b7b226164646564223a207b7d7d5d, '10', '1'), ('4', '2018-12-29 03:20:16.869563', 0x33, '生产环境', '1', 0x5b7b226164646564223a207b7d7d5d, '10', '1'), ('5', '2018-12-29 03:20:30.918200', 0x34, '同城灾备', '1', 0x5b7b226164646564223a207b7d7d5d, '10', '1'), ('6', '2018-12-29 03:20:43.823001', 0x35, '异地灾备', '1', 0x5b7b226164646564223a207b7d7d5d, '10', '1'), ('7', '2018-12-29 03:21:03.591052', 0x31, 'QQ-DBPU', '1', 0x5b7b226164646564223a207b7d7d5d, '8', '1'), ('8', '2018-12-29 08:05:08.259402', 0x31, '10.35.144.152', '1', 0x5b7b226164646564223a207b7d7d5d, '11', '1'), ('9', '2018-12-29 10:45:37.321700', 0x32, '10.35.144.142', '1', 0x5b7b226164646564223a207b7d7d5d, '11', '1'), ('10', '2018-12-29 12:51:51.880965', 0x32, '内存交易系统', '1', 0x5b7b226164646564223a207b7d7d5d, '9', '1'), ('11', '2018-12-29 12:52:23.684337', 0x33, '场外柜台系统', '1', 0x5b7b226164646564223a207b7d7d5d, '9', '1'), ('12', '2018-12-29 12:52:46.296452', 0x31, '个股期权系统', '2', 0x5b7b226368616e676564223a207b226669656c6473223a205b226170705f6e616d65225d7d7d5d, '9', '1'), ('13', '2018-12-30 01:46:57.265800', 0x33, '10.35.144.153', '1', 0x5b7b226164646564223a207b7d7d5d, '11', '1'), ('14', '2018-12-30 01:47:19.543662', 0x34, '10.35.144.154', '1', 0x5b7b226164646564223a207b7d7d5d, '11', '1'), ('15', '2019-01-01 07:45:22.234924', 0x31, 'Order object', '2', 0x5b7b226368616e676564223a207b226669656c6473223a205b2263757272656e745f656e76225d7d7d5d, '12', '1'), ('16', '2019-01-01 07:48:22.095525', 0x31, 'Order object', '2', 0x5b7b226368616e676564223a207b226669656c6473223a205b2263757272656e745f656e76225d7d7d5d, '12', '1'), ('17', '2019-01-01 11:04:21.245557', 0x32, 'Order object', '2', 0x5b7b226368616e676564223a207b226669656c6473223a205b2263757272656e745f656e76225d7d7d5d, '12', '1'), ('18', '2019-01-01 14:46:49.125557', 0x31, 'Order object', '2', 0x5b7b226368616e676564223a207b226669656c6473223a205b22656e765f33225d7d7d5d, '12', '1');
COMMIT;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry'), ('2', 'auth', 'group'), ('3', 'auth', 'permission'), ('4', 'auth', 'user'), ('9', 'cmdb', 'appsystem'), ('10', 'cmdb', 'environment'), ('11', 'cmdb', 'host'), ('8', 'cmdb', 'module'), ('7', 'config', 'userinfo'), ('5', 'contenttypes', 'contenttype'), ('12', 'deploy', 'order'), ('6', 'sessions', 'session');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-29 03:17:09.473545'), ('2', 'auth', '0001_initial', '2018-12-29 03:17:09.869761'), ('3', 'admin', '0001_initial', '2018-12-29 03:17:09.946636'), ('4', 'admin', '0002_logentry_remove_auto_add', '2018-12-29 03:17:09.987823'), ('5', 'contenttypes', '0002_remove_content_type_name', '2018-12-29 03:17:10.057752'), ('6', 'auth', '0002_alter_permission_name_max_length', '2018-12-29 03:17:10.091466'), ('7', 'auth', '0003_alter_user_email_max_length', '2018-12-29 03:17:10.129563'), ('8', 'auth', '0004_alter_user_username_opts', '2018-12-29 03:17:10.142528'), ('9', 'auth', '0005_alter_user_last_login_null', '2018-12-29 03:17:10.183124'), ('10', 'auth', '0006_require_contenttypes_0002', '2018-12-29 03:17:10.186325'), ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-12-29 03:17:10.201573'), ('12', 'auth', '0008_alter_user_username_max_length', '2018-12-29 03:17:10.242435'), ('13', 'cmdb', '0001_initial', '2018-12-29 03:17:10.487648'), ('14', 'config', '0001_initial', '2018-12-29 03:17:10.568720'), ('15', 'sessions', '0001_initial', '2018-12-29 03:17:10.614370'), ('16', 'cmdb', '0002_auto_20181229_1324', '2018-12-29 13:24:35.282475'), ('17', 'deploy', '0001_initial', '2018-12-30 05:32:40.489246'), ('18', 'deploy', '0002_auto_20181230_0746', '2018-12-30 07:46:58.532421'), ('19', 'deploy', '0002_auto_20181231_1304', '2018-12-31 13:04:37.285384'), ('20', 'deploy', '0003_auto_20181231_1307', '2018-12-31 13:08:25.964902'), ('21', 'deploy', '0004_auto_20181231_1307', '2018-12-31 13:08:25.969065'), ('22', 'deploy', '0002_order', '2018-12-31 13:12:17.582715'), ('23', 'deploy', '0003_order_current_env', '2019-01-01 05:39:45.723375');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
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
--  Records of `django_session`
-- ----------------------------
BEGIN;
INSERT INTO `django_session` VALUES ('2gryt2ike4t3zzoxv819sd5bistj07uc', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-12 04:01:11.333932'), ('4xgcnmvgv4qc57ew8m0wb9yjusnbfvco', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-13 13:23:44.194185'), ('7hvzh3ajcigwmuc9on3paowuigwrmoxi', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-13 13:12:42.668012'), ('8f1yvfccdbtzdw2nzfhg475yhrtwzztd', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-12 13:12:39.555317'), ('9b9bgihctm81u81qjxeyfdn7gahhzzvz', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-13 11:57:17.697524'), ('banjipovss0frcgxuur76xo8zhrhpwke', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-12 08:01:43.253075'), ('bmt6bvqmcfeqp4z1iavjut1bwmcuyou4', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-13 11:16:30.019345'), ('ic5vuqtym7hmbtj84psjh8y2r9ensykt', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-14 13:26:06.125746'), ('l8kyxoruf6sp4ezd6jga43hilub7cpsk', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-15 06:12:11.672931'), ('pzzjojqx0pi5bn1epi4warry0zezv8js', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-13 11:06:30.104409'), ('r4tgw7dbv4l0vz6vpjxl6njttavaykr0', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-15 06:12:53.072373'), ('tbfacbftt17zr98mjwaz1b9ofriq30rb', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-15 13:27:48.356028'), ('tebnl635c2gwzej31q9nwjcze5z5zoum', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-13 13:06:40.802065'), ('vehuputafs60wtyqrecj8h2rt0hs4p6x', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-12 04:02:55.447639'), ('z30s9t1si6esv91r236qx96rghsi6v9f', 0x59324e6c4d57517a59324a6a4e444d3059324d314d574e69597a5a695a44566d4e475135596a4a694e544a694d6a51334f474e6c596a7037496c39686458526f5833567a5a584a666147467a61434936496a59315932466d596d5a695a54646c5a4449784f445578595459344e5441354d6d45324e54566c4e574d304e44466d4f4751355a5445694c434a6659585630614639316332567958324a685932746c626d51694f694a6b616d46755a3238755932397564484a70596935686458526f4c6d4a685932746c626d527a4c6b31765a475673516d466a613256755a434973496c39686458526f5833567a5a584a66615751694f694978496e303d, '2019-01-15 14:45:27.030498');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
