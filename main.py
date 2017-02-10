from test import Test

class Start:
    
    def run(self, wordSearch, wordBank):

        directions = ['left', 'upLeft', 'up', 'upRight', 'right', 'downRight', 'down', 'downLeft'];

        def iterateOverWords():
            finalOutput = []
            for word in wordBank:
                coord = findWord(word)
                finalOutput.append(coord)
            Test().run(finalOutput)

        def findWord(word):
            for y in range(0, 50):
                for x in range(0, 50):
                    if wordSearch[y][x] == word[0:1]:
                        result = checkPaths(word, y, x)
                        if result != -1:
                            return result

        def checkPaths(word, y, x):
            for direction in directions:
                result = checkDirection(word, y, x, direction)
                if result !=  -1:
                    return result
            return -1

        def checkDirection(word, y, x, direction):
            coord = type('', (), {"x": x, "y": y})()
            startTuple = (x,y)
            coordinates = [startTuple]
            i = 0
            for letter in word:
                if i != 0:
                    coord = getCoord(coord.y, coord.x, direction)
                    if coord.x < 0 or coord.y < 0 or coord.x > 49 or coord.y > 49:
                        return -1
                    if letter != wordSearch[coord.y][coord.x]:
                        return -1
                    if i == len(word) - 1:
                        nextTuple = (coord.x, coord.y)
                        coordinates.append(nextTuple)
                        return coordinates
                    nextTuple = (coord.x,coord.y)
                    coordinates.append(nextTuple)
                i += 1

        def getCoord(y, x, direction):
            if direction == 'left':
                x -= 1
            if direction == 'upLeft':
                x -= 1
                y -= 1
            if direction == 'up':
                y -= 1
            if direction == 'upRight':
                y -= 1
                x += 1
            if direction == 'right':
                x += 1
            if direction == 'downRight':
                x += 1
                y += 1
            if direction == 'down':
                y += 1
            if direction ==  'downLeft':
                y += 1
                x -= 1
            return type('', (), {"x": x, "y": y})()

        iterateOverWords()
