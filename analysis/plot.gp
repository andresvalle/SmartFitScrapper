set format x "%d/%m %H:00"
set timefmt '%s'
#set timefmt '%Y-%m-%d %H:%M:%S'
set xdata time
set style fill solid border -1
set boxwidth 3000
set xtics 3600

set ylabel "Ingresos"

p 'pruned/mix_2022-07-15T19-41-33-0600.tsv' u ($2-6*3600):4  w boxes lc 'orange' t '15 de Julio'
pause -1
