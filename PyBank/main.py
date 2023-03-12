import os
import csv

budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

months = []
months2 = []
proflos = []
proflos_change = []



with open(budget_csv, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter = ',')
    
    next(budget_data) 

    for row in budget_data:
        months.append(row[0])
        proflos.append(int(row[1]))
    
    tot_months = len(months)
    #print(tot_months)

    tot_proflos = sum(proflos)
    #print(tot_proflos)

    print('Financial Analysis')
    print('----------------------------------')
    print('Total Months: ' + str(tot_months))
    print('Total: $' + str(tot_proflos))
    
with open(budget_csv, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter = ',')
    
    next(budget_data)  
    
    change = 0
    for row in budget_data:
        
        months2.append(row[0])   

        changes = int(row[1]) - change
        proflos_change.append(changes)

        change = int(row[1])

    ave_proflos_change = sum(proflos_change) / len(proflos_change) 
    
    print('Average Change: $' + str(ave_proflos_change)) 
    
    gr_inc = max(proflos_change)
    #print(gr_inc)

    gr_dec = min(proflos_change)
    #print(gr_dec)

    gr_incdec = dict(zip(months2, proflos_change))

    
    for key, value in gr_incdec.items():
        if value == gr_inc:
            print(f'Greatest Increase in Profits: {key} (${value})')
    
    #gr_inc_txt = (f'Greatest Increase in Profits: {key} (${value})')

    for key, value in gr_incdec.items():
        if value == gr_dec:
            print(f'Greatest Decrease in Profits: {key} (${value})')



        

with open(os.path.join("PyBank/Analysis", "main.txt"), 'w') as file:
   
    file.write(f'Financial Analysis')

    file.write(f'----------------------------------')

    file.write(f'Total Months: ' + str(tot_months))

    file.write(f'Total: $' + str(tot_proflos))

    file.write(f'Average Change: $' + str(ave_proflos_change))

    file.write(f'Greatest Increase in Profits: {key} (${value})')

    file.write(f'Greatest Decrease in Profits: {key} (${value})')





            


   
    

    
  


        
        

    

        







# print("Greatest Increase in Profits")
    
