DELIMITER $$
CREATE PROCEDURE `InsertCarros`(marcaInsert VARCHAR(45), modeloInsert VARCHAR(45), placaInsert VARCHAR(7), clientes_idclientesInsert INT)
BEGIN
INSERT INTO `carros`(`marca`,`modelo`,`placa`,`clientes_idclientes`)
VALUE(marcaInsert, modeloInsert, placaInsert, clientes_idclientesInsert);
END $$
DELIMITER ;