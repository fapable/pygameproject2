#### dit staat in de player class



def winner(self):
        if (self.pos.x, self.pos.y) == (16, 30) and self.moves == 0 and self.turn and self.alive and dubbel(self.namet) == False:
            # upload winner screen
            self.score += 10
            insert_naam(self.namet, self.score)
            update_score(self.namet, self.score)
        elif (self.pos.x, self.pos.y) == (16, 30) and self.moves == 0 and self.turn and self.alive :
            self.score += 10
            update_score(self.namet, self.score)
########################################
### vergeet niet aanteroepen voor elke speler###
