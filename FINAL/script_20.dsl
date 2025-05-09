load "ventas.csv";
filter column "precio_total" == 45359;
filter column "id_venta" == 63409;
aggregate count column "cantidad";
print;