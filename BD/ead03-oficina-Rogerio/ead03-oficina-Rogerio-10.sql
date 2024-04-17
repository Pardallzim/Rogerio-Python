/* Mostrar Cliente e o seu carro
*/
SELECT `clientes`.*, `carros`.*
FROM `carros`
INNER JOIN `clientes`
		ON `carros`.`clientes_idclientes` = `clientes`.`idclientes`
ORDER BY `clientes`.`idclientes`