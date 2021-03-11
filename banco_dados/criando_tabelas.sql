CREATE TABLE IF NOT EXISTS gastos(
	id_gastos INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
	id_estabelecimento INT NOT NULL,
    id_categoria INT NOT NULL,
    valor FLOAT NOT NULL,
    data_gasto TIMESTAMP,
    forma_pagamento VARCHAR(8) 
);

CREATE TABLE IF NOT EXISTS estabelecimentos(
	id_estabelecimento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	estabelecimento VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS categorias(
	id_categoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	categoria VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS usuarios(
	id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	usuario VARCHAR(20) UNIQUE
);

ALTER TABLE gastos ADD CONSTRAINT FK_estabelecimento
FOREIGN KEY (id_estabelecimento) REFERENCES estabelecimentos(id_estabelecimento);

ALTER TABLE gastos ADD CONSTRAINT FK_categoria
FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria);

ALTER TABLE gastos ADD CONSTRAINT FK_usuario
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario);

INSERT INTO categorias(
	categoria
	)
	VALUES(
	'Bar'
);

INSERT INTO estabelecimentos(
	estabelecimento)
	VALUES('Garrafeiros');

INSERT INTO usuarios(
	usuario)
    VALUES('Artur'),
	('Victor');
