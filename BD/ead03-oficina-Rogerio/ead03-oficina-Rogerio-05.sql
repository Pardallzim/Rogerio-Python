/* Mostrar Todos os Clientes e os seus Carros
*/
SELECT `clientes`.`nome`,`clientes`.`cidade`,`carros`.`marca`,`carros`.`modelo`
FROM `carros`
INNER JOIN `clientes`
		ON `carros`.`clientes_idclientes` = `clientes`.`idclientes` 
ORDER BY `clientes`.`idclientes`