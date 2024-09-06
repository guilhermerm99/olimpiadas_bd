-- Inserindo registros na tabela pais
INSERT INTO pais (nome, sigla, bandeira) VALUES
    ('Brasil', 'BRA', null),
    ('Estados Unidos', 'USA', null),
    ('República Popular da China', 'CHN', null),
    ('Japão', 'JPN', null),
    ('Alemanha', 'GER', null),
    ('França', 'FRA', null),
    ('Grã-Bretanha', 'GBR', null);

-- Inserindo registros na tabela confederacao
INSERT INTO confederacao (nome, id_pais) VALUES
    ('Comitê Olímpico do Brasil', 1),
    ('Comitê Olímpico e Paralímpico dos Estados Unidos', 2),
    ('Comitê Olímpico Chinês', 3),
    ('Comitê Olímpico Japonês', 4),
    ('Confederação Alemã de Esportes Olímpicos', 5);

-- Inserindo registros na tabela edicao
INSERT INTO edicao (ano, cidade_sede, id_pais) VALUES
    (2024, 'Paris', 6),
    (2020, 'Tóquio', 4),
    (2016, 'Rio de Janeiro', 1),
    (2012, 'Londres', 7),
    (2008, 'Pequim', 3);

-- Inserindo dados na tabela modalidade
INSERT INTO modalidade (nome) VALUES
    ('Atletismo'),
    ('Natação'),
    ('Ginástica'),
    ('Judô'),
    ('Vôlei'),
    ('Skate');

-- Inserindo dados na tabela evento
INSERT INTO evento (nome, data, tipo_numero, tipo_genero, id_modalidade, id_recorde) VALUES
    ('Final de Solo de Ginástica', '2024-08-05', 'Individual', 'Feminino', 3, NULL),
    ('Semifinal de Vôlei de Praia', '2024-08-08', 'Dupla', 'Feminino', 5, NULL),
    ('Final do Skate Park', '2024-08-07', 'Individual', 'Masculino', 6, NULL),
    ('Marcha Atlética 20km', '2024-08-01', 'Individual', 'Masculino', 1, NULL),
    ('Final da Competição por Equipes de Ginástica Artística', '2024-07-30', 'Equipe', 'Feminino', 3, NULL),
    ('Final de Vôlei de Praia', '2024-08-09', 'Dupla', 'Feminino', 5, NULL);

-- Inserindo dados na tabela equipe
INSERT INTO equipe (nome, id_confederacao, id_evento) VALUES
    ('Seleção Brasileira de Vôlei', 1, 5),
    ('Equipe de Ginástica Artística dos Estados Unidos', 2, 5),
    ('Equipe de Atletismo do Brasil', 1, 4),
    ('Equipe de Ginástica Artística do Brasil', 1, 5),
    ('Equipe de Skate do Brasil', 1, 3);

-- Inserindo dados na tabela atleta
INSERT INTO atleta (genero, data_nasc, nome, id_confederacao, id_modalidade, id_equipe) VALUES
    ('F', '1997-03-14', 'Simone Biles Owens', 2, 3, 2),
    ('F', '1999-05-08', 'Rebeca Rodrigues de Andrade', 1, 3, 4),
    ('M', '1991-03-19', 'Caio Oliveira de Sena Bonfim', 1, 1, 3),
    ('F', '1997-09-29', 'Ana Patrícia Silva Ramos', 1, 5, 1),
    ('F', '1998-08-01', 'Eduarda dos Santos Lisboa', 1, 5, 1);

-- Inserindo dados na tabela medalha
INSERT INTO medalha (tipo, id_atleta, id_equipe, id_evento) VALUES
    ('Ouro', 2, 4, 1),
    ('Bronze', 2, 4, 5),
    ('Ouro', 1, 2, 5),
    ('Ouro', 4, 1, 6),
    ('Ouro', 5, 1, 6);

-- Inserindo dados na tabela historico
INSERT INTO historico (desempenho, id_atleta, id_equipe, id_edicao) VALUES
    ('Medalha de ouro no Salto', 2, 4, 2020),
    ('4 medalhas de ouro na Ginástica', 1, 2, 2020),
    ('Medalha de ouro no Solo', 2, 4, 2024),
    ('Medalha de prata no Vôlei de Praia', 4, 1, 2020),
    ('Medalha de prata no Vôlei de Praia', 5, 1, 2020);

-- Inserindo dados na tabela eventos_edicao
INSERT INTO eventos_edicao (id_evento, ano) VALUES
    (1, 2024),
    (2, 2024),
    (3, 2024),
    (4, 2024),
    (5, 2024);

-- Inserindo dados na tabela participa_atleta
INSERT INTO participa_atleta (ano, id_atleta) VALUES
    (2024, 1),
    (2024, 2),
    (2024, 3),
    (2024, 4),
    (2024, 5);

-- Inserindo dados na tabela atleta1
INSERT INTO atleta1 (id_atleta, id_evento) VALUES
    (4, 2),
    (4, 6);

-- Inserindo dados na tabela atleta2
INSERT INTO atleta2 (id_atleta, id_evento) VALUES
    (5, 2),
    (5, 6);

-- Inserindo dados na tabela edicao_medalha
INSERT INTO edicao_medalha (id_medalha, ano) VALUES
    (1, 2024),
    (2, 2024),
    (3, 2024),
    (4, 2024),
    (5, 2024);

-- Inserindo dados na tabela paises_participantes
INSERT INTO paises_participantes (ano, id_confederacao) VALUES
    (2024, 1),
    (2024, 2),
    (2024, 3),
    (2024, 4),
    (2024, 5);
