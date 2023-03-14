import os, csv

filepath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#To create and write into a text file
with open(os.path.join('PyPoll/Analysis', 'main.txt'), 'w') as file:

    file.write(f'Election Results \n') # printing into terminal, write into the text file the header
    print('Election Results')

    file.write(f'-------------------------- \n')
    print(f'--------------------------')

    #Lines 15-30 are for retrieving "Total Votes", printing it into the terminal, as well as writing into PyPoll's main.txt
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

    #to get the unique values in the 'Candidates" column of the election_data.csv, I thought to turn row[2] into a dictionary, then into a set, and finally into a list so that I can assign the unique values to individual variables
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

    #I wwanted to use the candidates (unique values from row[2]) in conditional statements to count votes under their name, and append them into their own lists to be able to perform calculations
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

        #printing into terminal
        print(candidate1 + ': ' + str(pct_vote_cand1) + '% ' + '(' + str(tot_vote_cand1) + ')')
        print(candidate2 + ': ' + str(pct_vote_cand2) + '% ' + '(' + str(tot_vote_cand2) + ')')
        print(candidate3 + ': ' + str(pct_vote_cand3) + '% ' + '(' + str(tot_vote_cand3) + ')')
        print(f'--------------------------')

        #writing into text file
        file.write(candidate1 + ': ' + str(pct_vote_cand1) + '% ' + '(' + str(tot_vote_cand1) + ')' + '\n')
        file.write(candidate2 + ': ' + str(pct_vote_cand2) + '% ' + '(' + str(tot_vote_cand2) + ')' + '\n')
        file.write(candidate3 + ': ' + str(pct_vote_cand3) + '% ' + '(' + str(tot_vote_cand3) + ')' + '\n')
        file.write(f'-------------------------- \n')

    #I wanted to reuse the values that I got from the previous 'with open()' to make a dictionary of the candidates as 'value' and total votes as 'key'
    with open(filepath, 'r') as csvfile:
        poll_csv = csv.reader(csvfile, delimiter = ',')
        
        pop_vote= {
            tot_vote_cand1 : candidate1,
            tot_vote_cand2 : candidate2,
            tot_vote_cand3 : candidate3,
            }
        
        #all that is left is to go through the keys in the dictionary with conditionals to find the greatest/highest key/total votes and "get" the value/candidate attached to that key
        pop_vote_winr = 0
        for key in sorted(pop_vote.keys()):
            if key > pop_vote_winr:
                pop_vote_winr = key
        
        #finish off the work by printing into terminal, and writing into the text file.
        print(f'Winner: {pop_vote.get(pop_vote_winr)}')
        print(f'--------------------------')
        file.write(f'Winner: {pop_vote.get(pop_vote_winr)} \n')
        file.write(f'-------------------------- \n')



        



        
       





      
       
                

            
            
        
        
        


        

