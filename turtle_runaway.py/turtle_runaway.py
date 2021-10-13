# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import turtle, random, time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=25, init_dist=400):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('red')
        self.runner.penup()
        self.runner.setx(-init_dist / 2)

        self.chaser.shape('turtle')
        self.chaser.color('black')
        self.chaser.penup()
        self.chaser.setx(+init_dist / 2)
        self.chaser.setheading(180)

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()
        
        self.drawer1 = turtle.RawTurtle(canvas)
        self.drawer1.hideturtle()
        self.drawer1.penup()
        
        self.drawer1 = turtle.RawTurtle(canvas)    
        self.drawer1.hideturtle()
        self.drawer1.speed(0)
        self.drawer1.penup()
        self.drawer1.setpos(300,-300)
        self.drawer1.pendown()
        self.drawer1.setheading(90)
        for i in range(4):
            self.drawer1.forward(600)
            self.drawer1.left(90)
    

    def is_catch(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2
            

    def start(self, ai_timer_msec=100):
        self.ai_timer_msec = ai_timer_msec
        self.start_time = time.time()
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser)
        self.chaser.run_ai(self.runner)
        
        is_catched = self.is_catch()
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        elapse = time.time() - self.start_time
        score = (time.time() - self.start_time)**2
        self.drawer.write(f'Is the game over? {is_catched} / time:{elapse:.0f} / score:{score:.0f}', font = ("", 20))
        self.canvas.ontimer(self.step, self.ai_timer_msec)
   
class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        
        if self.xcor() > 300 or self.xcor() < -300:
           self.right(180)
        if self.ycor() > 300 or self.ycor() < -300:
           self.right(180)
        

class lessRandomMover1(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn


    def run_ai(self, oppoenent):
        opp_pos = oppoenent.pos()
        opp_heading = oppoenent.heading()
        mode = random.random()
        if mode < 0.7:
            self.forward(self.step_move)
        elif mode < 0.9:
            self.left(self.step_turn)
        else:
            self.right(self.step_turn)
            
        if self.xcor() > 300 or self.xcor() < -300:
           self.right(180)
        if self.ycor() > 300 or self.ycor() < -300:
           self.right(180)
            

if __name__ == '__main__':
    canvas = turtle.Screen()
    chaser = lessRandomMover1(canvas)
    runner = ManualMover(canvas)

    game = RunawayGame(canvas,  runner, chaser)
    game.start()
    canvas.mainloop()
