init:
    python in namereentry_four:
        def save_changes():
            player_name = renpy.store.persistent.player_name
            renpy.store.player_name = player_name
            renpy.store.mp.player_name = player_name

            renpy.store.mp.save()

    screen namereentry_four_colorbutton(color,colorname):
        button:
            child frame background Solid(color[1:]) #size (50,50)
            action [
                # SetVariable("playercolorname", colorname),
                # SetVariable("playercolor", color),
                SetField(persistent,"playercolorname",colorname),
                SetField(persistent,"playercolor",color),
                SetField(mp,"playercolorname",colorname),
                SetField(mp,"playercolor",color),
            ]


    screen namereentry_four:
        modal True
        window id "namereentry_four" at popup2:
            xfill True
            style "smallwindow"
            frame at center:
                background None
                top_padding 50

                has vbox
                hbox:
                    text "Name: "
                    input:
                        length 50
                        exclude '{%,[,]}'
                        value FieldInputValue(persistent, 'player_name', default=True, returnable=False)
                        color persistent.playercolor

                # for colorname,col in [("blue","#0000FF"), ("red","#FF0000"), ("yellow","#FFFF00"), ("green","#008000"), ("gray", "#d3d3d3"), ("cyan","#00FFFF"), ("magenta","#FF00FF"), ("lime","#00FF00"), ("orange","#ffa500"), ("white","#FFFFFF"), ("gold", "#ffd700"), ("silver", "#c0c0c0"), ("brass", "#b5a642"), ("bronze", "#cd7f32"), ("copper", "$cb6d51"), ("olive", "#808000"), ("brown", "#8b4513"), ("teal", "#008080"), ("purple", "#800080"), ("maroon", "#800000")]:
                #     python:
                #         if len(col) != 7:
                #             raise Exception("Color %s has length %d, not 7." % (col, len(col)))
                #     use namereentry_four_colorbutton(col,colorname)
                        
                textbutton _("Return") action [Play("audio","se/sounds/close.ogg"), namereentry_four.save_changes, Hide("namereentry_four")] hovered Play("audio","se/sounds/select.ogg") style "menubutton"