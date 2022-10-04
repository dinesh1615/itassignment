import pandas as ps

p=ps.DataFrame(
    {
    "Fruits":["Apple","Mangeo","Grapes"],
    "Animals":["Dog","Cat","Tiger"]
     },
     index=["a","b","c"]   
     )

print(p)