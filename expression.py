from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.naive_bayes
import GaussianNB

class Expression:
    def __init__(self):
        self.Train()
    def Train(self):
        ls = [] #Lista de angulos happy
        lh = [] #Lista de angulos sad
        filepath = 'foto_happy_angles.txt'  
        with open(filepath) as fp:  #Lendo o arquivo texto dos angulos e guardando na lista
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
        array = np.zeros((nh + ns,6)) #Criando um array vazio com as listas de angulos
        while i <= (ns+nh-1): #Preenchendo o array 
            array[i] = ls[x:x+6]
            x+=6
            i+=1
            while (i > ns-1) and (i <= (ns+nh-1)):
                array[i] = lh[y:y+6]
                i+=1
                y+=6
        dados = pd.DataFrame(data=array) #Criando o dataframe com o array
        X = dados.iloc[:,[0,1,2,3,4]]
        y = np.ravel(dados.iloc[:,[5]])
        dados = dados.sample(frac=1).reset_index(drop=True) #shuffle dataframe
        X_train = dados.iloc[:,[0,1,2,3,4]] #Pegando os angulos como entrada para o treinamento
        y_train = np.ravel(dados.iloc[:,[5]]) #A saida do treinamento diz se a foto é "happy" ou "sad"
        model = GaussianNB()
        return model.fit(X_train, y_train) #Salva o treinamento
        
    def Predict(angle_array):
        dados = pd.DataFrame(data=angle_array)
        X_pred = dados.iloc[:,[0,1,2,3,4]] #Pegando os angulos do frame como entrada para o treinamento
        y_pred = model.predict(X_pred) #Prevendo a saída
        return y_pred 