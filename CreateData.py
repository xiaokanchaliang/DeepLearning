import numpy as np
import csv

dataCount = 1000

calcinationTemperature=np.random.randint(1100,1350,size=[dataCount,1])
transitionWarehouseTemperature=np.random.randint(600,1200,size=[dataCount,1])
dischargeTemperature=np.random.randint(30,120,size=[dataCount,1])
grayChamberInletPressure=np.random.randint(-45,-5,size=[dataCount,1])
secondWindSpeed=np.random.randint(400,1200,size=[dataCount,1])
rotaryKilnMotorSpeed=np.random.randint(650,1200,size=[dataCount,1])
hourFeedingAmount=np.random.randint(0,25,size=[dataCount,1])
kilnHeadTemperature=np.random.randint(500,1000,size=[dataCount,1])
kilnEndTemperature=np.random.randint(800,1300,size=[dataCount,1])
kilnHeadPressure=np.random.randint(-15,0,size=[dataCount,1])
kilnEndPressure=np.random.randint(-45,-5,size=[dataCount,1])
grayChamberInletTemperature=np.random.randint(650,1350,size=[dataCount,1])
grayChamberOutletTemperature=np.random.randint(650,1350,size=[dataCount,1])

prcessData=np.concatenate((calcinationTemperature,
                           transitionWarehouseTemperature,
                           dischargeTemperature,
                           grayChamberInletPressure,
                           secondWindSpeed,
                           rotaryKilnMotorSpeed,
                           hourFeedingAmount,
                           kilnHeadTemperature,
                           kilnEndTemperature,
                           kilnHeadPressure,
                           kilnEndPressure,
                           grayChamberInletTemperature,
                           grayChamberOutletTemperature), axis = 1)

processDataFile=open('processDataFile.csv','w',newline='')
csv_writer=csv.writer(processDataFile)
csv_writer.writerows(prcessData)