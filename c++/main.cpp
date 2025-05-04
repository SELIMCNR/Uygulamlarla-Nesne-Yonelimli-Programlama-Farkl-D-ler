#include<iostream>
using std::string;

class Vehicle{
      protected:
        string manufacturer;
        int year;
        string color;

      public:
        string getManufacturer(){
            return manufacturer;
        }  
        void setManufacturer(string value){
        this->manufacturer = value;
        }

        int getYear(){
            return year;
        }

        void setYear(int value){
            this->year = value ;
        }

        string getColor(){
            return this->color;
        }

        void setColor(string value){
            this-> color = value;
        }

        Vehicle (){
            std::cout <<"\n An instance has been derived from Vehicle."<<std::endl;
        }

        Vehicle(string manufacturer,int year,string color): Vehicle(){
            this->manufacturer = manufacturer;
            this->year = year;
            this->color = color;
        }

        void start(){
            std::cout << "Vehicle has been started."<<std::endl;

        }
        void stop(){
            std::cout << "Vehicle has been stopped."<<std::endl;
        }
        void drive(){
            std::cout << "Vehicle is driving..."<<std::endl;
        }

};

class Car : public Vehicle{
    public:
        Car(){
            std::cout << "\nAn instance has been derived from Car. "<<std::endl;
        
        }
        Car(string manufacturer,int year,string color) : 
        Vehicle(manufacturer,year,color){
            std::cout << "\nAn instance with full parameters has been derived from Car. "<<std::endl;
        
        }
        void openSunroof(){
            std::cout << "The sunroof has been opened. "<<std::endl;
        }
};



int main(){
    Vehicle item1 = Vehicle();
    item1.setManufacturer( "TOGG");
    std::cout<<"Vehicle" << item1.getManufacturer() << std::endl;

    Vehicle item2 = Vehicle("Scoda",2019,"White");
    std::cout <<"Vehicle" << item2.getManufacturer()<<std::endl;

    Car car1 = Car();
    item1.setManufacturer( "Car1");
    std::cout<<"Car : " << car1.getManufacturer() << std::endl;

    char c = getchar();

    
    return 0;
}