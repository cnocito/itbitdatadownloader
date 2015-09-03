CREATE TABLE `ticker` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(45) NOT NULL,
  `bid` varchar(45) DEFAULT NULL,
  `volume24` varchar(45) DEFAULT NULL,
  `low24` varchar(45) DEFAULT NULL,
  `lastPrice` varchar(45) DEFAULT NULL,
  `askAmt` varchar(45) DEFAULT NULL,
  `vwapToday` varchar(45) DEFAULT NULL,
  `volumeToday` varchar(45) DEFAULT NULL,
  `ask` varchar(45) DEFAULT NULL,
  `lastAmt` varchar(45) DEFAULT NULL,
  `high24h` varchar(45) DEFAULT NULL,
  `vwap24h` varchar(45) DEFAULT NULL,
  `lowToday` varchar(45) DEFAULT NULL,
  `highToday` varchar(45) DEFAULT NULL,
  `serverTimeUTC` varchar(45) NOT NULL,
  `bidAmt` varchar(45) DEFAULT NULL,
  `openToday` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_ticker_symbol_serverTimeUTC` (`symbol`,`serverTimeUTC`)
) ENGINE=InnoDB AUTO_INCREMENT=366 DEFAULT CHARSET=big5;

CREATE TABLE `trade` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `matchnumber` bigint(20) DEFAULT NULL,
  `timestamp` varchar(45) NOT NULL,
  `amount` varchar(45) NOT NULL,
  `price` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `matchnumber_UNIQUE` (`matchnumber`)
) ENGINE=InnoDB AUTO_INCREMENT=178323 DEFAULT CHARSET=big5;
