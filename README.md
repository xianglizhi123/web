# web
 create DATABASE APPL;
  mysql> CREATE TABLE IF NOT EXISTS `appl`(
    -> `id` INT UNSIGNED AUTO_INCREMENT,
    -> `apply_date` INT UNSIGNED NOT NULL,
    -> `issue_date` INT UNSIGNED NOT NULL,
    -> `major` INT UNSIGNED NOT NULL,
    -> `province` INT UNSIGNED NOT NULL,
    -> `from_school` INT UNSIGNED NOT NULL,
    -> `to_school` INT UNSIGNED NOT NULL,
    -> `apply_location` INT UNSIGNED NOT NULL,
    -> `citizenship` INT UNSIGNED NOT NULL,
    -> `nick_name` VARCHAR(100),
    -> PRIMARY KEY (`id`)
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
ToDO due before Aug 5:
  1. finish sql connector impl
  2. add,delete,change,check impl for sql
