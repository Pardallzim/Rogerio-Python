SELECT `professores`.`nome`, `materias`.`materia`, `turmas`.`turma`, `alunos`.`idalunos`, `alunos`.`nome`
FROM `alunos`
INNER JOIN `matriculas`
		ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
INNER JOIN `turmas`
		ON `turmas`.`idturmas` = `matriculas`.`turmas_idturmas`
INNER JOIN `grade`
		ON `grade`.`turmas_idturmas` = `turmas`.`idturmas`
INNER JOIN `professores`
		ON `professores`.`materias_idmaterias` = `materias`.`idmaterias`
INNER JOIN `materias`
		ON `materias`.`idmaterias` = `grade`.`materias_idmaterias`
ORDER BY `professores`.`nome`