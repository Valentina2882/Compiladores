load "ventas.csv";
filter column "cantidad" > 111775;
filter column "id_venta" == 31046;
aggregate sum column "cantidad";
aggregate sum column "id_venta";
aggregate average column "precio_total";
print;