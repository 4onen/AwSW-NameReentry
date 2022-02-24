from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AwSWMod(Mod):    
    name = "Name Reentry"
    version = "v0.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    @staticmethod
    def mod_load():
        ( ml.Overlay()
            .add(['imagebutton auto "image/ui/namereentry_four_button_%s.png":'\
                 ,'    xalign 0.333'\
                 ,'    yalign 0.965'\
                 ,'    action [Show("namereentry_four", transition=dissolve), Play("audio", "se/sounds/open.ogg")]'\
                 ,'    hovered Play("audio", "se/sounds/select.ogg")'\
                ])
            .compile_to("main_menu")
        )

    @staticmethod
    def mod_complete():
        pass
