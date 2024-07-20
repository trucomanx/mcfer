#!/usr/bin/python3

import extras

DIR_BASE="../archive/train";

################################################################################

TRAIN={
    "negative": [
        "../archive/train/angry/angry-contempt",
        "../archive/train/angry/angry-disapproval",
        "../archive/train/angry/angry-frowning",
        "../archive/train/angry/attention-angry",
        "../archive/train/angry/clenching-teeth",
        "../archive/train/angry/hateful-look",
        "../archive/train/angry/steam-nose-face",
        "../archive/train/disgusted",
        "../archive/train/fearful",
        "../archive/train/sad",
        "../archive/train/surprised/surprised-fearful",
        "../archive/train/surprised/surprised-neutral"
    ],
    "neutral": [
        "../archive/train/neutral"
    ],
    "pain": [
        "../archive/train/surprised/surprised-fearful-terrified",
        "../archive/train/angry/baring-fangs",
        "../archive/train/angry/furious-scream",
        "../archive/train/angry/scolding"
    ],
    "positive": [
        "../archive/train/happy",
        "../archive/train/surprised/surprised-happy"
    ]
};

TRAIN_FILE='../archive/train/train.emotion4.csv';

extras.generate_dict(TRAIN, TRAIN_FILE, dir_base=DIR_BASE,format_list=[".png"], header=['filename', 'label'])


################################################################################

TEST={
    "negative": [
        "../archive/test/angry/angry-contempt",
        "../archive/test/angry/angry-disapproval",
        "../archive/test/angry/angry-frowning",
        "../archive/test/angry/attention-angry",
        "../archive/test/angry/clenching-teeth",
        "../archive/test/angry/hateful-look",
        "../archive/test/angry/steam-nose-face",
        "../archive/test/disgusted",
        "../archive/test/fearful",
        "../archive/test/sad",
        "../archive/test/surprised/surprised-fearful",
        "../archive/test/surprised/surprised-neutral"
    ],
    "neutral": [
        "../archive/test/neutral"
    ],
    "pain": [
        "../archive/test/surprised/surprised-fearful-terrified",
        "../archive/test/angry/baring-fangs",
        "../archive/test/angry/furious-scream",
        "../archive/test/angry/scolding"
    ],
    "positive": [
        "../archive/test/happy",
        "../archive/test/surprised/surprised-happy"
    ]
};

TEST_FILE='../archive/test/test.emotion4.csv';

extras.generate_dict(TEST, TEST_FILE, dir_base=DIR_BASE,format_list=[".png"], header=['filename', 'label'])

