#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

static int WIDTH = 640;
static int HEIGHT = 480;
bool dragging = false;
int keyArr[350];

// GLFW functions
static void Init(void) {
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  glClearColor(0.0, 0.0, 0.0, 1.0);
}

static void Update(GLFWwindow *window, float delta) {
  std::cout << "delta:" << delta << std::endl;
  if (keyArr[GLFW_KEY_ESCAPE])
    glfwSetWindowShouldClose(window, 1);
  // Why are things rotating tbh
  // rotatex += keyArr[GLFW_KEY_LEFT] - keyArr[GLFW_KEY_RIGHT];
  // rotatey += keyArr[GLFW_KEY_UP] - keyArr[GLFW_KEY_DOWN];
}

static void RenderScene(GLFWwindow *window, float delta) {
  glClear(GL_COLOR_BUFFER_BIT);
  glColor3f(1, 1, 1);

  glBegin(GL_LINE_LOOP);
  glVertex2f(-1.0, -1.0);
  glVertex2f(1.0, 1.0);
  glEnd();
  glFlush();
}

static void Resize(GLFWwindow *window, int w, int h) {
  if (h < 1)
    h = 1;
  glViewport(0, 0, w, h);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(45.0f, (float) w / (float) h, 0.1f, 1000.0f);
  gluLookAt(0.0f, 0.0f, 30, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f);
  glMatrixMode(GL_MODELVIEW);
}

static void KeyCallback(GLFWwindow *window, int key, int scancode, int action, int mods) {
  keyArr[key] = action;
}

static void MouseClickCallback(GLFWwindow *window, int button, int action, int mods) {
  switch (button) {
  case GLFW_MOUSE_BUTTON_1:
    dragging = action;
    break;
  }
}

static void MouseMotionCallback(GLFWwindow *window, double x, double y) {
  if (dragging) {
    // mousex += x;
    // mousey += y;
  }
}


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

int main(int argc, char** argv) {
  GLFWwindow *window;

  glfwInit();
  window = glfwCreateWindow(WIDTH, HEIGHT, argv[0], NULL, NULL);
  glfwMakeContextCurrent(window);

  Init();

  glfwSetWindowSizeCallback(window, Resize);
  glfwSetKeyCallback(window, KeyCallback);
  glfwSetMouseButtonCallback(window, MouseClickCallback);
  glfwSetCursorPosCallback(window, MouseMotionCallback);

  // Main loop
  while (!glfwWindowShouldClose(window)) {
    float delta = glfwGetTime();
    Update(window, delta);
    RenderScene(window, delta);
    glfwSetTime(0);
    glfwSwapBuffers(window);
    glfwPollEvents();
  }
  glfwDestroyWindow(window);
  return 0;  
}
