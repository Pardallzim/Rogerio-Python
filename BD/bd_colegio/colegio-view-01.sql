CREATE VIEW `vwAlunos_mensalidade` AS 
SELECT `alunos`.`nome`, `matriculas`.`mensalidade`,
 `matriculas`.`desconto`, 
 (`matriculas`.`mensalidade` - `matriculas`.`desconto`) AS `ValorFinal` 
 FROM `alunos`
 INNER JOIN `matriculas`
		ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
INNER JOIN `turmas`
		ON `matriculas`.`turmas_idturmas` = `turmas`.`idturmas`
