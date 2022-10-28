from Character import Character
from character_jobs import Fighter, Butcher, senior_javascript_dev

def test_fighter_exists():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    ryan = Fighter('Ryan', 'TheGoodGood', ability_scores, xp)
    assert ryan.is_alive == True

def test_fighter_has_attributes():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    ryan = Fighter('Ryan', 'TheGoodGood', ability_scores, xp)
    assert ryan.attack_roll_mod == 1

def test_fighter_has_custom_hp():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    ryan = Fighter('Ryan', 'TheGoodGood', ability_scores, xp)
    assert ryan.hit_points == 15

def test_custom_attributes():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    meme = Fighter('meme', 'bad guy', ability_scores, xp)
    assert meme.ability_scores[0] == 11

def test_butcher_and_attack():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    dabutcha = Butcher('dabutcha', 'best in the west', ability_scores, xp)
    victim = Character('nerd', 'dorkish', ability_scores, xp)
    dabutcha.smoked_butt(dabutcha, victim, 15)
    assert getattr(victim, 'hit_points') == 9

def test_butcher_custom_attributes():
    strength = 'we'
    dexterity = 'dont'
    constitution = 'actually' 
    wisdom = 'use'
    intelligence = 'these'
    charisma = '?'#we had mvp by the time we noticed this
    xp = 'one of the funny numbers'
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    dabutcha = Butcher('dabutcha', 'best in the west', ability_scores, xp)
    assert dabutcha.ability_scores[3] == 7, dabutcha.ability_scores[0] == 12

def test_butcher_bone_breaker():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    dabutcha = Butcher('dabutcha', 'best in the west', ability_scores, xp)
    victim = Character('nerd', 'dorkish', ability_scores, xp)
    dabutcha.bone_breaker(dabutcha, victim, 15)
    assert getattr(victim, 'hit_points') == 7

def test_is_senior_dev():
    strength = 'we'
    dexterity = 'dont'
    constitution = 'actually' 
    wisdom = 'use'
    intelligence = 'these'
    charisma = '?'#we had mvp by the time we noticed this
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    Justin_Hall = senior_javascript_dev('Justin Hall', 'The Code', ability_scores, xp)
    assert Justin_Hall != None

def test_is_senior_dev_and_forloop_crit():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    Justin_Hall = senior_javascript_dev('Justin Hall', 'The Code', ability_scores, xp)
    Logan_Hall = Character('Logan Hall', 'His Dad', ability_scores, xp)
    Justin_Hall.for_loop(Justin_Hall, Logan_Hall, 20)
    assert Logan_Hall.hit_points == 4

def test_senior_dev_forloop_normie():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    Josh_Stewart = senior_javascript_dev('Josh Stewart', 'To the Grind', ability_scores, xp)
    Michael_McGraw = Character('Michael McGraw', 'Oreos', ability_scores, xp)
    Josh_Stewart.for_loop(Josh_Stewart, Michael_McGraw, 10)
    Michael_McGraw.hit_points == 7

def test_random_fun():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    Logan_Hall = senior_javascript_dev('Logan', 'Technomancy', ability_scores, xp)
    Justin_Hall = senior_javascript_dev('Justin', 'The All Powerful Code', ability_scores, xp)
    Logan_Hall.for_loop(Logan_Hall, Justin_Hall, 20)
    Logan_Hall.for_loop(Logan_Hall, Justin_Hall, 15)
    Logan_Hall.for_loop(Logan_Hall, Justin_Hall, 11)
    assert Justin_Hall.is_alive == False
    # Logan_Hall.for_loop(Logan_Hall, Justin_Hall, 20)
