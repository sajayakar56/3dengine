#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <GLFW/glfw3.h>
using namespace std;

// Intersection formula AABB
float intersect(float ox, float oy,
	      float vx, float vy,
	      float bx, float by) {
  float tmin = -10000;
  float tmax = 10000;
  float result = 0.0;
  
  if (vx != 0.0) {
    float tx1 = (bx - ox) / vx;
    float tx2 = (bx + 1 - ox) / vx;

    tmin = max(tmin, min(tx1, tx2));
    tmax = min(tmax, max(tx1, tx2));
  }

  if (vy != 0.0) {
    float ty1 = (by - oy) / vy;
    float ty2 = (by + 1 - oy) / vy;

    tmin = max(tmin, min(ty1, ty2));
    tmax = min(tmax, max(ty1, ty2));
  }

  float x = oy + (tmin * vx);
  float y = oy + (tmin * vx);
  float dist = (float) sqrt(pow(ox - x, 2) + pow(oy - y, 2));
  result = dist;
  
  if (tmax >= tmin) {
    return result;
  } else {
    return -1.0;
  }
}

static void key_callback(GLFWwindow *window, int key, int scancode, int action, int mods) {
  if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS) {
    glfwSetWindowShouldClose(window, GLFW_TRUE);
  }  
}

int main() {
  printf("%f", intersect(0, 0, 1, 1, 1, 1));
  // Lets try drawing something
  if (!glfwInit()) {
    printf("init failed\n");
    return 0;
  }

  GLFWwindow *window = glfwCreateWindow(640, 480, "meow", NULL, NULL);
  if (!window) {
    printf("window init failed\n");
    return 0;
  }

  glfwMakeContextCurrent(window);
  glfwSetKeyCallback(window, key_callback);

  int width, height;
  glfwGetFramebufferSize(window, &width, &height);
  printf("width: %d\n", width);
  glViewport(0, 0, width, height);
  glClear(GL_COLOR_BUFFER_BIT);

  // Infinite loop
  while (!glfwWindowShouldClose(window)) {
  }
  
  glfwTerminate();
}
