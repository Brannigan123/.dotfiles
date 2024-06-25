static const char norm_fg[] = "#c9e1ec";
static const char norm_bg[] = "#00141D";
static const char norm_border[] = "#8c9da5";

static const char sel_fg[] = "#c9e1ec";
static const char sel_bg[] = "#29B6F6";
static const char sel_border[] = "#c9e1ec";

static const char urg_fg[] = "#c9e1ec";
static const char urg_bg[] = "#279BCF";
static const char urg_border[] = "#279BCF";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
