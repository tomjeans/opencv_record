import os
import copy
path_day = r'C:\Users\LKJ\Desktop\test'#E:\\7_12\\fileStore
room = os.listdir(path_day)

counts={}
words_table={}
inf_all_counts = {}
all_={}
for single in room:
    days=os.listdir(path_day+'\\'+single)
    inf_room_counts = {}
    inf_all_counts[single] = inf_room_counts
    for single_day in days:
        kinds=os.listdir(path_day+'\\'+single+'\\'+single_day)
        inf_day_counts = []
        for single_kind in kinds:
            inf_day_counts.append([single_kind,len(os.listdir(path_day+'\\'+single+'\\'+single_day+'\\'+single_kind))])
        inf_room_counts[single_day] = inf_day_counts
print(inf_all_counts)
for zhengshi in inf_all_counts:
    max = 0
    #print(zhengshi) #07 08
    for date in inf_all_counts[zhengshi]:
        #print(date)
        if len(inf_all_counts[zhengshi][date]) >= max:
            max = len(inf_all_counts[zhengshi][date])
            max_date = date
        #print(inf_all_counts[zhengshi][date])
        for s in inf_all_counts[zhengshi][date]:
            pass
    kinds = []       
    #print(max_date)
    for kind in inf_all_counts[zhengshi][max_date]:
        kinds.append(kind[0])
    print(kinds)
    for i,single_kind in enumerate(kinds):
        #print(i,single_kind)
        words_table[i]=single_kind
        locals()[single_kind] = 0
        for date_single in inf_all_counts[zhengshi]:
            for information in inf_all_counts[zhengshi][date_single]:
                if information[0] == single_kind:
                    exec('{} += {} '.format(single_kind,information[1]))
        
        exec('counts.update({}={})'.format(single_kind,single_kind))
    print('innn',counts)# per room counts
    k = copy.deepcopy(counts)
    all_[zhengshi]=k
    counts.clear()
    #print('ok')
    
print('all:',all_)
max_zhengshi = 0
zhengshi_kind = []
count_all={}
for zhengshi in all_:
    for kind in all_[zhengshi]:
        zhengshi_kind.append(kind)
print(zhengshi_kind)
kind_real=list(set(zhengshi_kind))
print(kind_real)
for i,kind in enumerate(kind_real):
    locals()[kind] = 0
    for zhengshi in all_:
        for kindd in all_[zhengshi]:
            if kindd == kind:
                exec('{} += {}'.format(kindd,all_[zhengshi][kindd]))
    exec('count_all.update({}={})'.format(kind,kind))
print('count_all',count_all)
        
        
    