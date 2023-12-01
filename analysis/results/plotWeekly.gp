set style data histograms
set yrange [750:1075]
set style histogram errorbars gap 2 lw 2
set errorbars fullwidth
set grid
set ylabel "Promedio de Asistencia"

set style fill solid 0.75 border lt -1

p 'weekly.tsv' u 2:3:xtic(1) lc 'orange' t ''

pause -1
