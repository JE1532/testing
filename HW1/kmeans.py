import sys

eplilon = 0.001
iter = 200
K = 0
N = 0
file = None
data = []
clusters= []

def validate_iter():
   if int(sys.argv[2]) < 2 or int(sys.argv[2]) > 999: 
         print("Invalid maximum iteration!")
         sys.exit(1)
         
def validate_K():
    if int(sys.argv[index]) < 2 or int(sys.argv[index]) > 999:
        print("Invalid maximum iteration!")
        sys.exit(1)
        
def process_input():  
    if len(sys.argv) == 3: # 2 arguments, no iter provided.
        validate_K()
        file = sys.argv[3]
    if len(sys.argv) == 4: # 3 arguments, iter provided.
        validate_K()
        validate_iter()
        iter = int(sys.argv[2])
        file = sys.argv[2]
    else: 
        print("An Error Has Occurred")
        sys.exit(1)
        
        
def read_data_from_file(file):
    try:
        with open(file, 'r') as file:
            for line in file:
                data.append([int(x) for x in line.split()])
                        
                        
    
def get_distance(centroid, datapoint):
    return math.sqrt(sum([(centroid[i] - datapoint[i]) ** 2 for i in range(len(centroid))]))

def get_current_cluster():
    for i in range(len(clusters)):
        if data_point in clusters[i]:
            return i
    throw new Exception("Data point not found in any cluster!")



def reassign_data_point(data_point, cluster_number):
    clusters[get_current_cluster(data_point)].remove(data_point)
    clusters[cluster_number].append(datapoint)

def check_convergence(centroids, copy_centroids):
    for i in range(len(centroids)):
        if abs(centroids[i] - copy_centroids[i]) > epsilon:
            return False
    return True

            
def kmeans(k, iter, data):
    for i in range(k):
        clusters.append([])
        centroids[i] = 0
        assign_datapoint_to_cluster(data[i], i)
        
    for i in range(iter):
        for j in range(len(data)):
            copy_centroids = list(centroids)
            diffs = [get_distance(centroid, data[j]) for centroid in centroids]
            closest_centroid = diffs.index(min(diffs))
            reassign_data_point(data[j], closest_centroid)
        check_convergence(centroids, copy_centroids)
        
        
 
def print_results():
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            print(clusters[i][j], end = " ")
        print("/n")               
    
                

def main():
    process_input()
    read_data_from_file(file)
    kmeans(K, iter, data)
    print_results()

        
    
        
            
