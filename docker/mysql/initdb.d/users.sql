CREATE TABLE IF NOT EXISTS `users` (
  `user_mail` VARCHAR(31) NOT NULL,
  `user_name` VARCHAR(20) NOT NULL DEFAULT '',
  `user_class` VARCHAR(20) NOT NULL DEFAULT '',
  `user_role` VARCHAR(20) NOT NULL DEFAULT 'student',
  PRIMARY KEY (`user_mail`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
