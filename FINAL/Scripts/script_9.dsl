load "ventas.csv";
filter column "precio_total" >= 10000 and column "precio_total" <= 100000;
aggregate sum column "precio_total";
aggregate average column "precio_total";
aggregate count column "cantidad";
print;

//Filtra por precio_total entre 10.000 y 100.000, luego 
//calcula suma y promedio de precio_total, y count de cantidad.