#!/usr/bin/python3

import extras

DIR_BASE="../archive/train";

################################################################################

TRAIN={
    "angry":     [ "../archive/train/angry" ],
    "disgusted": [ "../archive/train/disgusted" ],
    "fearful":   [ "../archive/train/fearful" ],
    "happy":     [ "../archive/train/happy" ],
    "neutral":   [ "../archive/train/neutral" ],
    "sad":       [ "../archive/train/sad" ],
    "surprised": [ "../archive/train/surprised" ]
};

TRAIN_FILE='../archive/train/training_labels.csv';

extras.generate_dict(TRAIN, TRAIN_FILE, dir_base=DIR_BASE,format_list=[".png"], header=['filename', 'label']);

################################################################################

TEST={
    "angry":     [ "../archive/test/angry" ],
    "disgusted": [ "../archive/test/disgusted" ],
    "fearful":   [ "../archive/test/fearful" ],
    "happy":     [ "../archive/test/happy" ],
    "neutral":   [ "../archive/test/neutral" ],
    "sad":       [ "../archive/test/sad" ],
    "surprised": [ "../archive/test/surprised" ]
};

TEST_FILE='../archive/test/test_labels.csv';

extras.generate_dict(TEST, TEST_FILE, dir_base=DIR_BASE,format_list=[".png"], header=['filename', 'label']);

