SELECT  `professores`.`idprofessores`, `professores`.`nome`, `materias`.`materia`
FROM `materias`
INNER JOIN `professores`
		ON `professores`.`materias_idmaterias` = `materias`.`idmaterias`
INNER JOIN `grade`
		ON `grade`.`materias_idmaterias` = `materias`.`idmaterias`
INNER JOIN `turmas`
		ON `turmas`.`idturmas` = `grade`.`turmas_idturmas`
WHERE `turmas`.`idturmas` = 4
ORDER BY `professores`.`nome`