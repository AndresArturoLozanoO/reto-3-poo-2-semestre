class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start:"Point", end:"Point"):
        self.start = start
        self.end = end
    def compute_lenght(self):
        lenght = ((-1*self.start.x+self.end.x)**2
                  + (-1*self.start.y+self.end.y)**2)**0.5
        self.lenght = lenght
        return lenght
    def compute_slope(self):
        slope = (self.end.y-self.end.x)/(self.end.x-self.start.x)
        self.slope = slope
        return slope
    def compute_horizontal_cross(self):
        return True if self.start.y*self.end.y <= 0 else False
    def compute_horizontal_cross(self):
        return True if self.start.x*self.end.x <= 0 else False
    
class Rectagle:
    def __init__(self, width:float=0, height:float=0, center:"Point"=(0.0)):
        self.width = width
        self.height = height
        self.center = center
        self.down_left = Point(self.center.x-self.width/2, 
                               self.center.y-self.height/2)
        self.top_right = Point(self.center.x+self.width/2, 
                               self.center.y+self.height/2)
        self.top_left = Point(self.center.x-self.width/2, 
                              self.center.y+self.height/2)
        self.down_right = Point(self.center.x+self.width/2, 
                                self.center.y-self.height/2)
        self.top_line = Line(self.top_left, self.top_right)
        self.right_line = Line(self.top_right, self.down_right)
        self.down_line = Line(self.down_right, self.down_left)
        self.left_line = Line(self.down_left, self.top_left)
    def compute_area(self):
        return self.width*self.height
    def compute_perimeter(self):
        return 2*(self.width+self.height)
    def inside_point(self,point_x:"Point"):
        return (point_x.x>=self.down_left.x 
                and point_x<=self.top_left.x 
                and point_x.y>=self.down_left.y 
                and point_x<=self.top_right.y)