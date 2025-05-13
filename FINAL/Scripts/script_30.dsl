load "ventas.csv";
filter column "precio_total" < 60000;
aggregate count column "precio_total";
aggregate sum column "precio_total";
aggregate average column "precio_total";
print;

//Filtra por precio_total < 60000 y calcula count, 
//suma y promedio de ese valor.