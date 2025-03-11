/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author DELL
 */
package car;

// Kelas Car merepresentasikan sebuah mobil dengan atribut brand dan model
public class Car { 
    // Atribut private hanya bisa diakses melalui metode setter dan getter
    private String brand;
    private String model;

    // Constructor
    public Car() { }

// Metode setter untuk mengatur nilai brand
    public void setBrand(String brand) {
        this.brand = brand;
    }
// Metode getter untuk mengatur nilai brand
// Setiap atribut memiliki metode setter dan getter
    public String getBrand() {
        return brand;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getModel() {
        return model;
    }
}
