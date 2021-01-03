def process_dataframe(df):
    df['Date'] = df['Date_of_Journey'].str.split('/').str[0]
    df['Month'] = df['Date_of_Journey'].str.split('/').str[1]
    df['Year'] = df['Date_of_Journey'].str.split('/').str[2]
    
    df['Date'] = df['Date'].astype(int)
    df['Month'] = df['Month'].astype(int)
    df['Year'] = df['Year'].astype(int)
    
    df = df.drop(['Date_of_Journey'],axis=1)
    
    df['Arrival_Time']=df['Arrival_Time'].str.split(' ').str[0]
    
    df['Total_Stops'] = df['Total_Stops'].fillna('1 stop')
    df['Total_Stops'] = df['Total_Stops'].replace('non-stop','0 stop')
    df['Stop'] = df['Total_Stops'].str.split(' ').str[0]
    df['Stop'] = df['Stop'].astype(int)
    df = df.drop(['Total_Stops'],axis=1)
    
    df['Arrival_Hour'] = df['Arrival_Time'] .str.split(':').str[0]
    df['Arrival_Minute'] = df['Arrival_Time'] .str.split(':').str[1]
    df['Arrival_Hour'] = df['Arrival_Hour'].astype(int)
    df['Arrival_Minute'] = df['Arrival_Minute'].astype(int)
    df = df.drop(['Arrival_Time'], axis=1)
    
    df['Departure_Hour'] = df['Dep_Time'] .str.split(':').str[0]
    df['Departure_Minute'] = df['Dep_Time'] .str.split(':').str[1]
    df['Departure_Hour']=df['Departure_Hour'].astype(int)
    df['Departure_Minute']=df['Departure_Minute'].astype(int)
    df=df.drop(['Dep_Time'],axis=1)
    
    df['Route_1']=df['Route'].str.split('→ ').str[0]
    df['Route_2']=df['Route'].str.split('→ ').str[1]
    df['Route_3']=df['Route'].str.split('→ ').str[2]
    df['Route_4']=df['Route'].str.split('→ ').str[3]
    df['Route_5']=df['Route'].str.split('→ ').str[4]
    df['Route_1'].fillna("None",inplace=True)
    df['Route_2'].fillna("None",inplace=True)
    df['Route_3'].fillna("None",inplace=True)
    df['Route_4'].fillna("None",inplace=True)
    df['Route_5'].fillna("None",inplace=True)
    df=df.drop(['Route'],axis=1)
    
    # df['Price'].fillna((df['Price'].mean()),inplace=True)
    
    df=df.drop(['Duration'],axis=1)
    
    # Encoding of data
    from sklearn.preprocessing import LabelEncoder
    encoder=LabelEncoder()
    df["Airline"]=encoder.fit_transform(df['Airline'])
    df["Source"]=encoder.fit_transform(df['Source'])
    df["Destination"]=encoder.fit_transform(df['Destination'])
    df["Additional_Info"]=encoder.fit_transform(df['Additional_Info'])
    df["Route_1"]=encoder.fit_transform(df['Route_1'])
    df["Route_2"]=encoder.fit_transform(df['Route_2'])
    df["Route_3"]=encoder.fit_transform(df['Route_3'])
    df["Route_4"]=encoder.fit_transform(df['Route_4'])
    df["Route_5"]=encoder.fit_transform(df['Route_5'])

    return df