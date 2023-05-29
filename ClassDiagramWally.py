class RobotActivity(object):
    def __init__(self):
        self.__Busqueda = ""
        
        self.robot_Wally = None
        
   
    def AbrirGarra(self):
        
        return False
        	
    def CerrarGarra(self):
        
        return False
        	
    def Agarrar(self, parameter, parameter2, parameter3, parameter4, parameter5):
        
        raise NotImplementedError
        	
    def Depositar(self, parameter, parameter2, parameter3, parameter4):
        
        raise NotImplementedError
        	
    def OrientarBase(self, parameter):
        
        return None
        	
    def OrientarBrazo(self, parameter):
        
        return None
        	
    def OrientarGarra(self, parameter):
        
        return None
        	
    def OrientarCamara(self, parameter):
        
        return None
        	
    def IdentificarObjetos(self, parameter):
        
        return None
        	
    def MedirDistancia(self, parameter, parameter2, parameter3):
        
        return 0.
        	
    def Avanzar(self, parameter):
        
        return None
        	
    def Retroceder(self, parameter):
        
        return None
        	
    def GirarDerecha(self, parameter):
        
        return None
        	
    def AdelanteAtrasBrazo(self, parameter):
        
        return None
        	
    def DerechaIzquierdaBrazo(self, parameter):
        
        return None
        	
    def RotarGarra(self, parameter):
        
        return None
        	
    def RotarCamara(self, parameter):
        
        return None
        	
    def Comunicar(self, parameter):
        
        return False
        	
    def Recarga(self, parameter):
        
        return False
        

    


class Dimensiones(object):
    def __init__(self):
        self.__Largo = 0.
        self.__Alto = 0.
        self.__Ancho = 0.
        
        self.deposito = None
        self.objetoReciclable = None
        self.zonaBusqueda = None
        
    
    def getLargo(self):
        
        return 0.
        	
    def setLargo(self):
        
        return 0.
        	
    def getAlto(self):
        
        return 0.
        	
    def setAlto(self):
        
        return 0.
        	
    def getAncho(self):
        
        return 0.
        	
    def setAncho(self):
        
        return 0.
        


class Imagen(object):
    def __init__(self):
        self.__Largo = 0.
        self.__Alto = 0.
        
        self.objeto = None
        self.zonaBusqueda = None
        
    
    def getLargo(self):
        
        return 0.
        	
    def setLargo(self):
        
        return 0.
        	
    def getAlto(self):
        
        return 0.
        	
    def setAlto(self):
        
        return 0.
        



class Deposito(object):
    def __init__(self):
        self.__dimensiones = None
        self.__coordenadas = None
        
        self.coordenadas2 = None
        self.dimensiones2 = None
        
    
    def getDimensiones(self):
        
        return None
        
    def setDimensiones(self, parameter):
        
        raise NotImplementedError
        
    def getCoordenadas(self):
        
        return None
        	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Deposito class

    # End of user code

class ZonaRecarga(object):
    def __init__(self):
        self.__coordenadas = None
        
        self.coordenadas2 = None
        
    # Start of user code -> properties/constructors for ZonaRecarga class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for ZonaRecarga class

    # End of user code

class Objeto(object):
    def __init__(self):
        self.__coordenadas = None
        self.__imagen = None
        self.__reciclable = False
        self.__distancia = 0.
        
        self.coordenadas2 = None
        self.imagen2 = None
        self.objetoReciclable = None
        
    # Start of user code -> properties/constructors for Objeto class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    def getImagen(self):
        # Start of user code protected zone for getImagen function body
        return None
        # End of user code	
    def setImagen(self, parameter):
        # Start of user code protected zone for setImagen function body
        raise NotImplementedError
        # End of user code	
    def getReciclable(self):
        # Start of user code protected zone for getReciclable function body
        return False
        # End of user code	
    def setReciclable(self):
        # Start of user code protected zone for setReciclable function body
        return False
        # End of user code	
    def getDistancia(self):
        # Start of user code protected zone for getDistancia function body
        return 0.
        # End of user code	
    def setDistancia(self):
        # Start of user code protected zone for setDistancia function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Objeto class

    # End of user code





