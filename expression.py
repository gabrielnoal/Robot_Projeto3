class Expression:
    def __init__(self):
        self.Train()
    def Train(self):
        ls = []
        lh = []
        filepath = 'foto_happy_angles.txt'  
        with open(filepath) as fp:  
           for cnt, line in enumerate(fp):
                if ("Imagens" not in line) and ("Foto" not in line):
                    parts = [p for p in line.split("\n")]
                    lh.append(parts[0])

        filepath = 'foto_sad_angles.txt'  
        with open(filepath) as fp:  
           for cnt, line in enumerate(fp):
                if ("Imagens" not in line) and ("Foto" not in line):
                    parts = [p for p in line.split("\n")]
                    ls.append(parts[0]) 
        x = 0
        y = 0
        i = 0
        ns = int(len(ls)/6)
        nh = int(len(lh)/6)
        array = np.zeros((nh + ns,6))
        while i <= (ns+nh-1):
            array[i] = ls[x:x+6]
            x+=6
            i+=1
            while (i > ns-1) and (i <= (ns+nh-1)):
                array[i] = lh[y:y+6]
                i+=1
                y+=6
        dados = pd.DataFrame(data=array)
        X = dados.iloc[:,[0,1,2,3,4]]
        y = np.ravel(dados.iloc[:,[5]])
        dados = dados.sample(frac=1).reset_index(drop=True) #shuffle dataframe
        n1 = int(0.8*dados.shape[0])
        X_train = dados.iloc[:n1,[0,1,2,3,4]]
        y_train = np.ravel(dados.iloc[:n1,[5]])
        model = GaussianNB()
        return model.fit(X_train, y_train)
        
    def Predict(angle_array):
        dados = pd.DataFrame(data=angle_array)
        X_pred = dados.iloc[:,[0,1,2,3,4]]
        y_pred = model.predict(X_pred)
        return y_pred