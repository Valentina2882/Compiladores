load "ventas.csv";
filter column "id_venta" == 124943;
aggregate average column "cantidad";
print;