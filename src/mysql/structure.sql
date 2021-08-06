create database bitso_client_db;
use bitso_client_db;

CREATE TABLE `bitcoin_hist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `high` varchar(45) DEFAULT NULL,
  `last` varchar(45) DEFAULT NULL,
  `created_at` varchar(45) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  `vwap` varchar(45) DEFAULT NULL,
  `low` varchar(45) DEFAULT NULL,
  `ask` varchar(45) DEFAULT NULL,
  `bid` varchar(45) DEFAULT NULL,
  `change_24` varchar(45) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=402 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

select * from bitcoin_hist;
select count(*) from bitcoin_hist;