class Contenedor(object):
    def __init__(self):
        self.__categoria = ""
        self.__coordenadas = None
        
        self.coordenadas2 = None
        
    # Start of user code -> properties/constructors for Contenedor class

    # End of user code
    def getCategoria(self):
        # Start of user code protected zone for getCategoria function body
        return ""
        # End of user code	
    def setCategoria(self, parameter):
        # Start of user code protected zone for setCategoria function body
        raise NotImplementedError
        # End of user code	
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Contenedor class

    # End of user code


class ObjetoReciclable(object):
    def __init__(self):
        self.__Categoria = ""
        self.__Color = ""
        self.__dimensiones = None
        self.__orientacion = None
        
        self.objeto = None
        self.orientacion2 = None
        self.dimensiones2 = None
        
    # Start of user code -> properties/constructors for ObjetoReciclable class

    # End of user code
    def getCategoria(self):
        # Start of user code protected zone for getCategoria function body
        return ""
        # End of user code	
    def setCategoria(self, parameter):
        # Start of user code protected zone for setCategoria function body
        raise NotImplementedError
        # End of user code	
    def getColor(self):
        # Start of user code protected zone for getColor function body
        return ""
        # End of user code	
    def setColor(self, parameter):
        # Start of user code protected zone for setColor function body
        raise NotImplementedError
        # End of user code	
    def getDimensiones(self):
        # Start of user code protected zone for getDimensiones function body
        return None
        # End of user code	
    def setDimensiones(self, parameter):
        # Start of user code protected zone for setDimensiones function body
        raise NotImplementedError
        # End of user code	
    def getOrientacion(self):
        # Start of user code protected zone for getOrientacion function body
        return None
        # End of user code	
    def setOrientacion(self, parameter):
        # Start of user code protected zone for setOrientacion function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for ObjetoReciclable class

    # End of user code


class Coordenadas(object):
    def __init__(self):
        self.__X = 0.
        self.__Y = 0.
        self.__Z = 0.
        
        self.contenedor = None
        self.deposito = None
        self.garra = None
        self.brazo = None
        self.base = None
        self.objeto = None
        self.zonaRecarga = None
        self.camara = None
        self.zonaBusqueda = None
        
    # Start of user code -> properties/constructors for Coordenadas class

    # End of user code
    def getX(self):
        # Start of user code protected zone for getX function body
        return 0.
        # End of user code	
    def setX(self):
        # Start of user code protected zone for setX function body
        return 0.
        # End of user code	
    def getY(self):
        # Start of user code protected zone for getY function body
        return 0.
        # End of user code	
    def setY(self):
        # Start of user code protected zone for setY function body
        return 0.
        # End of user code	
    def getZ(self):
        # Start of user code protected zone for getZ function body
        return 0.
        # End of user code	
    def setZ(self):
        # Start of user code protected zone for setZ function body
        return 0.
        # End of user code	
    # Start of user code -> methods for Coordenadas class

    # End of user code

class ZonaBusqueda(object):
    def __init__(self):
        self.__coordenadas = None
        self.__dimensiones = None
        self.__imagen = None
        
        self.coordenadas2 = None
        self.imagen2 = None
        self.dimensiones2 = None
        
    # Start of user code -> properties/constructors for ZonaBusqueda class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    def getDimensiones(self):
        # Start of user code protected zone for getDimensiones function body
        return None
        # End of user code	
    def setDimensiones(self, parameter):
        # Start of user code protected zone for setDimensiones function body
        raise NotImplementedError
        # End of user code	
    def getImagen(self):
        # Start of user code protected zone for getImagen function body
        return None
        # End of user code	
    def setImagen(self, parameter):
        # Start of user code protected zone for setImagen function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for ZonaBusqueda class

    # End of user code







