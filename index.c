#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_BLOCKS 100

typedef struct {
    int bit_vector[MAX_BLOCKS];
    int directory[MAX_BLOCKS];
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

void show_directory(Disk *disk) {
    printf("Directory:\n");
    for (int i = 0; i < disk->num_blocks; i++) {
        if (disk->directory[i] != -1) {
            printf("File '%d' starts at block %d\n", disk->directory[i], i);
        }
    }
}

void delete_file(Disk *disk) {
    int file_index;
    printf("Enter the index of the file to delete: ");
    scanf("%d", &file_index);

    if (file_index < 0 || file_index >= disk->num_blocks) {
        printf("Invalid file index.\n");
        return;
    }

    int start_block = disk->directory[file_index];
    if (start_block == -1) {
        printf("No file exists with index %d.\n", file_index);
        return;
    }

    disk->directory[file_index] = -1;
    for (int i = start_block; i < disk->num_blocks; i++) {
        if (disk->bit_vector[i] == file_index) {
            disk->bit_vector[i] = 0;
        } else if (disk->bit_vector[i] == -1) {
            break;
        }
    }

    printf("File '%d' deleted successfully.\n", file_index);
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
        printf("2. Show Directory\n");
        printf("3. Delete File\n");
        printf("4. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                show_bit_vector(&disk);
                break;
            case 2:
                show_directory(&disk);
                break;
            case 3:
                delete_file(&disk);
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
