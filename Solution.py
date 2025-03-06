import Game
import time
import Model
import tqdm


"""
This file is the file to train the flappy bird into a model.
-> The file uses the Model.py to create a model and train it.
"""
def computeDetails(inputDetails):
    global oldY, oldTop, oldBottom, oldX
    if(abs(inputDetails[0]-oldY)>10
       or abs(inputDetails[3]-oldX)>10):
        oldY = inputDetails[0] - (inputDetails[0]%10)
        oldTop = inputDetails[1] - (inputDetails[1]%2)
        oldBottom = inputDetails[2] - (inputDetails[2]%2)
        oldX = inputDetails[3] - (inputDetails[3]%10)
        return True
    else:
        return False


gameModel = Model.Model(0.01,0.9,0.4,[0,1])
# gameModel = Model.loadModel("model1.xml",0.3,0.98,0)
oldY = 0
oldTop = 0
oldBottom = 0
oldX = 0
prevX = 0

breakBool = True
calcOn = False
for epoch in tqdm.tqdm(range(0,100)):
    game = Game.Game()
    # game.show()
    while breakBool:
        # time.sleep(0.0000001)
        if(computeDetails(game.getDetails())):
            calcOn = True
            returnededPred = gameModel.compute([oldY,oldTop,oldBottom,oldX])
            if(returnededPred==1):
                game.jump()

        game.update() 

        if game.status_code in [-1, -2]:
            if(calcOn):
                gameModel.train(game.status_code*10)
                calcOn = False
            breakBool = False
        if(calcOn):
            if(prevX<oldX):
                gameModel.train(1000)
            prevX = oldX
            gameModel.train(1)
            calcOn=False

        game.draw()
    breakBool = True

gameModel.saveModel("model1")

a = input("Retrain?")
while a=="":
    gameModel = Model.loadModel("model1.xml",0.1,0.98,0.15)
    oldY = 0
    oldTop = 0
    oldBottom = 0
    oldX = 0

    breakBool = True
    calcOn = False
    for epoch in tqdm.tqdm(range(0,100)):
        game = Game.Game()
        while breakBool:
            if(computeDetails(game.getDetails())):
                calcOn = True
                returnededPred = gameModel.compute([oldY,oldTop,oldBottom,oldX])
                if(returnededPred==1):
                    game.jump()

            game.update() 

            if game.status_code in [-1, -2]:
                if(calcOn):
                    gameModel.train(game.status_code*10)
                    calcOn = False
                breakBool = False
            if(calcOn):
                if(prevX<oldX):
                    gameModel.train(1000)
                prevX = oldX
                gameModel.train(1)
                calcOn=False

            game.draw()
        breakBool = True

    gameModel.saveModel("model1")
    a = input("Retrain?")