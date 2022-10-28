from Character import Character
from roll_modifier import roll_modifier
class Fighter(Character):
    def __init__(self, Name, alignment, ability_scores, xp):
        strength = 11  #foo class changed default value(10) by: +1
        dexterity = 10
        constitution = 10 
        wisdom = 10
        intelligence = 10
        charisma = 10
        xp = 1000
        ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
        super().__init__(Name, alignment, ability_scores, xp)
        self.attack_roll_mod = 0 + int(self.level_number)
        self.hit_points = 5 + ((10 + roll_modifier(ability_scores[2])) * self.level_number)
        
class Butcher(Character):
    def __init__(self, Name, alignment, ability_scores, xp):
        strength = 12#foo class changed default value(10) by: +2
        dexterity = 12#foo class changed default value(10) by: +2
        constitution = 11#foo class changed default value(10) by: +1 
        wisdom = 7#foo class changed default value(10) by: -3
        intelligence = 7#foo class changed default value(10) by: 
        charisma = 6#foo class changed default value(10) by: +2
        xp = 1000
        ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
        super().__init__(Name, alignment, ability_scores, xp)
    def smoked_butt(self, target1, target2, roll):
        if target2.hit_points > 0:
            roll = int(roll + self.attack_roll_mod)
            if roll >= 20:
                return setattr(target2, 'hit_points', (int(target2.hit_points) - (int(target1.attack_points) * 2))), setattr(target1, 'xp', self.xp + 10)
            elif roll < 20 and roll > 1:
                return setattr(target2, 'hit_points', (int(target2.hit_points) - (int(target1.attack_points)))), setattr(target1, 'xp', self.xp + 10)
            elif roll == 1:
                print('you really suck')
        else: return setattr(target2, 'is_alive', False)
    def bone_breaker(self, target1, target2, roll):
        if target2.hit_points > 0:
            roll = int(roll + self.attack_roll_mod)
            if roll >= 20:
                return setattr(target2, 'hit_points', (int(target2.hit_points) - (int(target1.attack_points + 2) * 2))), setattr(target1, 'xp', self.xp + 10)
            elif roll < 20 and roll > 1:
                return setattr(target2, 'hit_points', (int(target2.hit_points) - (int(target1.attack_points + 2)))), setattr(target1, 'xp', self.xp + 10)
            elif roll == 1:
                print('you really suck')
        else: return setattr(target2, 'is_alive', False)

class senior_javascript_dev(Character):
    def __init__(self, Name, alignment, ability_scores, xp):
        strength = 8#foo class changed default value(10) by: -2
        dexterity = 9#foo class changed default value(10) by: -1
        constitution = 10 
        wisdom = 13#foo class changed default value(10) by: +3
        intelligence = 13#foo class changed default value(10) by: +3
        charisma = 10
        xp = 1000
        ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
        super().__init__(Name, alignment, ability_scores, xp)
        self.hit_points = 5 + ((2 + roll_modifier(ability_scores[2])) * self.level_number)
    def for_loop(self, target1, target2, roll):
        roll = int(roll + self.attack_roll_mod)
        if target2.hit_points > 0:
            if roll >= 20:
                test = target2.hit_points
                for x in range(1, 4):
                    test -= (int(target1.attack_points) * 2)
                return setattr(target2, 'hit_points', test)
            elif roll < 20 and roll > 1:
                test = target2.hit_points
                for x in range(1, 4):
                    test -= (int(target1.attack_points))
                return setattr(target2, 'hit_points', test)
            elif roll == 1:
                print('you really suck but 3 times')
        else: return setattr(target2, 'is_alive', False)
