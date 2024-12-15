package corejava.core;

public class StringVowel {
    public static void main(String[] args){
        String regex = ".*[aeiou].*";
        String shortName ="Rqwsdfnt";
        String fullName = "Gajendra";
        
        System.out.println(shortName.toLowerCase().matches(regex));
        System.out.println(fullName.toLowerCase().matches(regex));
    }
    
}
