load "ventas.csv";
filter column "id_cliente" != 22;
filter column "precio_total" == 146431;
aggregate count column "cantidad";
aggregate sum column "cantidad";
aggregate average column "precio_total";
print;