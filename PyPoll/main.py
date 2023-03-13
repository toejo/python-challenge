import os, csv

filepath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#To create and write into a text file
with open(os.path.join('PyPoll/Analysis', 'main.txt'), 'w') as file:

    file.write(f'Election Results \n')
    print('Election Results')

    file.write(f'-------------------------- \n')
    print(f'--------------------------')


    #def  


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
    
        for row in poll_csv:

            cand.append(row[2])
        
        candids = set(cand)
        candidates = list(candids)

        candidate1 = (candidates[0])
        candidate2 = (candidates[1])
        candidate3 = (candidates[2])

    with open(filepath, 'r') as csvfile:
        poll_csv = csv.reader(csvfile, delimiter = ',')
        
        next(poll_csv)

        vote_cand1 = []
        vote_cand2 = []
        vote_cand3 = []

        for row in poll_csv:

            if row[2] == candidate1:
                vote_cand1.append(row[0])
            elif row[2] == candidate2:
                vote_cand2.append(row[0])
            else:
                vote_cand3.append(row[0])
        
        

        print(candidate1 + ':' )
        print(candidate2 + ':')
        print(candidate3 + ':')
        print(f'--------------------------')




      
       
                

            
            
        
        
        


        

