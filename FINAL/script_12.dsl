load "ventas.csv";
filter column "precio_total" < 505;
filter column "id_cliente" > 28373;
aggregate sum column "precio_total";
aggregate count column "precio_total";
aggregate average column "precio_total";
print;