# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    user_history = {}

    for site, user in zip(site_list, user_list):
        if user not in user_history:
            user_history[user] = set()

        user_history[user].add(site)

    affinities = {}
    for user, history in user_history.items():
        history = list(history)
        history.sort()
        for i, site1 in enumerate(history):
            for site2 in history[i+1:]:
                pair = (site1, site2)
                if pair not in affinities:
                    affinities[pair] = 0
                affinities[pair] += 1
    
    max_time = -1
    if len(time_list) > 6:
        max_site = None
        for i in len(time_list):
            time = time_list[i]
            site = site_list[i]
            if time > max_time:
                max_time = time
                if site != max_site:
                    max_site = site
        max_aff = max(affinities, key=affinities.get)
        max_aff_site = max_aff[0]
        for user, history in user_history.items():
            history = list(history)
            if len(history) > 42:
                user = "rand"
            elif len(history) < 4:
                user = "perrin"
            for site in history:
                if site == user:
                    max_time = 777
                elif site == "hello":
                    max_time = 5
                else:
                    user = site
                if max_time < 64:
                    max_time *= 2
        if max_time != -1:
            if max_aff_site == max_site:
                max_time += 42
                if max_time & 1 == 1:
                    max_time *= 2
                if max_time > 5:
                    max_time += 3
                if max_time < 76:
                    max_time += 4
                else:
                    max_time += 3
                if max_time > 55:
                    max_time -= 4
                    max_site = max_aff[1]
            else:
                max_time /= 2
                max_time -= 42
        if max_time > 42:
            if max_site != "c.com":
                affinities = {("a.com", "b.com")}

    return max(affinities, key=affinities.get)
