import random
import math

def simulate_plate_appearance(outcome_probabilities):
    outcomes = ['single', 'double', 'triple', 'home_run', 'walk', 'strikeout', 'out']
    outcome = random.choices(outcomes, outcome_probabilities)[0]
    return outcome

def simulate_half_inning():
    runs_away = 0
    runs_home = 0
    outs_away, outs_home = 0, 0
    first, second, third = 0, 0, 0

    outcome_probabilities = [0.158, 0.207, 0.212, 0.241, 0.334, 0.499, 0.984]
    
    while outs_away < 3:
        result = math.ceil(random.random())
        plate_appearance = simulate_plate_appearance(outcome_probabilities)

        if plate_appearance == 'single':
            if first == 0 and second == 0 and third == 0:
                first = 1
            elif first == 1 and second == 0 and third == 0:
                first, second = 1, 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 1, 1, 1
                runs_away += 1
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 1, 1, 0
                runs_away += 1
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 1, 1, 1
                runs_away += 1
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 1, 0, 1
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 1, 0, 1
                runs_away += 1
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 1, 0, 0
                runs_away += 1
        elif plate_appearance == 'double':
            # Logic for doubles (advance two bases)
            if first == 0 and second == 0 and third == 0:
                first, second = 0, 1
            elif first == 1 and second == 0 and third == 0:
                first, second, third = 0, 1, 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 0, 1, 1
                runs_away += 1
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 0, 1, 1
                runs_away += 1
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 0, 1, 1
                runs_away += 2
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 0, 1, 0
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 0, 1, 0
                runs_away += 2
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 0, 1, 0
                runs_away += 1
        elif plate_appearance == 'triple':
            # Logic for triples (advance three bases)
            if first == 0 and second == 0 and third == 0:
                first, second, third = 0, 0, 1
            elif first == 1 and second == 0 and third == 0:
                first, second, third = 0, 0, 1
                runs_away += 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 0, 0, 1
                runs_away += 2
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 0, 0, 1
                runs_away += 2
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 0, 0, 1
                runs_away += 3
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 0, 0, 1
                runs_away += 1
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 0, 0, 1
                runs_away += 2
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 0, 0, 1
                runs_away += 1
        elif plate_appearance == 'home_run':
            # Logic for home runs (all runners score)
            if first == 1 and second == 1 and third == 1:
                first, second, third = 0, 0, 0
                runs_away += 4
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 0, 0, 0
                runs_away += 3
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 0, 0, 0
                runs_away += 3
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 0, 0, 0
                runs_away += 3
            elif first == 1 and second == 0 and third == 0:
                first, second, third = 0, 0, 0
                runs_away += 2
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 0, 0, 0
                runs_away += 2
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 0, 0, 0
                runs_away += 2
            elif first == 0 and second == 0 and third == 0:
                first, second, third = 0, 0, 0
                runs_away += 1
        elif plate_appearance == 'walk':
            # Logic for walks
            if first == 0 and second == 0 and third == 0:
                first = 1
            elif first == 1 and second == 0 and third == 0:
                first, second = 1, 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 1, 1, 1
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 1, 1, 1
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 1, 1, 1
                runs_away += 1
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 1, 1, 0
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 1, 1, 1
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 1, 0, 1
                
        elif plate_appearance == 'strikeout':
           
            if random.choice([True, False]):  
                outs_away += 1
            else:
                outs_home += 1

    return runs_away

    while outs_home < 3:
        result = math.ceil(random.random())
        plate_appearance = simulate_plate_appearance(outcome_probabilities)

        if plate_appearance == 'single':
            if first == 0 and second == 0 and third == 0:
                first = 1
            elif first == 1 and second == 0 and third == 0:
                first, second = 1, 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 1, 1, 1
                runs_home += 1
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 1, 1, 0
                runs_home += 1
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 1, 1, 1
                runs_home += 1
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 1, 0, 1
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 1, 0, 1
                runs_home += 1
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 1, 0, 0
                runs_home += 1
        elif plate_appearance == 'double':
            # Logic for doubles (advance two bases)
            if first == 0 and second == 0 and third == 0:
                first, second = 0, 1
            elif first == 1 and second == 0 and third == 0:
                first, second, third = 0, 1, 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 0, 1, 1
                runs_home += 1
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 0, 1, 1
                runs_home += 1
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 0, 1, 1
                runs_home += 2
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 0, 1, 0
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 0, 1, 0
                runs_home += 2
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 0, 1, 0
                runs_home += 1
        elif plate_appearance == 'triple':
            # Logic for triples (advance three bases)
            if first == 0 and second == 0 and third == 0:
                first, second, third = 0, 0, 1
            elif first == 1 and second == 0 and third == 0:
                first, second, third = 0, 0, 1
                runs_home += 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 0, 0, 1
                runs_home += 2
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 0, 0, 1
                runs_home += 2
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 0, 0, 1
                runs_home += 3
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 0, 0, 1
                runs_home += 1
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 0, 0, 1
                runs_home += 2
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 0, 0, 1
                runs_home += 1
        elif plate_appearance == 'home_run':
            # Logic for home runs (all runners score)
            if first == 1 and second == 1 and third == 1:
                first, second, third = 0, 0, 0
                runs_home += 4
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 0, 0, 0
                runs_home += 3
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 0, 0, 0
                runs_home += 3
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 0, 0, 0
                runs_home += 3
            elif first == 1 and second == 0 and third == 0:
                first, second, third = 0, 0, 0
                runs_home += 2
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 0, 0, 0
                runs_home += 2
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 0, 0, 0
                runs_home += 2
            elif first == 0 and second == 0 and third == 0:
                first, second, third = 0, 0, 0
                runs_home += 1
        elif plate_appearance == 'walk':
            # Logic for walks
            if first == 0 and second == 0 and third == 0:
                first = 1
            elif first == 1 and second == 0 and third == 0:
                first, second = 1, 1
            elif first == 1 and second == 1 and third == 0:
                first, second, third = 1, 1, 1
            elif first == 1 and second == 0 and third == 1:
                first, second, third = 1, 1, 1
            elif first == 1 and second == 1 and third == 1:
                first, second, third = 1, 1, 1
                runs_home += 1
            elif first == 0 and second == 1 and third == 0:
                first, second, third = 1, 1, 0
            elif first == 0 and second == 1 and third == 1:
                first, second, third = 1, 1, 1
            elif first == 0 and second == 0 and third == 1:
                first, second, third = 1, 0, 1
                
        elif plate_appearance == 'strikeout':
           
            if random.choice([True, False]):  
                outs_away += 1
            else:
                outs_home += 1

    return runs_home

def simulate_extra_innings():
    
    probability_extended_inning = 0.5  

    away_score = 0
    home_score = 0
    total_innings = 9  

    
    for inning in range(10, 20):  
        
        if random.random() < probability_extended_inning:
           
            runs_away = simulate_half_inning()
            runs_home = simulate_half_inning()

           
            away_score += runs_away
            home_score += runs_home

           
            total_innings += 1

        
    return away_score, home_score, total_innings

    


final_away_score, final_home_score, total_innings = simulate_extra_innings()

print(f"Final Away Score: {final_away_score}")
print(f"Final Home Score: {final_home_score}")
print(f"Total Number of Innings: {total_innings}")
