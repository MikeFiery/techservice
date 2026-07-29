DROP DATABASE IF EXISTS techservice_db;

CREATE DATABASE techservice_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE techservice_db;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    status TINYINT NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL,
    deleted_at DATETIME NULL
);

CREATE TABLE equipamento (
    id_equipamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    numero_serie VARCHAR(100) NOT NULL UNIQUE,
    data_compra DATE NOT NULL,
    observações VARCHAR(200),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)

CREATE TABLE ordem_de_servico (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    id_equipamento INT NOT NULL,
    data_abertura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    diagnostico VARCHAR(500) NOT NULL,
    solucao VARCHAR(500) NOT NULL,
    status ENUM('ABERTA', 'EM_ANDAMENTO', 'AGUARDANDO_PECAS', 'CONCLUIDA') NOT NULL DEFAULT 'ABERTA',
    prioridade ENUM('BAIXA', 'MEDIA', 'ALTA') NOT NULL DEFAULT 'MEDIA',
    valor_servico DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    valor_pecas DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    desconto DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    valor_total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    observacoes VARCHAR(500),
    FOREIGN KEY (id_equipamento) REFERENCES equipamento(id_equipamento)
)

