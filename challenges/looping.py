shows = ["Succession", "White Lotus", "The Crown", "Friends", "Arrested Development"]

for x in shows:
    word_list = x.split()
    if len(word_list) <= 2:
        print(x)

times_watched = [1, 3, 5, 10, 2]

if len(shows) == len(times_watched):
    show_times = {}
    for i in range(len(shows)):
        show_times[shows[i]] = times_watched[i]

print(show_times)

for show, time in show_times.items():
    print(show, time)

print(dict(zip(shows, times_watched)))
