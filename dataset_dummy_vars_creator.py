def CreateDummies(dataset, column):
    dummyVars= pd.get_dummies(dataset[column], prefix=column)
    dataset.drop([column], axis=1)
    dataset= pd.concat([dataset, dummyVars], axis=1)
    return dataset
