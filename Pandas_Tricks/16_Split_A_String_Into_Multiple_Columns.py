import pandas as pd

df = pd.DataFrame({'name':['John Arthur Doe', 'Jane Ann Smith'],
				   'location':['Los Angeles, CA', 'Washington, DC']})

print(df)

#               name         location
# 0  John Arthur Doe  Los Angeles, CA
# 1   Jane Ann Smith   Washington, DC

print(df.name.str.split(' ', expand = True))

#       0       1      2
# 0  John  Arthur    Doe
# 1  Jane     Ann  Smith

df[['first','middle','last']] = df.name.str.split(' ', expand=True)
print(df)
# 		name         		location  first  middle   last
# 0  John Arthur Doe  Los Angeles, CA  John  Arthur    Doe
# 1   Jane Ann Smith   Washington, DC  Jane     Ann  Smith

df['city'] = df.location.str.split(',', expand=True)[0]
print(df)
#               name         location first  middle   last        city
# 0  John Arthur Doe  Los Angeles, CA  John  Arthur    Doe  Los Angeles           
# 1   Jane Ann Smith   Washington, DC  Jane     Ann  Smith   Washington