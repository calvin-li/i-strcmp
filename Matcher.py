import cv2

match_methods = [
    'cv2.TM_CCOEFF_NORMED',
    'cv2.TM_CCORR_NORMED',
    'cv2.TM_SQDIFF_NORMED'
    ]


def pprint(score):
    print(score["text"], end='\n\t')
    for m in match_methods:
        print("{:.3f}".format(score["values"][m]), end='\t')
    print("{:.3f}".format(score["maxValue"]))


def match(text, image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)
    result = [cv2.matchTemplate(template, image, eval(m)) for m in match_methods]
    score = get_score(text, result)
    pprint(score)
    return result, score["maxValue"]


def get_score(text, results):
    scores = dict()
    scores["text"] = text
    scores["values"] = dict()
    for j in range(0, len(match_methods)):
        min_val, max_val, _, _ = cv2.minMaxLoc(results[j])
        method = match_methods[j]
        if method == 'cv2.TM_SQDIFF_NORMED':
            max_val = 1 - min_val
        scores["values"][method] = max_val
    scores["maxValue"] = max(scores["values"].values())
    return scores
