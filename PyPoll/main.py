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
        
        tot_vote_cand1 = len(vote_cand1)
        tot_vote_cand2 = len(vote_cand2)
        tot_vote_cand3 = len(vote_cand3)

        pct_vote_cand1 = round(((tot_vote_cand1/tot_votes)*100), 3)
        pct_vote_cand2 = round(((tot_vote_cand2/tot_votes)*100), 3)
        pct_vote_cand3 = round(((tot_vote_cand3/tot_votes)*100), 3)

        print(candidate1 + ': ' + str(pct_vote_cand1) + '% ' + '(' + str(tot_vote_cand1) + ')')
        print(candidate2 + ': ' + str(pct_vote_cand2) + '% ' + '(' + str(tot_vote_cand2) + ')')
        print(candidate3 + ': ' + str(pct_vote_cand3) + '% ' + '(' + str(tot_vote_cand3) + ')')
        print(f'--------------------------')

        file.write(candidate1 + ': ' + str(pct_vote_cand1) + '% ' + '(' + str(tot_vote_cand1) + ')' + '\n')
        file.write(candidate2 + ': ' + str(pct_vote_cand2) + '% ' + '(' + str(tot_vote_cand2) + ')' + '\n')
        file.write(candidate3 + ': ' + str(pct_vote_cand3) + '% ' + '(' + str(tot_vote_cand3) + ')' + '\n')
        file.write(f'-------------------------- \n')


    with open(filepath, 'r') as csvfile:
        poll_csv = csv.reader(csvfile, delimiter = ',')
        
        pop_vote_winr = {
            tot_vote_cand1 : candidate1,
            tot_vote_cand2 : candidate2,
            tot_vote_cand3 : candidate3,
            }

        for key, value in pop_vote_winr.items():
            if int(key) > int(key):
                print({value})
       





      
       
                

            
            
        
        
        


        

