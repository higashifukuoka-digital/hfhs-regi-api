CREATE TABLE IF NOT EXISTS `setting` (
  `class_name` VARCHAR(16) NOT NULL,
  `goal` BIGINT NOT NULL,
  `reserve` BIGINT NOT NULL,
  PRIMARY KEY (`class_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
