#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_BLOCKS 100

typedef struct {
    int bit_vector[MAX_BLOCKS];
    int directory[MAX_BLOCKS][2]; // Stores the starting block and length of files
    int num_blocks;
} Disk;

void initialize_disk(Disk *disk, int num_blocks) {
    disk->num_blocks = num_blocks;
    memset(disk->bit_vector, 0, sizeof(disk->bit_vector));
    memset(disk->directory, -1, sizeof(disk->directory));
}

void show_bit_vector(Disk *disk)
