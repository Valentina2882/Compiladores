load "ventas.csv";
filter column "precio_total" < 38394;
aggregate average column "id_venta";
aggregate average column "id_venta";
aggregate count column "precio_total";
print;