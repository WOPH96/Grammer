import pickle

profile_file = open("profile.pickle","wb")

profile = {"이름":"양원필","나이":27,"취미":["축구","코딩"]}

print(profile)

pickle.dump(profile,profile_file)

# profile_file = open("profile.pickle","rb")

# profile = pickle.load(profile_file)

# print(profile)

profile_file.close()


# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))