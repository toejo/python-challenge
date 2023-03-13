import os, csv

filepath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#To create and write into a text file
with open(os.path.join('PyPoll/Analysis', 'main.txt'), 'w') as file:

    file.write(f'Election Results \n')
    print('Election Results')

    file.write(f'-------------------------- \n')
    print(f'--------------------------')



    #Lines 17-32 are for retrieving "Total Votes"
    with open(filepath, 'r') as csvfile:
        poll_csv = csv.reader(csvfile, delimiter = ',')

        next(poll_csv)

        votes = []

        for row in poll_csv:
            votes.append(row[0])
            #print(votes)

        tot_votes = len(votes)
        print(f'Total Votes: ' + str(tot_votes))
        print(f'--------------------------')
        file.write(f'Total Votes: ' + str(tot_votes) + '\n')
        file.write(f'-------------------------- \n')


    with open(filepath, 'r') as csvfile:
        poll_csv = csv.reader(csvfile, delimiter = ',')

        next(poll_csv)

        cand = []
        
        #for each row of the csv file...
        for row in poll_csv:

            #idea 1: if row, column 2 is not the same as row, column 2 then put that value
            #into the variable 'candidate'. we then build a list 'candidates' with the
            #different value.  
            # if row[2] != row[2]:
                
            #     candidate = row[2]

            #     candidates.append(candidate)

            #     candidate = " "

            #idea 2: make a list, turn into set, then find unique values
            cand.append(row[2])
            #print(len(cand)) -- returned the right value
            candidates = set(cand)
            print(candidates)
            
        
        
        


        

