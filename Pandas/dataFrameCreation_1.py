import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Emily', 'Michael', 'David' ],
    'Age': [29, 35, 30, 25, 40, 32, 38],
    'City': ['New York', 'Los Angeles', 'Paris', 'Tokyo', 'Berlin', 'London', 'Madrid' ]
}

df = pd.DataFrame(data)
print(df.head(20))    

