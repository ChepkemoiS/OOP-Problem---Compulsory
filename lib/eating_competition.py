def create_scoreboard(participants):
    for participant in participants:
        # Calculate the score for each participant
        participant['score'] = participant['chickenwings'] * 5 + \
                                participant['hamburgers'] * 3 + \
                                participant['hotdogs'] * 2
    
    # Sort the participants by score (in descending order)
    # and alphabetically by name (in lexicographic order)
    sorted_participants = sorted(
        participants,
        key=lambda x: (-x['score'], x['name']),
    )
    
    # Remove the 'score' property from each participant
    for participant in sorted_participants:
        del participant['score']

    return sorted_participants