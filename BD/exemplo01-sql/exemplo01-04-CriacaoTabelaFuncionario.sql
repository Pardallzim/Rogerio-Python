CREATE TABLE `funcionario`(
	`idFuncionario` INT NOT NULL AUTO_INCREMENT,
    `Nome` VARCHAR(45) NOT NULL,
    `Endereco` VARCHAR(45) NOT NULL,
    `Cidade` VARCHAR(45) NOT NULL,
    `Estado` VARCHAR(45) NOT NULL,
    `CEP` INT NOT NULL,
    `CPF` INT NOT NULL,
    `E-mail` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`idFuncionario`)
) ENGINE = InnoDB;