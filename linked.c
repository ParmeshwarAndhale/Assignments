#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_BLOCKS 100

typedef struct {
    int bit_vector[MAX_BLOCKS];
    int directory[MAX_BLOCKS][MAX_BLOCKS];
    int num_blocks;
} Disk;

void initialize_disk(Disk *disk, int num_blocks) {
    disk->num_blocks = num_blocks;
    memset(disk->bit_vector, 0, sizeof(disk->bit_vector));
    memset(disk->directory, -1, sizeof(disk->directory));
}

void show_bit_vector(Disk *disk) {
    printf("Bit Vector:\n");
    for (int i = 0; i < disk->num_blocks; i++) {
        printf("%d ", disk->bit_vector[i]);
    }
    printf("\n");
}

void create_new_file(Disk *disk) {
    char file_name[20];
    printf("Enter file name: ");
    scanf("%s", file_name);

    int allocated_blocks[MAX_BLOCKS];
    int count = 0;

    for (int i = 0; i < disk->num_blocks; i++) {
        if (rand() % 2 == 1) {
            allocated_blocks[count] = i;
            disk->bit_vector[i] = 1;
            count++;
        }
    }

    for (int i = 0; i < count; i++) {
        disk->directory[allocated_blocks[0]][i] = allocated_blocks[i+1];
    }

    printf("File '%s' created with allocated blocks: ", file_name);
    for (int i = 0; i < count; i++) {
        printf("%d ", allocated_blocks[i]);
    }
    printf("\n");
}

void show_directory(Disk *disk) {
    printf("Directory:\n");
    for (int i = 0; i < disk->num_blocks; i++) {
        if (disk->directory[i][0] != -1) {
            printf("%d: ", i);
            int j = 0;
            while (disk->directory[i][j] != -1) {
                printf("%d ", disk->directory[i][j]);
                j++;
            }
            printf("\n");
        }
    }
}

int main() {
    srand(time(NULL));
    Disk disk;
    int choice;

    printf("Enter the number of blocks in the disk: ");
    scanf("%d", &disk.num_blocks);

    initialize_disk(&disk, disk.num_blocks);

    while (1) {
        printf("\nMenu:\n");
        printf("1. Show Bit Vector\n");
        printf("2. Create New File\n");
        printf("3. Show Directory\n");
        printf("4. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                show_bit_vector(&disk);
                break;
            case 2:
                create_new_file(&disk);
                break;
            case 3:
                show_directory(&disk);
                break;
            case 4:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice, please try again.\n");
        }
    }

    return 0;
}
