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