package corejava.core;

// import java.util.ArrayList;
// import java.util.HashMap;
// import java.util.Map;
// import java.util.Map.Entry;

public class Demo {
    public static void main(String[] args) {
        // ArrayList<String> list = new ArrayList<String>();
        // list.add("list");
        // list.add("test2");
        // System.out.println(list.toString());

        // Map<Integer+String> map = new HashMap<>();
        // map.put(1+"mapValue1");

        // for(Entry<Integer,String> entry : map.entrySet()){
        //     System.out.println(entry.getKey() +" "+ entry.getValue());
        // }

        String userName = System.getProperty("user.name");
        System.out.println(userName);
        System.out.println(System.getProperty("java.version") + "Java version number");
        System.out.println (System.getProperty("java.vendor") + "Java vendor specific string");
        System.out.println (System.getProperty("java.vendor.url")+"Java vendor URL");
        System.out.println ("java.home"+"Java installation directory");
        System.out.println ("java.class.version"+"Java class version number");
        System.out.println ("java.class.path"+"Java classpath");
        System.out.println ("os.name"+"Operating System Name");
        System.out.println ("os.arch"+"Operating System Architecture");
        System.out.println ("os.version"+"Operating System Version");
        System.out.println ("file.separator"+"File separator");
        System.out.println ("path.separator"+"Path separator");
        System.out.println ("line.separator"+"Line separator");
        System.out.println ("user.name"+"User account name");
        System.out.println ("user.home"+"User home directory");
        System.out.println ("user.dir"+"User's current working directory");

    }    
}
