CREATE VIEW `vwAlunos_Turma_like` AS 
SELECT `alunos`.`nome`, `turmas`.`turma`, 
 (`matriculas`.`mensalidade` - `matriculas`.`desconto`) AS `ValorFinal` 
 FROM `alunos`
 INNER JOIN `matriculas`
		ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
INNER JOIN `turmas`
		ON `matriculas`.`turmas_idturmas` = `turmas`.`idturmas`
WHERE `alunos`.`nome` LIKE '%A%' AND `alunos`.`nome` LIKE '%E%' AND `alunos`.`nome` LIKE '%I%' AND `alunos`.`nome` LIKE '%O%' AND `alunos`.`nome` LIKE '%U%'