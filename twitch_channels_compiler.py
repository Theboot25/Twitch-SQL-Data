import pandas as pd
import numpy as np
from pandas.compat import StringIO

#df = pd.read_csv('twitch_channels.log', sep = '\t', header = None, engine = 'python')
#df1 = pd.read_csv('twitch_channels.log.1', sep = '\t', header = None, engine = 'python')
#df2 = pd.read_csv('twitch_channels.log.2', sep = '\t', header = None, engine = 'python')
#df3 = pd.read_csv('twitch_channels.log.3', sep = '\t', header = None, engine = 'python')
#df4 = pd.read_csv('twitch_channels.log.4', sep = '\t', header = None, engine = 'python')
#df5 = pd.read_csv('twitch_channels.log.5', sep = '\t', header = None, engine = 'python')
#df6 = pd.read_csv('gap.twitch_channels.log', sep = '\t', header = None, engine = 'python')

df = pd.read_csv('game.json', sep = '\t', header = None, engine = 'python')
#df1 = pd.read_csv('total.json', sep = '\t', header = None, engine = 'python')

df.replace({' ': '\t'}, regex=True)


#df = df.append(df1)
#df = df.append(df2)
#df = df.append(df3)
#df4 = df.append(df4)
#df4 = df4.append(df5)
#df4 = df4.append(df6)

#df.columns = ['Time_Stamp', 'ID', 'Viewers', 'Game', 'Followers', 'Partner']
df.to_csv('game.json', sep='\t', index = False)


#f = open(, 'r')
#with open("twitch_channels_total.log", "w") as f1:
#	for line in f:
		#if "ROW" in line:
#		f1.write(line)