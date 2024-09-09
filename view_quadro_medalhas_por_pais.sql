CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `olimpiadasdb`.`quadro_medalhas_por_pais` AS
    SELECT 
        `e`.`ano` AS `ano_edicao`,
        `p`.`sigla` AS `sigla_pais`,
        COUNT(DISTINCT (CASE
                WHEN
                    (`m`.`tipo` = 'Ouro')
                THEN
                    CONCAT(`ap`.`identificador_equipe`,
                            `m`.`id_evento`)
                ELSE NULL
            END)) AS `medalhas_ouro`,
        COUNT(DISTINCT (CASE
                WHEN
                    (`m`.`tipo` = 'Prata')
                THEN
                    CONCAT(`ap`.`identificador_equipe`,
                            `m`.`id_evento`)
                ELSE NULL
            END)) AS `medalhas_prata`,
        COUNT(DISTINCT (CASE
                WHEN
                    (`m`.`tipo` = 'Bronze')
                THEN
                    CONCAT(`ap`.`identificador_equipe`,
                            `m`.`id_evento`)
                ELSE NULL
            END)) AS `medalhas_bronze`,
        COUNT(DISTINCT CONCAT(`ap`.`identificador_equipe`,
                    `m`.`id_evento`,
                    `m`.`tipo`)) AS `total_medalhas`
    FROM
        (((((`olimpiadasdb`.`medalha` `m`
        JOIN `olimpiadasdb`.`atleta` `a` ON ((`m`.`id_atleta` = `a`.`id_atleta`)))
        JOIN `olimpiadasdb`.`confederacao` `c` ON ((`a`.`id_confederacao` = `c`.`id_confederacao`)))
        JOIN `olimpiadasdb`.`pais` `p` ON ((`c`.`id_pais` = `p`.`id_pais`)))
        JOIN `olimpiadasdb`.`edicao` `e` ON ((`m`.`id_edicao` = `e`.`ano`)))
        JOIN `olimpiadasdb`.`atletas_participantes` `ap` ON (((`m`.`id_atleta` = `ap`.`id_atleta`)
            AND (`m`.`id_evento` = `ap`.`id_evento`))))
    GROUP BY `e`.`ano` , `p`.`sigla`