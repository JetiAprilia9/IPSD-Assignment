/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author DELL
 */
package car;

public class Main {  // Kelas Main digunakan sebagai titik awal eksekusi program
    public static void main(String[] args) {  // Metode utama (entry point) program
        Car myCar = new Car();  // Membuat objek dari kelas Car
        myCar.setBrand("Toyota");  // Mengatur merek mobil menjadi "Toyota"
        myCar.setModel("Corolla");  // Mengatur model mobil menjadi "Corolla"

        // Menampilkan informasi mobil ke layar
        System.out.println("Brand: " + myCar.getBrand());  
        System.out.println("Model: " + myCar.getModel());  
    }
}
