/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Mobil;

/**
 *
 * @author DELL
 */
public class PhoneAction {
    
    public static void main(String[] args) {
        Phone phone1 = new Phone();
        phone1.brand = "Oppo";
        phone1.yearRelease = 2023;
        Phone phone2 = new Phone();
        System.out.println("Phone 1 brand: " +  phone1.brand);
        System.out.println("Phone 1 brand: " +  phone1.yearRelease);
        
        phone1.TurnOn();
        phone1.Call();
        phone1.SMS();
        phone1.TurnOff();
    }
    
}
