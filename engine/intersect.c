#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Should have six arguments
// v is the vector
// o is the origin
// b is the box
// o_x, o_y, v_x, v_y, b_x, b_y
// returns distance (negative if not inside)
int main(int argc, char *argv[]) {
  float o_x = atof(argv[1]);
  float o_y = atof(argv[2]);
  float v_x = atof(argv[3]);
  float v_y = atof(argv[4]);
  float b_x = atof(argv[5]);
  float b_y = atof(argv[6]);
  /* float o_x = 0; */
  /* float o_y = 0; */
  /* float v_x = 1; */
  /* float v_y = 1; */
  /* float b_x = 1; */
  /* float b_y = 1; */

  float tmin = -10000;
  float tmax = 10000;

  if (v_x != 0.0) {
    float tx1 = (b_x - o_x) / v_x;
    float tx2 = (b_x + 1 - o_x) / v_x;

    tmin = fmaxf(tmin, fminf(tx1, tx2));
    tmax = fminf(tmax, fmaxf(tx1, tx2));
  }
  
  if (v_y != 0.0) {
    float ty1 = (b_y - o_y) / v_y;
    float ty2 = (b_y + 1 - o_y) / v_y;

    tmin = fmaxf(tmin, fminf(ty1, ty2));
    tmax = fminf(tmax, fmaxf(ty1, ty2));
  }
      
  float x = o_x + (tmin * v_x);
  float y = o_y + (tmin * v_x);
  float dist = (float) sqrt(pow(o_x - x, 2) + pow(o_y - y, 2));
  // This won't work as float has 32bit precision, whereas int has 8
  if (tmax >= tmin) {
    printf("%f\n", dist);
    return dist;
  } else {
    return -1.0;
  }
}
