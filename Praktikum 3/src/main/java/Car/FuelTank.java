/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author DELL
 */
package car; 

public class FuelTank {  // Kelas FuelTank merepresentasikan tangki bahan bakar
    private int fuelLevel;  // Atribut private untuk menyimpan level bahan bakar

    // Constructor tanpa parameter, menetapkan nilai awal fuelLevel = 100
    public FuelTank() {
        this.fuelLevel = 100;
    }

    // Metode getter untuk mendapatkan nilai fuelLevel
    public int getFuelLevel() {
        return fuelLevel;
    }

    // Metode setter untuk mengubah nilai fuelLevel
    public void setFuelLevel(int fuelLevel) {
        this.fuelLevel = fuelLevel;
    }
}
