#NAME: Group 9 
#September 16
#CPSC-51100, Fall 2018
#PROGRAMMING ASSIGNMENT #2

def main():
    """ Main function """

    print("CPSC-51100, Fall 1, 2018")
    print("NAME: GROUP 9")
    print("PROGRAMMING ASSIGNMENT #2")

    k = int(raw_input("Enter the number of clusters: "))
    data=[float(x.rstrip()) for x in open("prog2-input-data.txt")]
    centroids=dict(zip(range(k), data[0:k])) 
    clusters = dict(zip(range(k),[[] for i in range(k)]))
    point_assignments = {} 

    for index, key in enumerate(data, 0):
        point_assignments.update( {index : 0} )
       
     

    assign_to_clusters(data, clusters, centroids, point_assignments)
    update_clusters(data, clusters, centroids)
    
    

    print "Point Assigments: ", point_assignments
    for index in data:
        print "Point ", index, " in cluster "
       
       
        
   

    #for key, value in centroids.iteritems():
    #    clusters[key].append(value)

def assign_to_clusters(data, clusters, centroids, point_assignments):
    """ Align points to their nearest centroid in each cluster """

    old_point_assignments={}
    smallvalue = 100000

    for index, dvalue in enumerate(data,0):
        for key, cvalue in centroids.items():
            smallest = abs(cvalue - dvalue)
            if smallest < smallvalue:
                smallvalue = smallest 
                smallindex = index
                centindex = key
                
                               
        clusters[centindex].append(dvalue)
        point_assignments.update( {index : centindex} )
        old_point_assignments = point_assignments.copy()
        smallvalue = 100000
        
        print "Iteration ", index
        for item in clusters:
            print item, clusters[centindex]
            
        print clusters[centindex]
              
       
def update_clusters(data, clusters, centroids):
    """ Recomputes Centroids for each cluster """ 

    status = True

    while status:
        clength = dict(zip(clusters.keys(), [[len(item)] for item in clusters.values()]))
        c2 = dict(zip(clusters.keys(), [[sum(item)] for item in clusters.values()]))
            
        summedList = [] #a list to contain the summed cluster values
        mean = [] #new mean calculated in each iteration down below
       
        for d1, list1 in c2.iteritems():
            for x in list1:
                summedList.append(x) #build a list of summed clusters
               
               
                
        for d2, list2 in clength.iteritems():
            for numberInList in list2:
                mean.append(summedList[d2]/numberInList) #compute mean by dividing sum by num in list 
                cen = 0
                for y, z in centroids.iteritems(): #logic to get out of recomputing centroids
                    cen = cen + z 
                    
                            
                   
                if sum(mean) != cen:              #bail out when these two equal each other
                    centroids[d2] = mean[d2]      #otherwise keep going
                else:
                    status = False                #change status to False and quit
                    
                    
                

if __name__ == "__main__":
    main()
