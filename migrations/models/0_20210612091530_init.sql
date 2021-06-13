-- upgrade --
CREATE TABLE IF NOT EXISTS `aerich`
(
    `id`      INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app`     VARCHAR(20)  NOT NULL,
    `content` JSON         NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `category_info`
(
    `id`            INT         NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at`    DATETIME(6) DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at`   DATETIME(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_del`        INT         DEFAULT 0,
    `category_id`   VARCHAR(50) NOT NULL UNIQUE,
    `category_name` VARCHAR(50) NOT NULL UNIQUE
) CHARACTER SET utf8mb4 COMMENT ='分类表';
CREATE TABLE IF NOT EXISTS `user_info`
(
    `id`            INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at`    DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at`   DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_del`        INT                   DEFAULT 0,
    `auth_user_id`  VARCHAR(255) NOT NULL UNIQUE,
    `username`      VARCHAR(100),
    `is_admin`      INT          NOT NULL DEFAULT 0,
    `password_hash` VARCHAR(255) NOT NULL,
    `avatar`        VARCHAR(100)          DEFAULT '98d2d0f6-6851-49a8-8d31-8603204cc7311591066453.png'
) CHARACTER SET utf8mb4 COMMENT ='用户表';
CREATE TABLE IF NOT EXISTS `robot_info`
(
    `id`               INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at`       DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at`      DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_del`           INT                   DEFAULT 0,
    `robot_id`         VARCHAR(255) NOT NULL UNIQUE,
    `robot_name`       VARCHAR(255) NOT NULL,
    `download_counter` INT          NOT NULL DEFAULT 666,
    `image`            LONGTEXT,
    `category_id`      VARCHAR(50)  NOT NULL,
    `publisher_id`     VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_robot_in_category_2e28986f` FOREIGN KEY (`category_id`) REFERENCES `category_info` (`category_id`) ON DELETE CASCADE,
    CONSTRAINT `fk_robot_in_user_inf_dc6423fc` FOREIGN KEY (`publisher_id`) REFERENCES `user_info` (`auth_user_id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT ='机器人应用';
CREATE TABLE IF NOT EXISTS `robot_details_info`
(
    `id`          INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at`  DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_del`      INT                   DEFAULT 0,
    `details_id`  VARCHAR(255) NOT NULL UNIQUE,
    `content`     LONGTEXT     NOT NULL,
    `cur_version` VARCHAR(255) NOT NULL DEFAULT 'v1.0.0',
    `video`       VARCHAR(255),
    `robot_id`    VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_robot_de_robot_in_2cf42d53` FOREIGN KEY (`robot_id`) REFERENCES `robot_info` (`robot_id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT ='机器人详情';
CREATE TABLE IF NOT EXISTS `robot_update_info`
(
    `id`             INT          NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at`     DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at`    DATETIME(6)           DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_del`         INT                   DEFAULT 0,
    `update_id`      VARCHAR(255) NOT NULL UNIQUE,
    `update_date`    DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `version`        VARCHAR(255),
    `update_content` LONGTEXT,
    `robot_id`       VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_robot_up_robot_in_c76594bc` FOREIGN KEY (`robot_id`) REFERENCES `robot_info` (`robot_id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT ='机器人更新历史';
