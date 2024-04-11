SELECT `materias`.`materia`,`turmas`.*, `alunos`.* 
FROM `turmas`
INNER JOIN `matriculas`
	ON `matriculas`.`turmas_idturmas` = `turmas`.`idturmas`
INNER JOIN `alunos`
	ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
INNER JOIN `grade`
	ON `grade`.`turmas_idturmas` = `turmas`.`idturmas`
INNER JOIN `materias`
	ON `grade`.`materias_idmaterias` = `materias`.`idmaterias`
WHERE `materias`.`idmaterias` = 1
		OR `materias`.`idmaterias` = 2
        OR `materias`.`idmaterias` = 6
        OR `materias`.`idmaterias` = 5
ORDER BY `materia`,`nome`