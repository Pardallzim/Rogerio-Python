/* 	Criação da View */ 
CREATE VIEW `vwTotalVendas` AS
SELECT SUM(`itensvendas`.`Quantidade`) AS `Qtde_Vendida`,
	`itensvendas`.`Produto`, `produtos`.`Descricao`
    FROM `itensvendas`
INNER JOIN `Produtos`
	ON `itensvendas`.`Produto` = `produtos`.`Referencia`
GROUP BY `itensvendas`.`Produto`
ORDER BY `produtos`.`Descricao`;
