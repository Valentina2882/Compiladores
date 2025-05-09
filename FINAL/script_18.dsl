load "ventas.csv";
filter column "id_venta" <= 168804;
aggregate count column "precio_total";
aggregate average column "cantidad";
aggregate sum column "id_venta";
print;