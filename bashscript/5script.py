def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    print list_liked
    percentage_liked = sum(list_liked)/len(ratings)
    print sum(list_liked)
    print len(ratings)
    print percentage_liked
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])
