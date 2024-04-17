/* Mostrar Mecanico e a Ordem de serviço
*/
SELECT `mecanicos`.*, `ordem`.*
FROM `mecanicos`
INNER JOIN `ordem`
		ON `mecanicos`.`idmecanicos` = `ordem`.`mecanicos_idmecanicos`
ORDER BY `mecanicos`.`idmecanicos`