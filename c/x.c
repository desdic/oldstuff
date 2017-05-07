#include <stdio.h>
#include <stdlib.h>
#include <X11/Xlib.h>

int main(int argc, char **argv) {
    char *display_name = NULL;
    Display *display;
    int screen_num;
    //Screen *screen_ptr;

    if ( (display=XOpenDisplay(display_name)) == NULL ) {
        (void) fprintf( stderr, "cannot connect to X server %s\n",
            XDisplayName(display_name));
        exit( -1 );
    }
    screen_num = DefaultScreen(display);
    //screen_ptr = DefaultScreenOfDisplay(display);

    XWindowAttributes ra;
    (void) XGetWindowAttributes(display, DefaultRootWindow(display), &ra);

    (void) fprintf( stdout, "Num: %d, Width: %d, Height: %d (%d %d)",
        screen_num, ra.width, ra.height, ra.x, ra.y);

    return 0;
}
