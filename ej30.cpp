//Tomado del ejercicio anterior

#include <fstream>
#include <iostream>
#include<stdio.h> 
#include <cmath>
#include <string>
#include <sstream> 
using namespace std;

const double k=0.7;
const double D=1; //Constante de difusion
const int Nx = 30; //numero de pasos
const double phi1=0.0;
const double phi2=0.0;

//Condiciones:
double xi = -1.0;
double xf = 1.0;
double phi0 = 0.0;
double ti = 0.0;

double s0=1;
int dx= (xf-xi)/Nx;

void eq(string nombre);
	
int main() 
{ 
	string nombre = "ej29.dat";
 	eq(nombre);
	return 0; 
} 


void eq (string nombre){
	ofstream file;
	file.open(nombre);
	float datosp[Nx][Nx];
	float datosn[Nx][Nx];
	double s=s0;
	double phi = phi0;
	for (int n = 0; n < Nx; n++){
		for (int j= -1; j< xf; j++){
            if(n==0){
                datosp[n][j] = 0;
            }
            
            else{
			float dphi = D*(-4* pow(sin(k*dx/2),2))*phi + s;
			
			datosp[n][j]= dphi;
			file << n <<" "<< j<< " " << datosp[n][j] << std::endl;                
                
            }

		}
	}
	file.close();
}
