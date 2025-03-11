/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author DELL
 */
package car;

public class Transmission {  // Kelas Transmission merepresentasikan sistem transmisi mobil
    private int gears;  // Atribut private untuk menyimpan jumlah gigi (gears)

    // Constructor tanpa parameter, menetapkan nilai awal gears = 5
    public Transmission() {
        this.gears = 5;
    }

    // Metode getter untuk mendapatkan jumlah gigi (gears)
    public int getGears() {
        return gears;
    }

    // Metode setter untuk mengubah jumlah gigi (gears)
    public void setGears(int gears) {
        this.gears = gears;
    }
}
