set style data histograms
set yrange [800:1050]
set style histogram errorbars gap 2 lw 2
set errorbars fullwidth
set grid
set ylabel "Promedio de Asistencia"

set style fill solid 0.75 border lt -1

p 'dayOfTheWeek.tsv' u 3:4:xtic(2) lc 'orange' t ''

pause -1
