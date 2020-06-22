no_of_units = int(input())
if no_of_units < 1:
    print('no army')
elif 1 <= no_of_units <= 9:
    print('few')
elif 9 < no_of_units < 50:
    print('pack')
elif 49 < no_of_units < 500:
    print('horde')
elif 499 < no_of_units < 1000:
    print('swarm')
else:
    print('legion')
