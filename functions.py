def find_all(string,letter):
  indexes = []
  for indx,char in enumerate(string):
    if char == letter:
      indexes.append(indx)
  return indexes
