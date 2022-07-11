from collections import deque

graph = {"copacabana":{"cristo redentor": 11900, "pao de acucar": 3000, "museu do amanha": 13700, "ipanema": 2000, "jardim botanico": 6300, "parque lage": 5600},
"cristo redentor":{"copacabana": 11900, "pao de acucar": 12300, "museu do amanha": 13300, "ipanema": 12800, "jardim botanico": 9500, "parque lage": 8300},
"pao de acucar":{"copacabana": 3000, "cristo redentor": 12300, "museu do amanha": 10600, "ipanema": 5, "jardim botanico": 6, "parque lage": 7},
"museu do amanha":{"copacabana": 13700, "cristo redentor": 13300, "pao de acucar": 10600, "ipanema": 15900, "jardim botanico": 12600, "parque lage": 11500},
"ipanema":{"copacabana": 2000, "cristo redentor": 12800, "pao de acucar": 6400, "museu do amanha": 15900, "jardim botanico": 4900, "parque lage": 5200},
"jardim botanico":{"copacabana": 6300, "cristo redentor": 9500, "pao de acucar": 6700, "museu do amanha": 12600, "ipanema": 4900, "parque lage": 1400},
"parque lage":{"copacabana": 5600, "cristo redentor": 8300, "pao de acucar": 5800, "museu do amanha": 11500, "ipanema": 5200, "jardim botanico": 1400}}

def dijkstra(node):
    queue = deque([node])
    distance = {node: 0}
    visitados = 0
    while queue:
        t = queue.popleft()
        if visitados != 0 and t == node:
            break
        for adjacent in graph[t]:
                queue.append(adjacent)
                newDistance = distance[t] + graph[t][adjacent]
                if(adjacent not in distance or newDistance < distance[adjacent]):
                    distance[adjacent] = newDistance
        visitados = visitados+1                

    return distance

def caminho(distance):
    route = {}
    len(route)
    while len(route) < len(distance):
        #a = input()
        d = 50000
        v = ""
        for place in distance:
            #print(distance[place])
            if distance[place] < d:
                d = distance[place]
                v = place
        route[v] = d
        distance[v] = 50000
        #print(v)
    print(route)


def selector(myEnter):
    switcher ={
        1: "copacabana",
        2: "cristo redentor",
        3: "pao de acucar",
        4: "museu do amanha",
        5: "ipanema",
        6: "jardim botanico",
        7: "parque lage"}

    node = switcher.get(myEnter, "nothing")
    if node != "nothing":
        dist = dijkstra(node)
        caminho(dist)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    print("escolhar o número de onde deseja começar as visitas e pressione enter\n")
    print("1-copacabana  2-cristo redentor  3-pao de acucar  4-museu do amanha  5-ipanema  6-jardim botanico  7-parque lage")
    myEnter = int(input())
    selector(myEnter)