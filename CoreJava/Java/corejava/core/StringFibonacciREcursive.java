package corejava.core;

public class StringFibonacciREcursive {
    public static int fibonacci(int count){
        if(count <=1)
            return count;
        return fibonacci(count-1)+fibonacci(count-2);
    }
    public static void main(String[] args){
        int count = 20;
        for(int i=0;i < count;i++){
            System.out.print(fibonacci(i) +" ");
        }
    }
}
