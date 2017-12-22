#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

static int WIDTH = 640;
static int HEIGHT = 480;
static float MAX_RAY_DIST = 999.0;
bool dragging = false;
int keyArr[350];
float PI = 3.14159;

// GLFW functions
static void Init(void) {
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  glClearColor(0.0, 0.0, 0.0, 1.0);
}

static void Update(GLFWwindow *window, float delta) {
  // std::cout << "delta:" << delta << std::endl;
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

  if (tmax >= 0) {
    float x = ox + (tmin * vx);
    float y = oy + (tmin * vy);
    float dist = sqrt(pow((ox - x), 2) + pow((oy - y), 2));
    return dist;
  } else {
    return -1.0;
  }
}

// 3DEngine stuff
float degreesToRadians(float degrees) {
  return (degrees / 180) * PI;
}

struct Vector {
    float x;
    float y;
};
typedef struct Vector Vector;

struct Camera {
  float x;
  float y;
  float fov;
  // Angle 
  float direction;
};
typedef struct Camera Camera;

struct Box {
  float x;
  float y;
};
typedef struct Box Box;

struct Map {
  Box *boxes;
  int size;
};
typedef struct Map Map;  

Vector angleToVector(float angle) {
  Vector v;
  v.x = cos(angle);
  v.y = sin(angle);
  return v;
}

float mapHit(Map *m, Vector v, float ox, float oy) {
  float minIntersection = MAX_RAY_DIST;
  for (int i = 0; i < m->size; i++) {
    Box box = m->boxes[i];
    float intersection = intersect(ox, oy, v.x, v.y, box.x, box.y);
    if (intersection != 0.0 && intersection != -1.0 && intersection < minIntersection) {
	minIntersection = intersection;
    }
  }
  return minIntersection;
}

// Raycast one ray
float raycast(float ox, float oy, float angle, Map *m) {
  Vector v = angleToVector(angle);
  printf("Vector x, y, a: (%f, %f, %f)\n", v.x, v.y, angle);
  return mapHit(m, v, ox, oy);
}

// Cast multiple rays for the camera
float *castRays(Camera *c, int n, Map *m) {
  float delta_fov = c->fov / (n - 1);
  float theta = c->direction + (c->fov / 2);
  float *rays = (float *) malloc(sizeof(float) * n - 1);
  for (int i = 0; i < (n - 1); i++) {
    float ray = raycast(c->x, c->y, theta, m);
    rays[i] = ray;
    theta -= delta_fov;
  }
  return rays;
}

Map createMap(int size) {
  Map m;
  m.size = size;
  m.boxes = (Box *) malloc(sizeof(Box) * size);
  return m;
}

int main(int argc, char** argv) {
  // Some sample code to cast rays
  Camera c;
  c.x = 0.0, c.y = 0.0, c.fov = degreesToRadians(70), c.direction = degreesToRadians(45);
  Map m = createMap(1);
  // This is a bad idea, should be double pointers right?
  // Actually, it might be on the heap, since i'm copying into it???
  Box b;
  b.x = 1.0, b.y = 1.0;
  m.boxes[0] = b;
  // How many rays to cast
  int N = 20;
  float *rays = castRays(&c, N, &m);
  for (int i = 0; i < N - 1; i++) {
    printf("%f\n", rays[i]);
  }

  printf("Some independent tests\n");
  float x = intersect(0, 0, 0.5, 0.5, 1, 1);
  float y = intersect(0, 0, 0.45, 0.5, 1, 1);
  printf("a: %f, b: %f\n", x, y);
  
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
