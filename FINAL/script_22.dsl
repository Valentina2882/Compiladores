load "ventas.csv";
filter column "id_cliente" > 127252;
aggregate average column "cantidad";
aggregate sum column "cantidad";
aggregate average column "id_venta";
print;