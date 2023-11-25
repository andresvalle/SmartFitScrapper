#!/usr/bin/python
import numpy as np

defaultFile = "/home/andres/workshop/smartFitData/analysis/results/attendanceMix.tsv"
inputHandle = defaultFile
#inputHandle = input('Enter the file name: ') or defaultFile

#dailyData = { 1: [], 2: [], 3: [], 4: [], 5: [] }
textoSemana = [ "Lunes", "Martes", "Miércoles", "Jueves", "Viernes" ]
dailyData = {n: [] for n in range(1,6)}
weeklyData = {n: [] for n in range(1,154)}

with open(inputHandle) as file: 
    for line in file:
        dailyData[int(line.rstrip().split()[1])].append( int(line.rstrip().split()[2]) )
        weeklyData[int(line.rstrip().split()[3])].append( int(line.rstrip().split()[2]) )

#Daily
with open("dayOfTheWeek.tsv", "w") as file: 
    file.write("# Día de la Semana \t Promedio \t Error\n")
    for key in dailyData:
        media = np.mean( np.array( dailyData[key] ) )
        error = np.std( np.array( dailyData[key] ) ) / np.sqrt( len(dailyData[key]) )
        if len(dailyData[key]) == 1:
            error = np.sqrt( dailyData[key][0] )
        else:
            error = np.std( np.array( dailyData[key] ) ) / np.sqrt( len(dailyData[key]) )
        file.write( str(key)+"\t"+textoSemana[key-1]+"\t"+str(media)+"\t"+str(error)+"\n" )

#Weekly
with open("weekly.tsv", "w") as file: 
    file.write("# Semana (1-53) \t Promedio \t Error\n")
    for key in weeklyData:
        if weeklyData[key]:
            media = np.mean( np.array( weeklyData[key] ) )
            if len(weeklyData[key]) == 1:
                error = np.sqrt( weeklyData[key][0] )
            else:
                error = np.std( np.array( weeklyData[key] ) ) / np.sqrt( len(weeklyData[key]) )
            file.write( str(key)+"\t"+str(media)+"\t"+str(error)+"\n" )
