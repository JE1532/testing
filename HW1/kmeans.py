import sys

eplilon = 0.001
iter = 200
K = 0
N = 0
file = None
data = []
clusters_numbers = [] # same size as data. each element is a cluster number.
centroids = []

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
                if line.strip() == '':
                    continue  
                    data.append([int(x) for x in line.split()])
                        
                        
                    
def assign_datapoint_to_cluster(datapoint_index, cluster_number):        
    pass
            
def kmeans(k, iter, data):
    for i in range(k):
        assign_datapoint_to_cluster(i, i)
    for i in range(iter):
        
        
 
            
                

def main():
    process_input()
    read_data_from_file(file)
    
    
    
        
            
