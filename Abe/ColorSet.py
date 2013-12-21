# Copyright(C) 2011,2012,2013 by Abe developers.

# ColorSet.py: similar to ngcccbase/coloredcoinlib/colorset.py with many fewer features.


import hashlib
import json

def deterministic_json_dumps(obj):
    """TODO: make it even more deterministic!"""
    return json.dumps(obj, separators=(',', ':'), sort_keys=True)


class ColorSet(object):
    def __init__(self, color_desc_list):
        self.color_desc_list = color_desc_list

    def get_hash_string(self):
        """Returns a deterministic string for this color set.
        Useful for creating deterministic addresses for a given color.
        """
        json = deterministic_json_dumps(sorted(self.color_desc_list))
        return hashlib.sha256(json).hexdigest()

