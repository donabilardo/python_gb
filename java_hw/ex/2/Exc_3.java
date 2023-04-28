// Разработайте программу, которая выбросит Exception, когда пользователь вводит
//  пустую строку. Пользователю должно показаться сообщение, что пустые строки 
//  вводить нельзя.
package Exceprion_DZ2;

import java.util.Scanner;

public class Exc_3 {
    public static void main(String[] args) {

            System.out.println("Введите строку: ");
            Scanner s = new Scanner(System.in);
            if (s.nextLine().equals("")) {
                s.close();
                throw new RuntimeException("Пустые строки вводить нельзя!");
            }
            s.close();
        }
     
    }