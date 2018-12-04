from collections import defaultdict


def parse_claim(line):
  data = line.split()
  claim_id = data[0][1:]
  claim_x = data[2].split(',')[0]
  claim_y = data[2].split(',')[1][0:-1]
  claim_width = data[3].split('x')[0]
  claim_length = data[3].split('x')[1]
  return {"id": claim_id,"x": int(claim_x), "y": int(claim_y),"width": int(claim_width),"length": int(claim_length)}

def fill_board(claim, board, count, not_overlapped):
  overlapped = False
  for row in range(claim["x"], claim["x"] + claim["width"]):
    for box in range(claim["y"], claim["y"] + claim["length"]):
        if len(board[row][box]) == 1:
          count += 1
        if len(board[row][box]) >= 1:
          overlapped = True
          for claim_id in board[row][box]:
            if claim_id in not_overlapped:
              not_overlapped.remove(claim_id)
        board[row][box].append(claim["id"])
  if not overlapped:
    not_overlapped.append(claim["id"])
  return board, count, not_overlapped

with open('input.txt', 'r') as f:
  data = f.read()
  board = [[[] for _ in range(1000)] for _ in range(1000)]
  count = 0
  not_overlapped = []
  for claim in data.split('\n'):
    pclaim = parse_claim(claim)
    board, count, not_overlapped = fill_board(pclaim, board, count, not_overlapped)
  print(count)
  print(not_overlapped)