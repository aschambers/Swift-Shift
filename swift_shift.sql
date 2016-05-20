-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema swiftshift
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema swiftshift
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `swiftshift` DEFAULT CHARACTER SET utf8 ;
USE `swiftshift` ;

-- -----------------------------------------------------
-- Table `swiftshift`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swiftshift`.`customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `phone` INT NULL,
  `address` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swiftshift`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swiftshift`.`employees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `phone` INT NULL,
  `address` VARCHAR(255) NULL,
  `employee_id` VARCHAR(255) NULL,
  `hiredate` DATE NULL,
  `workday` VARCHAR(255) NULL,
  `employee_level` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swiftshift`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swiftshift`.`address` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `street` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `state` VARCHAR(255) NULL,
  `zipcode` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `customers_id` INT NOT NULL,
  `employees_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_address_customers1_idx` (`customers_id` ASC),
  INDEX `fk_address_employees1_idx` (`employees_id` ASC),
  CONSTRAINT `fk_address_customers1`
    FOREIGN KEY (`customers_id`)
    REFERENCES `swiftshift`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_address_employees1`
    FOREIGN KEY (`employees_id`)
    REFERENCES `swiftshift`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swiftshift`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swiftshift`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `messages` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `customer_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_customers1_idx` (`customer_id` ASC),
  INDEX `fk_messages_employees1_idx` (`employee_id` ASC),
  CONSTRAINT `fk_messages_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `swiftshift`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `swiftshift`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swiftshift`.`appointments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swiftshift`.`appointments` (
  `id` INT NOT NULL,
  `start_time` DATETIME NULL,
  `end_time` DATETIME NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `customer_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_appointments_customers1_idx` (`customer_id` ASC),
  INDEX `fk_appointments_employees1_idx` (`employee_id` ASC),
  CONSTRAINT `fk_appointments_customers1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `swiftshift`.`customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_appointments_employees1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `swiftshift`.`employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
