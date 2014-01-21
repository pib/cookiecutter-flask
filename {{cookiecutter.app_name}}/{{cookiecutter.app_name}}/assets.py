# -*- coding: utf-8 -*-
from flask.ext.assets import Bundle, Environment

css = Bundle(
    "css/style.scss",
    filters="scss",
    output="public/css/common.css"
)

js_top = Bundle(
    "libs/modernizr/modernizr.js",
)

js = Bundle(
    "libs/jquery/jquery-1.10.2.min.js",
    "libs/fastclick/fastclick.js",
    "libs/placeholder/placeholder.js",

    # Foundation components, those which aren't used can be removed
    "libs/foundation5/js/foundation/foundation.js",
    "libs/foundation5/js/foundation/foundation.abide.js",
    "libs/foundation5/js/foundation/foundation.accordion.js",
    "libs/foundation5/js/foundation/foundation.alert.js",
    "libs/foundation5/js/foundation/foundation.clearing.js",
    "libs/foundation5/js/foundation/foundation.dropdown.js",
    "libs/foundation5/js/foundation/foundation.interchange.js",
    "libs/foundation5/js/foundation/foundation.joyride.js",
    "libs/foundation5/js/foundation/foundation.magellan.js",
    "libs/foundation5/js/foundation/foundation.offcanvas.js",
    "libs/foundation5/js/foundation/foundation.orbit.js",
    "libs/foundation5/js/foundation/foundation.reveal.js",
    "libs/foundation5/js/foundation/foundation.tab.js",
    "libs/foundation5/js/foundation/foundation.tooltip.js",
    "libs/foundation5/js/foundation/foundation.topbar.js",

    "js/plugins.js",
    "js/script.js",
    filters="jsmin",
    output="public/js/common.js",
)

assets = Environment()

assets.register("js_top", js_top)
assets.register("js_bottom", js)
assets.register("css_all", css)
