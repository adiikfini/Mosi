#include <iostream>
#include <cmath>
#include <iomanip>


using namespace std;

const double g= -9.806;
const double PI = 3.141592654;

int main()
{
    double massa;
    double ax=0;
    double ay=g;
    double tstep=0.01;
    double t=0;
    double Vo,Vx,Vy,Vxo,Vyo,Xo,Yo,sudut;
    double y = 0;
    double x = 0;
    cout<<"Masukkan Kecepatan Awal (Vo) : "<<endl;
    cin>>Vo;
    cout<<"Masukkan Sudut Kemiringan (sudut) : "<<endl;
    cin>>sudut;

    cout<<endl;

    Vx = Vo * cos (sudut*PI/180);
    Vy = Vo * sin (sudut*PI/180);


    cout<<"Numerik: "<<endl;

    do{
        Vy = Vy + (ay*tstep);
        Vx = Vx + (ax * tstep);
        y = y + (Vy*tstep);
        x = x + (Vx * tstep);
        t = t + tstep;
        cout<<"y :"<<y<<endl;
        cout<<"x: "<<x<<endl;
        cout<<"t :"<<t<<endl;

    }while(y > 0);

    cout<<" "<<endl;
    cout<<"Analitik: "<<endl;
    x = 0;
    y = 0;
    Vx = Vo * cos (sudut*PI/180);
    Vy = Vo * sin (sudut*PI/180);
    x = x + (Vx*t)+ (0.5 * ax * t *t);
    y = y + (Vy * t) + (0.5 * ay * t *t);
    cout<<"y :"<<y<<endl;
    cout<<"x: "<<x<<endl;
    cout<<"t :"<<t<<endl;

    return 0;
}
