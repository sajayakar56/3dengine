/***********************
 * Let's try drawing a line
 * Stephen Jayakar
 ************************/

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstdlib>
#include <iostream>

static int WIDTH = 640;
static int HEIGHT = 480;
float rotatex = 0, rotatey = 0, mousex = 0, mousey = 0;
bool dragging = false;
int keyArr[350];

static void Init(void) {
  glMatrixMode(GL_MODELVIEW);
  // TODO: This might be shaders
  glLoadIdentity();
  // The background color
  glClearColor(0.0, 0.0, 0.0, 1.0);
}

static void Update(GLFWwindow *window, float delta) {
  std::cout << "delta:" << delta << std::endl;
  if (keyArr[GLFW_KEY_ESCAPE])
    glfwSetWindowShouldClose(window, 1);
  // Why are things rotating tbh
  rotatex += keyArr[GLFW_KEY_LEFT] - keyArr[GLFW_KEY_RIGHT];
  rotatey += keyArr[GLFW_KEY_UP] - keyArr[GLFW_KEY_DOWN];
}

static void RenderScene(GLFWwindow *window, float delta) {
  glClear(GL_COLOR_BUFFER_BIT);
  glColor3f(1, 1, 1);

  glBegin(GL_LINE_LOOP);
  glVertex2f(0.25, 0.25);
  glVertex2f(0.75, 0.25);
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
    mousex += x;
    mousey += y;
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
