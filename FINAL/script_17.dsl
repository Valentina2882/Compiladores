load "ventas.csv";
filter column "id_venta" <= 32168;
filter column "id_venta" == 47116;
filter column "precio_total" == 123208;
aggregate sum column "precio_total";
print;