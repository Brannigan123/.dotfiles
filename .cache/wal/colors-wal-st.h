const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#00141D", /* black   */
  [1] = "#279BCF", /* red     */
  [2] = "#29B6F6", /* green   */
  [3] = "#48B2E2", /* yellow  */
  [4] = "#4FC3F7", /* blue    */
  [5] = "#6ECEF9", /* magenta */
  [6] = "#89B4C8", /* cyan    */
  [7] = "#c9e1ec", /* white   */

  /* 8 bright colors */
  [8]  = "#8c9da5",  /* black   */
  [9]  = "#279BCF",  /* red     */
  [10] = "#29B6F6", /* green   */
  [11] = "#48B2E2", /* yellow  */
  [12] = "#4FC3F7", /* blue    */
  [13] = "#6ECEF9", /* magenta */
  [14] = "#89B4C8", /* cyan    */
  [15] = "#c9e1ec", /* white   */

  /* special colors */
  [256] = "#00141D", /* background */
  [257] = "#c9e1ec", /* foreground */
  [258] = "#c9e1ec",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
