SELECT `alunos`.`idalunos`, `alunos`.`nome`, `matriculas`.`mensalidade`, `matriculas`.`desconto`, `matriculas`.`mensalidade` - `matriculas`.`desconto` AS vlr_liquido
FROM `alunos`
INNER JOIN `matriculas`
		ON `matriculas`.`alunos_idalunos` = `alunos`.`idalunos`
ORDER BY `nome`