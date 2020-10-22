from itertools import combinations

class Shiki():
    #type是指拥有的式神，loc是指羁绊在diction2的位置，包括0，
    #comb是指各羁绊能组合成的组合，使用loc来表示羁绊所处位置
    #total是集合了羁绊组合，组合占用人数和增强buff的字典
    def __init__(self,type):
        self.type = type
        self.loc = []
        self.total = {}
        self.best_max = 0
        self.best = {}

    #获取所有羁绊可以组成的组合,请注意当i=1时，羁绊可组成的组合只有一个
    #而元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
    def combine(self):
        '''根据n获得列表中的所有可能组合（n个元素为一组）'''
        temp_list2 = []
        end_list = []
        for i in range(len(self.loc)):
            for c in combinations(self.loc,i):
                temp_list2.append(c)
                #print(i,c,len(c))
        temp_list2.append(tuple(self.loc))
        #temp_list2 = sorted(list(set(temp_list2)))
        return temp_list2

