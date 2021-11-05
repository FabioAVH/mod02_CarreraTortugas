import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        '''self.width = width
        self.height = height
        '''
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2+20
        self.__finishLine = width/2-20
                
        self.__createRunner() #esto crea los corredores cuando se crea la clase
        
    
    def __createRunner(self):
        
        for i in range(4):
            new_turtle =turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
    
    def Correr(self):
        
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                tortuga.forward(random.randint(1,6))
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print('La tortuga {} ha ganado!!!'.format(tortuga.color()[0]))    

if __name__ == '__main__':
    circuito = Circuito(640,480)
    circuito.Correr()