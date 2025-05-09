load "ventas.csv";
filter column "precio_total" == 168427;
aggregate sum column "cantidad";
aggregate average column "precio_total";
print;