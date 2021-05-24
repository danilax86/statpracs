#include <iostream>
#include <array>
#include <cmath>

using namespace std;
const int arr_size = 15;

double getX(array<double, arr_size> array) {
    double sum = 0;
    for (double i : array)
        sum += i;
    return sum / array.size();
}

double getX2(array<double, arr_size> array) {
    double sum = 0;
    for (double i : array)
        sum += i * i;
    return sum / array.size();
}

double getS(array<double, arr_size> array) {
    double dispersion = getX2(array) - pow(getX(array), 2);
    double arr = array.size() + 0.0;
    double s = sqrt(arr / (arr - 1) * dispersion);
    return s;
}

void res(int task) {
    if (task == 1) {
        array<double, arr_size> arr1{63.4, 64.5,
                                     57.1, 51.7,
                                     40.1, 37.7,
                                     45.8, 54.9,
                                     35.9, 31.0,
                                     35.5, 19.2,
                                     13.6, 31.4,
                                     40.1};

        // Значение из таблицы
        float t = 1.753;

        double res1 = getX(arr1) - t * getS(arr1) / pow(arr1.size(), 0.5);
        double res2 = getX(arr1) + t * getS(arr1) / pow(arr1.size(), 0.5);
        cout << "Доверительный интервал 1: " << res1 << " < m < " << res2 << endl;

    } else if (task == 2) {
        float avg_x = 82;
        float sx2 = 686800;
        float n = 100;
        double sigma2 = (sx2 / n) - pow(avg_x, 2);
        double sigma = sqrt(sigma2);

        // Значение из таблицы (взял 120, как близкое к 100)
        float t = 2.358;

        double res1 = avg_x - (t * sigma) / sqrt(n);
        double res2 = avg_x + (t * sigma) / sqrt(n);
        cout << "Доверительный интервал 2: " << res1 << " < m < " << res2 << endl;
    } else {
        cerr << "Неправильный номер задания" << endl;
    }

}

int main() {
    res(1);
    res(2);
    return 0;
}
