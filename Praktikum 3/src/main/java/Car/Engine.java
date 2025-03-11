/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author DELL
 */
package car;  

public class Engine {  // Kelas Engine merepresentasikan mesin kendaraan
    private int horsepower;  // Atribut private untuk menyimpan tenaga mesin (dalam HP)

    // Constructor tanpa parameter, menetapkan nilai default 150 HP
    public Engine() {
        this.horsepower = 150;
    }

    // Metode getter untuk mendapatkan nilai tenaga mesin
    public int getHorsepower() {
        return horsepower;
    }

    // Metode setter untuk mengubah nilai tenaga mesin
    public void setHorsepower(int horsepower) {
        this.horsepower = horsepower;
    }
}
