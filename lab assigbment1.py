#include <iostream>
using namespace std;

class Employee {
private:
    string name, department;
    int empID;
    float basicSalary;

public:
    void getData() {
        cout << "Enter Employee Name: ";
        getline(cin, name);
        cout << "Enter Employee ID: ";
        cin >> empID;
        cin.ignore();
        cout << "Enter Department: ";
        getline(cin, department);
        cout << "Enter Basic Salary: ";
        cin >> basicSalary;
    }

    void calculateSalary() {
        float DA, HRA, TA, grossSalary, netSalary;

        DA = 0.92 * basicSalary;
        HRA = 0.58 * basicSalary;
        TA = 0.30 * basicSalary;

        grossSalary = basicSalary + DA + HRA + TA;
        netSalary = grossSalary - 500;   // LIC deduction

        cout << "\n--- Employee Salary Details ---\n";
        cout << "Name: " << name << endl;
        cout << "Employee ID: " << empID << endl;
        cout << "Department: " << department << endl;
        cout << "Basic Salary: Rs. " << basicSalary << endl;
        cout << "DA: Rs. " << DA << endl;
        cout << "HRA: Rs. " << HRA << endl;
        cout << "TA: Rs. " << TA << endl;
        cout << "LIC Deduction: Rs. 500" << endl;
        cout << "Net Salary: Rs. " << netSalary << endl;
    }
};

int main() {
    Employee e;
    e.getData();
    e.calculateSalary();
    return 0;
}
