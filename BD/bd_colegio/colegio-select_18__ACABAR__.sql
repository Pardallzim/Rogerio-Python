SELECT `professores`.`nome`, `materias`.`materia`, `turmas`.`turma`, `alunos`.`idalunos`, `alunos`.`nome`
FROM `alunos`
INNER JOIN `matriculas`
		ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
INNER JOIN `turmas`
		ON `turmas`.`idturmas` = `matriculas`.`turmas_idturmas`
INNER JOIN `grade`