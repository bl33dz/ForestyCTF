#include <stdio.h>
#include <string.h>

char flag[60] = "]MACnMEV[Wh^KhS]PBVf^Yg]EU\\EhL]hZWX@gZXFfC_]mGCVPEY_hFVE\\K";
char keys[7] = "7827197";

void decrypt_flag()
{
    for (int i = 0; i < strlen(flag); i++)
        flag[i] ^= keys[i % strlen(keys)];
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s <pin>\n", *argv);
        return -1;
    }

    if (!strncmp(argv[1], keys, strlen(keys)))
    {
        decrypt_flag();
        printf("ForestyCTF{%s}\n", flag);
        return 0;
    }
    
    puts("Nope!");
    return -1;
}