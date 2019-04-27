import pandas as pd
from sklearn.preprocessing import Imputer
import sklearn.preprocessing
dataorig = pd.read_csv("/Users/segerard/src/SOM/src/data/SongCSV.csv")
hd = dataorig.columns
feats = hd[0:-5]
labels = hd[-5:]
data = dataorig[feats]
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(data)
trans = imp.transform(data)

min_max_scaler = sklearn.preprocessing.MinMaxScaler()
transscale = min_max_scaler.fit_transform(trans)

transdf = pd.DataFrame(transscale)
labelsdf = dataorig[labels]
finaldf = pd.concat([transdf,labelsdf],axis=1)
finaldf.columns = hd
finaldf.to_csv('Song.csv',index=False,sep=',')

#transdf.columns = feats
#labelsdf.columns = labels
transdf.to_csv('Features.txt',index=False,header=False,columns=None,sep=' ')
labelsdf.to_csv('Labels.txt',index=False,header=False,columns=None,sep=' ')

