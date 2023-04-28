// Дан следующий код, исправьте его там, где требуется
package Exceprion_DZ2;

import java.io.FileNotFoundException;

public class Exc2_2 {
    public static void main(String[] args) {
        try {
            int a = 90;
            int b = 0;
            System.out.println(a / b);
            printSum(23, 234);
            int[] abc = { 1, 2 };
            abc[1] = 9;
        }  catch (FileNotFoundException ex) {
            System.out.println("Файл не найден!");
        }  catch (ArithmeticException ex) {
            System.out.println("Деление на ноль запрещено!");   
        }  catch (NullPointerException ex) {
            System.out.println("Указатель не может указывать на null!");
        }  catch (IndexOutOfBoundsException ex) {
            System.out.println("Индекс выходит за пределы установленных  границ!");
        }  catch (Throwable ex) {
            System.out.println("Что-то пошло не так...");
        }


     }
     public static void printSum(Integer a, Integer b) throws FileNotFoundException {
        System.out.println(a + b);
     }
     

}