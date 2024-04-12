SELECT `matriculas`.`idmatriculas`, `turmas`.`turma`, `matriculas`.`alunos_idalunos`,
		`alunos`.`nome`, `matriculas`.`mensalidade`, `matriculas`.`desconto`
FROM `matriculas`
INNER JOIN `turmas`
		ON `turmas`.`idturmas` = `matriculas`.`turmas_idturmas`
INNER JOIN `alunos`
		ON `alunos`.`idalunos` = `matriculas`.`alunos_idalunos`
WHERE `matriculas`.`desconto` < 25
ORDER BY `alunos`.`nome`