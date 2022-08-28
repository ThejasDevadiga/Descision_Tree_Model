import pandas as pd
import numpy as np
class training_Model():
    def __init__(self, data , max_depth: int):
        self.data = data
        self.max_depth = max_depth
        self.root = {}
    def build_tree(self,show_tree: bool):
        root = self.get_split(self.data)
        self.split(root, self.max_depth, 1, 1)
        self.root = root
        if(show_tree):
            self.print_tree(self.root)
        return root
    def print_tree(self ,node, depth=0):
        if isinstance(node, dict):
            print('%s[X%d < %.3f]' % ((depth*' ' , (node['index']+1), node['value'])))
            self.print_tree(node['left'], depth+1)
            self.print_tree(node['right'], depth+1)
        else:
            print('%s[%s]' % ((depth*' ', node)))  
    
    def split(self , node, max_depth, min_size, depth):
        left, right = node['groups']
        del(node['groups'])
        if not left or not right:
            node['left'] = node['right'] = self.terminal_node(left + right)
            return
        if depth >= max_depth:
            node['left'], node['right'] = self.terminal_node(left), self.terminal_node(right)
            return     
        if len(left) <= min_size:
            node['left'] = self.terminal_node(left)
        else:
            node['left'] = self.get_split(left)
            self.split(node['left'], max_depth, min_size, depth+1)
        if len(right) <= min_size:
            node['right'] = self.terminal_node(right)
        else:
            node['right'] = self.get_split(right)
            self.split(node['right'], max_depth, min_size, depth+1)
   
    def terminal_node(self, group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)
    
    def get_split(self ,dataset):
        max = np.array(dataset).max()
        class_values = list(set(row[-1] for row in dataset))
        b_index, b_value, b_score, b_groups = max+100, max+100, max+100, None
        for index in range(len(dataset[0])-1):
            for row in dataset:
                groups = self.test_split(index, row[index], dataset)
                gini = self.gini_index(groups,class_values)
	    	      
                if gini < b_score:
        	         b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return {'index':b_index, 'value':b_value, 'groups':b_groups}
   
    def test_split(self,index, value, dataset):
        left, right = list(), list()
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right
	
    def gini_index(self,groups, classes):
        n_instances = float(sum([len(group) for group in groups]))
        gini = 0.0
        for group in groups:
            size = float(len(group))
            if size == 0:
                continue
            score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
        return gini
        
 
	
