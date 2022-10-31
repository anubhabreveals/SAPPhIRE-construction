import graphviz

f = graphviz.Digraph('ER', filename='er.gv', engine='dot', format='png')

n=6



for i in range(1,n):
    with f.subgraph(name='cluster_'+str(i)) as e:
        e.attr('node', shape='box')
        e.edge('State change'+str(i), 'Action'+str(i), splines='true')
        e.edge('Phenomena'+str(i), 'State change'+str(i), splines='true')
        e.edge('Effect'+str(i), 'Phenomena'+str(i), splines='true')
        e.edge('oRgan'+str(i), 'Effect'+str(i), splines='true')
        e.edge('Part'+str(i), 'oRgan'+str(i), splines='true')
        e.edge('Input'+str(i), 'Effect'+str(i), splines='true')
        e.attr(label='Instance'+str(i))

  
#f.edge('Action1', 'Input2', splines='ortho', constraint='false')
#f.edge('Action1', 'Input3', splines='true')
f.graph_attr['rankdir']='BT'
f.view()