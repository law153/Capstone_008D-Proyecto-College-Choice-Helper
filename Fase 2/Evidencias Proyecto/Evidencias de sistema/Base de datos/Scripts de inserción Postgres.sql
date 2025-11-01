INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$1000000$mpINIoj0p9JUO0DYt1aEcU$brgBdGOyuwfChGmUpTV40XFQ14wpzV6a09Gf0oUhAlo=', NULL, false, 'estudiante@gmail.com', '', '', '', false, true, '2025-09-17 17:42:31.669437-03');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (3, 'pbkdf2_sha256$1000000$FRDS06rOM8dD48LWXVkg0g$7f+Kt3yjulITlxMd5Ynhxr07kMddGBuCt5PBYNRpiC0=', NULL, false, 'institucion@gmail.com', '', '', '', false, true, '2025-09-17 17:45:08.978033-03');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (4, 'pbkdf2_sha256$1000000$lJGVqknMdt3SfrKSwZFD7p$iJtZkcJH+XxvYO4vpnqCjT5d0hjjz8Hr2EdVqYg49Us=', NULL, false, 'administrador@gmail.com', '', '', '', false, true, '2025-09-17 17:45:24.586827-03');


INSERT INTO public.core_rol (id_rol, nombre_rol) VALUES (0, 'Estudiante');
INSERT INTO public.core_rol (id_rol, nombre_rol) VALUES (1, 'Gestor institucional');
INSERT INTO public.core_rol (id_rol, nombre_rol) VALUES (2, 'Administrador');

INSERT INTO public.core_usuario ("idUsuario_id", correo, "comunaUsuario", rol_id) VALUES (2, 'estudiante@gmail.com', 'Renca', 0, 1, null);
INSERT INTO public.core_usuario ("idUsuario_id", correo, "comunaUsuario", rol_id) VALUES (3, 'institucion@gmail.com', 'Quilicura', 1, 1, null);
INSERT INTO public.core_usuario ("idUsuario_id", correo, "comunaUsuario", rol_id) VALUES (4, 'administrador@gmail.com', 'Ovalle', 2, 1, null);

INSERT INTO public.core_parametros VALUES (2, true, 1000000, true, 7, true, 900, 'Ingenieria informatica', true, true, false, true, true, true);

INSERT INTO public.core_institucion VALUES (2, 'Universidad de chile', 'Santiago', true, true, 7, 3, 'https://uchile.cl', 'default_insti.png', 'Universidad', 1, null);
INSERT INTO public.core_institucion VALUES (1, 'Duoc', 'Huechuraba', false, true, 7, 3, 'https://www.duoc.cl', 'default_insti.png', 'IP', 1, null);
INSERT INTO public.core_institucion VALUES (3, 'Colo colo', 'Renca', true, false, 0, 3, 'https://www.colocolo.cl', 'default_insti.png', 'Universidad', 1, null);
INSERT INTO public.core_institucion VALUES (4, 'Universidad San Sebastian', 'El centro', true, false, 2, 3, 'https://www.uss.cl', 'default_insti.png', 'Universidad', 1, null);
INSERT INTO public.core_institucion VALUES (5, 'Inacap', 'Providencia', false, true, 1, 3, 'https://portal.inacap.cl', 'default_insti.png', 'IP'), 1, null;
INSERT INTO public.core_institucion VALUES (6, 'Universidad catolica', 'Recoleta', true, false, 3, 3, 'https://www.uc.cl', 'default_insti.png', 'CFT', 1, null);
INSERT INTO public.core_institucion VALUES (7, 'Universidad Santo Tomas', 'Quilicura', true, true, 4, 3, 'https://www.ust.cl', 'default_insti.png', 'Universidad', 1, null);
INSERT INTO public.core_institucion VALUES (8, 'Universidad tecnica Federico Santa Maria', 'Huechuraba', true, false, 6, 3, 'https://usm.cl', 'default_insti.png', 'Universidad', 1, null);


INSERT INTO public.core_carrera VALUES (3, 'Ingenieria en redes', 500, 2, 2000000, 1, null);
INSERT INTO public.core_carrera VALUES (6, 'Ingenieria en redes', 600, 3, 4000000, 1, null);
INSERT INTO public.core_carrera VALUES (7, 'Ingenieria en redes', 700, 4, 6000000, 1, null);
INSERT INTO public.core_carrera VALUES (8, 'Ingenieria en redes', 800, 5, 8000000, 1, null);

INSERT INTO public.core_carrera VALUES (4, 'Ingenieria en artes', 900, 2, 3000000, 1, null);
INSERT INTO public.core_carrera VALUES (9, 'Ingenieria en artes', 1000, 8, 1000000, 1, null);
INSERT INTO public.core_carrera VALUES (10, 'Ingenieria en artes', 200, 7, 400000, 1, null);
INSERT INTO public.core_carrera VALUES (11, 'Ingenieria en artes', 400, 6, 4000000, 1, null);

INSERT INTO public.core_carrera VALUES (5, 'Ingenieria en ingenio', 100, 1, 200000, 1, null);
INSERT INTO public.core_carrera VALUES (1, 'Ingenieria informatica', 200, 1, 545452545, 1, null);

INSERT INTO public.core_peticiones VALUES (5, 'ola ola ola', 'Problema', ' He encontrado un problema', '2025-09-26 17:50:34.244684-03', 3, 'Revisada');