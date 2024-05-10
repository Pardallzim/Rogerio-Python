CREATE VIEW `Clientes_Carros` AS 
SELECT `clientes`.`nome`,`clientes`.`cidade`,`carros`.`marca`,`carros`.`modelo`
FROM `carros`
INNER JOIN `clientes`
		ON `carros`.`clientes_idclientes` = `clientes`.`idclientes` 
ORDER BY `clientes`.`idclientes`;

SELECT * FROM `Clientes_Carros`clientes