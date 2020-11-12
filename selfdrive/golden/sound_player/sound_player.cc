#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>
#include <assert.h>
#include <sys/mman.h>
#include <sys/resource.h>
#include  <signal.h>

#include "common/timing.h"

extern "C"{
#include "slplay.h"
}


void sound_init()
{
    char *error = NULL;
    slplay_setup(&error);
    if (error)
    {
        printf ("%s\n", error);
        exit(1);
    }
}

void sound_destroy()
{
    slplay_destroy();
}

void set_volume(int volume)
{
    char volume_change_cmd[64];
    sprintf(volume_change_cmd, "service call audio 3 i32 3 i32 %d i32 1 &", volume);

    // 5 second timeout at 60fps
    int volume_changed = system(volume_change_cmd);
    printf ("volume_changed to %d\n", volume_changed);
}

bool loop = false;
bool running = true;
void end_callback()
{
    printf ("end_callback !!! \n");

    if (!loop)
    {
        running = false;
    }
}

void  sig_handle(int sig)
{
    printf ("handle ctrl+c\n");
    sound_destroy();
    exit(0);
}

int main(int argc, char* argv[]) {
    for (int i=0; i<argc; ++i)
    {
        printf ("argv[%d]=%s\n", i, argv[i]);
    }

    if (argc < 2)
    {
        printf ("Usage: sound_player [sound file] [is_loop(0|1)] \n");
        return 1;
    }

    sound_init();
    slplay_set_end_callback(end_callback);
    signal(SIGINT, sig_handle);

    const char* snd_file = argv[1];
    char* error = NULL;
    slplay_create_player_for_uri(snd_file, &error);
    if (error)
    {
        printf ("%s\n", error);
        return 1;
    }

    if( access( snd_file, F_OK ) == -1 ) {
        printf ("%s not found.\n", snd_file);
        return 1;
    }

    if (argc >= 3)
    {
        const char* loop_str = argv[2];
        loop = loop_str[0] == '1';
    }

    slplay_play(snd_file, loop, &error);
    if(error) {
        printf("error playing sound: %s \n", error);
    }

    while (running)
    {
        usleep(100);
    }

    slplay_stop_uri(snd_file, &error);
    if (error)
    {
        printf("error stopping sound: %s \n", error);
    }

    sound_destroy();
    return 0;
}
