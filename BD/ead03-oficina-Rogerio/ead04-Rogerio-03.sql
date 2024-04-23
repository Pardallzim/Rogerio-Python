CREATE VIEW `Clientes_Defeitos` AS 
SELECT `mecanicos`.`nome`, `carros`.`marca`,`carros`.`modelo`, `ordem`.`defeito`
FROM `carros`
INNER JOIN `ordem`
		ON `ordem`.`carros_idcarros` = `carros`.`idcarros`
INNER JOIN `mecanicos`
		ON `mecanicos`.`idmecanicos` = `ordem`.`mecanicos_idmecanicos`
ORDER BY `mecanicos`.`idmecanicos`;

SELECT * FROM `Clientes_Defeitos`