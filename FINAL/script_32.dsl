load "ventas.csv";
filter column "precio_total" >= 84519;
aggregate sum column "precio_total";
aggregate count column "precio_total";
print;