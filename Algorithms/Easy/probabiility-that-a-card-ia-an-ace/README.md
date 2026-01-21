### Problem Description

You have a shuffled deck of cards, which consists of 52 cards with 4 suits: clubs, diamonds, hearts, and spades. Each suit has the same number of 13 cards: 'A', '2', '3', ..., '10', 'J', 'Q', 'K'. 

Write a function `solution(deck)` that calculates the probability that a randomly drawn card from the given `deck` is an ace.

### Input Format
- `deck`: a list of strings, where each string represents a card in the format of 'AS' (Ace of Spades), '10H' (Ten of Hearts), etc. (Any order).

### Output Format
- Return a float representing the probability of drawing an ace from the deck. The result should be rounded to two decimal places.

### Example

```python
solution(['AS', '2H', '3D', 'AC'])
```

Output:
```python
0.5
```

### Constraints
- You may assume `deck` contains at least 1 card and at most 52 cards.