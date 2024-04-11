SELECT `turmas`.*, `alunos`.* 
FROM `turmas`
INNER JOIN `matriculas`
	ON `matriculas`.`turmas_idturmas` = `turmas`.`idturmas`
INNER JOIN `alunos`
	ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
GROUP BY `nome`
ORDER BY `idturmas`, `idalunos`;