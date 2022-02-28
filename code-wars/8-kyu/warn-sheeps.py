def warn_the_sheep(queue):
    if queue.index('wolf') == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number " + str(len(queue)- 1 - queue.index('wolf')) + "! You are about to be eaten by a wolf!"