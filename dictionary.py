#diction是一个列表，把每一个羁绊的各属性都单独放在一个字典中
import shiki as sk

#将所有羁绊组合的属性放入一个字典中，并将所有羁绊组合的字典放入一个列表中
"""羁绊组合字典属性说明
    namet:
"""
#diction是一个列表，把各属性key和各羁绊的对应属性值value放在一个字典中，其中value属性值也是一个列表
diction = [
    {'namet':['tram1','tram2','tram3','tram4','tram5','tram6','tram7''tram8',
                      'tram9','tram10','tram11','tram12','tram13','tram14','tram15','tram16']},
    {'tram_per':[{'樱花妖','桃花妖'},{'酒吞童子','茨木童子'},{'山兔','孟婆'},{'鬼使黑','鬼使白'},
                       {'镰鼬','铁鼠'},{'少羽大天狗','大天狗'},{'鬼使黑','鬼使白','阎魔'},{'白狼','妖刀姬','萤草'},
                       {'白狼','妖刀姬'},{'傀儡师','阎魔'},{'独眼小僧','蝴蝶精'},
                       {'天邪鬼黄','天邪鬼赤','天邪鬼青','天邪鬼绿'},{'大天狗','雪女'},{'萤草','白狼'},{'九命猫','犬神'},
                       {'蝴蝶精','巫蛊师'}]},
    {'person':[2,2,2,2,2,2,3,3,2,2,2,4,2,2,2,2]},
    {'level':[2,4,2,2,2,4,3,4,3,3,2,2,3,2,2,2]},
    {'name':['whereisspring','drinkthewine','runningfrogandpan','whiteandblack','repeathappily','fromthesky',
             'bosspleasesay','girlshouldbestrong','girlgroup','onedaytravelatthree','Icanchant','F4','FORjustice',
             'myidol','catordog','monstercatchingbutterfly']}
            ]

shiki_all = sk.Shiki({'白狼','茨木童子','大天狗','独眼小僧','鬼使白','鬼使黑','蝴蝶精','九命猫','酒吞童子','傀儡师',
             '镰鼬','孟婆','犬神','山兔','少羽大天狗','桃花妖','天邪鬼赤','天邪鬼黄','天邪鬼绿','天邪鬼青',
             '铁鼠','巫蛊师','雪女','阎魔','妖刀姬','樱花妖','萤草'})

