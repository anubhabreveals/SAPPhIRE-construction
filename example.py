import graphviz

f = graphviz.Digraph('ER', filename='er.gv', engine='dot', format='png')

n=2



for i in range(1,n):
    with f.subgraph(name='cluster_'+str(i)) as e:
        e.attr('node', shape='box')
        e.node('Input'+str(i), label='<<FONT COLOR="BLUE"><b><u>I</u></b>nput:</FONT><BR/>'+str(i)+'>')
        e.node('Part'+str(i), label='<<FONT COLOR="BLUE"><b><u>P</u></b>art:</FONT><BR/>'+str(i)+'>')
        e.node('oRgan'+str(i), label='<<FONT COLOR="BLUE">o<b><u>R</u></b>gan:</FONT><BR/>'+str(i)+'>')
        e.node('Effect'+str(i), label='<<FONT COLOR="BLUE"><b><u>E</u></b>ffect:</FONT><BR/>'+str(i)+'>')
        e.node('Phenomena'+str(i), label='<<FONT COLOR="BLUE"><b><u>Ph</u></b>enomena:</FONT><BR/>'+str(i)+'>')
        e.node('State change'+str(i), label='<<FONT COLOR="BLUE"><b><u>S</u></b>tate change:</FONT><BR/>'+str(i)+'>')
        e.node('Action'+str(i), label='<<FONT COLOR="BLUE"><b><u>A</u></b>ction:</FONT><BR/>'+str(i)+'>')

        e.edge('State change'+str(i), 'Action'+str(i), splines='true')
        e.edge('Phenomena'+str(i), 'State change'+str(i), splines='true')
        e.edge('Effect'+str(i), 'Phenomena'+str(i), splines='true')
        e.edge('oRgan'+str(i), 'Effect'+str(i), splines='true')
        e.edge('Part'+str(i), 'oRgan'+str(i), splines='true')
        e.edge('Input'+str(i), 'Effect'+str(i), splines='true')

  
#f.edge('Action1', 'Input2', splines='ortho', constraint='false')
#f.edge('Action1', 'Input3', splines='true')
f.graph_attr['rankdir']='BT'
f.view()