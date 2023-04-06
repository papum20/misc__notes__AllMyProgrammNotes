# OBJECTS  
  
## FUNCTIONS  
  
MAIN / INIT / SYSTEM  
bool can_change_color() : terminal can change default colors  
endwin() : deallocates memory, clears screen  
bool has_colors() : terminal has different colors  
initscr() : initializes screen, sets up memory, clears screen  
  
ATTRIBUTES  
int attr_get(attr_t, short, void*) : modifies att_t with current attribute,  
short with current color pair  
attron(attribute_name) : attribute (constant defined in ncurses) / color_pair on  
		only in stdscr, not affecting other windows  
attroff(attribute_name) : attribute (constant defined in ncurses) / color_pair off  
chgat() :  
wchgat() :  
mvchgat() :  
mvwchgat(WINDOW*, y, x, int n, attr_t a, short c, o) : changes a attribute for n  
(-1/n>cols=until end of line) chars (already printed)  
to color pair c (o = NULL) (doesn’t move cursor after)  
COLOR_PAIR(int id) : gets color by id  
init_color(color, int r, g, b) : changes color constant with rgb (0-999)  
init_pair(int id, color, color) : initializes pair (text_color, background)  
identified as id (colors constants defined in ncurses  
wattr_get(WINDOW*, attr_t, short, void*) :  
wattron(WINDOW*, attribute) : attribute on (only in window, not affecting others)  
wattroff(WINDOW*, attribute) : /  
INIT  
start_color() : initializes colors  
  
SCREEN  
bkgd(chtype) : sets and applies chtype as background for all screen  
bkgdset(chtype) : sets chtype as default background for all screen, i.e. it doesn’t apply it, 		but if you print something it will be ORed with the background  
clear() : clears all screen (and calls clearok())  
clearok(bool) : “if (bool) prints all screen from scratch”  
clrtoeol() : clear to end of line  
clrtobot() : clear to bottom  
erase() : clears all screen (prints spaces, doesn’t call clearok())  
refresh() : refreshes standard/main screen (stdscr) (with what is in memory)  
  
WINDOWS  
box(WINDOW *, int left_right, int top_bottom) : draws a box around a window, made of input						 chars (0, 0= default | - )  
color_set(short, void*) : sets <short> color_pair for window (void* = NULL)  
getbegyx(WINDOW *, int y, int x) : changes y, x with window top-left corner (min)  
getmaxyx(WINDOW *, int y, int x) : changes y, x with window bottom-right corner (max)  
int getmaxx(WINDOW *) :  
int getmaxy(WINDOW *) :  
getyx(WINDOW *, int y, int x) : changes y, x with cursor y, x  
WINDOW * newwin(int height, width, start_y, start_x) : new window  
scrl(int) : scrolls up active window by int  
wscrl(WINDOW *, int) :  
scroll(WINDOW *) : scrolls up by 1  
scrollok(WINDOW *, bool) : sets if scroll allowed  
wbkgd(WINDOW *, chtype) :  
wbkgdset(WINDOW *, chtype) :  
wborder(WINDOW *, int left, right, top, bottom, tlc, trc, blc, brc) : draws a box  
around window, with specified chars for each border and corner  
wclrtobot(WINDOW*) :  
wclrtoeol(WINDOW*) :  
wcolor_set(WINDOW*, short, void*) :  
werase(WINDOW *) : clears / empties window  
wrefresh(WINDOW *) : refreshes a window  
  
INPUT  
int getch() : (refreshes stdscr and) get int(char)  
int wgetch(WINDOW *) : (refreshes window and) get int(char) in window  
INIT  
cbreak() : Ctrl+C exits  
halfdelay(int t) : waits t tenths of second for input, if not given  
returns const ERR  
keypad(WINDOW *, bool) : if(bool) window can use special keys (arrows, F_ …)  
nodelay(WINDOW *, bool) : if(bool) returns ERR when no given input  
noecho() : doesn’t print input values  
raw() : gets input as it is (i.e. Ctrl+C doesn’t exit)  
timeout(int t) : if(t<0) waits for input, else waits t milliseconds  
before returning ERR  
wtimeout(WINDOW*, int t) :   
  
OUTPUT  
// y (from top), x (from left)  
addch(chtype) : prints char  
mvaddch(int y, int x, chtype) : moves and prints char  
mvwaddch(WINDOW *, int y, int x, chtype) : moves and prints char to window  
move(int y, int x) : move cursor to print  
printw(char *) : prints string (char *) to window  
wprintw(WINDOW *, char *) : prints to window  
mvprintw(int y, int x, char *) : moves and prints  
mvwprintw(WINDOW *, int y, x, char *) : moves and prints to window  
wmove(WINDOW*, int y, int x) :  
  
MISC  
beep() :   
curs_set(0/1/2) : set cursor 0 (invisible) / 1 (normal) / 2 (very visible)  
flash() :  
keyname(char) : string key_name of ascii char  


## CONSTANTS

WINDOW * stdscr : default window  
  
ATTRIBUTES  
  
bit-masks:	//chtype & bit-mask = (only) attribute / color / text (char)  
A_ATTRIBUTES : attribute + color  
A_COLOR : color  
A_CHARTEXT : text (char)  
  
COLORS  
  
CHARS  
KEY_UP  
KEY_F(int) : F_  
  
OTHER  
ERR = -1 : error value  
