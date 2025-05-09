load "ventas.csv";
filter column "cantidad" != 151374;
filter column "precio_total" == 157906;
filter column "precio_total" == 32234;
aggregate count column "id_venta";
print;