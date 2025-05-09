load "ventas.csv";
filter column "id_venta" == 43406;
filter column "id_venta" != 22029;
aggregate sum column "id_venta";
print;