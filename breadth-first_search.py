from collections import deque

"""
(ANUJ)                               (THOM)
        ^                                    ^
         \                                  /
          \                                /
         (BOB) <-------- (YOU) --------> (CLAIRE)
         /                 |                 \
        /                  |                  \
       v                   v                   v
    (PEGGY) <--------- (ALICE)              (JONNY)
"""

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# if a person's name ends with the letter 'm' they are a mango seller
def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque() # creates a new queue
    search_queue += graph[name]  # adds all of your neighbors to the search queue
    searched = [] # this array is how you keep track of which people you've searched before
    while search_queue: # while the queue isn't empty...
        person = search_queue.popleft() # ...grabs the first person off the queue
        if not person in searched: # only serch this person if you haven't already searched them
            if person_is_seller(person): # checks whether the person is a mango seller
                print(person + " is a mango seller!") # yes, they're a mango seller
                return True
            else:
                search_queue += graph[person] # no, they aren't; add all of this person's friends to the search queue
                searched.append(person) # marks this person as searched
    return False # if you reached here, no one in the queue was a mango seller
    
search("you")
