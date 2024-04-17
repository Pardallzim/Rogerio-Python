/* Mostrar Todos os Carros e os defeitos e quanto sera cobrado 
*/
SELECT `carros`.`marca`,`carros`.`modelo`, `ordem`.`defeito`, `ordem`.`valor`, `ordem`.`desconto`,(`ordem`.`valor` - `ordem`.`desconto`) AS valorFinal
FROM `carros`
INNER JOIN `ordem`
		ON `ordem`.`carros_idcarros` = `carros`.`idcarros`
INNER JOIN `mecanicos`
		ON `mecanicos`.`idmecanicos` = `ordem`.`mecanicos_idmecanicos`
ORDER BY `carros`.`idcarros`