import graphviz
from kiwisolver import Constraint

g = graphviz.Digraph('ER', filename='er.gv', engine='dot', format='png')

n=6


with g.subgraph(name='cluster_c1') as f:
    for i in range(1,n):
        with f.subgraph(name='cluster_'+str(i)) as e:
            e.attr('node', shape='box')
            e.edge('State change'+str(i), 'Action'+str(i))
            e.edge('Phenomena'+str(i), 'State change'+str(i))
            e.edge('Effect'+str(i), 'Phenomena'+str(i))
            e.edge('oRgan'+str(i), 'Effect'+str(i))
            e.edge('Part'+str(i), 'oRgan'+str(i))
            e.edge('Input'+str(i), 'Effect'+str(i))
            e.attr(label='Instance'+str(i))
    

g.graph_attr['rankdir'] = 'BT'   

g.view()