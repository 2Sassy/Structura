import json
import os


class animations:
    def __init__(self, path_to_default="Vanilla_Resource_Pack"):
        self.default_size = {"format_version": "1.8.0",
                             "animations": {"animation.armor_stand.ghost_blocks.scale": {
                                 "loop": True,
                                 "bones": {
                                     "ghost_blocks": {"scale": 16.0}}}}}
        pathtofile = f"{path_to_default}/animations/armor_stand.animation.json"
        with open(pathtofile) as f:
            self.sizing = json.load(f)
        self.poses = {
            0: "animation.armor_stand.default_pose",
            1: "animation.armor_stand.no_pose",
            2: "animation.armor_stand.solemn_pose",
            3: "animation.armor_stand.athena_pose",
            4: "animation.armor_stand.brandish_pose",
            5: "animation.armor_stand.honor_pose",
            6: "animation.armor_stand.entertain_pose",
            7: "animation.armor_stand.salute_pose",
            8: "animation.armor_stand.riposte_pose",
            9: "animation.armor_stand.zombie_pose",
            10: "animation.armor_stand.cancan_a_pose",
            11: "animation.armor_stand.cancan_b_pose",
            12: "animation.armor_stand.hero_pose",
        }

    def insert_layer(self, y):
        name = f"layer_{y}"
        # self.sizing["animations"][self.poses[0]]["bones"][name]={"scale":16}
        for i in range(12):
            if y % (12) != i:
                # self.sizing["animations"][self.poses[i+1]]["bones"][name]={"scale":16}
                self.sizing["animations"][self.poses[i+1]
                                          ]["bones"][name] = {"scale": 0.08}

    def export(self, pack_name):
        path_to_ani = f"{pack_name}/animations/armor_stand.animation.json"
        try:

            os.makedirs(os.path.dirname(path_to_ani), exist_ok=True)
        except:
            pass
        with open(path_to_ani, "w+") as json_file:
            json.dump(self.sizing, json_file, indent=2)
        path_to_rc = (
            f"{pack_name}/animations/armor_stand.ghost_blocks.scale.animation.json"
        )
        try:
            os.makedirs(os.path.dirname(path_to_rc), exist_ok=True)
        except:
            pass
        with open(path_to_rc, "w+") as json_file:
            json.dump(self.default_size, json_file, indent=2)
