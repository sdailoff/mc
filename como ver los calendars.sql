SELECT * FROM mc.schedule_schedule as SC
INNER JOIN mc.schedule_schedule_inicio as I ON SC.id = I.schedule_id
INNER JOIN mc.schedule_hourini H on H.id = I.hourini_id
INNER JOIN mc.usuarios_usuario U on U.id = SC.usuario1_id