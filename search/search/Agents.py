import random
from game import Agent
from game import Directions

class DumbAgent(Agent):

 def getAction(self, state):

    print("Location: ", state.getPacmanPosition())
    print("Actions available:", state.getLegalPacmanActions())
    if Directions.WEST in state.getLegalPacmanActions():
        print("Going West.")
        return Directions.WEST
    else:
        print("Stopping.")
        return Directions.STOP





class BetteRandomAgent(Agent):

 def getAction(self, state):

    print("Location: ", state.getPacmanPosition())
    print("Actions available:", state.getLegalPacmanActions())
    legal_actions = state.getLegalPacmanActions()

    if Directions.STOP in legal_actions:
        legal_actions.remove(Directions.STOP)

    chosen_action = random.choice(legal_actions)
    print(f"Chosen action: {chosen_action}")

    return chosen_action



class RandomAgent(Agent):

     def getAction(self, state):
         print("Location: ", state.getPacmanPosition())
         print("Actions available:", state.getLegalPacmanActions())
         legal_actions = state.getLegalPacmanActions()

         chosen_action = random.choice(legal_actions)
         print(f"Chosen action: {chosen_action}")

         return chosen_action







class ReflexAgent(Agent):
    def getAction(self, state):
        """
        Verilen bir oyun durumu için, reflex agent'ın alacağı aksiyonu döndürür.
        """
        # Pac-Man'in mevcut pozisyonu ve yasal aksiyonlar
        print("Location: ", state.getPacmanPosition())
        legal_actions = state.getLegalPacmanActions()

        # 'Stop' aksiyonunu yasal aksiyonlardan çıkar
        if Directions.STOP in legal_actions:
            legal_actions.remove(Directions.STOP)

        # 4 yönü kontrol et: Kuzey, Güney, Doğu, Batı
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            if action in legal_actions:
                successor_state = state.generatePacmanSuccessor(action)  # Bu aksiyonu aldıktan sonraki durum
                new_position = successor_state.getPacmanPosition()  # Pac-Man'in yeni pozisyonu
                food_grid = successor_state.getFood()  # Yeni durumdaki yemek grid'i

                # Yeni pozisyonda yemek var mı?
                if food_grid[new_position[0]][new_position[1]]:
                    print(f"Chosen action: {action} (Food eaten)")
                    return action
        chosen_action = random.choice(legal_actions)
        print(f"Chosen action: {chosen_action} (No food eaten)")

        return chosen_action
        # Eğer hiç yemek yenmezse, rastgele bir yasal aksiyon seç

