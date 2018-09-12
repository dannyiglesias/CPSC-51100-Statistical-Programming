print("CPSC-51100, Fall 1, 2018")
print("NAME: GROUP 9")
print("PROGRAMMING ASSIGNMENT #2")

#I will comment before writting the statement      

k = int(raw_input("Enter the number of clusters: "))
data=[float(x.rstrip()) for x in open("prog2-input-data.txt")]

#print(data)
centroids=dict(zip(range(k), data[0:k]))
clusters = dict(zip(range(k),[[] for i in range(k)]))

#print(centroids)
#print(clusters)

for key, value in centroids.iteritems():
    clusters[key].append(value)
   #print(clusters)

old_point_assignments={}
