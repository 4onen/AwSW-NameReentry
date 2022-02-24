init:
    python in namereentry_four:
        def save_namechange():
            player_name = renpy.store.player_name
            renpy.store.persistent.player_name = player_name
            renpy.store.mp.player_name = player_name
            renpy.store.mp.save()
            renpy.restart_interaction()

        # This is semi-duplicated from renpy/common/00action_data.rpy, but with more fields.
        @renpy.pure
        class SetPlayercolor(renpy.store.Action, renpy.store.FieldEquality):
            """
            :doc: data_action

            Causes the a field on an object to be set to a given value.
            `object` is the object, `field` is a string giving the name of the
            field to set, and `value` is the value to set it to.
            """

            identity_fields = [ "color", "colorname" ]
            equality_fields = [ "color", "colorname" ]

            def __init__(self, color, colorname):
                self.color = color
                self.colorname = colorname

            def __call__(self):
                setattr(renpy.store, 'playercolor', self.color)
                setattr(renpy.store, 'playercolorname', self.colorname)

                c = getattr(renpy.store,'c',None)
                if c is not None:
                    c.who_args['color'] = self.color

                renpy.store.persistent.playercolorname = self.colorname
                renpy.store.persistent.playercolor = self.color
                renpy.store.mp.playercolorname = self.colorname
                renpy.store.mp.playercolor = self.color
                renpy.store.mp.save()
                renpy.restart_interaction()

            def get_selected(self):
                return getattr(renpy.store, 'playercolorname', None) == self.colorname

    screen namereentry_four tag smallscreen2:
        modal True
        window id "namereentry_four" at popup2:
            style "smallwindow"
            if getattr(renpy.store,'player_name',None) is not None:
                vbox:
                    align (0.5, 0.5)
                    spacing 50

                    hbox:
                        xalign 0.5
                        spacing 50
                        text "Current Name:" size 50
                        text "[renpy.store.persistent.player_name]" size 50 color playercolor

                    hbox:
                        xalign 0.5
                        spacing 50
                        input:
                            xalign 0.5
                            size 60
                            length 50
                            exclude '{%,[,]}'
                            value VariableInputValue('player_name')
                            color playercolor

                        textbutton "Change Name":
                            style "menubutton"
                            action [namereentry_four.save_namechange]

                    hbox:
                        xalign 0.5
                        spacing 3
                        for colorname,col in [("blue","#0000FF"), ("red","#FF0000"), ("yellow","#FFFF00"), ("green","#008000"), ("gray", "#d3d3d3"), ("cyan","#00FFFF"), ("magenta","#FF00FF"), ("lime","#00FF00"), ("orange","#ffa500"), ("white","#FFFFFF"), ("gold", "#ffd700"), ("silver", "#c0c0c0"), ("brass", "#b5a642"), ("bronze", "#cd7f32"), ("copper", "#cb6d51"), ("olive", "#808000"), ("brown", "#8b4513"), ("teal", "#008080"), ("purple", "#800080"), ("maroon", "#800000")]:
                            button:
                                background Solid(col)
                                xysize (50,50)
                                action namereentry_four.SetPlayercolor(col,colorname)
                imagebutton:
                    idle "image/ui/close_idle.png"
                    hover "image/ui/close_hover.png"
                    action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")]
                    hovered Play("audio", "se/sounds/select.ogg")
                    style "smallwindowclose"
                    at nav_button
            else:
                vbox:
                    xfill True
                    spacing 50
                    text _("User profile not found.") xalign 0.5
                    text _("Please enter create a user profile by clicking START from the main menu.") xalign 0.5
                imagebutton:
                    idle "image/ui/close_idle.png"
                    hover "image/ui/close_hover.png"
                    action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")]
                    hovered Play("audio", "se/sounds/select.ogg")
                    style "smallwindowclose"
                    at nav_button

label namereentry_four:
    label .before_main_menu:
        python in namereentry_four:
            if renpy.store.persistent.player_name is not None:
                renpy.store.player_name = renpy.store.persistent.player_name
            if renpy.store.persistent.playercolor is not None:
                renpy.store.playercolor = renpy.store.persistent.playercolor
                renpy.store.playercolorname = renpy.store.persistent.playercolorname
        jump namereentry_four.before_main_menu_return