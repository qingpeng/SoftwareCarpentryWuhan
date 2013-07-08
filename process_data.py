#!/usr/bin/env python


  #MONTH       DAY      YEAR      HOUR  AVG TEMP  
  #                                 CST        ?C  
  #     1         1      2007       100      -0.4  
  #     1         1      2007       200      -0.6  
  #     1         1      2007       300      -0.6  
  #     1         1      2007       400      -0.3  
  #     1         1      2007       500       0.0  
  #     1         1      2007       600       0.4  
  #     1         1      2007       700       0.4  
  #     1         1      2007       800      -0.2  
  #     1         1      2007       900      -0.3  
  #     1         1      2007      1000       0.6  
  #     1         1      2007      1100       1.9  
  #     1         1      2007      1200       3.3  
  #     1         1      2007      1300       4.7  
  #     1         1      2007      1400       5.8
  
  
f_temp = open('temperature.txt','r')

  
# average high temp and low temp of every month

e = f_temp.readline()
e = f_temp.readline()
lines = f_temp.readlines()
ave_high_temp_list=[]
ave_low_temp_list = []


for i in range(1,13):
    sum_high_temp=0
    sum_low_temp = 0
    day = 0
    for line in lines:
        line=line.rstrip()
        fields = line.split()
        month = int(fields[0])
        hour = fields[3]
        temp = float(fields[4])
        if  month== i:
            if hour == "100":
                temps=[]
                temps.append(temp)
            elif hour == "2400":
                temps.append(temp)
                high_temp = max(temps)
                #print high_temp
                sum_high_temp = sum_high_temp + high_temp
                low_temp = min(temps)
                sum_low_temp = sum_low_temp + low_temp
                day=day+1
                
            else:
                temps.append(temp)
    ave_high_temp = sum_high_temp/day
    ave_low_temp = sum_low_temp/day
    ave_high_temp_list.append(ave_high_temp)
    ave_low_temp_list.append(ave_low_temp)


file_out = open('temp_result.txt','w')
file_out.write('Month\tHigh\tLow\n')
for i in range(12):
    month = i+1

    ave_high_temp = '%.3f' %(ave_high_temp_list[i])
    ave_low_temp = '%.3f' %(ave_low_temp_list[i])
    file_out.write(str(month)+'\t'+str(ave_high_temp)+'\t'+str(ave_low_temp)+'\n')
    



  #MONTH       DAY      YEAR      HOUR  AVG TEMP  
  #                                 CST        ?C  
  #     1         1      2007       100      -0.4  
  #     1         1      2007       200      -0.6  
  #     1         1      2007       300      -0.6  
  #     1         1      2007       400      -0.3  

  
  
f_temp = open('temperature.txt','r')
f_solar = open('solar_radiation.txt','r')
  
# average high temp and low temp of every month

e = f_temp.readline()
e = f_temp.readline()
temp_lines = f_temp.readlines()

e = f_solar.readline()
e = f_solar.readline()
e = f_solar.readline()
e = f_solar.readline()
solar_lines = f_solar.readlines()


ave_temp_list=[]

for h in range(1,25):
    h = h*100
    sum_temp = 0
    day = 0
    for line in temp_lines:
        line=line.rstrip()
        fields = line.split()
        month = int(fields[0])
        hour = int(fields[3])
        temp = float(fields[4])
        if  month== 6 and  hour == h:
            sum_temp = sum_temp+temp
            day = day+1
    ave_temp = sum_temp/day
    ave_temp_list.append(ave_temp)

ave_solar_list = []
for h in range(1,25):
    h = h*100
    sum_solar = 0
    day = 0
    for line in solar_lines:
        line=line.rstrip()
        fields = line.split()
        month = int(fields[0])
        hour = int(fields[3])
        solar = float(fields[4])
        if  month== 6 and  hour == h:
            sum_solar = sum_solar+solar
            day = day+1
    ave_solar = sum_solar/day
    ave_solar_list.append(ave_solar)


file_out = open('temp_solar_result.txt','w')
file_out.write('Hour\tTemp\tSolar\n')

for i in range(24):
    hour = i+1
    
    ave_temp = '%.3f' %(ave_temp_list[i])
    ave_solar = '%.3f' %(ave_solar_list[i])
    file_out.write(str(hour)+'\t'+str(ave_temp)+'\t'+str(ave_solar)+'\n')









