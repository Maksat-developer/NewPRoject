# Task 7
def biggest_guy(age, age1, age2):
  if age > age1 and age > age2:
    return age
  elif age1 > age and age1 > age2:
    return age1
  else:
    return age2
def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'

  except (AssertionError) as e:
    print(e)
    print("Wrong!!")

print("Correct buddy!!!")
test_biggest_guy()
