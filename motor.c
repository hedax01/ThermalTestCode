#include<stdio.h>
#include <wiringPi.h>

#define EN 21
#define PUL 3
#define DIR 22
#define UP 1
#define DOWN 0

void init()
{
  pinMode(EN, OUTPUT);
  pinMode(PUL, OUTPUT);
  pinMode(DIR, OUTPUT);
  digitalWrite(EN, 1);
}

void generaFulse(long duration)
{
  digitalWrite(PUL, 1);
  delayMicroseconds(duration);
  digitalWrite(PUL, 0);
  delayMicroseconds(duration);
}

void moveUp(long v, int steps)
{
  digitalWrite(EN, 0);
  digitalWrite(DIR, UP);
  int i = 0;
  while (i < steps)
  {
    generaFulse(v);
    i++;
  }
  digitalWrite(EN, 1);
}

void moveDown(long v, int steps)
{
  digitalWrite(EN, 0);
  digitalWrite(DIR, DOWN);
  int i = 0;
  while (i < steps)
  {
    generaFulse(v);
    i++;
  }
  digitalWrite(EN, 1);
}

int main(void)
{
  wiringPiSetup();
  // pinMode (0, OUTPUT) ;
  init();
  printf("move Up v=30 steps=12800\n");
  moveUp(30, 12800);
  return 0;
}