with open('input.txt') as f:
    puzzle = [list(line) for line in f.read().splitlines()]

word = "XMAS"

def traverse(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    if grid[row][col] != word[0]:
        return []
    
    word_length = len(word)

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    results = []

    for dir in range(8):
        currX, currY = row + x[dir], col + y[dir]
        k = 1

        while k < word_length:
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break
            if grid[currX][currY] != word[k]:
                break
            currX += x[dir]
            currY += y[dir]
            k += 1

        if k == word_length:
            results.append((row, col, dir))
        
    return results

def search_word(grid, word):
    m = len(grid)
    n = len(grid[0])

    occurrences = []

    for i in range(m):
        for j in range(n):
            occurrences += traverse(grid, i, j, word)

    return occurrences

words = search_word(puzzle, word)

print(f"Number of occurrences of 'XMAS': {len(words)}")