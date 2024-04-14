static const char norm_fg[] = "#e6d2f1";
static const char norm_bg[] = "#12121b";
static const char norm_border[] = "#a193a8";

static const char sel_fg[] = "#e6d2f1";
static const char sel_bg[] = "#F18EAC";
static const char sel_border[] = "#e6d2f1";

static const char urg_fg[] = "#e6d2f1";
static const char urg_bg[] = "#F8BD96";
static const char urg_border[] = "#F8BD96";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
