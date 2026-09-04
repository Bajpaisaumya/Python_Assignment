'''Scenario: You are organizing a movie marathon. You start with a playlist: ["Inception", "The Matrix", "Interstellar"]. Prompt the user to enter the name of a movie they want to add.

If the movie is already in the list, print "Already added!" and do not insert it.
If it is not in the list, append it to the end of the list. Finally, sort the movie list alphabetically and print the updated playlist.
Sample Input: "Interstellar"
Sample Output:
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
'''
def movie_night_playlist():
    list=["Inception", "The Matrix", "Interstellar"]
    
    str=input("Enter your recommended movie:").title()
    if str in list:
            print("Already added")
            
    else:
        list.append(str)

    updated_list=sorted(list)
    print(f"Alphabetical Playlist: {updated_list}")
movie_night_playlist()
    

