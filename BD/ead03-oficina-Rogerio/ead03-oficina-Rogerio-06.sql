/* Mostrar Todos os Clientes, os seus Carros e os  mecanicos Responsaveis
*/
SELECT `clientes`.`nome`,`clientes`.`cidade`,`carros`.`marca`,`carros`.`modelo`, `mecanicos`.`nome`, `mecanicos`.`cidade`
FROM `carros`
INNER JOIN `clientes`
		ON `carros`.`clientes_idclientes` = `clientes`.`idclientes` 
INNER JOIN `ordem`
		ON `ordem`.`carros_idcarros` = `carros`.`idcarros`
INNER JOIN `mecanicos`
		ON `mecanicos`.`idmecanicos` = `ordem`.`mecanicos_idmecanicos`
ORDER BY `clientes`.`idclientes`