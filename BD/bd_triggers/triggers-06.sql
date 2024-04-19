/* 
Desliga o modo seguro para execução do delete
Delete o primeiro registro de ItensVendas
Lista a tabela ItensVendas 
*/
SET SQL_SAFE_UPDATES = 0;
DELETE 	FROM `ItensVendas` WHERE `Venda` = 1 AND `Produto` = '001';
SET SQL_SAFE_UPDATES = 1;

SELECT *
	FROM `ItensVendas`;