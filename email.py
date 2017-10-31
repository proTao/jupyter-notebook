def splitMultiSender(data):
    # 输入data是直接读入的email.csv
    # 函数功能是把target中的多个联系人拆分开
    data.columns = ['id','target', 'source']
    target = data[['id','target']]
    group_by_id = target.groupby("id")["target"]
    target = group_by_id.apply(splt)
    print("group and apply done!")
    
    targetid = []
    for i in target.index:
        targetid.append(i[0])
    target.index = targetid
    target.columns =["target"]
    result = pd.merge(data[['id','source']], target, left_on="id", right_index=True)
    print("merge done!")
    return result


def splt(l):                   
    return pd.DataFrame(l.values[0].split(";"))
