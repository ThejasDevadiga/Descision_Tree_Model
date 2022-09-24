class testing_model():
    def __init__(self,test_set, tree: dict):
        self.test_data = test_set
        self.tree = tree
        self.accuracy =0
    def predict(self):
        for row in self.test_data:
            prd = self.predictor(self.tree, row)
            # print("excepted : ", row[-1]  ," Got :", prd )
            if row[-1] ==prd:
                self.accuracy += 1
        self.accuracy = (self.accuracy/len(self.test_data))*100
    def predictor(self, node , row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self.predictor(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.predictor(node['right'], row)
            else:
                return node['right']      
    