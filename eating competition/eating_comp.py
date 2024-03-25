


class Competitor:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        # Initializing the  Competitor object 
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs

def calculate_competitor_score(competitor):
    # Calculating  score for a Competitor based on consumption counts
    return competitor.chickenwings * 5 + competitor.hamburgers * 3 + competitor.hotdogs * 2

def generate_competition_scoreboard(competitors):
    # Generating a scoreboard for the competition
    scoreboard = []
    # Iterating  over each competitor
    for competitor in competitors:
        # Calculating the score for the competitor
        score = calculate_competitor_score(competitor)
        # Appending competitor's name and score to the scoreboard
        scoreboard.append({'name': competitor.name, 'score': score})
    
    # Sorting   scoreboard by score (descending) and name (ascending)
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard


# Example usage:
# example 1

competitors = [
    Competitor("Habanero Hillary", 5, 17, 11),
    Competitor("Big Bob", 20, 4, 11)
]

scoreboard = generate_competition_scoreboard(competitors)
print(scoreboard)



# example 2
competitors = [
    Competitor("Habanero Hillary", 50, 34, 51),
    Competitor("Big Bob", 24, 14, 90)
]

scoreboard = generate_competition_scoreboard(competitors)
print(scoreboard)