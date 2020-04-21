'''
统计成绩

从成绩单文件 report.txt（点击下载）中读取班级成绩，并完成统计分析。

姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理
小A 89 94 90 96 89 92 54 73 80
小B 92 37 93 43 67 77 82 84 89
小C 90 88 87 89 82 79 79 80 82
...

要求：

读取 report.txt 文件中的成绩；
统计每名学生总成绩、计算平均并从高到低重新排名；
汇总每一科目的平均分和总平均分（见下表第一行）；
添加名次，替换60分以下的成绩为“不及格”；
将处理后的成绩另存为一个新文件（result.txt）。
'''


with open('report.txt','r',encoding='utf-8') as f:
    lines=f.readlines()
    grades=[]
    for line in lines:
        line=line.split()
        grades.append(line)
    grades[0].append('总分')
    grades[0].append('平均分')
    grades[0].insert(0,'名次')

#添加每名学生的总分,平均分
for grade in grades[1:]:
    scores=0
    for i in grade[1:]:
        scores+=int(i)
    grade.append(str(scores))
    score_avg=round(scores/(len(grade)-2),1)
    grade.append(str(score_avg))

#排名
grades.sort(key=lambda x:x[-2],reverse=True)

#汇总每一科目的平均分和总平均分 
su_scores=[]
for j in range(1,len(grade)):
    su_sum=0
    for m in grades[1:]:
        su_sum+=float(m[j])
    su_avg=round(su_sum/(len(grades)-1),1)
    su_scores.append(str(su_avg))
su_scores.insert(0,'平均')    
su_scores.insert(0,'0')
grades.insert(1,su_scores)    

#添加名次，替换60分以下的成绩为“不及格”
rank=1
for r in grades[2:]:
    r.insert(0,str(rank))
    rank+=1
    for x in range(2,len(r)-1):        
        if int(r[x]) < 60:
            r[x]='不及格'
print(grades)

#写入文件
with open('result.txt','w',encoding='utf-8') as w:
    for ls in grades:
        for l in ls:
            w.write(l+' ')
        w.write('\n')