SELECT `funcionario`.`Nome`,`funcionario`.`idDepartamento`,`departamento`.`Turno`
FROM `funcionario`
INNER JOIN `departamento`
ON (`funcionario`.`idDepartamento` = `departamento`.`idDepartamento`)
GROUP BY `funcionario`.`Nome`
ORDER BY `Nome`;