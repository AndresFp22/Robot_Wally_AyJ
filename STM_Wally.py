from transitions import Machine
from ClassDiagramWally import*
from Robot_Wally import*

accionamiento=Robot_Wally()

states=['home','exploracion','reconocimiento_objetos','deteccion','posicionar_garra','orientar_garra','medir_distancia','mover_garra','agarrar','depositar','verificar_reecoleccion','siguiente_categoria','finalizacion','mover_zona']

transitions = [
    { 'trigger': 'explorar_terreno', 'source': 'home', 'dest': 'exploracion' },
    { 'trigger': 'capturar_imagen', 'source': 'exploracion', 'dest': 'reconocimiento_objetos' },
    { 'trigger': 'identifico_objetos', 'source': 'reconocimiento de objetos', 'dest': 'deteccion' },
    { 'trigger': 'posiciona', 'source': 'deteccion', 'dest': 'posicionar_garra' },
    { 'trigger': 'dirige_garra', 'source': 'posicionar_garra', 'dest': 'orientar_garra' },
    { 'trigger': 'medir_distancia_og', 'source': 'orientar garra', 'dest': 'medir_distancia' },
    { 'trigger': 'mover', 'source': 'medir distancia', 'dest': 'mover garra' }   ,
    { 'trigger': 'agarrar', 'source': 'mover_garra', 'dest': 'agarrar' },
    { 'trigger': 'mover_contenedor', 'source': 'agarrar', 'dest': 'depositar' },
    { 'trigger': 'verificar_recoleccion', 'source': 'depositar', 'dest': 'verificar_recoleccion' },
    { 'trigger': 'no_hay_objetos_categoria', 'source': 'verificar_recoleccion', 'dest': 'siguiente_categoria' },
    { 'trigger': 'finaliza_recoleccion', 'source': 'siguiente categoria', 'dest': 'finalizacion' },
    { 'trigger': 'mover_nueva_zona', 'source': 'finalizacion', 'dest': 'mover_zona' },
    { 'trigger': 'estado_inicial', 'source': 'mover_zona', 'dest': 'home' },
    { 'trigger': 'falla_robot', 'source': 'reconocimiento_objetos', 'dest': 'home' },
    { 'trigger': 'objeto_no_recogido', 'source': 'agarrar', 'dest': 'reconocimiento_objetos' },
    { 'trigger': 'alcance_limitado', 'source': 'medir_distancia', 'dest': 'reconocimiento_objetos' }
    ]    


statemachineRobot_Wally= Machine(model=accionamiento, states=states, transitions=transitions, initial='home')

print (accionamiento.state)
accionamiento.explorar_terreno()
print (accionamiento.state)