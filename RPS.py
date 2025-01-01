def player(prev_play, opponent_history=[]):
    if not opponent_history:
        opponent_history.clear()
        
    opponent_history.append(prev_play)
    
    # Initialize ideal counters
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    # Default move for first play
    if not prev_play:
        return 'P'

    # Detect patterns in last 4 moves
    if len(opponent_history) > 4:
        last_four = ''.join(opponent_history[-4:])
        pattern_count = {}
        
        # Count pattern frequencies
        for i in range(len(opponent_history) - 4):
            pattern = ''.join(opponent_history[i:i+4])
            next_move = opponent_history[i+4]
            if pattern in pattern_count:
                if next_move in pattern_count[pattern]:
                    pattern_count[pattern][next_move] += 1
                else:
                    pattern_count[pattern][next_move] = 1
            else:
                pattern_count[pattern] = {next_move: 1}
        
        # Predict next move based on most common follow-up
        if last_four in pattern_count:
            prediction = max(pattern_count[last_four].items(), 
                           key=lambda x: x[1])[0]
            return ideal_response[prediction]
    
    # Fallback strategy - counter last move
    if prev_play:
        return ideal_response[prev_play]
        
    return 'P'