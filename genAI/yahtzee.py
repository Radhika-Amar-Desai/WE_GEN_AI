def score(dice):
    categories = {
        "Ones": sum(d for d in dice if d == 1),
        "Twos": sum(d for d in dice if d == 2),
        "Threes": sum(d for d in dice if d == 3),
        "Fours": sum(d for d in dice if d == 4),
        "Fives": sum(d for d in dice if d == 5),
        "Sixes": sum(d for d in dice if d == 6),
        "Three of a Kind": sum(dice) if any(dice.count(d) >= 3 for d in dice) else 0,
        "Four of a Kind": sum(dice) if any(dice.count(d) >= 4 for d in dice) else 0,
        "Full House": sum(dice) if any(dice.count(d) == 3 for d in dice) and any(dice.count(d) == 2 for d in dice) else 0,
        "Small Straight": 30 if sorted(set(dice)) in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]] else 0,
        "Large Straight": 40 if sorted(set(dice)) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]] else 0,
        "Yahtzee": 50 if any(dice.count(d) == 5 for d in dice) else 0,
        "Chance": sum(dice)
    }
    return categories

test_cases = [([1, 1, 2, 3, 4], {'Ones': 2, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 11}), 
               ([2, 2, 3, 3, 3], {'Ones': 0, 'Twos': 4, 'Threes': 9, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 13, 'Four of a Kind': 0, 'Full House': 13, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 13}), 
               ([4, 4, 4, 4, 5], {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 16, 'Fives': 5, 'Sixes': 0, 'Three of a Kind': 21, 'Four of a Kind': 21, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 21}), 
               ([1, 2, 3, 4, 5], {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 40, 'Yahtzee': 0, 'Chance': 15}), 
               ([6, 6, 6, 6, 6], {'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 30, 'Three of a Kind': 30, 'Four of a Kind': 30, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 50, 'Chance': 30}), 
               ([1, 2, 3, 4, 6], {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 0, 'Sixes': 6, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 16}), 
               ([3, 3, 3, 4, 4], {'Ones': 0, 'Twos': 0, 'Threes': 9, 'Fours': 8, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 17, 'Four of a Kind': 0, 'Full House': 17, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 17}), 
               ([1, 1, 2, 2, 3], {'Ones': 2, 'Twos': 4, 'Threes': 3, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 9}), 
               ([3, 3, 4, 4, 5], {'Ones': 0, 'Twos': 0, 'Threes': 6, 'Fours': 8, 'Fives': 5, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 19}), 
               ([2, 2, 3, 4, 4], {'Ones': 0, 'Twos': 4, 'Threes': 3, 'Fours': 8, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 15}), 
               ([1, 1, 1, 1, 1], {'Ones': 5, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 5, 'Four of a Kind': 5, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 50, 'Chance': 5}), 
               ([2, 3, 4, 5, 5], {'Ones': 0, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 10, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 19}), 
               ([1, 1, 2, 2, 2], {'Ones': 2, 'Twos': 6, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 8, 'Four of a Kind': 0, 'Full House': 8, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 8}), 
               ([2, 3, 4, 5, 5], {'Ones': 0, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 10, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 19}), 
               ([3, 4, 5, 6, 6], {'Ones': 0, 'Twos': 0, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 12, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 24}), 
               ([1, 2, 2, 3, 3], {'Ones': 1, 'Twos': 4, 'Threes': 6, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 11}), 
               ([2, 2, 3, 3, 4], {'Ones': 0, 'Twos': 4, 'Threes': 6, 'Fours': 4, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 14}), 
               ([1, 1, 3, 3, 3], {'Ones': 2, 'Twos': 0, 'Threes': 9, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 11, 'Four of a Kind': 0, 'Full House': 11, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 11}), 
               ([1, 1, 1, 1, 2], {'Ones': 4, 'Twos': 2, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 6, 'Four of a Kind': 6, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 6}), 
               ([2, 3, 3, 4, 5], {'Ones': 0, 'Twos': 2, 'Threes': 6, 'Fours': 4, 'Fives': 5, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 17}), 
               ([2, 3, 4, 5, 6], {'Ones': 0, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 40, 'Yahtzee': 0, 'Chance': 20}), 
               ([1, 2, 3, 4, 4], {'Ones': 1, 'Twos': 2, 'Threes': 3, 'Fours': 8, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 14}), 
               ([2, 3, 4, 5, 5], {'Ones': 0, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 10, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 30, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 19}), 
               ([1, 1, 2, 2, 3], {'Ones': 2, 'Twos': 4, 'Threes': 3, 'Fours': 0, 'Fives': 0, 'Sixes': 0, 'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 9}), 
               ([1, 1, 6, 1, 2], {'Ones': 3, 'Twos': 2, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 6, 'Three of a Kind': 11, 'Four of a Kind': 0, 'Full House': 0, 'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 11})]
# Perform testing
for i, (input_dice, expected_output) in enumerate(test_cases):
    # Calculate the output using the score function
    output = score(input_dice)
    
    # test_cases [ i ] = ( input_dice , output )

    if output == expected_output:
        print ( f"Test case {i + 1} : Passed." )
    else:
        print ( f"Test case {i + 1} : Failed." )
        print ( f"Expected output : {expected_output}" )
        print ( f"Your Output : {output}" )

# print ( test_cases )