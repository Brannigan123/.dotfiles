const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#12121b", /* black   */
  [1] = "#F8BD96", /* red     */
  [2] = "#F18EAC", /* green   */
  [3] = "#9FD7A7", /* yellow  */
  [4] = "#ABE9B3", /* blue    */
  [5] = "#9AB0D2", /* magenta */
  [6] = "#DDB6F2", /* cyan    */
  [7] = "#e6d2f1", /* white   */

  /* 8 bright colors */
  [8]  = "#a193a8",  /* black   */
  [9]  = "#F8BD96",  /* red     */
  [10] = "#F18EAC", /* green   */
  [11] = "#9FD7A7", /* yellow  */
  [12] = "#ABE9B3", /* blue    */
  [13] = "#9AB0D2", /* magenta */
  [14] = "#DDB6F2", /* cyan    */
  [15] = "#e6d2f1", /* white   */

  /* special colors */
  [256] = "#12121b", /* background */
  [257] = "#e6d2f1", /* foreground */
  [258] = "#e6d2f1",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
