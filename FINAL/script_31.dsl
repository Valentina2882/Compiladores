load "ventas.csv";
filter column "id_cliente" > 193753;
filter column "cantidad" != 92318;
aggregate sum column "cantidad";
aggregate count column "cantidad";
aggregate average column "cantidad";
print;