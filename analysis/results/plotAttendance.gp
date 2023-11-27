set format x "%d/%m"
#set timefmt '%s'
set timefmt '%Y-%m-%d'
set grid
set xdata time
set style fill solid border -1
set boxwidth 3600*24
set yrange [800:1100]
#set xtics 36

set ylabel "Asistencia"

p 'attendanceMix.tsv' u 1:3  w boxes lc 'orange' t 'Mix'
#p 'attendanceTikal.tsv' u 1:3  w boxes lc 'purple' t 'Tikal'
pause -1
