SELECT  `professores`.`idprofessores`, `professores`.`nome`, `materias`.`materia`
FROM `materias`
INNER JOIN `professores`
		ON `professores`.`materias_idmaterias` = `materias`.`idmaterias`
INNER JOIN `grade`
		ON `grade`.`materias_idmaterias` = `materias`.`idmaterias`
INNER JOIN `turmas`
		ON `turmas`.`idturmas` = `grade`.`turmas_idturmas`
WHERE `turmas`.`idturmas` = 3
		AND (`materias`.`idmaterias` = 1 OR `materias`.`idmaterias` = 2 OR `materias`.`idmaterias` = 6)
ORDER BY `professores`.`nome`