SELECT `aluno`.`idAluno`, `aluno`.`Nome`,
       `aluno`.`idTurma`, `turma`.`Sala` 
FROM `aluno`
INNER JOIN `turma`
	ON `aluno`.`idTurma` = `turma`.`idTurma`
ORDER BY `aluno`.`Nome`, `aluno`. `idAluno`;