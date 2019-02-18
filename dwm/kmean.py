from random import shuffle

data = [12,23,43,12,12,34,63,56,76,34,98,67,45]
print(data)
cluster_no = 4
shuffle(data)
print("Shuffling data .....")
print(data)
cluster_group = []
ind = 0
for cluster_grp_no in range((len(data)//cluster_no) +1):
    sub_grp = []
    for i in range(cluster_no):
        if ind >= len(data):
            break
        sub_grp.append(data[ind])
        ind += 1

    cluster_group.append(sub_grp)
    if ind >= len(data):
        break
means = []
d_mean =[]
means_list = []
for i in range(len(cluster_group)):
    means.append({sum(cluster_group[i])//len(cluster_group[i]):[]})
    means_list.append(sum(cluster_group[i])//len(cluster_group[i]))
# print(means)

d_mean =[]


def find_custor(means,d_mean):
    for i in data:
        for j in means:
            for mean in j.keys():
                d_mean.append(abs(i-mean))
        # print(d_mean)
        print(d_mean.index(min(d_mean)))

        for key,val in means[d_mean.index(min(d_mean))].items():
            val.append(i)
        # print(means[d_mean.index(min(d_mean))][d_mean.index(min(d_mean)).keys()].append(i))
        d_mean = []

for i in data:
    for j in means:
        for mean in j.keys():
            d_mean.append(abs(i-mean))
    # print("dddddddddd")
    # print(d_mean)
    # print(d_mean.index(min(d_mean)))

    for key,val in means[d_mean.index(min(d_mean))].items():
        val.append(i)
    # print(means[d_mean.index(min(d_mean))][d_mean.index(min(d_mean)).keys()].append(i))
    d_mean = []
print(means)

def till_same_mean(means,means_list,pmeans_list=None,pmeans=None,d_mean=[]):
    if pmeans_list !=None :
        if set(means_list) == set(pmeans_list):
            return means,means_list,pmeans_list,pmeans
        else :
            pmeans_list = means_list.copy()
            means_list =[]
            pmeans = means.copy()
            means = []
            for i in pmeans:
                for key,val in i.items():
                    # print(i)
                    means_list.append(sum(val)//len(val))
                    means.append({(sum(val)//len(val)):[]})
            print(means)
            for i in data:
                for j in means:
                    for mean in j.keys():
                        d_mean.append(abs(i-mean))
                    # print(d_mean.index(min(d_mean)))
                for key,val in means[d_mean.index(min(d_mean))].items():
                    val.append(i)
                d_mean = []
            print("means")
            print(means)
    else :
        pmeans_list = means_list.copy()
        means_list =[]
        pmeans = means.copy()
        means = []
        for i in pmeans:
            for key,val in i.items():
                # print(i)
                means_list.append(sum(val)//len(val))
                means.append({(sum(val)//len(val)):[]})
        # print(means)
        d_mean = []
        # print(d_mean)
        for i in data:
            for j in means:
                for mean in j.keys():
                    d_mean.append(abs(i-mean))
                # print(d_mean.index(min(d_mean)))
            for key,val in means[d_mean.index(min(d_mean))].items():
                val.append(i)
            d_mean = []
        print("means")
        print(means)
    return till_same_mean(means,means_list,pmeans_list,pmeans)
means,means_list,pmeans_list,pmeans =till_same_mean(means,means_list)
