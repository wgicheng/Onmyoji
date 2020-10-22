import dictionary as dic
import re



#判断input的内容是不是为N或n，即对方不愿意继续分享其拥有的式神名称
def check_go_on(shiki):
    Out = False
    if shiki == 'N' or shiki == 'n':
        Out = True
    return Out

#对输入内容进行处理，确认其符合要求
def check_list(shiki):
    #将输入内容中所有非中文部分都替换为','
    mark = re.compile(r'[^\u4e00-\u9fa5]')
    a = re.sub(mark, ',', shiki)
    #根据分隔符',',对输入内容进行分隔去重
    shiki = list(set(a.split(',')))
    #对输入内容的每一个文字内容进行判定，确认其是否为式神录中的式神名称。
    for a in shiki.copy():
        #如是，继续判断下一个；
        if {a}.issubset(dic.shiki_all.type):
            continue
        #如不是，删掉该部分。
        else:
            shiki.remove(a)
    #返回处理过的输入内容，当前内容应不包含任何不存在于式神录的文字及符号
    return shiki

#
def input_shiki(shiki,shiki_you):
    #将输入的式神列表改为集合，方便进行判定和去重
    shiki = {i for i in list(check_list(shiki))}
    #将输入的式神列表放入使用者的式神录中
    shiki_you.type.update(shiki)
    return

#获取使用者式神可组成的所有羁绊，并保存羁绊在字典中的位置至变量loc
def get_dic(shiki_you):
    #确认使用者式神录是否能够组成diction中的羁绊
    for i in dic.diction[1]['tram_per']:
        #如果使用者式神录存在可组成羁绊的式神，保存该羁绊在字典中的指针
        #因为该指针可便于获取该羁绊在diction其他字典中的对应值
        if i.issubset(shiki_you.type):
            shiki_you.loc.append(dic.diction[1]['tram_per'].index(i))
    return shiki_you


#记录羁绊组合的各项属性值
def comp_buff_assign(shiki_you,type_shiki,buff,memberc):
    shiki_you.total['pers'].append(len(type_shiki))
    shiki_you.total['team'].append(type_shiki)
    shiki_you.total['level'].append(buff)
    shiki_you.total['usecomb'].append(memberc)
    return


#对每个羁绊组合的占用人数，增强buff等相关信息都进行获取和录入
def comp_buff(shiki_you,n):
    #对于每一个羁绊组合都进行计算
    for i in shiki_you.total['comb']:
        buff = 0
        type_shiki = set(())
        memberc = []
        #当羁绊的组合方式为空，可对各项属性值进行初始定义
        if len(i) == 0:
            comp_buff_assign(shiki_you, type_shiki, buff, memberc)
            continue
        #每个羁绊组合进行x（拥有羁绊数量）次的重复，以计算每种羁绊组合的属性
        for x in range(len(i)):
            # y用于获取羁绊组合在diction中的所处位置
            y = int(i[x])
            # type_shiki用于获取羁绊组合要占用的人数，并自动去重
            # memberc是获取使用到的羁绊，buff为增强buff的数值
            type_shiki.update(dic.diction[1]['tram_per'][y])
            memberc.append(dic.diction[1]['tram_per'][y])
            buff += dic.diction[3]['level'][y]
        #记录羁绊组合占用人数不大于设定的羁绊组合
        if len(type_shiki) <= n:
            comp_buff_assign(shiki_you, type_shiki, buff, memberc)
    return shiki_you


#输出可组成的增强buff最大的羁绊组合信息
def print_best(shiki_you,best):
    print('\n根据您现有的式神，当前可获得最大增强buff的羁绊组合信息如下：')
    print('最大Buff值:', shiki_you.best_max)
    print('组合占用人数:', len(shiki_you.best))
    print('使用到的羁绊:', shiki_you.total['usecomb'][best])
    print('使用到的式神:',shiki_you.best)

    print('\nBases on your shikis, we can provide below group details which can make you get maximum benefit：')
    print('Buff Level:', shiki_you.best_max)
    print('Number of Shiki:', len(shiki_you.best))
    print('Combination Used:', shiki_you.total['usecomb'][best])
    print('Shiki Used:',shiki_you.best)


# 对每个羁绊组合的增强buff进行比较，获得buff最大值的羁绊组合，保存在使用者的变量best,best_max中
def compare_buff(shiki_you):
    best=0
    # 开始对每组的数据进行比较,先设定一个保存最大值的变量
    shiki_you.best_max = shiki_you.total['level'][0]
    # shiki_you.total = {羁绊组合'comb':shiki_you.comb,
    # 占用人数'pers':[],'team':[],增强等级'level':[],'usecomb':[]}
    for i in range(len(shiki_you.total['level'])):
        if shiki_you.best_max < shiki_you.total['level'][i]:
            shiki_you.best_max = shiki_you.total['level'][i]
            shiki_you.best = shiki_you.total['team'][i]
            best = i
    print_best(shiki_you,best)
    return shiki_you


#通过计算获得可组成的最大增强buff的羁绊组合
def get_max_buff(shiki_you,n=8):
    # 获取使用者式神可组成的所有羁绊，并保存羁绊在字典中的位置至变量loc
    get_dic(shiki_you)

    # 将可组成的所有羁绊进行自由组合，并定义部分初始变量并保存相关信息在total字典中。
    """
    comb保存自由组合成的羁绊组合（在字典中的位置）
    pers保存每种羁绊组合的占用人数
    team保存每种羁绊组合所使用到的式神
    level保存每种羁绊组合可获得的buff增强值
    usecomb保存每种羁绊组合所使用到的羁绊
    """
    shiki_you.total = {'comb': shiki_you.combine(), 'pers': [], 'team': [], 'level': [], 'usecomb': []}

    # 对每个羁绊组合的占用人数，增强buff等相关信息都进行获取和录入
    comp_buff(shiki_you,n)

    # 对每个羁绊组合的增强buff进行比较，获得buff最大值的羁绊组合，输出并保存在使用者的变量best,best_max中
    compare_buff(shiki_you)