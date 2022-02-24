from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

def create_profile_button(depart_screen):
    return 

@loadable_mod
class AwSWMod(Mod):    
    name = "Name Reentry"
    version = "v0.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        ml.register_mod_settings(self,'namereentry_four')
        ( ml.find_label('before_main_menu')
            .hook_to('namereentry_four.before_main_menu')
        )

    @staticmethod
    def mod_complete():
        pass
