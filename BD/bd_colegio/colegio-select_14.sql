SELECT `turmas`.`turma`, `alunos`.*
FROM `turmas`
INNER JOIN `matriculas`
		ON `matriculas`.`turmas_idturmas` = `turmas`.`idturmas`
INNER JOIN `alunos`
		ON `alunos`.`idalunos` = `matriculas`.`alunos_idalunos` 
ORDER BY `turmas`.`idturmas`, `alunos`.`nome`