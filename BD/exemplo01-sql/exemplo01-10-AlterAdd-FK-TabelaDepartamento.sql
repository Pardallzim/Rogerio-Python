ALTER TABLE `funcionario`
	ADD COLUMN `idDepartamento` INT NOT NULL;
ALTER TABLE `funcionario`
		ADD FOREIGN KEY `fk_de_departamento` (`idDepartamento`)
	REFERENCES `departamento`(`idDepartamento`)
	ON DELETE RESTRICT;