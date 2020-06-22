age = int(input())
print('Lion King' if age < 17 else
      "Trainspotting" if 16 < age < 26 else
      'Matrix' if 25 < age < 41 else
      'Pulp Fiction' if 40 < age < 61 else
      "Breakfast at Tiffany's")
