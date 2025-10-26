from random import choice

class RandomWalk:
    def __init__(self,num_points=5000):
        #initialize attributes of a walk
        self.num_points = num_points
        #all walks start at (0,0)
        self.x_value = [0]
        self.y_value = [0]

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        return step
    
    def fill_walk(self):
        #keep store for reaches to 5000 digit
        while len(self.x_value) < self.num_points:
            #decide the direction right or left and how far
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step ==0:
                continue

            x = self.x_value[-1]  + x_step
            y = self.y_value[-1] +  y_step

            self.x_value.append(x)
            self.y_value.append(y)

        
        