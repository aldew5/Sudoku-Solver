
import pygame
import solver

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.Font(None, 32)


clock = pygame.time.Clock()

class Cell(object):
    def __init__(self, value, x, y, length, width):
        self.value = value
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def draw(self):
        if self.value != 0:
            txt_surface = font.render(self.value, True, (0,0,0))
        else:
            txt_surface = font.render('', True, (0,0,0))
            
        win.blit(txt_surface, (self.x + 10, self.y + 10))      
        pygame.draw.rect(win, (0,0,0), ((self.x, self.y),\
                                        (self.length, self.width)), 1)

    def collidepoint(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + self.width:
            if pos[1] >= self.y and pos[1] <= self.y + self.width:
                return True
        return False
    
    def set_value(self, new_value):
        self.value = new_value

    

class Puzzle(object):
    def __init__(self):
        self.solved = False
        self.cells = []
        self.input_status = {}
        self.values = []

        y, index = 0, 9
        # create a list of the cells and a 2D list of their values
        while y < 495.5:
            x = 0
            while x < 495.5:
                new_cell = Cell(0, x, y, 55.5, 55.5)
                self.cells.append(new_cell)
                # cell default to false meaning not clicked
                self.input_status[new_cell] = False

                # build a row that will contain the values of cells
                if len(self.cells) % 9 == 0:
                    row = []
                    for cell in self.cells[index - 9 : index]:
                        row.append(cell.value)
                    self.values.append(row)

                    # look at the next nine values
                    index += 9
                
                x += 55.5
                
            y += 55.5
        

    def draw(self, win):
        # draw all the cells
        for cell in self.cells:
            cell.draw()

    def updateValues(self):
        self.values = []
        index = 8
        for cell in self.cells:
            index += 1
            # create a row of length nine
            if index % 9 == 0:
                row = []
                for cell in self.cells[index -9 :index]:
                    row.append(int(cell.value))
            
                if len(row) != 0:
                    self.values.append(row)
                    
    def displaySolution(self):
        y, c = 0,0
        while y < len(self.values):
            x = 0
            while x < 9:
                self.cells[c].set_value(str(self.values[y][x]))

                x += 1
                c += 1
                
            y += 1
        
       
        
def drawWindow():
    win.fill((255,255,255))
    puzzle.draw(win)

    pygame.display.update()
        


puzzle = Puzzle()

run = True
while run:
    for event in pygame.event.get():
        # close the window
        if event.type == pygame.QUIT:
            run = False
        # click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # the user clicked on the rect
            for cell in puzzle.cells:
                if cell.collidepoint(event.pos):
                    # the cell now accepts input
                    puzzle.input_status[cell] = True
                else:
                     puzzle.input_status[cell] = False

        new_value = ''
        # get user input for the clicked cell
        if event.type == pygame.KEYDOWN:
            for cell in puzzle.cells:
                # a cell was clicked on
                if puzzle.input_status[cell]:
                    
                    # return triggers the solution of the puzzle
                    if event.key == pygame.K_RETURN:
                        puzzle.updateValues()

                        if solver.solve(puzzle.values):
                            solver.print_puzzle(puzzle.values)
                            puzzle.displaySolution()
                            puzzle.draw(win)

                    # delete a character
                    elif event.key == pygame.K_BACKSPACE:
                        new_value = '0'
                        cell.set_value(new_value)
                        
                    # add a character 
                    else:
                        new_value += event.unicode
                        cell.set_value(new_value)
                        
    drawWindow()










    
        
