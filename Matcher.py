import cv2
from Constants import global_constants as constants

match_methods = [
    'cv2.TM_CCOEFF_NORMED',
    'cv2.TM_CCORR_NORMED',
    'cv2.TM_SQDIFF_NORMED']


def match_one(image_path, template_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)
    return [cv2.matchTemplate(template, image, eval(m)) for m in match_methods]


def get_score(results):
    scores = dict()
    for i in range(0, len(constants.forbidden_strings)):
        text = constants.forbidden_strings[i]
        scores[text] = dict()
        for j in range(0, len(match_methods)):
            min_val, max_val, _, _ = cv2.minMaxLoc(results[i][j])
            method = match_methods[j]
            if method == 'cv2.TM_SQDIFF_NORMED':
                max_val = 1 - min_val
            scores[text][method] = max_val
    return scores


def match(image_path, templates):
    results = [match_one(image_path, t) for t in templates]
    print(get_score(results))
