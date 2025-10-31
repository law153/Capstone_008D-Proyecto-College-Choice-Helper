SELECT setval(pg_get_serial_sequence('"core_institucion"', 'idInstitucion'),
              COALESCE(MAX("idInstitucion"), 1),
              TRUE)
FROM "core_institucion";

-- Ajusta la secuencia para Carrera
SELECT setval(pg_get_serial_sequence('"core_carrera"', 'idCarrera'),
              COALESCE(MAX("idCarrera"), 1),
              TRUE)
FROM "core_carrera";

-- Ajusta la secuencia para Peticiones
SELECT setval(pg_get_serial_sequence('"core_peticiones"', 'idPeticiones'),
              COALESCE(MAX("idPeticiones"), 1),
              TRUE)
FROM "core_peticiones";

-- Ajusta la secuencia para User django
SELECT setval(
    pg_get_serial_sequence('"auth_user"', 'id'),
    COALESCE(MAX("id"), 1),
    TRUE
)
FROM "auth_user";