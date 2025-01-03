# Lab 10
# scores.py


# Purpose: make a dictionary given two lists
# Input: (must be of same length)
    # names: list of names given as strings
    # scores: list of scores given as ints
# Return: dictionary containing the name and score pairs
def make_dictionary(names, scores):
    score_dict = {}
    for index, name in enumerate(names):
        score_dict[name] = scores[index]
    return score_dict


def main():
    names = ['joe', 'tom', 'barb', 'sue', 'sally']
    scores = [10,23,13,18,12]

    name_score = make_dictionary(names, scores) 

    # 1
    print(f"Barb: {name_score['barb']}")  
    # 2
    name_score["john"] = 19    
    # 3
    sorted_scores = list(name_score.values())
    sorted_scores.sort()  # actually sorted by sort()
    print(f"Sorted: {sorted_scores}")  # print sorted scores

    # 4
    scores_total = 0
    for i in sorted_scores:
        scores_total += i
    print(f"Average: {scores_total/len(sorted_scores)}")

    # 5
    del name_score["tom"]

    # 6
    name_score["sally"] = 13

    # 7
    def get_score(name, dict):
        if name in dict.keys():
            return dict[name]
        else:
            return -1
    print(f"Testing get_score with joe: {get_score('joe', name_score)}")
    print(f"Testing get_score with tom: {get_score('tom', name_score)}")
    print(f"Testing get_score with joe: {get_score('sally', name_score)}")


if __name__ == "__main__":
    main()
    