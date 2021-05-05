// Wzor funkcji Rosenbrocka:
// f(x, y) = (1-x)^2 + 100*(y-x^2)^2 = 100*x^4 - 200*x^2*y + x^2 - 2*x + 100*y^2 + 1

// Pierwsze pochodne:
// df(x, y)/dx = 400*x^3 - 400*x*y + 2x - 2
// df(x, y)/dy = 200*y - 200*x^2

//Drugie pochodne:
// d^2f(x, y)/dx^2 = 1200*x^2 - 400*y + 2
// d^2f(x, y)/dy^2 = 200
// d^2f(x, y)/dxdy = 400*x

//Macierz Hessego:
//  H(x) = [(1+lambda)*(1200*x^2 - 400*y + 2),            400*x ]
//         [400*x,                           , (1+lambda)*(200) ]
//  H^(-1)(x) = [(1+lambda)/(400*x^2-400*y+1200*x^2*lambda^2-400*y*lambda^2+2*x^2*lambda-800*y*lambda+4*lambda+2)     , (-x)/(200*x^2-200*y+600*x^2*lambda^2-200*y*lambda^2+lambda^2+1200*x^2*lambda-400*y*lambda+2*lambda+1)]
//              [(-x)/(200*x^2-200*y+600*x^2*lambda^2-200*y*lambda^2+lambda^2+1200*x^2*lambda-400*y*lambda+2*lambda+1), (600*x^2-200*y+600*x^2*lambda-200*y*lambda+lambda+1)/(40000*x^2-40000*y+120000*x^2*lambda^2-40000*y*lambda^2+200*lambda^2+240000*x^*lambda-80000*y*lambda+400*lambad+200)]

//Gradient:
// [400*x^3 - 400*x*y + 2*x - 2, 200*y - 200*x^2]

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;
#define iteracje 1000000

double gradient[2];
double hessian[2][2];
double lambda = 0.001;
double x = 3.14;
double y = 2.71;
double xTest;
double yTest;
double f;

void gradientCalculate()
{
  gradient[0] = 400 * pow(x, 3) - 400 * x * y + 2 * x - 2;
  gradient[1] = 200 * y - 200 * pow(x, 2);
}

void hessianCalculate()
{
  hessian[0][0] = (1 + lambda) / (400 * pow(x, 2) - 400 * y + 1200 * pow(x, 2) * pow(lambda, 2) - 400 * y * pow(lambda, 2) + 2 * pow(x, 2) * lambda - 800 * y * lambda + 4 * lambda + 2);
  hessian[1][0] = (-x) / (200 * pow(x, 2) - 200 * y + 600 * pow(x, 2) * pow(lambda, 2) - 200 * y * pow(lambda, 2) + pow(lambda, 2) + 1200 * pow(x, 2) * lambda - 400 * y * lambda + 2 * lambda + 1);
  hessian[0][1] = hessian[1][0];
  hessian[1][1] = (600 * pow(x, 2) - 200 * y + 600 * pow(x, 2) * lambda - 200 * y * lambda + lambda + 1) / (40000 * pow(x, 2) - 40000 * y + 120000 * pow(x, 2) * pow(lambda, 2) - 40000 * y * pow(lambda, 2) + 200 * pow(lambda, 2) + 240000 * pow(x, 2) * lambda - 80000 * y * lambda + 400 * lambda + 200);
}

void xyCalculate()
{
  xTest = x - (hessian[0][0] * gradient[0] + hessian[1][0] * gradient[1]);
  yTest = y - (hessian[0][1] * gradient[0] + hessian[1][1] * gradient[1]);
}

double fCalculate(double x, double y)
{
  f = 100 * pow(x, 4) - 200 * pow(x, 2) * y + pow(x, 2) - 2 * x + 100 * pow(y, 2) + 1;
  return f;

  
}

void LevenbergMarquardt()
{
  if (fCalculate(xTest, yTest) > fCalculate(x, y))
  {
    lambda *= 8;
    hessianCalculate();
  }
  else
  {
    lambda /= 8;
    x = xTest;
    y = yTest;
    gradientCalculate();
  }
  xyCalculate();
}

int main()
{
  gradientCalculate();
  hessianCalculate();
  xyCalculate();
  for (int i = 0; i < iteracje; i++)
  {
    LevenbergMarquardt();
  }
  cout << "x = " << x << endl;
  cout << "y = " << y << endl;
  cout << "f(x,y) = " << fCalculate(x, y);
}