class Robot_Wally(object):
    def __init__(self):
        
        self.robotActivity = None
        
    # Start of user code -> properties/constructors for Robot Wally class

    # End of user code
    # Start of user code -> methods for Robot Wally class

    # End of user code



class Orientacion(object):
    def __init__(self):
        self.__roll = 0.
        self.__pitch = 0.
        self.__yaw = 0.
        
        self.brazo = None
        self.garra = None
        self.base = None
        self.objetoReciclable = None
        self.camara = None
        
    # Start of user code -> properties/constructors for Orientacion class

    # End of user code
    def getRoll(self):
        # Start of user code protected zone for getRoll function body
        return 0.
        # End of user code	
    def setRoll(self, parameter):
        # Start of user code protected zone for setRoll function body
        raise NotImplementedError
        # End of user code	
    def getPitch(self):
        # Start of user code protected zone for getPitch function body
        return 0.
        # End of user code	
    def setPitch(self, parameter):
        # Start of user code protected zone for setPitch function body
        raise NotImplementedError
        # End of user code	
    def getYaw(self):
        # Start of user code protected zone for getYaw function body
        return 0.
        # End of user code	
    def setYaw(self, parameter):
        # Start of user code protected zone for setYaw function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Orientacion class

    # End of user code




class Camara(Robot_Wally):
    def __init__(self):
        self.__coordenadas = None
        self.__orientacion = None
        
        self.coordenadas2 = None
        self.orientacion2 = None
        
    # Start of user code -> properties/constructors for Camara class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    def getOrientacion(self):
        # Start of user code protected zone for getOrientacion function body
        return None
        # End of user code	
    def setOrientacion(self, parameter):
        # Start of user code protected zone for setOrientacion function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Camara class

    # End of user code

class Base(Robot_Wally):
    def __init__(self):
        self.__coordenadas = None
        self.__orientacion = None
        self.__distancia = 0.
        
        self.coordenadas2 = None
        self.orientacion2 = None
        
    # Start of user code -> properties/constructors for Base class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    def getOrientacion(self):
        # Start of user code protected zone for getOrientacion function body
        return None
        # End of user code	
    def setOrientacion(self, parameter):
        # Start of user code protected zone for setOrientacion function body
        raise NotImplementedError
        # End of user code	
    def getDistancia(self):
        # Start of user code protected zone for getDistancia function body
        return 0.
        # End of user code	
    def setDistancia(self, parameter):
        # Start of user code protected zone for setDistancia function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Base class

    # End of user code

class Brazo(Robot_Wally):
    def __init__(self):
        self.__coordenadas = None
        self.__orientacion = None
        
        self.coordenadas2 = None
        self.orientacion2 = None
        
    # Start of user code -> properties/constructors for Brazo class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    def getOrientacion(self):
        # Start of user code protected zone for getOrientacion function body
        return None
        # End of user code	
    def setOrientacion(self, parameter):
        # Start of user code protected zone for setOrientacion function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Brazo class

    # End of user code

class Garra(Robot_Wally):
    def __init__(self):
        self.__coordenadas  = None
        self.__orientacion = None
        self.__estado = False
        
        self.orientacion2 = None
        self.coordenadas = None
        
    # Start of user code -> properties/constructors for Garra class

    # End of user code
    def getCoordenadas(self):
        # Start of user code protected zone for getCoordenadas function body
        return None
        # End of user code	
    def setCoordenadas(self, parameter):
        # Start of user code protected zone for setCoordenadas function body
        raise NotImplementedError
        # End of user code	
    def getOrientacion(self):
        # Start of user code protected zone for getOrientacion function body
        return None
        # End of user code	
    def setOrientacion(self, parameter):
        # Start of user code protected zone for setOrientacion function body
        raise NotImplementedError
        # End of user code	
    def getEstado(self):
        # Start of user code protected zone for getEstado function body
        return False
        # End of user code	
    def setEstado(self, parameter):
        # Start of user code protected zone for setEstado function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Garra class

    # End of user code


# Start of user code -> functions/methods for FINAL PROJECT package

# End of user code
