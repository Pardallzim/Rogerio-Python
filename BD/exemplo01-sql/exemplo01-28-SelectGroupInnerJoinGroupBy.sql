SELECT `funcionario`.`idDepartamento`, `departamento`.`Turno`,COUNT(*)
FROM `funcionario`
INNER JOIN `departamento`
ON `funcionario`.`idDepartamento` = `departamento`.`idDepartamento`
GROUP BY `departamento`.`Turno`
ORDER BY `Turno`;