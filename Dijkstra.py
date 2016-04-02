# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os.path

'''dijkstra_logo class contains all the methods 
needed to implement Dijkstra algorithm'''

class dijkstra_algo(object):
    
    def loadFile(self, file_name):
        try:
            '''Read all the lines from the file and put it into a list.'''
            paths = []
            input_file = open(file_name, 'r')
            for x in input_file.readlines():
                paths.append(x.rstrip('\r\n'))
            self.routers = {}
            i = 0
            
            size = {}
            '''Store the size of each line of the file for the validation of square matrix'''
            for x in range(len(paths)):
                size[x] = paths[x].split()

            '''Validate the size of each column to be same'''
            for x in range(len(size)):
                if x !=0:
                    if(len(size[x-1])!=len(size[x])):
                        raise X
            
            '''Values are read and put into dictionary having row number as key, 
            and value as a sub-dictionary of column number as key and value as list 
            of distance and row number (represents as source router) '''
            
            for each in paths:
                values = each.split()
                j = 0
                
                '''Vaidate the presence of only validate characters'''
                if each.count(" ")!=len(size[0])-1 or each.count('\t')!=0:
                    raise X

                distance = {}
                for value in values:
                    temp_list = []
                    temp_list.append(int(value))
                    temp_list.append(`i`)
                    distance[`j`] = temp_list
                    j+=1
    
                self.routers[`i`]=distance
                i+=1
            '''Validation of square matrix'''
            if i!=j:
                raise X
            self.connection_table = False
        except:
            print "Invalid Input File"

    '''Display the distance values got from the file by fetching from the dictionary'''
    def display_the_matrix(self):
        print "Review original topology matrix:"
        i = 0
        for k,v in self.routers.iteritems():
            j = 0
            connection = ""
            for k1, v1 in v.iteritems():
                connection+=str(self.routers.get(`i`).get(`j`)[0])+"\t"
                j+=1
            print connection
            i+=1
                
        
    '''getSourceRouter is used to prompt the user to enter the source router'''
    def getSourceRouter(self):
        source_router = raw_input("Enter the source router:")
        return source_router
        
    '''
    replace_min_values(self, minimum_distance_router, minimum_distance) is used to check 
    whether the distance by routing adjacent routers is smaller than the distance stored in the route_table
    Parameters: 
        minimum_distance_router : The available minimum distance router adjacent to the previously visited router
        minimum_distance: The distance required to reach the minimum_distance_router from the source router
    Returns:
        The updated route table which contains the minimum distance values until visited
    '''
    def replace_min_values(self, minimum_distance_router, minimum_distance):
        temp_path = self.routers.get(minimum_distance_router)
        route_table_temp = {}
        for k,v in self.route_table.iteritems():
            if v[0] < 0 and temp_path[k][0]>0:
                temp_list = []
                temp_list.append(temp_path[k][0]+minimum_distance)
                temp_list.append(minimum_distance_router)
               	route_table_temp[k] = temp_list
            else:
                if temp_path[k][0] > 0 and self.route_table[k][0]> temp_path[k][0]+minimum_distance :
                    temp_list = []
                    temp_list.append(temp_path[k][0]+minimum_distance)
                    temp_list.append(minimum_distance_router)
                    route_table_temp[k] = temp_list
                else:
                    temp_list = []
                    temp_list.append(v[0])
                    temp_list.append(v[1])
                    route_table_temp[k] = temp_list
        self.route_table = route_table_temp        
        minimum_distance = min(filter(lambda x : x>0, temp_path.values()))
        for router, distance in temp_path.iteritems():
            if distance==minimum_distance:
                minimum_distance_router = router
                break                
        return self.route_table
    
    '''
    sort_route_distance() sorts the route_table with the minimum distance values from the previously visited router
    Returns:
        ascending_order_router: Sorted route_table with minimum distance values first.
    '''
    def sort_route_distance(self):
        ascending_order_router = filter(lambda x : self.route_table.get(x)[0]>=0,
                                        sorted(self.route_table.iterkeys(),key = lambda x : self.route_table.get(x)[0]))
        return ascending_order_router

    '''
    dijkstra(source_router) is the main Dijkstra algorithm implementation.
    '''
    def dijkstra(self, source_router):
        try:
            self.route_table = self.routers.get(source_router).copy()
            visited = []
            unvisited = self.route_table
            sorted_route_table = self.sort_route_distance()
            for x in unvisited:
                sorted_route_table = self.sort_route_distance()
                sorted_route_table = [x for x in sorted_route_table if x not in visited]
                self.route_table = self.replace_min_values(sorted_route_table[0], self.route_table.get(sorted_route_table[0])[0])
                visited.append(sorted_route_table[0])
        except:
            print ""    
    
    '''
    calculate_path(self,router, source_router) is a recursive method which 
    recurse until it reaches the source router that helps in computing the 
    path from source to destination.
    Parameters:
            router: a previous router to the current router
            source_rouer: the source router
    Returns:
            self.temp_path: a list that keeps updating with previously visited
                            router until it reaches source router
    '''
    def calculate_path(self,router, source_router):
        if(router!=source_router):
            self.temp_path.append(router)
            pre_router = self.route_table.get(router)[1]
            self.calculate_path(pre_router, source_router)
        return self.temp_path

    '''
    compute_path(source_router) computes the path from a source router to all
    other destination routers available in the graph.
    Parameters:
            source_router: the source_router string
    Returns:
            route_table_with_path: a dictionary that contains the from router as key 
                                    and a value of distance and to router.
    '''
    def compute_path(self, source_router):
        final_route_table = {}
        self.temp_path = []
        path = []
        route_table_with_path = {}
        for k,v in self.route_table.iteritems():
            path.append(k)
            for x in self.calculate_path(v[1], source_router):
                path.append(x)
            path.append(source_router)
            route_table_with_path[k] = [v[0],path[::-1]]
            self.temp_path = []
            path = []
        return route_table_with_path

    '''
    display_path(route_table_with_path, source_router, dest_router) displays the path for a
    given source and destination routers
    Parameters:
        route_table_with_path: a dictionary that contains the from router as key 
                                    and a value of distance and to router.
        source_router: source router string
        dest_router: destination router string
    '''
    def display_path(self, route_table_with_path, source_router, dest_router):
        value_path = route_table_with_path.get(dest_router)
        self.src_to_dest = source_router
        for x,y in enumerate(value_path[1]):
            if(x!=0):
                self.src_to_dest += "->"+y
        print "Distance is %d and Path is %s"%(route_table_with_path[dest_router][0],self.src_to_dest)
        
    '''
    get_path_for_a_dest(route_table_with_path, source_router, dest_router) computes the path for a
    given source and destination routers
    Parameters:
        route_table_with_path: a dictionary that contains the from router as key 
                                    and a value of distance and to router.
        source_router: source router string
        dest_router: destination router string
    Returns:
        src_to_dest which is a string that contains the source to destintaion path
    '''
    def get_path_for_a_dest(self, route_table_with_path, source_router, dest_router):
        value_path = route_table_with_path.get(dest_router)
        self.src_to_dest = source_router
        for x,y in enumerate(value_path[1]):
            if(x!=0):
                self.src_to_dest += "->"+y
        return self.src_to_dest
        
    '''
    get_router_to_remove() is used to get the router to be removed from the graph
    Returns:
        router_to_remove: the string value of router to be removed
    '''
    def get_router_to_remove(self):
        router_to_remove = raw_input("Enter the router to remove")
        return router_to_remove
    
    '''
    remove_router(router_to_remove) is used to remove a router from the routers
    Parameter:
        router_to_remove: the string value of router to be removed
    '''
    def remove_router(self, router_to_remove):
        updated_routers = {k:v for k, v in self.routers.iteritems() if k!=router_to_remove}
        for k,v in updated_routers.iteritems():
            new_values = {k1:v1 for k1, v1 in v.iteritems() if k1!=router_to_remove}
            updated_routers[k] = new_values
	self.routers = updated_routers
   
        
    '''
    create_a_network_topology() does the required functionalities to meet the menu 1.create_a_network_topology
    '''
    def create_a_network_topology(self):
        file_name = raw_input("Input original network topology matix data file:")
        if os.path.isfile(file_name):
            self.loadFile(file_name)
        else:
            print "File doesn't exist"
        self.create_topology = True
        self.display_the_matrix()
    
    '''
    build_a_connection_table() does the functionalaties to meet the menu 2.build_a_connection_table
    '''
    def build_a_connection_table(self):
        
        sr = self.getSourceRouter()

        if sr in self.routers.iterkeys():
            self.source_router = sr
            self.dijkstra(self.source_router)
            print "Router"+self.source_router+" Connection Table"
            print "Destination\tInterface\n============================="
            self.route_table_with_path = self.compute_path(self.source_router)
            dest_routers = sorted([k for k in self.routers.iterkeys()])
            for x in dest_routers:
                if self.route_table_with_path[x][0]!=-1 and self.route_table_with_path[x][0]!=0:
                    print x+"\t\t"+self.get_path_for_a_dest(self.route_table_with_path, self.source_router,str(x))
                #self.display_shortest_path_graph()
            self.connection_table = True
        else:
            print "Source router entered is not in connection table"
    
    
    '''
    rebuild_a_connection_table() is called when a router is removed and rebuild a router table
    '''
    def rebuild_a_connection_table(self):
        sr = self.source_router
        if sr in self.routers.iterkeys():
            self.source_router = sr
            self.dijkstra(self.source_router)
            print "Router"+self.source_router+" Connection Table"
            print "Destination\tInterface\n============================="
            self.route_table_with_path = self.compute_path(self.source_router)
            dest_routers = sorted([k for k in self.routers.iterkeys()])
            for x in dest_routers:
                if self.route_table_with_path[x][0]!=-1 and self.route_table_with_path[x][0]!=0:
                    print x+"\t\t"+self.get_path_for_a_dest(self.route_table_with_path, self.source_router,str(x))
                #self.display_shortest_path_graph()
        else:
            self.build_a_connection_table()
    
    
    '''
    shortest_path_to_destination_router() does the required functionalities to meet 3.shortest_path_to_destination_router
    '''
    def shortest_path_to_destination_router(self):
        dest_router = raw_input("Enter a destination router: ")
        if dest_router in self.routers.iterkeys():
            self.display_path(self.route_table_with_path, self.source_router,dest_router)
            #self.display_shortest_path_graph()
        else:
            print "Destination router does not exist in connectio table"
        
    '''
    modify_a_topology does the required functionalities to meet 4.modify_a_topology
    '''
    def modify_a_topology(self):
        if self.create_topology:
            router_to_remove = self.get_router_to_remove()
            self.remove_router(router_to_remove)
            if self.connection_table:
                self.rebuild_a_connection_table()
                #self.shortest_path_to_destination_router()
    
    def compute_connection_table_all(self):
        for x in self.routers.iterkeys():
            self.source_router = x
            self.dijkstra(self.source_router)
            print "Router"+self.source_router+" Connection Table"
            print "Destination\tInterface\n============================="
            self.route_table_with_path = self.compute_path(self.source_router)
            dest_routers = sorted([k for k in self.routers.iterkeys()])
            for x in dest_routers:
                if self.route_table_with_path[x][0]!=-1 and self.route_table_with_path[x][0]!=0:
                    print x+"\t\t"+self.get_path_for_a_dest(self.route_table_with_path, self.source_router,str(x))
                #self.display_shortest_path_graph()
            self.connection_table = True
        
        
def main():
   
    algorithm = dijkstra_algo()
    user_input = 0
    fns = {1:"create_a_network_topology", 2:"build_a_connection_table", 3:"shortest_path_to_destination_router",
           4:"modify_a_topology",5:"compute_connection_table_all", 6:"exit"}
    algorithm.create_topology = False
    algorithm.first_error = True
    while(user_input!=6):
        
        print "\n================:Menu:================"
        print "1.Create a network topology\n2.Build a Connection Table\n3.Shortest Path to destination router\n4.Modify a topology\n5.Compute all connection table\n6.Exit"
        print "======================================\n"
        try:
            user_input = int(raw_input("Enter a command"))
            if user_input<6:
                to_call = [v for k,v in fns.iteritems() if user_input==k]
                method = getattr(algorithm, to_call[0])
                method()
            elif user_input==6:
                print "Exiting the menu"
            else:
                print "Enter a correct option"
        except:
            print "Invalid entry"
            
        
        
if  __name__ =='__main__':main()

