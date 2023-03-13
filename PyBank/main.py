#import the modules
import os
import csv

#set the path
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#declare variables ahead
months = []
months2 = []
proflos = []
proflos_change = []

#create and write into a text file in the "Analysis" folder
with open(os.path.join("PyBank/Analysis", "main.txt"), 'w') as file:
    
    #lines 18-22 are for setting the header, and for printing into terminal and writing into 'main.txt'
    file.write(f'Financial Analysis \n')
    print('Financial Analysis')
    file.write(f'---------------------------------- \n')
    print('----------------------------------')

    #lines 22 - 41 are for finding total months and profit/loss total, then printing into terminal
    with open(budget_csv, 'r') as csvfile:
        budget_data = csv.reader(csvfile, delimiter = ',')
        
        next(budget_data) 

        for row in budget_data:
            months.append(row[0])
            proflos.append(int(row[1]))
        
        tot_months = len(months)
        #print(tot_months) --> to check

        tot_proflos = sum(proflos)
        #print(tot_proflos) --> to check
    
        print('Total Months: ' + str(tot_months))
        print('Total: $' + str(tot_proflos))
    
    ##
    file.write(f'Total Months: ' + str(tot_months) + '\n')

    file.write(f'Total: $' + str(tot_proflos) + '\n')
   

    with open(budget_csv, 'r') as csvfile:
        budget_data = csv.reader(csvfile, delimiter = ',')
        
        next(budget_data)  
        
        change = int(next(budget_data)[1])
        for row in budget_data:
            
            months2.append(row[0])   

            changes = int(row[1]) - change
            proflos_change.append(changes)

            change = int(row[1])

        ave_proflos_change = round((sum(proflos_change) / len(proflos_change)), 2)
        
        print('Average Change: $' + str((ave_proflos_change)))
        file.write(f'Average Change: $' + str(ave_proflos_change) + '\n') 
        
        gr_inc = max(proflos_change)
        #print(gr_inc)

        gr_dec = min(proflos_change)
        #print(gr_dec)

        gr_incdec = dict(zip(months2, proflos_change))

        
        for key, value in gr_incdec.items():
            if value == gr_inc:
                print(f'Greatest Increase in Profits: {key} (${value})')
                file.write(f'Greatest Increase in Profits: {key} (${value})' + '\n')
        #gr_inc_txt = (f'Greatest Increase in Profits: {key} (${value})')

        for key, value in gr_incdec.items():
            if value == gr_dec:
                print(f'Greatest Decrease in Profits: {key} (${value})')
                file.write(f'Greatest Decrease in Profits: {key} (${value})' + '\n')