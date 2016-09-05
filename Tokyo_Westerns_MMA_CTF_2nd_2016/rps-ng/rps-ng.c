#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char buf[100];
char *pname[3] = {
  "Rock",
  "Paper",
  "Scissors"
};
int table_initalized = 0;
int table[3][3];
int last;

// create random table
void init_table() {
  int i, j;
  for(i = 0; i < 3; i++) {
    for(j = 0; j < 3; j++) {
      table[i][j] = rand() % 6;
    }
  }
  last = 0;
}

void update_table(int c) {
  table[last][c]++;
  last = c;
}

int next_hand() {
  if(!table_initalized) {
    init_table();
    table_initalized = 1;
  }
  int m = -1;
  int ret = 0;
  int i;
  for(i = 0; i < 3; i++) {
    if(m < table[last][i]) {
      m = table[last][i];
      ret = i;
    }
  }
  return (ret + 1) % 3;
}

int main() {
  int seed;
  int i;
  int win = 0;
  FILE *fp = fopen("/dev/urandom", "r");
  fread(&seed, 4, 1, fp);
  fclose(fp);
  srand(seed);

  puts("Let's janken");
  fflush(stdout);

  for(i = 0; i < 50; i++) {
    printf("Game %d/50 Your win: %d/%d\n", i + 1, win, i);
    printf("Rock? Paper? Scissors? [RPS]");
    fflush(stdout);
    int t;
    while(t = getchar()) {
      if(t == EOF) {
        t = 0;
        break;
      }
      if(t == ' ' || t == '\n' || t == '\r' || t == '\t') continue;
      break;
    }
    if(t == 0) {
      puts("Bye bye");
      fflush(stdout);
      return 0;
    }
    int c;
    switch(t) {
    case 'R':
      c = 0;
      break;
    case 'P':
      c = 1;
      break;
    case 'S':
      c = 2;
      break;
    default:
      puts("Wrong input");
      fflush(stdout);
      return 1;
    }
    int p = next_hand();
    printf("%s-%s\n", pname[c], pname[p]);
    if(p == c) {
      puts("Draw");
    }else if((p+1) % 3 == c) {
      puts("You win!!");
      win++;
    } else {
      puts("You lose");
    }
    usleep(100000);
    update_table(c);
    fflush(stdout);
  }
  if(win >= 40) {
    printf("Congrats!!!!\n");

    fp = fopen("flag.txt", "r");
    fgets(buf, 100, fp);
    puts(buf);
  } else {
    printf("Not enough wins\n");
  }
  fflush(stdout);
  return 0;
}
